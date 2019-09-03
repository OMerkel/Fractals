Julia Sets
==========

See it rendered live using WebGL Shader Library on https://omerkel.github.io/Fractals/Julia_Set/Shader_Library

The Julia Sets are closely related to the [Mandelbrot sets](../Mandelbrot).

Here with z,c &Element; &#x2102; where z<sub>0</sub> corresponds the position inside a Complex Plane
the value of z is rendered in iterations and checked whether it remains bounded. c is set to be a fixed
constant complex number for a whole image.

z<sub>n+1</sub>=z<sub>n</sub><sup>2</sup>+c

The position gets a color value dependend on the number of iterations reaching the BAILOUT value of 2.0 for
|z|.

For animated Julia sets c gets variated over multiple images following a path inside the Complex Plane.
