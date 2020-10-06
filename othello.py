'''
James Ronderos
'''

from tkinter import *
from tkinter import messagebox
from math import *
from time import *
from random import *
from copy import deepcopy

depth = 6
nodes = 0  # for checking path later
moves = 0
player_choice = 0
start_points = 0  # starting pieces on the board
new_move = [-1, -1]
ai_new_move = [-1, -1]


# for scaling later
# screen_height
sh = 900
# screen_width
sw = 0.8333 * sh
per = sh / 600  # Scaling percent

# Tkinter info and images
root = Tk()
screen = Canvas(root, width=sw, height=sh, background="#7B7D7D", highlightthickness=0)
screen.pack(fill="both", expand=True)


class Board:
    def __init__(self):
        # set player to 1 for black, black goes first
        self.player = 1
        self.passed = False
        self.won = False
        self.ai_on = True
        self.var = IntVar()
        self.confirm_check = 0
        # Initializing an empty board
        self.array = []
        for x in range(8):
            self.array.append([])
            for y in range(8):
                self.array[x].append(None)

        # Initializing center values
        if start_points == 0:
            self.array[3][3] = "w"
            self.array[3][4] = "b"
            self.array[4][3] = "b"
            self.array[4][4] = "w"
        else:
            self.array[3][3] = "b"
            self.array[3][4] = "w"
            self.array[4][3] = "w"
            self.array[4][4] = "b"

        # backup array values
        self.back_board = self.array
        self.turn_back_player = deepcopy(self.array)  # for going back a turn
        self.turn_back_ai = deepcopy(self.array)  # for going back a turn
        self.turn_back_player2 = deepcopy(self.array)  # for going back a turn
        self.turn_back_ai2 = deepcopy(self.array)  # for going back a turn
        # self.turn_back_player3 = self.array  # for going back a turn
        # self.turn_back_ai3 = self.array  # for going back a turn

    def confirm(self):
        self.confirm_check = 1
        sr1 = 54 * per
        sr2 = 96 * per
        sr3 = 50 * per

        for x in range(8):
            for y in range(8):
                if self.back_board[x][y] == "w":
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y,
                                       tags="{0}-{1}".format(x, y), fill="white", outline="black")

                elif self.back_board[x][y] == "b":
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y,
                                       tags="{0}-{1}".format(x, y), fill="black", outline="black")

        # screen.update()
        # change color after choice
        for x in range(8):
            for y in range(8):
                if self.array[x][y] != self.back_board[x][y] and self.array[x][y] == "w":
                    screen.delete("{0}-{1}".format(x, y))
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="tile",
                                       fill="white",
                                       outline="black")

        for x in range(8):
            for y in range(8):
                if self.array[x][y] != self.back_board[x][y] and self.array[x][y] == "b":
                    screen.delete("{0}-{1}".format(x, y))
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="tile",
                                       fill="black",
                                       outline="black")

        # print("confirmed")

    # Update board with Tkinter // piece colors
    def update(self):
        global new_move, player_choice, ai_new_move
        sr1 = 54 * per
        sr2 = 96 * per
        sr3 = 50 * per
        sr4 = 68 * per
        sr5 = 32 * per
        screen.delete("highlight")
        screen.delete("newpiece")
        screen.delete("tile")
        screen.delete("turn")
        if self.player is 1:
            screen.create_text(sw * .50, sh * .9, anchor="c",
                               text="Black Turn",
                               font=("Helvetica", 30), tags="turn", fill="black")
        else:
            screen.create_text(sw * .50, sh * .9, anchor="c",
                               text="White Turn",
                               font=("Helvetica", 30), tags="turn", fill="white")
        # print(player_choice)
        for x in range(8):
            for y in range(8):
                if self.back_board[x][y] == "w":
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y,
                                       tags="tile {0}-{1}".format(x, y), fill="white", outline="black")

                elif self.back_board[x][y] == "b":
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y,
                                       tags="tile {0}-{1}".format(x, y), fill="black", outline="black")

        # change color after choice
        for x in range(8):
            for y in range(8):
                if self.array[x][y] != self.back_board[x][y] and self.array[x][y] == "w":
                    screen.delete("{0}-{1}".format(x, y))
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="tile", fill="orange",
                                       outline="black")
                if player_choice != self.player and self.player == 1:
                    if x is new_move[0] and y is new_move[1]:
                        screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="newpiece",
                                           fill="red",
                                           outline="black")
                if player_choice == self.player and self.player == 1:
                    if x is ai_new_move[0] and y is ai_new_move[1]:
                        screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="newpiece",
                                           fill="red",
                                           outline="black")
        for x in range(8):
            for y in range(8):
                if self.array[x][y] != self.back_board[x][y] and self.array[x][y] == "b": # and self.player == player_choice:
                    screen.delete("{0}-{1}".format(x, y))
                    screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="tile", fill="blue",
                                       outline="black")
                if player_choice != self.player and self.player == 0:
                    if x is new_move[0] and y is new_move[1]:
                        screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="newpiece",
                                           fill="green",
                                           outline="black")
                if player_choice == self.player and self.player == 0:
                    if x is ai_new_move[0] and y is ai_new_move[1]:
                        screen.create_oval(sr1 + sr3 * x, sr1 + sr3 * y, sr2 + sr3 * x, sr2 + sr3 * y, tags="newpiece",
                                           fill="green",
                                           outline="black")

        # Display possible move circles
        for x in range(8):
            for y in range(8):
                # Maybe add text
                # Player possible moves
                if self.player is player_choice:
                    if valid_move(self.array, self.player, x, y):
                        screen.create_oval(sr4 + sr3 * x, sr4 + sr3 * y, sr5 + sr3 * (x + 1), sr5 + sr3 * (y + 1),
                                           tags="highlight", fill="blue", outline="green")
                # AI possible moves
                if self.player is not player_choice:
                    if valid_move(self.array, self.player, x, y):
                        screen.create_oval(sr4 + sr3 * x, sr4 + sr3 * y, sr5 + sr3 * (x + 1), sr5 + sr3 * (y + 1),
                                           tags="highlight", fill="red", outline="green")

        if not self.won:
            # Draw the scoreboard and update the screen
            self.show_scores()
            screen.update()
            self.confirm_check = 0
            # confirm button interrupt
            self.var = IntVar()
            button = Button(root, text="Confirm", command=lambda: [self.var.set(1), self.confirm()])
            button.config(height=3, width=20)
            button.place(relx=.5, rely=.846, anchor="c")

            # Confirm button
            # print("waiting for confirmation")
            button.wait_variable(self.var)
            # print("Confirmed.")
            # If the computer is AI, make a move
            if self.ai_on is True:
                if self.player != player_choice:
                    startTime = time()
                    self.turn_back_ai = deepcopy(self.array)  # for stepping back a turn
                    self.turn_back_ai2 = deepcopy(self.back_board)

                    self.back_board = self.array
                    alphaBetaResult = self.alpha_beta_prune(self.array, depth, -float("inf"), float("inf"), 1)
                    self.array = alphaBetaResult[1]

                    if len(alphaBetaResult) >= 3:
                        ai_new_move = alphaBetaResult[2]  # Get AI move coords

                    if len(alphaBetaResult) == 3:
                        # print("test")
                        position = alphaBetaResult[2]
                        self.back_board[position[0]][position[1]] = "b"

                    if self.player is 1:
                        self.player = 0
                    elif self.player is 0:
                        self.player = 1
                    deltaTime = round((time() - startTime) * 100) / 100

                    print("Turn time: " + str(deltaTime))
                    # check if pass is required
                    self.check_pass()
        else:
            screen.create_text(sw * .75, sh * .85, anchor="c", font=("Helvetica", 20), fill="red", text="Game over!")

    # update board with player click moves and player switch
    def update_board(self, x, y):
        global new_move
        # self.turn_back_player = self.array
        # self.turn_back_player2 = self.back_board
        new_move = [x, y]
        self.back_board = self.array
        if player_choice == 0:
            self.back_board[x][y] = "w"
            self.array = move(self.array, x, y)
        if player_choice == 1:
            self.back_board[x][y] = "b"
            self.array = move(self.array, x, y)

        # Switch Player
        if self.player is 1:
            self.player = 0
        elif self.player is 0:
            self.player = 1
        self.update()

        # Check if player has to pass
        self.check_pass()
        self.update()

    # Print scores on screen with Tkinter
    def show_scores(self):
        global moves
        screen.delete("score")
        screen.delete("pass")

        # Count all tiles to find score
        player_score = 0
        computer_score = 0
        for x in range(8):
            for y in range(8):
                if self.array[x][y] == "w":
                    player_score += 1
                elif self.array[x][y] == "b":
                    computer_score += 1

        if player_choice == 1:
            player_color = "white"
            computer_color = "black"
            screen.create_oval(sw * .01, sh * .9, sw * .05, sh * .933, fill=player_color, outline=player_color)  # left side
            screen.create_oval(sw * .86, sh * .9, sw * .9, sh * .933, fill=computer_color, outline=computer_color)  # right side

            # Print score numbers to screen
            screen.create_text(sw * .06, sh * .916, anchor="w", tags="score", font=("Helvetica", 50), fill=player_color,  # left side
                               text=player_score)
            screen.create_text(sw * .9, sh * .916, anchor="w", tags="score", font=("Helvetica", 50), fill=computer_color,  # right side
                               text=computer_score)
        else:
            player_color = "white"
            computer_color = "black"
            screen.create_oval(sw * .01, sh * .9, sw * .05, sh * .933, fill=player_color, outline=player_color)
            screen.create_oval(sw * .86, sh * .9, sw * .9, sh * .933, fill=computer_color, outline=computer_color)

            # Print score numbers to screen
            screen.create_text(sw * .06, sh * .916, anchor="w", tags="score", font=("Helvetica", 50), fill="white",
                               text=player_score)
            screen.create_text(sw * .9, sh * .916, anchor="w", tags="score", font=("Helvetica", 50), fill="black",
                               text=computer_score)

        moves = player_score + computer_score

    # check if pass is required
    def check_pass(self):
        cpass = True
        for x in range(8):
            for y in range(8):
                if valid_move(self.array, self.player, x, y):
                    cpass = False
        if cpass:
            if self.player is 1:
                self.player = 0
            elif self.player is 0:
                self.player = 1
            if self.passed is True:
                self.won = True
            else:
                self.passed = True
                print("Nowhere to move, had to pass.")
                screen.create_text(sw * .06, sh * .85, anchor="w", tags="pass", font=("Helvetica", 40), fill="red", text="Passed")
            self.update()
        else:
            self.passed = False

        self.update()

    # Alpha Beta Pruning
    def alpha_beta_prune(self, node, depth, alpha, beta, maximizing):
        global nodes
        nodes += 1
        boards = []
        possible_moves = []

        for x in range(8):
            for y in range(8):
                if valid_move(self.array, self.player, x, y):
                    test = move(node, x, y)
                    boards.append(test)
                    possible_moves.append([x, y])

        if depth == 0 or len(possible_moves) == 0:
            return [score_heur(node), node]
        # Maximizing
        if maximizing:
            value = -float("inf")
            bestBoard = []
            bestChoice = []
            for board in boards:
                boardValue = self.alpha_beta_prune(board, depth - 1, alpha, beta, 0)[0]
                if boardValue > value:
                    value = boardValue
                    bestBoard = board
                    bestChoice = possible_moves[boards.index(board)]
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return [value, bestBoard, bestChoice]
        # Minimizing
        else:
            value = float("inf")
            bestBoard = []
            bestChoice = []
            for board in boards:
                boardValue = self.alpha_beta_prune(board, depth - 1, alpha, beta, 1)[0]
                if boardValue < value:
                    value = boardValue
                    bestBoard = board
                    bestChoice = possible_moves[boards.index(board)]
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return [value, bestBoard, bestChoice]


