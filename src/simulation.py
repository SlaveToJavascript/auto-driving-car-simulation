class Simulation:
    def __init__(self, field):
        self.field = field

    def run(self):
        max_commands = max(len(car.commands) for car in self.field.cars)
        for i in range(max_commands):
            # move car for current step
            for car in self.field.cars:
                if i < len(car.commands):
                    command = car.commands[i]
                    car.execute_command(command, self.field)

            # check for collisions after all cars moved current step
            pos_after_move = {}
            for car in self.field.cars:
                if (car.x, car.y) not in pos_after_move:
                    pos_after_move[(car.x, car.y)] = [car]
                else:
                    pos_after_move[(car.x, car.y)].append(car)

            for position, cars in pos_after_move.items():
                if len(cars) > 1:  # got collision
                    for car in cars:
                        colliding_cars = [c for c in cars if c != car]
                        for colliding_car in colliding_cars:
                            print(f"- {car.name}, collides with {colliding_car.name} at {position} at step {car.steps_taken}")
                    return

        # no collisions -> print final positions of cars
        for car in self.field.cars:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")