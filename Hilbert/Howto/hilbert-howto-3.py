#!/usr/bin/env python3

"""
How to draw a Hilbert Curve - Step 3

In step 2 the turtle drew a hilbert curve in iteration n=0
"""

import turtle

COLOR = [ 'blue' ]

def hilbert( turtle, length, depth ):
  """
  hilbert shall recursively call itself
  
  The function holds a parameter depth that is decreased on each call
  
  Reaching a negative depth value will abort the recursive calls
  """
  if depth>=0:
    """
    Each forward movement can be seen as a transition into a quadrant
    
    +-------+    +---+---+
    |       |    |   |   |
    | 2---3 |    | 2 | 3 |
    | |   | |    |   |   |
    | |   | |    +---+---+
    | |   | |    |   |   |
    | 1   4 |    | 1 | 4 |
    |       |    |   |   |
    +-------+    +---+---+
    
    Now the idea is that in one of our next 'how to' steps the
    turtle shall draw the U shape again in each deeper recursive call
    
    Per quadrant we call the recursive function
    
    The turtle moves forward between the calls
    """
    turtle.left(90)
    hilbert(turtle, length, depth-1)
    turtle.forward(length)
    turtle.right(90)
    hilbert(turtle, length, depth-1)
    turtle.forward(length)
    hilbert(turtle, length, depth-1)
    turtle.right(90)
    turtle.forward(length)
    hilbert(turtle, length, depth-1)
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

n = 0
hilbert(flitzi, length, depth = n)

screen.exitonclick()
