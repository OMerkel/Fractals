# Mandelbrot Set

See it rendered live using WebGL Shader Library on https://omerkel.github.io/Fractals/Mandelbrot/Shader_Library

The Mandelbrot Set is named after Benoît Mandelbrot (&#42; 20.11.1924; &#x2020; 14.10.2010).

With z,c &Element; &#x2102; where z<sub>0</sub>=0 and c corresponding the position inside a Complex Plane
the value of z is rendered in iterations and checked whether it remains bounded.

z<sub>n+1</sub>=z<sub>n</sub><sup>2</sup>+c

The position gets a color value dependend on the number of iterations reaching the BAILOUT value of 2.0 for
|z|.

From Jupyter Notebook _[Mandelbrot Set.ipynb](Mandelbrot%20Set.ipynb)_ :

<table>
  <tr><td> <img src='out.png' /> </td>
    <td> <img src='out-2.png' /> </td></tr>
  <tr><td> <img src='out-3.png' /> </td>
    <td> <img src='out-4.png' /> </td></tr>
</table>

From Jupyter Notebook _[Render a Mandelbrot Set.ipynb](Render%20a%20Mandelbrot%20Set.ipynb)_ :
![From Jupyter Notebook _Render a Mandelbrot Set.ipynb_](mandelbrot1.png)

Rendered with _mandelbrot_ascii.py_ :
![Rendered with _mandelbrot_ascii.py_](mandelbrot_ascii.py.330x100.jpg)
