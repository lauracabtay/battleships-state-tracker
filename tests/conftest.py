import pytest
from src.battleship_game import BattleshipGame

@pytest.fixture
def game():
    return BattleshipGame(10)

@pytest.fixture
def game_with_ship(game):
    game.add_battleship(3, "A1", "horizontal")
    return game

@pytest.fixture
def game_with_invalid_position(game):
    game.add_battleship(3, "A#1", "horizontal")
    return game

@pytest.fixture
def game_with_invalid_input(game):
    game.add_battleship("3", "A1", "horizontal")
    return game

@pytest.fixture
def game_with_outbound_position(game):
    game.add_battleship(3, "Z1", "horizontal")
    return game
