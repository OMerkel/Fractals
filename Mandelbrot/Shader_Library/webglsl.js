/**
 * @file webglsl.js
 * @author Oliver Merkel <Merkel(dot)Oliver(at)web(dot)de>
 * @date 2019 August 20th
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
 * @brief WebGLSL rendering environment.
 *
 * While our visit of Evoke2019 demo party/conference in Cologne, Germany,
 * we decided to implement a GLSL fragment shader to render a zoom path
 * into a Mandelbrot set while live shifting the color palette.
 * The version implemented first used a glslViewer on Linux.
 *
 * https://github.com/patriciogonzalezvivo/glslViewer
 *
 * Here a wrapper for WebGL SL is implemented to run the same Shaders in
 * a browser environment. Mind the canvas context is 'experimental-webgl'.
 *
 * Minor third party code was taken from sources as indicated by
 * mentined URLs. These code parts claimed to be freely available and
 * license compatible with MIT.
 *
 * normal gl code logic:
 * =====================
 *
 * preload
 *   init
 *     gl.createProgram
 *     gl.createShader( type );
 *       gl.shaderSource( shader, src );
 *       gl.compileShader( shader );
 *     gl.attachShader( program, instance );
 *     gl.linkProgram( program );
 *   animate
 *     gl.useProgram( currentProgram );
 *
 */

// paulirish.com/2011/requestanimationframe-for-smart-animating/
window.requestAnimationFrame = window.requestAnimationFrame || ( function() {
  return  window.webkitRequestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.oRequestAnimationFrame ||
    window.msRequestAnimationFrame ||
    function( callback, element ) {
      window.setTimeout( callback, 1000 / 60 );
    };
})();

var canvas,
    gl,
    buffer,
    vertex_shader, fragment_shader,
    currentProgram,
    vertex_position,
    timeLocation,
    resolutionLocation,
    parameters = {  start_time  : new Date().getTime(),
                    time        : 0,
                    screenWidth : 0,
                    screenHeight: 0 };

preload('https://omerkel.github.io/Fractals/Mandelbrot/Shader_Library/');

function preload(base_url) {
  vertex_url = base_url + 'mandelbrot.vert';
  fragment_url = base_url + 'mandelbrot.frag';
  fetch(vertex_url)
  .then(response => response.text())
  .then((data) => {
    vertex_shader = data;

    fetch(fragment_url)
    .then(response => response.text())
    .then((data) => {
      fragment_shader = data;

      init();
      animate();
  }); });
}

function init() {
  canvas = document.querySelector( 'canvas' );

  try {
    gl = canvas.getContext( 'experimental-webgl' );
  } catch( error ) { }
  if ( !gl ) {
    throw "cannot create webgl context";
  }

  buffer = gl.createBuffer();
  gl.bindBuffer( gl.ARRAY_BUFFER, buffer );
  gl.bufferData( gl.ARRAY_BUFFER, new Float32Array(
    [ -1.0, -1.0,  1.0,
      -1.0, -1.0,  1.0,
       1.0, -1.0,  1.0,
       1.0, -1.0,  1.0 ] ), gl.STATIC_DRAW );

  currentProgram = createProgram( vertex_shader, fragment_shader );

  timeLocation = gl.getUniformLocation( currentProgram, 'u_time' );
  resolutionLocation = gl.getUniformLocation( currentProgram, 'u_resolution' );
}

function createProgram( vertex, fragment ) {
  var program = gl.createProgram();

  var vs = createShader( vertex, gl.VERTEX_SHADER );
  var fs = createShader( fragment, gl.FRAGMENT_SHADER );
  if ( vs == null || fs == null ) {
    return null;
  }

  gl.attachShader( program, vs );
  gl.attachShader( program, fs );

  gl.deleteShader( vs );
  gl.deleteShader( fs );

  gl.linkProgram( program );

  if ( !gl.getProgramParameter( program, gl.LINK_STATUS ) ) {
    alert(
      "ERROR:\nVALIDATE_STATUS: " + gl.getProgramParameter( program, gl.VALIDATE_STATUS ) +
      "\nERROR: " + gl.getError() +
      "\nVertex Shader:\n" + vertex +
      "\nFragment Shader:\n" + fragment
    );
    return null;
  }
  return program;
}

function createShader( src, type ) {
  var shader = gl.createShader( type );

  gl.shaderSource( shader, src );
  gl.compileShader( shader );

  if ( !gl.getShaderParameter( shader, gl.COMPILE_STATUS ) ) {
    alert( ( type == gl.VERTEX_SHADER ? "VERTEX" : "FRAGMENT" ) + " SHADER:\n" + gl.getShaderInfoLog( shader ) );
    return null;
  }
  return shader;
}

function resizeCanvas( event ) {
  if ( canvas.width != canvas.clientWidth ||
    canvas.height != canvas.clientHeight ) {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;

    parameters.screenWidth = canvas.width;
    parameters.screenHeight = canvas.height;

    gl.viewport( 0, 0, canvas.width, canvas.height );
  }
}

function animate() {
  resizeCanvas();
  if ( currentProgram ) {
    render();
  }
  requestAnimationFrame( animate );
}

function render() {
  parameters.time = new Date().getTime() - parameters.start_time;

  gl.clear( gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT );

  gl.useProgram( currentProgram );

  gl.uniform1f( timeLocation, parameters.time / 1000 );
  gl.uniform2f( resolutionLocation, parameters.screenWidth, parameters.screenHeight );

  gl.bindBuffer( gl.ARRAY_BUFFER, buffer );
  gl.vertexAttribPointer( vertex_position, 2, gl.FLOAT, false, 0, 0 );
  gl.enableVertexAttribArray( vertex_position );
  gl.drawArrays( gl.TRIANGLES, 0, 6 );
  gl.disableVertexAttribArray( vertex_position );
}
