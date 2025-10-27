# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isosceles','4,4,5 is a Isosceles triangle')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(5,4,4),'Isosceles','5,4,4 is a Isosceles triangle')

    def testIsoscelesTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,4),'Isosceles','4,5,4 is a Isosceles triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(4,8,5),'Scalene','4,8,5 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(8,5,4),'Scalene','8,5,4 is a Scalene triangle')

    def testScaleneTriangleC(self): 
        self.assertEqual(classifyTriangle(5,4,8),'Scalene','5,4,8 is a Scalene triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','-1,1,1 should be an InvalidInput')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(300,1,1),'InvalidInput','300,1,1 should be an InvalidInput')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle("1",1,1),'InvalidInput','\"1\",1,1 should be an InvalidInput')

    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(2,4,8),'NotATriangle','2,4,8 should be NotATriangle')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(4,8,2),'NotATriangle','4,8,2 should be NotATriangle')

    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(8,2,4),'NotATriangle','8,2,4 should be NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

