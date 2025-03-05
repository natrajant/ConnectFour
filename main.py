# Finds whose turn it is to play next
def getCurrentPlayer(board):
    # Valid board check
    if not isStateValid(board):
        raise Exception("Invalid board state")

    redCount, yellowCount = getColorCounts(board)
    # Assuming yellow always starts the game (as also shown in the example)
    # if red hasn't matched yellow's turns, it is red's turn to play, otherwise it it yellow's turn to play
    if yellowCount == redCount:
        return "y"
    return "r"


# Checks board's validity
def isStateValid(board):
    # Checks for invalid color placement on board, invalid color on board and invalid count of colors (yellow or red)
    redCount, yellowCount = 0, 0
    for i in range(len(board[0])):
        colorFound = False
        for j in range(len(board)):
            if colorFound and not board[j][i]:
                # None found after a color was found
                return False

            if board[j][i] in {"r", "y"}:
                # Set colorFound flag to mark the beginning of colors. There should be no None after this
                colorFound = True
                if board[j][i] == "r":
                    redCount += 1
                else:
                    yellowCount += 1
            elif board[j][i]:
                # Board has a color that's not red or yellow
                return False

    # Valid if yellowCount == redCount or yellowCount - 1 == redCount (Assuming yellow always starts)
    return yellowCount == redCount or yellowCount - 1 == redCount


# Makes a move by placing color in column
def play(board, column, color):
    if not 0 <= column <= 6:
        raise Exception("Invalid column value")

    if color not in {"r", "y"}:
        raise Exception("Invalid color")

    current_player = getCurrentPlayer(board)  # Will raise exception if board is invalid
    if color != current_player:
        raise Exception(f"Not {color}'s turn to play")

    if board[0][column]:  # Column is already full, can't insert
        raise Exception("Invalid move")

    makeMove(board, column, color)

    return board


# Checks if there are 4 colors in a row
def hasWinner(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                # Checking top down. only check until 3 columns above last row
                if (i < len(board) - 3 and board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]):
                    return True

                # Checking left to right. only check until 3 columns before last column
                if (j < len(board[i]) - 3 and board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]):
                    return True

                # Checking left to right, diagonally. only until 3 rows and columns before end
                if (i < len(board) - 3 and j < len(board[i]) - 3 and board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]):
                    return True

                # Checking right to left, diagonally, only until 3 rows and columns before end
                if (i < len(board) - 3 and j >= 3 and board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3]):
                    return True
    return False


# Suggests next move
def figureNextMove(board):
    player = getCurrentPlayer(board)

    # check if win possible by placing in different positions and checking for winner
    res = bestMove(board, player)
    if res:
        return res

    player = "r" if player == "y" else "y"

    # if win not possible, check if other player can win in one move and try and block the winning move
    res = bestMove(board, player)
    if res:
        return res

    # Choose first viable column that will work
    for i in range(len(board[0])):
        if not board[0][i]:
            return i


# Returns the count of red and yellow as tuple
def getColorCounts(board):
    redCount, yellowCount = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Count the red and while colors
            if board[i][j] == "y":
                yellowCount += 1
            elif board[i][j] == "r":
                redCount += 1
    return (yellowCount, redCount)


# Returns position to insert next color within a column
def getInsertPosition(board, column):
    for i in range(len(board)):
        if board[i][column]:
            break
    return (i - 1, column)


# Finds position and sets color
def makeMove(board, column, color):
    x, y = getInsertPosition(board, column)
    board[x][y] = color


# Finds position and unsets last set color in a column
def undoMove(board, column, color=None):
    x, y = getInsertPosition(board, column)
    board[x + 1][y] = color


# Print board
def printState(board):
    state = ""
    for i in range(len(board)):
        row = ""
        for j in range(len(board[0])):
            row += f"{board[i][j] if board[i][j] else 'O'} "
        state += row + "\n"
    print(state)


# Try to get the best move for the player
# places color in each column to see if any one of them fetches a win
def bestMove(board, player):
    for i in range(len(board[0])):
        if not board[0][i]:
            makeMove(board, i, player)
            if hasWinner(board):
                return i
            undoMove(board, i)
    return None


gameState = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, "y", "r", None, None, None],
    [None, None, "r", "y", None, None, None],
    ["r", "y", "y", "y", "r", "r", "y"],
    ["r", "r", "y", "y", "r", "y", "r"],
];
current_player = getCurrentPlayer(gameState)
print(current_player)
