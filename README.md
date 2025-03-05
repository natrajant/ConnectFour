# Connect 4

## Setup
Simply checkout and install the dependencies from the `requirements.txt` (recommended in a virtual environment) from the root folder of the project

```pip install -r requirements.txt```


The following are the assumption made for the implementation:
- Player with Yellow always starts the game 

The `main.py` file has the implementation of the following core methods:


`getCurrentPlayer(board)` - Accepts the current game state and returns the player who should play the next move. Return values are either "r" or "y"

`isStateValid(board)` - Checks the game state passed in and evaluates for validity and correctness. Returns boolean value - True or False

`play(board, column, color)` - Accepts the current game state, a zero based index column number (0 through 6), a color to place in the column specified. Returns the board after the move has been made. Will throw exceptions if invalid moves are played

`hasWinner(board)` - Checks the provided game state to identify a winner. Returns a bookean value depending on the outcome - True or False

`figureNextMove(board)` - Evaluates the next move to score a win or defend.


Any of these methods can be invoked by importing the main.py into your file for testing them.


## Usage

#### Example python code

    from main import getCurrentPlayer

    gameState = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, "y", "r", None, None, None],
        [None, None, "r", "y", None, None, None],
        ["r", "y", "y", "y", "r", "r", "y"],
        ["r", "r", "y", "y", "r", "y", "r"],
    ];

    print(getCurrentPlayer(gameState))
    # Outputs "y"


## Testing

To run some basic tests that exercise the above functions, run the following command from the project root
`pytest test_main.py`