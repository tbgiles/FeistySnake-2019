from astar import AStar
from helper import Helper

class State_Grow():

    # width = data.get("width")
    # height = data.get("height")
    # food = data.get("food").get("data") #Array
    # snakes = data.get("snakes").get("data") #Array
    # you = data.get("you")
    # myHealth = you.get("health")
    # myLength = you.get("body").get("length")
    # mySnake = you.get("body").get("data")
    # myID = you.get("id")

    def __init__(self):
        self.name = "grow state"

    def get_move(self, grid_data, data):
        self.height = data.get("board").get("height")
        self.width = data.get("board").get("width")
        self.head_x = data.get("you").get("body")[0].get("x")
        self.head_y = data.get("you").get("body")[0].get("y")
        self.my_snake_health = data.get("you").get("health")
        self.my_snake_length = len(data.get("you").get("body"))
        self.pathfinder = AStar((self.head_x, self.head_y), grid_data[0], self.width, self.height)
        self.grid_data = grid_data
        self.data = data

        move = self.move_to_food()

        #NOTE FIND TAIL MODE
        # if self.my_snake_length > 3 and self.my_snake_health > 75 or move == None: #85
        #     move = chase_tail(self.my_snake_health == 100)

        if move:
            return move
        else:
            move = self.chase_tail(self.my_snake_health == 100)
            if move:
                return move
            else:
                neighbours = self.helper.get_last_resort((self.head_x, self.head_y), grid_data[0], self.height, self.width)
                if neighbours:
                    return self.helper.get_move_letter((self.head_x, self.head_y), neighbours[0])
                else:
                    # Snake will almost certainly die
                    return 'up'


    def move_to_food(self):
        food_list = self.grid_data[1]
        current_minimum = float('inf')
        current_path = None
        for food in food_list:
            path = self.pathfinder.compute_path((self.head_x, self.head_y), tuple(food))
            if path:
                path = list(path)
                if len(path) < current_minimum:
                    current_minimum = len(path)
                    current_path = path
        if current_path:
            return Helper.get_move_letter((self.head_x, self.head_y), list(current_path)[1])
        return None

    def chase_tail(self, isGonnaGrow):
        my_tail = (self.data.get("you").get("body")[-1].get("x"), self.data.get("you").get("body")[-1].get("y"))
        self.grid_data[0][my_tail[1]][my_tail[0]] = 1
        path = self.pathfinder.compute_path((self.head_x, self.head_y), my_tail)
        self.grid_data[0][my_tail[1]][my_tail[0]] = 0
        if path:
            if not isGonnaGrow:
                return get_move_letter((self.head_x, self.head_y), list(path)[1])
            else:
                neighbours = Helper.get_neighbors(my_tail, self.grid_data[0], self.height, self.width)
                for neighbour in neighbours:
                    path = self.pathfinder.compute_path((self.head_x, self.head_y), neighbour)
                    if path:
                        return Helper.get_move_letter((self.head_x, self.head_y), list(path)[1])
        return None
