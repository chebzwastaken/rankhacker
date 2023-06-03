#ifdef GL_ES
precision mediump float;
#endif

#define rot(a)mat2(cos(a+vec4(0,33,11,0)))

uniform vec2 u_resolution;
uniform float u_time;

void main(){
    vec2 r=u_resolution;
    vec2 u=gl_FragCoord.xy;
    vec4 O=gl_FragColor;
    
    u+=u-r;
    float i=0.,t,d,m=u_time*2.;// 0.5
    
    for(int j=0;j<4;j++){
        t=m*.5;
        d=length(u-r*.5);
        u=rot(t)*u;
        u+=vec2(cos(d+t),sin(d+t))*.5;
        i+=1./d;
    }
    
    O=vec4(vec3(i*.1,i*.2,i*.3),1.);
    
    gl_FragColor=O;
    
}