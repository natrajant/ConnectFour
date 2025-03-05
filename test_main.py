import unittest
from main import getCurrentPlayer, printState, isStateValid, play, hasWinner, figureNextMove

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, "y", "r", None, None, None],
            [None, None, "r", "y", None, None, None],
            ["r", "y", "y", "y", "r", "r", "y"],
            ["r", "r", "y", "y", "r", "y", "r"],
        ];

    def test_current_player(self):
        assert getCurrentPlayer(self.gameState) == "y"
        self.gameState[3][0] = "y"
        assert getCurrentPlayer(self.gameState) == "r"
    
    def test_state_validity(self):
        # misplaced color
        self.gameState[1][0] = "y"
        assert isStateValid(self.gameState) is False

        self.gameState[1][0] = None
        assert isStateValid(self.gameState) is True

        # invalid color
        self.gameState[3][0] = "x"
        assert isStateValid(self.gameState) is False

        # Mismatched count of colors 
        # more reds than yellows
        self.gameState[3][0] = "r"
        assert isStateValid(self.gameState) is False
        # two extra yellows than red
        self.gameState[2][0] = "y"
        self.gameState[3][0] = "y"
        assert isStateValid(self.gameState) is False

    def test_play(self):
        assert self.gameState[3][1] is None
        play(self.gameState, 1, "y")
        assert self.gameState[3][1] == "y"

    def test_winner(self):
        # Easy to visualize
        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "y", None, None, None],
            ["r", "r", "r", "y", "y", None, None],
            ["r", "y", "y", "y", "r", "r", "y"],
            ["r", "r", "y", "y", "r", "y", "r"],
        ]
        assert hasWinner(self.gameState) is True # Column index 3 has 4 vertical "y"

        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "y", None, None, None],
            ["r", "r", "r", "r", "y", "y", None],
            ["r", "y", "y", "y", "r", "r", "y"],
            ["r", "r", "y", "y", "r", "y", "r"],
        ]
        assert hasWinner(self.gameState) is True # Row index 3 has 4 horizontal "x"

        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "y", None, None, None],
            [None, "r", "y", "r", None, None, None],
            [None, "y", "r", "y", None, None, None],
            ["y", "r", "y", "r", None, None, None],
        ]
        assert hasWinner(self.gameState) is True # y has a diagonal (right to left) win

        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "y", None, None, None],
            [None, None, None, "r", "y", "r", None],
            [None, None, None, "y", "r", "y", None],
            [None, None, None, "r", "y", "r", "y"],
        ]
        assert hasWinner(self.gameState) is True # y has a diagonal (right to left) win

        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "r", "y", "r", None],
            [None, None, None, "y", "r", "y", None],
            [None, None, None, "r", "y", "r", "y"],
        ]
        assert hasWinner(self.gameState) is False
        
    def test_suggest_move(self):
        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "r", "y", "r", None],
            [None, None, None, "y", "r", "y", None],
            [None, None, None, "r", "y", "r", "y"],
        ]
        
        # With yellow to play next, placing in index 3 is winning
        assert figureNextMove(self.gameState) == 3

        self.gameState = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "r", "y", "r", None],
            [None, None, None, "y", "r", "y", None],
            [None, "y", None, "r", "y", "r", "y"],
        ]
        
        # With red to play next, placing in index 3 will block yellow's win
        assert figureNextMove(self.gameState) == 3
