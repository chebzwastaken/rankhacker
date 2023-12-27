#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define PI 3.1415926535897932384626433832795
#define dot2(A) dot(A,A)

// signed distance function

float sdHexagram(in vec2 p,in float r)
{
    const vec4 k=vec4(-.5,.8660254038,.5773502692,1.7320508076);
    p=abs(p);
    p-=2.*min(dot(k.xy,p),0.)*k.xy;
    p-=2.*min(dot(k.yx,p),0.)*k.yx;
    p-=vec2(clamp(p.x,r*k.z,r*k.w),r);
    return length(p)*sign(p.y);
}


vec3 palette(float t, vec3 a, vec3 b, vec3 c, vec3 d){
    return a + b*cos( 6.28318*(c*t+d) );
}

void main(){ 
    vec2 st = (2.0 * gl_FragCoord.xy - u_resolution.xy) / u_resolution.y;
    // st = exp(fract(st * 2.) - .5);

    float ani=-7.+u_time*2.;
    
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