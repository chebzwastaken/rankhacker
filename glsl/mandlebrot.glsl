#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

float IterateMandelbrot( in vec2 c )
{
    const float B = 256.0;

    float n = 0.0;
    vec2 z  = vec2(0.0);
    for( int i=0; i<200; i++ )
    {
        z = vec2( z.x*z.x - z.y*z.y, 2.0*z.x*z.y ) + c; // z = z² + c
        if( dot(z,z)>(B*B) ) break;
        n += 1.0;
    }

    // float sn = n - log(log(length(z))/log(B))/log(2.0); // smooth iteration count
    float sn = n - log2(log2(dot(z,z))) + 4.0;  // equivalent optimized smooth iteration count
    
    return sn;
}



void main(){
    vec2 uv = gl_FragCoord.xy/u_resolution.xy;
    uv.x *= u_resolution.x/u_resolution.y;

    uv = uv*2.0 - 1.;
    // uv.x move to the left and uv to zoom in over time
    uv.x -= (u_time*0.1) * 2.; // uv.x moving to the left
    uv *= 1.5; // zoom in
   
    

    float n = IterateMandelbrot( uv );
    float c = n/100.0;
    // zoom in
    
    vec3 col = vec3( c );
    gl_FragColor = vec4(col,1.0);
}