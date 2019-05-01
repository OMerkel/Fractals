#!/usr/bin/env python3

"""
How to draw a Hilbert Curve - Step 1
"""

import turtle

COLOR = [ 'blue' ]

def hilbert( turtle, length ):
  """
  Here the drawing of the curve is intended
  
  First let us draw a line of specific length only
  """
  turtle.forward(length)

"""
Preparation of Screen and Turtle
"""
screen = turtle.Screen()
flitzi = turtle.Turtle()

"""
Length of the line to be drawn
"""
length = 300

"""
Position the turtle onto an offset position before drawing anything

This initial offset should be half of the chosen length

To avoid drawing artifacts it must
* first be lifted with penup and
* set down again with pendown
"""
flitzi.penup()
offset = -length * (0.5)
flitzi.goto( offset, offset )
flitzi.pendown()

flitzi.color( COLOR[0] )
flitzi.pensize( 1 )

"""
Call the drawing function
"""
hilbert(flitzi, length)

screen.exitonclick()
