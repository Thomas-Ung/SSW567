import unittest

def classify_triangle(a, b, c):
    if a == b == c:
        triangle_type = 'Equilateral'
    elif a == b or b == c or a == c:
        triangle_type = 'Isosceles'
    else:
        triangle_type = 'Scalene'
    
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + b ** 2 == a ** 2:
        return f'{triangle_type} and Right'
    else:
        return triangle_type

class test_classify_triangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles')
        self.assertEqual(classify_triangle(3, 2, 2), 'Isosceles')
        self.assertEqual(classify_triangle(2, 3, 2), 'Isosceles')

    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene and Right')
        self.assertEqual(classify_triangle(5, 3, 4), 'Scalene and Right')
        self.assertEqual(classify_triangle(4, 5, 3), 'Scalene and Right')

    def test_scalene(self):
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene')
        self.assertEqual(classify_triangle(4, 2, 3), 'Scalene')
        self.assertEqual(classify_triangle(3, 4, 2), 'Scalene')


if __name__ == '__main__':
    unittest.main()
