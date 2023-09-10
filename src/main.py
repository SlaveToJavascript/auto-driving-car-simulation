from field import Field
from car import Car
from simulation import Simulation

def main():
    print('Welcome to Auto Driving Car Simulation!\n')

    # GET WIDTH, HEIGHT OF FIELD
    while True:
        try:
            width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
            if width > 0 and height > 0: # correct
                break
            else:
                print("Error: width and height should be positive integers. Please try again.")
        except ValueError:
            # ValueError is raised by the line "width, height = map()...", when:
                # you enter any non-integer chars except space
                # you give less/more than 2 values (not enough/too many values to unpack)
            print("Error: Input format is wrong. Please try again.")

    # e.g. width = 10, height = 10
    field = Field(width, height)
    print(f"You have created a field of {width} x {height}.\n")

    # OPTIONS: ADD CAR / RUN SIMULATION
    while True:
        print("Please choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        option = input()

        # OPTION 1: ADD CAR
        if option == "1":
            name = input("Please enter the name of the car: ")

            # GET X Y DIRECTION OF CAR
            while True:
                try:
                    x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
                    x, y = int(x), int(y)
                    if direction in ['N', 'E', 'S', 'W']: # correct
                        break
                    else:
                        print("Error: direction should be either 'N', 'E', 'S' or 'W'. Please try again.")
                except ValueError:
                    # ValueError is raised by the line "x, y, direction = input()...", when:
                        # you give less/more than 3 values (not enough/too many values to unpack)
                    # ValueError is raised by the line "x, y = int(x), int(y)", when:
                        # you enter any non-integer chars for x and y input arguments
                    print("Error: input format is wrong. Please try again.")

            car = Car(name, x, y, direction)
            
            # GET COMMANDS FOR CAR
            while True:
                commands = input(f"Please enter the commands for car {name}: ")
                if all(command in ['L', 'R', 'F'] for command in commands): # correct
                    break
                else: # if command contains chars other than L, R, F:
                    print("Error: invalid command. Please try again.")

            for command in commands: # for each command char,
                car.add_command(command) # add command char to self.commands array
            
            field.add_car(car) # adds car to field.cars array

            # PRINT ALL CARS WE HAVE NOW
            if field.cars: # if field.cars array is not empty (i.e. we have cars)
                print("Your current list of cars are:")
                for car in field.cars:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")
                print()

        # OPTION 2: RUN SIMULATION
        elif option == "2":
            if field.cars: # if field.cars array is not empty (i.e. we have cars)
                print("Your current list of cars are:")
                for car in field.cars:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")
                print()

                print("After simulation, the result is:")
                simulation = Simulation(field)
                simulation.run()
                    # if got collision, the colliding cars + colliding coords are printed
                    # if no collision, final coords of cars are printed
                print()
                
                print("Please choose from the following options:")
                print("[1] Start over")
                print("[2] Exit")
                option2 = input()

                # OPTION 1: START OVER
                if option2 == "1":
                    field.cars = [] # remove all cars we had
                    main() # start over
                
                # OPTION 2: EXIT
                elif option2 == "2":
                    print("Thank you for running the simulation. Goodbye!")
                    return
            
            # Want to run simulation but no cars are added
            else: # field.cars array is empty
                print("Error: please add at least 1 car first.\n")
                continue
        
        # INVALID OPTION
        else:
            print("Error: invalid option. Please try again.\n")
            continue

if __name__ == "__main__":
    main()