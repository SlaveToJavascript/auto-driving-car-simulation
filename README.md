# Auto Driving Car Simulation
This is a simple car simulation program.

## Project description
The Auto Driving Car Simulation is a command-line program that simulates an autonomous car in a rectangular field. The simulation includes features like multiple car handling, collision detection, and various car commands. It provides an engaging platform for testing different scenarios in autonomous driving.

## Features
- Rectangular field simulation with customizable dimensions.
- Multiple autonomous cars with unique identifiers.
- Command-based car movement (Left, Right, Forward).
- Collision detection and handling in multi-car scenarios.
- Interactive command-line user interface.

## Instructions to Run the Application

### Environment
- Operating System: The application is platform-independent and can be run on Windows, Linux, or macOS
- Python: Python 3.x is required. Python3 can be installed from [here](https://www.python.org/downloads/)

### Steps
1. Open a terminal (MacOS) or command prompt (Windows) and navigate to the auto-driving-car-simulation directory.
```bash
cd path/to/auto-driving-car-simulation
```
2. Execute the main.py script located inside the src directory
```bash
python3 src/main.py
```
3. To run tests: navigate to the tests directory in auto-driving-car-simulation and execute the test files
```bash
cd tests
python3 -m unittest test_car.py
python3 -m unittest test_field.py
```
