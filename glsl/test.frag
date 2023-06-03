#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define PI 3.1415926535897932384626433832795
#define dot2(A) dot(A,A)

// signed distance function
float sdCircle(vec2 st, float radius){
    return length(st) - radius;
}

float sdRoundedBox(in vec2 p,in vec2 b,in vec4 r)
{
    r.xy=(p.x>0.)?r.xy:r.zw;
    r.x=(p.y>0.)?r.x:r.y;
    vec2 q=abs(p)-b+r.x;
    return min(max(q.x,q.y),0.)+length(max(q,0.))-r.x;
}

float sdHexagram(in vec2 p,in float r)
{
    const vec4 k=vec4(-.5,.8660254038,.5773502692,1.7320508076);
    p=abs(p);
    p-=2.*min(dot(k.xy,p),0.)*k.xy;
    p-=2.*min(dot(k.yx,p),0.)*k.yx;
    p-=vec2(clamp(p.x,r*k.z,r*k.w),r);
    return length(p)*sign(p.y);
}

float sdBezier(in vec2 pos,in vec2 A,in vec2 B,in vec2 C)
{
    vec2 a=B-A;
    vec2 b=A-2.*B+C;
    vec2 c=a*2.;
    vec2 d=A-pos;
    float kk=1./dot(b,b);
    float kx=kk*dot(a,b);
    float ky=kk*(2.*dot(a,a)+dot(d,b))/3.;
    float kz=kk*dot(d,a);
    float res=0.;
    float p=ky-kx*kx;
    float p3=p*p*p;
    float q=kx*(2.*kx*kx-3.*ky)+kz;
    float h=q*q+4.*p3;
    if(h>=0.)
    {
        h=sqrt(h);
        vec2 x=(vec2(h,-h)-q)/2.;
        vec2 uv=sign(x)*pow(abs(x),vec2(1./3.));
        float t=clamp(uv.x+uv.y-kx,0.,1.);
        res=dot2(d+(c+b*t)*t);
    }
    else
    {
        float z=sqrt(-p);
        float v=acos(q/(p*z*2.))/3.;
        float m=cos(v);
        float n=sin(v)*1.732050808;
        vec3 t=clamp(vec3(m+m,-n-m,n-m)*z-kx,0.,1.);
        res=min(dot2(d+(c+b*t.x)*t.x),
        dot2(d+(c+b*t.y)*t.y));
        // the third root cannot be the closest
        // res = min(res,dot2(d+(c+b*t.z)*t.z));
    }
    return sqrt(res);
}


vec3 palette(float t, vec3 a, vec3 b, vec3 c, vec3 d){
    return a + b*cos( 6.28318*(c*t+d) );
}

void main(){ 
    vec2 st = (2.0 * gl_FragCoord.xy - u_resolution.xy) / u_resolution.y;
    // st = exp(fract(st * 2.) - .5);

    float ani=-7.+u_time*2.;
    
    // float d = sdCircle(st, 0.);

    // float d = sdRoundedBox(st, vec2(.5), vec4(.1, .1, .1, .1));
    
    
    // float d = sdBezier(st, vec2(-.5, -.5), vec2(0., .5), vec2(.5, -.5));

    
    float d = sdHexagram(st, .5);


    d = sin(d * 8.0 - ani);


    vec3 color=palette(length(st),
        vec3(.5),
        vec3(.5),
        vec3(1.), 
        vec3(0.0039, 0.1961, 0.2941)
    );

    d=abs(d);
    d = .1 / d;

    color *= d;

    // gl_FragColor = vec4(d, d, d, 1.0);
    gl_FragColor = vec4(color, 1.0);
}