#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # About Triangle Project 2
    sides = sorted([a, b, c])
    if 0 in sides: raise TriangleError
    if True in map(lambda x: x < 0, sides): raise TriangleError
    if sides[0] + sides[1] <= sides[2]: raise TriangleError

    # About Triangle Project 1
    num_of_unequal_sides = len(set(sides))
    if num_of_unequal_sides == 1:
        return 'equilateral'
    elif num_of_unequal_sides == 2:
        return 'isosceles'
    elif num_of_unequal_sides == 3:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
