/**
 * @file mandelbrot.frag
 * @author Oliver Merkel <Merkel(dot)Oliver(at)web(dot)de>
 * @author PJ
 * @date 2019 August 17th
 *
 * @section LICENSE
 *
 * Copyright 2019, Oliver Merkel <Merkel(dot)Oliver(at)web(dot)de>
 * All rights reserved.
 *
 * Released under the MIT license.
 * Use of this code is governed by a
 * MIT license that can be found in the LICENSE file.
 *
 * @section DESCRIPTION
 *
 * @brief GLSL fragment shader to render a zoom path into a Mandelbrot set.
 *
 * While our visit of Evoke2019 demo party/conference in Cologne, Germany,
 * we decided to implement a GLSL fragment shader to render a zoom path
 * into a Mandelbrot set while live shifting the color palette.
 *
 * Minor third party information related to color palette creation were
 * taken from following sources indicating to be freely available and
 * license compatible with MIT.
 *
 * - https://www.iquilezles.org/www/articles/palettes/palettes.htm
 *
 * Changes on 2019 August 19th:
 *   Minor modifications so that the shader runs as
 *     WEBGL SL instead of glslViewer from
 *     https://github.com/patriciogonzalezvivo/glslViewer
 *
 *   Sinusoidal path instead of linear path movement
 *
 */

#ifdef GL_ES
precision mediump float;
#endif

#extension GL_OES_standard_derivatives : enable

uniform float u_time;
uniform vec2 u_mouse;
uniform vec2 u_resolution;

#define PI2 6.28318530718
#define MAXITER 500

vec2 cmpxmul( in vec2 a, in vec2 b) {
  return vec2( a.x * b.x - a.y * b.y, a.y * b.x + a.x * b.y);
}

vec3 getcolor( in float i) {
  float t = 20.0 * i + u_time / 3.0;
  // https://www.iquilezles.org/www/articles/palettes/palettes.htm
  vec3 a = vec3( 0.50, 0.50, 0.50);
  vec3 b = vec3( 0.50, 0.50, 0.50);
  vec3 c = vec3( 1.00, 1.00, 1.00);
  vec3 d = vec3( 0.30, 0.20, 0.20);
  return a + b * cos( PI2 * ( c * t + d));
}

void main( void ) {
  vec2 st = gl_FragCoord.xy / u_resolution.xy;
  float aspect = u_resolution.x / u_resolution.y;
  st.x *= aspect;
  vec3 color = vec3( 0.0);

  // range
  vec2 begx = vec2( -2.0, +0.6);
  vec2 begy = vec2( -1.3, +1.3);
  vec2 endx = vec2( -0.743643887035762993093485, -0.743643887035762993093486);
  vec2 endy = vec2(  0.131825904212599176276485, 0.131825904212599176276486);

  // limit amplitude due to precision of float in GL_ES with this parameter set
  float t = 0.49998 * sin( u_time / 20.0 ) + 0.5;

  vec2 rx = t * (endx - begx) + begx;
  vec2 ry = t * (endy - begy) + begy;

  // mapping
  st.x = st.x * ( rx.y-rx.x) + rx.x;
  st.y = st.y * ( ry.y-ry.x) + ry.x;

  vec2 C = st;
  vec2 Z = vec2( 0.0);

  float c = 0.0;
  for( int i=0; i<MAXITER; ++i ) {
    Z = cmpxmul( Z, Z) + C;
    float r = sqrt( Z.x * Z.x + Z.y * Z.y);

    if( r>=2.0) {
      c = float(i);
      break;
    }
  }

  color = c > 0.0 ? getcolor( c / float(MAXITER) ) : vec3( 0.0);

  gl_FragColor = vec4( color, 1.0);
}
