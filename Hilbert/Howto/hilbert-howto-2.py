#!/usr/bin/env python3

"""
How to draw a Hilbert Curve - Step 2

In step 1 the turtle drew a line and kept its orientation
Turtle is looking to the right
"""

import turtle

COLOR = [ 'blue' ]

def hilbert( turtle, length, depth ):
  """
  Draw the U shape of iteration depth 1
  """
  turtle.left(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(length)
  """
  Finally turn into same direction we started with
  """
  turtle.left(90)

screen = turtle.Screen()
flitzi = turtle.Turtle()

length = 300

flitzi.penup()
offset = -length * (0.5)
flitzi.goto( offset, offset )
flitzi.pendown()

flitzi.color( COLOR[0] )
flitzi.pensize( 1 )

"""
The iteration depth shall start counting from 0 upwards
"""
n = 0
hilbert(flitzi, length, depth = n)

screen.exitonclick()
