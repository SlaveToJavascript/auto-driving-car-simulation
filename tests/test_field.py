import unittest
import sys
sys.path.append('../src/')

from car import Car
from field import Field

class TestField(unittest.TestCase):
    # A, (1,2) N, FFRFFFFRRL
    # B, (7,8) W, FFLFFFFFFF
    def setUp(self):
        self.field = Field(10, 10)
        self.carA = Car("A", 1, 2, "N")
        self.carB = Car("B", 7, 8, "W")

    def test_add_car(self):
        # add car A
        self.field.add_car(self.carA)
        self.assertIn(self.carA, self.field.cars)

        # add car B
        self.field.add_car(self.carB)
        self.assertIn(self.carB, self.field.cars)

    def test_collision(self):
        # move car B to collide with car A
        self.carB.x = 1
        self.carB.y = 2
        self.field.add_car(self.carA)
        self.field.add_car(self.carB)
        
        colliding_cars = self.field.check_collision(1, 2)
        self.assertIn(self.carA, colliding_cars)
        self.assertIn(self.carB, colliding_cars)

    def test_car_command(self): # checks if car is in the correct position after command
        self.field.add_car(self.carA)
        self.carA.execute_command('F', self.field) # move north
        self.assertEqual(self.carA.x, 1)
        self.assertEqual(self.carA.y, 3)

        self.field.add_car(self.carB)
        self.carB.execute_command('F', self.field) # move west
        self.assertEqual(self.carB.x, 6)
        self.assertEqual(self.carB.y, 8)
    
    def test_boundary_check_true(self):
        self.assertTrue(self.field.is_within_boundary(0, 0))
        
    def test_boundary_check_false(self): # out of bounds check
        self.assertFalse(self.field.is_within_boundary(-1, 0))
        self.assertFalse(self.field.is_within_boundary(11, 11))

if __name__ == '__main__':
    unittest.main()