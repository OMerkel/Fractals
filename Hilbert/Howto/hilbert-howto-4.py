#!/usr/bin/env python3

"""
How to draw a Hilbert Curve - Step 4

In step 2 and step 3 the turtle drew the same hilbert curve in iteration n=0
Now we prepare things for the next deeper iteration
"""

import turtle

COLOR = [ 'blue', 'red' ]

def hilbert_old( turtle, length, depth ):
  if depth>=0:
    turtle.left(90)
    hilbert_old(turtle, length, depth-1)
    turtle.forward(length)
    turtle.right(90)
    hilbert_old(turtle, length, depth-1)
    turtle.forward(length)
    hilbert_old(turtle, length, depth-1)
    turtle.right(90)
    turtle.forward(length)
    hilbert_old(turtle, length, depth-1)
    turtle.left(90)

def hilbert( turtle, length, depth ):
  if depth>=0:
    turtle.left(90)
    hilbert(turtle, length, depth-1)

    turtle.color( COLOR[depth] )
    turtle.pensize( depth * 3 )
    turtle.forward(length)

    turtle.right(90)
    hilbert(turtle, length, depth-1)

    turtle.color( COLOR[depth] )
    turtle.pensize( depth * 3 )
    turtle.forward(length)

    hilbert(turtle, length, depth-1)
    turtle.right(90)

    turtle.color( COLOR[depth] )
    turtle.pensize( depth * 3 )
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

"""
Turtle draws iteration 0 as expected
"""
n = 0
hilbert_old(flitzi, length, depth = n)


flitzi.penup()
offset = -length * (0.75)
flitzi.goto( offset, offset )
flitzi.pendown()

flitzi.color( COLOR[1] )
flitzi.pensize( 1 )

"""
Now turtle draws the next iteration 1

but here we see that something must be done to
correct orientation of the U shapes

 red lines are drawn on depth 1
blue lines are drawn on depth 0

Remember the quadrants

    +-------+    +---+---+
    |       |    |   |   |
    | 2---3 |    | 2 | 3 |
    | |   | |    |   |   |
    | |   | |    +---+---+
    | |   | |    |   |   |
    | 1   4 |    | 1 | 4 |
    |       |    |   |   |
    +-------+    +---+---+

Actually we expect the blue U shapes to be drawn like

* clockwise in quadrants 2 and 3
* counterclockwise in quater 1 and 4

But the latter is still not happening
"""
n = 1
hilbert(flitzi, length/2, depth = n)

screen.exitonclick()
