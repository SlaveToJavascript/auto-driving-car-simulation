class Simulation:
    def __init__(self, field):
        self.field = field

    def run(self):
        # orchestrates simulation based on commands assigned to each car
        # checks for collisions at each step
        max_commands = max(len(car.commands) for car in self.field.cars) # calculates the max no. of commands among all cars -> so we know how many iterations the simulation needs to run, ensuring all commands of all cars are executed
        
        for i in range(max_commands): # iterates through each command for each car
            for car in self.field.cars:
                if i < len(car.commands):
                    command = car.commands[i]
                    car.execute_command(command, self.field) # execute each command for each car

            # CHECK FOR COLLISIONS AFTER ALL CARS MOVED CURRENT STEP
            pos_after_move = {}
                # key = coords (x, y)
                # value = list of cars at that coord (x,y)
            for car in self.field.cars:
                if (car.x, car.y) not in pos_after_move:
                    pos_after_move[(car.x, car.y)] = [car] # add each car to pos_after_move hashmap at their respective coords (x,y)
                else:
                    pos_after_move[(car.x, car.y)].append(car)

            for position, cars in pos_after_move.items():
                if len(cars) > 1: # if there's more than 1 car at the same coords, there is collision
                    for car in cars:
                        colliding_cars = [c for c in cars if c != car] # add each collided car to array
                        for colliding_car in colliding_cars:
                            print(f"- {car.name}, collides with {colliding_car.name} at {position} at step {car.steps_taken}") # report each collided car by printing it
                    return # if there are colliding cars, we end function here and do not go to the next few lines where, if no collisions, we print final positions of cars

        # no collisions -> print final positions of cars
        for car in self.field.cars:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")