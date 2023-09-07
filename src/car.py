class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = []
        self.steps_taken = 0

    def add_command(self, command):
        self.commands.append(command)

    def execute_command(self, command, field):
        if command == 'F': # forward
            if self.direction == 'N':
                self.y += 1
            elif self.direction == 'E':
                self.x += 1
            elif self.direction == 'S':
                self.y -= 1
            elif self.direction == 'W':
                self.x -= 1
        
        elif command == 'L': # left
            self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) - 1) % 4]
        
        elif command == 'R':
            self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) + 1) % 4]
        
        self.steps_taken += 1