#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mandelbrot set ASCII renderer.
Copyright (c) 2025 by Oliver Merkel <Merkel(dot)Oliver(at)web(dot)de>
License: MIT
Generates an ASCII representation of the Mandelbrot set in the terminal.
"""


class MyCanvas:
    """A simple ASCII canvas for drawing characters at
    specified coordinates."""
    def __init__(self, size):
        """Initialize the canvas with given size (width, height).

        Parameters:
        size (tuple): A tuple (width, height) defining the size of the canvas.
        """
        (x, y) = size
        self.canvas = []
        for _ in range(y):
            self.canvas.append(list(" " * x))

    def point(self, p, c):
        """Draw a character at the specified point.

        Parameters:
        p (tuple): A tuple (x, y) defining coordinates to draw the character.
        c (str): The character to draw at the specified coordinates.
        """
        (x, y) = p
        self.canvas[len(self.canvas)-1-y][x] = c

    def flush(self):
        """Print the canvas to the terminal.

        Parameters:
        None
        """
        for _, row in enumerate(self.canvas):
            print(''.join(row))


class Mandelbrot:
    """Class to generate and display the Mandelbrot set in ASCII."""
    def __init__(self, area, maxiter=26, maxcolor=26):
        """Initialize the Mandelbrot set renderer.
        Parameters:
        area (tuple): A tuple defining the area of the complex plane to render.
        maxiter (int): Maximum number of iterations for Mandelbrot calculation.
        maxcolor (int): Maximum number of colors (characters) to use.
        """
        ((bottom, left), (top, right)) = area
        (width, height) = (64, 32)
        canvas = MyCanvas(size=(width, height))
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            for x in range(width):
                cr = left + x*(right - left)/width
                i = self.mandelbrot(complex(cr, ci), maxiter)
                if i == maxiter:
                    canvas.point((x, y), ".")
                else:
                    canvas.point((x, y), str(chr(65+(i % maxcolor))))
        canvas.flush()

    def mandelbrot(self, c, maxiter):
        """
        Compute the Mandelbrot iteration count for a given complex point.

        Parameters:
        c (complex): The complex point to evaluate.
        maxiter (int): The maximum number of iterations to perform.

        Returns:
        int: Iteration count at which point escapes, or maxiter if it does not.
        """
        bailout = 2.0
        z = c
        for i in range(maxiter):
            if abs(z) > bailout:
                return i
            z = z**2 + c
        return maxiter


if __name__ == "__main__":
    # Mandelbrot(area=((0.065053, -0.74877),
    #                  (0.065103, -0.74872)),
    #            maxiter=2048, maxcolor=12 )
    Mandelbrot(area=((-1.3, -2.0), (1.3, 0.65)))
    # Mandelbrot(area=((-2.0, -2.5), (2.0, 2.0)))