# board after making a move
def move(passedArray, x, y):
    # Copy the passedArray so as not to alter the original
    array = deepcopy(passedArray)
    # Set color and set the moved location to be that color
    if board.player == 0:
        color = "w"
    else:
        color = "b"
    array[x][y] = color

    # neighbors
    neighbors = []
    for i in range(max(0, x - 1), min(x + 2, 8)):
        for j in range(max(0, y - 1), min(y + 2, 8)):
            if array[i][j] is not None:
                neighbors.append([i, j])

    # Which tiles to convert
    convert = []

    # check if neighbors make a line to convert
    for neighbor in neighbors:
        neighX = neighbor[0]
        neighY = neighbor[1]
        if array[neighX][neighY] != color:
            # The path of each individual line
            path = []

            # Determining direction to move
            deltaX = neighX - x
            deltaY = neighY - y

            tempX = neighX
            tempY = neighY

            while 0 <= tempX <= 7 and 0 <= tempY <= 7:
                path.append([tempX, tempY])
                value = array[tempX][tempY]
                # check for blank tile
                if value is None:
                    break
                if value == color:
                    for node in path:
                        convert.append(node)
                    break
                # Move the tile
                tempX += deltaX
                tempY += deltaY

    # Convert all the appropriate tiles
    for node in convert:
        array[node[0]][node[1]] = color

    return array


