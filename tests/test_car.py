import unittest
import sys
sys.path.append('../src/')

from car import Car
from field import Field

class TestCar(unittest.TestCase):
    # A, (1,2) N, FFRFFFFRRL
    # B, (7,8) W, FFLFFFFFFF
    def setUp(self):
        self.field = Field(10, 10)
        self.carA = Car("A", 1, 2, "N")
        self.carB = Car("B", 7, 8, "W")
        self.field.add_car(self.carA)
        self.field.add_car(self.carB)

    def test_simulation(self):
        commands = "FFRFFFFRRL"
        for command in commands:
            self.carA.execute_command(command, self.field)
        
        # check final position and direction
        self.assertEqual(self.carA.x, 5)
        self.assertEqual(self.carA.y, 4)
        self.assertEqual(self.carA.direction, "S")

    def test_collision(self):
        commands_a = "FFRFFFFRRL"
        commands_b = "FFLFFFFFFF"

        for i in range(max(len(commands_a), len(commands_b))):
            if i < len(commands_a):
                self.carA.execute_command(commands_a[i], self.field)
            if i < len(commands_b):
                self.carB.execute_command(commands_b[i], self.field)
            
            collision = self.field.check_collision(self.carA.x, self.carA.y)
            if collision:
                # check position of collision
                self.assertEqual(self.carA.x, 5)
                self.assertEqual(self.carA.y, 4)

                # check no. of steps to collision
                self.assertEqual(i + 1, 7) # i+1 since i starts from 0
                break

if __name__ == '__main__':
    unittest.main()