#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sierpinski

Drawing a Sierpinski triangle step by step.

Third Party Dependencies:
    Computer Vision Library OpenCV, https://opencv.org/

Copyright (c) 2023, Oliver Merkel.
Please see the AUTHORS file for details.
All rights reserved.

Use of this code is governed by a
MIT license that can be found in the LICENSE file.
"""
import numpy as np
import cv2
import random

major, minor, patchlevel = cv2.__version__.split(".")
assert major == "4", "Could not import OpenCV version 4"

class Sierpinski:
  def __init__(self):
    self.corner = [ (256,0), (0,511), (511,511) ]
    self.cursor = { 'x': 100, 'y': 100 }

  def run(self):
    imgTriangle = np.zeros((512,512,3), np.uint8)
    cv2.line(imgTriangle, self.corner[0], self.corner[1],(255,0,0), 1)
    cv2.line(imgTriangle, self.corner[1], self.corner[2],(255,0,0), 1)
    cv2.line(imgTriangle, self.corner[2], self.corner[0],(255,0,0), 1)
    key = 0
    cv2.imshow("Sierpinski", imgTriangle)
    while key!=27:
      if key==32:
        randomCorner = random.choice(self.corner)
        imgTriangle[self.cursor['y'], self.cursor['x']] = (0,0,255)
        imgOverlay = imgTriangle.copy()
        cv2.line(imgOverlay,(self.cursor['x'], self.cursor['y']),randomCorner,(255,255,255),1)
        cv2.circle(imgOverlay,(self.cursor['x'], self.cursor['y']),4,(0,255,255),-1)
        cv2.circle(imgOverlay, randomCorner, 4, (0,255,255),-1)
        self.cursor = {
          'x': int((self.cursor['x']+randomCorner[0])/2),
          'y': int((self.cursor['y']+randomCorner[1])/2) }
        # imgOverlay[self.cursor['y'], self.cursor['x']] = (0,0,255)
        cv2.circle(imgOverlay,(self.cursor['x'], self.cursor['y']),4,(0,0,255),-1)
        cv2.imshow("SierpinskiOverlay", imgOverlay)
        cv2.imshow("Sierpinski", imgTriangle)
      key = cv2.waitKey(1) & 0xff

if '__main__' == __name__:
  instance = Sierpinski()
  instance.run()
