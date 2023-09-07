from field import Field
from car import Car
from simulation import Simulation

def main():
    print('Welcome to Auto Driving Car Simulation!\n')

    while True:
        try:
            width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
            if width > 0 and height > 0: # correct
                break
            else:
                print("Error: width and height should be positive integers. Please try again.")
        except ValueError:
            print("Error: Input format is wrong. Please try again.")

    # 10 10
    field = Field(width, height)
    print(f"You have created a field of {width} x {height}.\n")

    while True:
        print("Please choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        option = input()

        if option == "1": # add car to field
            name = input("Please enter the name of the car: ")

            # A: 1 2 N
            # B: 7 8 W
            while True:
                try:
                    x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
                    x, y = int(x), int(y)
                    if direction in ['N', 'E', 'S', 'W']: # correct
                        break
                    else:
                        print("Error: direction should be either 'N', 'E', 'S' or 'W'. Please try again.")
                except ValueError:
                    print("Error: input format is wrong. Please try again.")

            car = Car(name, x, y, direction)
            
            # A: FFRFFFFRRL
            # B: FFLFFFFFFF
            while True:
                commands = input(f"Please enter the commands for car {name}: ")
                if all(command in ['L', 'R', 'F'] for command in commands): # correct
                    break
                else:
                    print("Error: invalid command. Please try again.")

            for command in commands:
                car.add_command(command)
            field.add_car(car)

            if field.cars:
                print("Your current list of cars are:")
                for car in field.cars:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")
                print()

        elif option == "2": # run simulation
            if field.cars:
                print("Your current list of cars are:")
                for car in field.cars:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")
                print()

                print("After simulation, the result is:")
                simulation = Simulation(field)
                simulation.run()
                print()
                
                print("Please choose from the following options:")
                print("[1] Start over")
                print("[2] Exit")
                option2 = input()

                if option2 == "1": # start over
                    field.cars = []
                    main()
                elif option2 == "2": # exit
                    print("Thank you for running the simulation. Goodbye!")
                    return
            else: # no cars were added
                print("Error: please add at least 1 car first.\n")
                continue
        else: # invalid option
            print("Error: invalid option. Please try again.\n")
            continue

if __name__ == "__main__":
    main()