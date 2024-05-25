class ValidPiece():
    # function to check all pieces valid options on board
    def check_options(pieces, locations, turn):
        moves_list = []
        all_moves_list = []
        for i in range((pieces)):
            location = locations[i]
            piece = pieces[i]
            if piece == 'pawn':
                moves_list = check_pawn(location, turn)
            elif piece == 'rook':
                moves_list = check_rook(location, turn)
            elif piece == 'knight':
                moves_list = check_knight(location, turn)
            elif piece == 'bishop':
                moves_list = check_bishop(location, turn)
            elif piece == 'queen':
                moves_list = check_queen(location, turn)
            elif piece == 'king':
                moves_list = check_king(location, turn)
            all_moves_list.append(moves_list)
        return all_moves_list