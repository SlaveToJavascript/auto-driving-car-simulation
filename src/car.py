class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction):
        self.name = name # e.g. A
        self.x = x # e.g. 1
        self.y = y # e.g. 2
        self.direction = direction # e.g. N
        self.commands = [] # e.g. ['F', 'F', 'R', 'F', 'F', 'F', 'F', 'R', 'R', 'L']
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
                # -1 decreases index in DIRECTIONS array by 1 -> the new index is the direction in DIRECTION array after car turns 90º to the left
                # % 4: index wraps around to the end of the list if it goes below 0
                    # e.g. original direction = N, after index-1 in DIRECTIONS, new direction = W
        
        elif command == 'R':
            self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) + 1) % 4]
                # +1 increases index in DIRECTIONS array by 1 -> the new index is the direction in DIRECTION array after car turns 90º to the right
                # % 4: index wraps around to the start of the list if it goes above last index
                    # e.g. original direction = W, after index+1 in DIRECTIONS, new direction = N
        
        self.steps_taken += 1