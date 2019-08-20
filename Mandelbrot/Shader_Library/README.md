WebGL Shader Library Mandelbrot Set
===================================

See it in action on https://omerkel.github.io/Fractals/Mandelbrot/Shader_Library/

While our visit of [Evoke2019 demo party/conference](https://2019.evoke.eu/) in Cologne, Germany,
we decided to implement a GLSL fragment shader to render a zoom path
into a Mandelbrot set while live shifting the color palette.
The version implemented first used a __glslViewer__ on Linux.

* https://github.com/patriciogonzalezvivo/glslViewer

Here a wrapper for WebGL SL is implemented to run the same Shaders in
a browser environment. Mind the canvas context is 'experimental-webgl'.

Minor third party code was taken from sources as indicated in the code by
mentioned URLs. These code parts claimed to be freely available and
license compatible with MIT.

Normal gl code logic
====================

* preload
    * init
        * gl.createProgram
        * gl.createShader( type );
            * gl.shaderSource( shader, src );
            * gl.compileShader( shader );
        * gl.attachShader( program, instance );
        * gl.linkProgram( program );
    * animate
        * gl.useProgram( currentProgram );
