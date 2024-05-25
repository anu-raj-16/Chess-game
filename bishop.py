class Bishop():
    # check valid bishop moves
    def check_bishop(position, color):
        moves_list = []
        if color == 'while':
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations

        for i in range(4): # up-right, up-left, down-right, down-left
            path = TRUE
            chain = 1
            if i == 0:
                x = 1
                y = -1
            elif i == 1:
                x = -1
                y = -1
            elif i == 2:
                x = 1
                y = 1
            else:
                x = -1
                y = 1
            while path:
                if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                        0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                    if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
                
        return moves_list
        