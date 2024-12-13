import os
import time

class position:
    def __init__(self, row, column, character):
        self.row = row
        self.column = column
        self.character = character

    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def getCharacter(self):
        return self.character
    
    def changeCharacter(self):
        self.character = 'o'

class Map:
    positions_explored = []
    current_position = ""
    movement_direction = 'up'

    def __init__(self, input):
        self.map = []
        with open(input, 'r') as f:
            read = f.readlines()
        for row, line in enumerate(read):
            for column, character in enumerate(line.strip()):
                self.map.append(position(row, column, character))

        for i in self.map:
            if i.getCharacter() == "^":
                Map.current_position = (i.getRow(), i.getColumn())
    

    def print_map(self):
        # time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(0, 16900, 130):
            line = self.map[i:i+130]
            line_string = ""
            for j in line:
                line_string += j.getCharacter()
            print(line_string)
    
    def update_position(self, new_row, new_column):
        for i, v in enumerate(self.map):
            if v.getRow() == new_row and v.getColumn() == new_column:
                self.map[i].changeCharacter()
                Map.current_position = (new_row, new_column)
                if v not in Map.positions_explored:
                    Map.positions_explored.append(v)
    
    def update_explored_positions(self, new_position):
        Map.positions_explored.append(new_position)

    def get_current_position(self):
        return Map.current_position
    
    def define_next_move(self, direction_check):
        currentRow = Map.current_position[0]
        currentColumn = Map.current_position[1]

        for i in self.map:

            if direction_check == "up" and (i.getRow() == currentRow - 1) and (i.getColumn() == currentColumn) and (i.getCharacter() == '#'):
                Map.movement_direction = 'right'
            elif direction_check == "right" and (i.getRow() == currentRow) and (i.getColumn() == currentColumn + 1) and (i.getCharacter() == '#'):
                Map.movement_direction = 'down'
            elif direction_check == "down" and (i.getRow() == currentRow + 1) and (i.getColumn() == currentColumn) and (i.getCharacter() == '#'):
                Map.movement_direction = 'left'
            elif direction_check == "left" and (i.getRow() == currentRow) and (i.getColumn() == currentColumn - 1) and (i.getCharacter() == '#'):
                Map.movement_direction = 'up'
        
        return Map.movement_direction

    def move_by_direction(self, direction):
        if direction == 'up':
            new_move = (Map.current_position[0] - 1, Map.current_position[1])
        elif direction == 'right':
            new_move = (Map.current_position[0], Map.current_position[1] + 1)
        elif direction == 'down':
            new_move = (Map.current_position[0] + 1, Map.current_position[1])
        elif direction == 'left':
            new_move = (Map.current_position[0] , Map.current_position[1] - 1)

        return new_move


        
u = Map("input.txt")
u.print_map()
print(" ")
next_move = u.move_by_direction("up")
while (next_move[0] >= 0 and next_move[0] <= 129) and (next_move[1] >= 0 and next_move[1] <= 129):
    u.update_position(next_move[0], next_move[1])
    direction = u.define_next_move(u.movement_direction)
    next_move = u.move_by_direction(direction)
    u.print_map()
    print('')

print("Number of distinct positions:", len(u.positions_explored))
