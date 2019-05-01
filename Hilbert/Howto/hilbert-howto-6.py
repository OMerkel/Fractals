#!/usr/bin/env python3

"""
How to draw a Hilbert Curve - Step 6
"""

import turtle

COLOR = [ 'blue', 'red', 'orange', 'green' ]

def hilbert( turtle, length, orientation, depth ):
  if depth>=0:
    turtle.left(orientation * 90)
    hilbert(turtle, length, -orientation, depth-1)

    turtle.color( COLOR[depth] )
    turtle.pensize( depth * 3 )
    turtle.forward(length)

    turtle.right(orientation * 90)
    hilbert(turtle, length, orientation, depth-1)

    turtle.color( COLOR[depth] )
    turtle.pensize( depth * 3 )
    turtle.forward(length)

    hilbert(turtle, length, orientation, depth-1)
    turtle.right(orientation * 90)

    turtle.color( COLOR[depth] )
    turtle.pensize( depth * 3 )
    turtle.forward(length)

    hilbert(turtle, length, -orientation, depth-1)
    turtle.left(orientation * 90)

screen = turtle.Screen()
flitzi = turtle.Turtle()

length = 300

for n in range(4):
  flitzi.penup()
  offset = -length * (1 - 0.5 ** (n+1))
  flitzi.goto( offset, offset )
  flitzi.pendown()

  flitzi.color( COLOR[n] )
  flitzi.pensize( 1 )

  hilbert(flitzi, length * (0.5 ** n), 1, n)

screen.exitonclick()
