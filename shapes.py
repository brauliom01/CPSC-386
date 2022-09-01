#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: brauliom01
"""
import math

def print_message(msg, end=False):
    if not end: 
        print()
    print('=' * 50)
    print(msg)
    print('=' * 50)
class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    def __repr__(self):           # __repr__ means represent (2 underscores before/after)
        return f'({self.x},{self.y})'
    def move_to(self, x, y): 
        self.x, self.y = x, y
    def move_by(self, deltax, deltay):
        self.x += deltax
        self.y += deltay
    @staticmethod
    def run_tests():
        print_message('RUNNING TESTS on class POINT')
        pt = Point()
        print(f'pt is {pt}')
        pt.move_to(x=10, y=20)
        print(f'pt has been moved to {pt}')
        pt.move_by(deltax=1, deltay=1)
        print(f'pt has been moved by (1, 1) to {pt}')
        pt2 = Point(x=3, y=-3)
        print(f'pt2 is {pt2}')
        pt2.move_to(x=1, y=2)
        print(f'pt2 has been moved to {pt2}')
        pt2.move_by(deltax=3, deltay=-3)
        print(f'pt2 has been moved by (3, -3) to {pt2}')
        print_message('ENDING TESTS on class POINT', end=True)

    
class Rectangle:
    
    def __init__(self, length=0, width=0, center=Point()):
        self.length, self.width, self.center = length, width, center

    def __repr__(self):
        return f'Rectangle(length={self.length},width{self.width},area={self.area():.2f},perimeter={self.perimeter():.2f},center={self.center})'

    
    def diameter(self): return math.sqrt((self.length ** 2) + (self.width ** 2))
    
    
    def area(self): return self.length * self.width
    
    def perimeter(self): return (self.length + self.width) * 2

    def inflate(self, deltal, deltaw): 
        self.length += deltal 
        self.width += deltaw

    def move_to(self, x, y): self.center.move_to(x, y)

    def move_by(self, deltax, deltay): self.center.move_by(deltax, deltay) 

    @staticmethod
    
    def run_tests():
        print_message('RUNNING TESTS on class RECTANGLE')

        r = Rectangle(length=5, width=10, center=Point())
        print(r)
        r.move_to(x=10, y=20)
        print(f'r has been moved to {r}')
        r.move_by(deltax=1, deltay=1)
        print(f'r has been moved by (1, 1) to {r}')

        r2 = Rectangle(length=10, width=20, center=Point(4, 8))
        print(r2)
        r2.move_to(x=20, y=30)
        print(f'r2 has been moved to {r2}')
        r2.move_by(deltax=2, deltay=2)
        print(f'r2 has been moved by (2, 2) to {r2}')

        print_message('ENDING TESTS on class RECTANGLE', end=True)
    
def main():
    Point.run_tests()
    Rectangle.run_tests()
    print()
            
if __name__ == '__main__':
    main()
 
# ==================================================
# OUTPUT
# ==================================================

# ==================================================
# RUNNING TESTS on class POINT
# ==================================================
# pt is (0,0)
# pt has been moved to (10,20)
# pt has been moved by (1, 1) to (11,21)
# pt2 is (3,-3)
# pt2 has been moved to (1,2)
# pt2 has been moved by (3, -3) to (4,-1)
# ==================================================
# ENDING TESTS on class POINT
# ==================================================

# ==================================================
# RUNNING TESTS on RECTANGLE
# ==================================================
# Rectangle(length=5),(width=10), area=50, perimeter=30, center=(5,10)
# r has moved to Recangle (length=5),(width=10), area=50, perimeter=30, center=(10,20)
# r has been moved by (1,1) to Rectangle(length=5),(width=10), area=50, perimeter=30, center=(11,21)
# Rectangle(length=10),(width=20), area=200, perimeter=60, center=(5,10)
# r2 has been moved to Rectangle(length=10),(width=20), area=200, perimeter=60, center=(20,30)
# r2 has been moved by (2,2) to Rectangle(length=10),(width=20), area=200, perimeter=60, center=(22,32)
# ===================================================
# ENDING TESTS on Rectangle
# ===================================================








