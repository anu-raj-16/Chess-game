class ValidRookMoves():
    def check_rook(posiiton,color):
        moves_list =[]
        if color == 'white':
            enemies_list = black_locations
            friends_list = white_locations

        else:
            enemies_list = black_locations
            friends_list = white_locations

        for i in range(4):  # down, up, right, left
            path = True
            chain = 1
            if i == 0:
                x = 0
                y = 1
            elif i == 1:
                x = 0
                y = -1
            elif i == 2:
                x = 1
                y = 0
            else:
                x = -1
                y = 0
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