# Draw grids and outline
def display_bg():
    # print("funk9")
    screen.create_rectangle(sw * .1, sh * .08333, sw * .9, sh * .75, outline="#111")
    letters = ['A','B','C','D','E','F','G','H']
    numbers = ['1','2','3','4','5','6','7','8']

    screen.create_text(sw * .05, sh * .8, anchor="w", text="'Q' to Quit, 'R' to Restart, and 'Z' to change starting board state.", font=("Helvetica", 13), fill="white")

    # Drawing the board lines
    for i in range(7):
        grid_spacer = (sw * .1) + (sw * .1) * (i + 1)

        screen.create_text(grid_spacer - 50, sh * .08333 - 20, anchor="w", text=str(letters[i]), font=("Helvetica", 30), fill="white")
        screen.create_text(sw * .1 - 30, grid_spacer - 50, anchor="w", text=str(numbers[i]), font=("Helvetica", 30), fill="white")

        if i == 6:
            screen.create_text(grid_spacer + 20, sh * .08333 - 20, anchor="w", text=str(letters[i+1]),
                               font=("Helvetica", 30), fill="white")
            screen.create_text(sw * .1 - 30, grid_spacer + 40, anchor="w", text=str(numbers[i+1]),
                               font=("Helvetica", 30), fill="white")

        # Horizontal line
        screen.create_line(sw * .1, grid_spacer, sw * .9, grid_spacer, fill="#111")

        # Vertical line
        screen.create_line(grid_spacer, sh * .08333, grid_spacer, sh * .75, fill="#111")

    screen.update()


