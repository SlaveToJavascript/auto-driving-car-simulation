class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def check_collision(self, x, y):
        # checks if any cars in self.cars array collides with coords x,y
        colliding_cars = [car for car in self.cars if car.x == x and car.y == y]
        return colliding_cars if len(colliding_cars) > 1 else None