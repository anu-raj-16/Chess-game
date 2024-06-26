import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.SysFont('fonts/8-bit Arcade Out.ttf', 20)
big_font = pygame.font.SysFont('fonts/8-bit Arcade Out.ttf', 50)
timer = pygame.time.Clock()
fps = 60

            
 # chess pieces 
 # 8x8 board                
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]


#captured pieces 
captured_white_pieces  = []
captured_black_pieces  = []

# 0 - white's turn, no selection
# 1 - white's turn, piece selected
# 2 - black's turn, no selection
# 3 - black's turn, piece selected
game_phase = 0 # to check which phase the piece is in 
selection = 10
valid_moves = []

# game pieces : queen, king, bishop, knight, pawn 


# black pieces 

#loading the piece 
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80)) # bigger version of the piece 

# smaller version of the piece 
black_queen_small = pygame.transform.scale(black_queen, (45, 45))


# doing the same for the rest of the pieces
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))


# white pieces 
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))



#lists 
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]


black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]


piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']


def draw_board():
    for i in range(32): #representing the 32 squares of the board that need to be drawn.
        column = i % 4 #calculates the column (0 to 3) for the square.
        row = i // 4 #calculates the row (0 to 7) for the square.
        #ensures that the light gray squares alternate correctly on the board
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100]) #gray rectangle-bottom of the screen 
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5) #gold border-gray rectangle
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5) #gold border-right side of the screen
        #message corresponding to the current game phase is rendered 
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[game_phase], True, 'black'), (20, 820))

        #drawing grid lines
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)

        #displays forfeit button   
        screen.blit(big_font.render('FORFEIT', True, 'black'), (810, 830))

# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)): # we do not write 16 because the pieces might get eliminated in the midst of the game
        index = piece_list.index(white_pieces[i])
        # stores the index of the piece (taken from the list white_pieces) in the piece_list
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
            # we're typing in the position of the pawn separately as it is smaller than the rest of the pieces
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if game_phase < 2: # this is to highlight the piece selected by the user. If game pahse is less than two, 
                           # it is the whtie player's turn.
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        # stores the index of the piece (taken from the list black_pieces) in the piece_list
        if black_pieces[i] == "pawn":
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if game_phase >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

# check for valid moves for just selected piece
def check_valid_moves():
    if game_phase < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# draw valid moves on screen
def draw_valid(moves):
    if game_phase < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range (len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50, 5))

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)


    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False

    pygame.display.flip()
pygame.quit()