# Heuristic to aim for corners & edges
def score_heur(array):
    score = 0
    # Set player and opponent colors
    if player_choice == 1:
        color = "b"
        opponent = "w"
    else:
        color = "w"
        opponent = "b"
    # Go through all the tiles
    for x in range(8):
        for y in range(8):
            # Normal tiles worth 1
            add = 1
            # Edge tiles worth 3
            if (x == 0 and 1 < y < 6) or (x == 7 and 1 < y < 6) or (y == 0 and 1 < x < 6) or (y == 7 and 1 < x < 6):
                add = 3
            # Corner tiles worth 5
            elif (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                add = 5
            # tally score
            if array[x][y] == color:
                score += add
            elif array[x][y] == opponent:
                score -= add
    return score


# Checks if a move is valid for a given array.
def valid_move(array, player, x, y):
    # Sets player color
    if player == 0:
        color = "w"
    else:
        color = "b"

    if array[x][y] is not None:
        return False

    else:
        # Generating the list of neighbors
        neighbor = False
        neighbors = []
        for i in range(max(0, x - 1), min(x + 2, 8)):
            for j in range(max(0, y - 1), min(y + 2, 8)):
                if array[i][j] is not None:
                    neighbor = True
                    neighbors.append([i, j])
        # check for neighbors
        screen.update()
        if not neighbor:
            return False
        else:
            # check neighbors to see if we can make a line
            valid = False
            for neighbor in neighbors:

                neighX = neighbor[0]
                neighY = neighbor[1]

                if array[neighX][neighY] == color:
                    continue
                else:
                    # where is line going
                    deltaX = neighX - x
                    deltaY = neighY - y
                    tempX = neighX
                    tempY = neighY

                    while 0 <= tempX <= 7 and 0 <= tempY <= 7:
                        if array[tempX][tempY] is None:
                            break
                        if array[tempX][tempY] == color:
                            valid = True
                            break
                        tempX += deltaX
                        tempY += deltaY
            return valid


# on click check if valid and make move
def click_event(event):
    # print("funk12")
    global depth, player_choice
    depth = 4
    xMouse = event.x
    yMouse = event.y
    if running:
        if board.player == player_choice: #or board.player is not player_choice:  # Delete part to disable click on AI's turn
            # Delete the highlights
            x = int((event.x - (50 * per)) / (50 * per))
            y = int((event.y - (50 * per)) / (50 * per))

            if 0 <= x <= 7 and 0 <= y <= 7:
                if valid_move(board.array, board.player, x, y):
                    board.turn_back_player = deepcopy(board.array)
                    board.turn_back_player2 = deepcopy(board.back_board)
                    board.update_board(x, y)
    else:
        # click area for color selection
        if (sh * .4) <= yMouse <= (sh * .5):
            # Black
            if (sw * .2) <= xMouse <= (sw * .45):
                player_choice = 0
                print("Player chose white")
                start_game()
            # White
            elif (sw * .55) <= xMouse <= (sw * .8):
                player_choice = 1
                print("Player chose black")
                start_game()


def key_event(event):
    # print("funk13")
    global start_points
    symbol = event.keysym
    if symbol.lower() == "r":  # Restart game with the "R" key
        start_game()
    elif symbol.lower() == "q":  # Quit game with the "Q" key
        root.destroy()
    elif symbol.lower() == "a":  # Enable/Disable AI with the "A" key
        if board.ai_on is True:
            board.ai_on = False
        else:
            board.ai_on = True
    elif symbol.lower() == "i":  # Go back a turn with the "I" (eye) key
        # board.array = board.turn_back_player
        # board.back_board = board.turn_back_player2
        print(board.turn_back_player)
        print(board.turn_back_player2)
        print("turn back player")
        # if board.player is 0:
        #     board.player = 1
        # else:
        #     board.player = 0
        board.update()
    elif symbol.lower() == "z":  # flip the starting piece colors with the "Z" key
        if start_points == 1:
            start_points = 0
            start_game()
        else:
            start_points = 1
            start_game()
        print("changed board state.")


def play_game():
    # print("funk15")
    global running
    running = False
    # Title and shadow
    screen.create_text(sw / 8, sh / 3, anchor="w", text="Choose a color: ", font=("Helvetica", 50), fill="black")

    # White or Black select
    # Black
    screen.create_rectangle(sw * .2, sh * .4, sw * .45, sh * .5, fill="white", outline="black")  # square
    screen.create_text(sw * .23, sh * .45, anchor="w", text="White", font=("Helvetica", 40), fill="black")  # text
    # White
    screen.create_rectangle(sw * .55, sh * .4, sw * .8, sh * .5, fill="black", outline="white")  # square
    screen.create_text(sw * .58, sh * .45, anchor="w", text="Black", font=("Helvetica", 40), fill="white")  # text

    screen.update()


def start_game():
    # print("funk16")
    global board, running
    running = True
    screen.delete(ALL)
    board = 0

    # Draw the background
    display_bg()

    # Create the board and update it
    board = Board()
    board.update()


play_game()

# set what each key does
screen.bind("<Button-1>", click_event)
screen.bind("<Key>", key_event)
screen.focus_set()

# tkinter loop
root.wm_title("CPSC 427 - Othello")
root.mainloop()
