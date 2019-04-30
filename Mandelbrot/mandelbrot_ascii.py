#!/usr/bin/env python3

class MyCanvas:
  def __init__(self, size):
    (x, y) = size
    self.canvas = []
    for n in range(y):
      self.canvas.append(list(" " * x))

  def point(self, p, c):
    (x, y) = p
    self.canvas[len(self.canvas)-1-y][x] = c

  def flush(self):
    for n in range(len(self.canvas)):
      print(''.join(self.canvas[n]))

class Mandelbrot:
  def __init__(self, area, maxiter=26, maxcolor=26):
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
    bailout = 2.0
    z = c
    for i in range(maxiter):
      if abs(z) > bailout:
        return i
      z = z**2 + c
    return maxiter

if __name__ == "__main__":
  # Mandelbrot( area=((0.065053, -0.74877), (0.065103, -0.74872)), maxiter=2048, maxcolor=12 )
  Mandelbrot( area=((-1.3, -2.0), (1.3, 0.65)) )
  # Mandelbrot( area=((-2.0, -2.5), (2.0, 2.0)) )
