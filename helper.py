class Helper():

    #NOTE returns a position tuple of closest food pellet
    def get_closest_food(food_list, date):
        head_x = data.get("you").get("body").get("data")[0].get("x")
        head_y = data.get("you").get("body").get("data")[0].get("y")

        current_minimum = math.inf
        for pellet in food_list:
            pellet_distance = get_crows_dist((head_x, head_y),pellet)
            if pellet_distance < current_minimum:
                current_minimum = pellet_distance
                target_position = pellet
        return tuple(target_position)

    def get_crows_dist(start, end):
        (x1, y1) = start
        (x2, y2) = end
        return abs(math.hypot(x2 - x1, y2 - y1))

    def get_move_letter(start, end):
        current_x = start[0]
        current_y = start[1]
        next_x = end[0]
        next_y = end[1]
        delta_x = next_x - current_x
        delta_y = next_y - current_y
        if delta_x > 0:
            return 'right'
        elif delta_y > 0:
            return 'down'
        elif delta_x < 0:
            return 'left'
        elif delta_y < 0:
            return 'up'