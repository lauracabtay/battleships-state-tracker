from pprint import pprint
from battleship_game import BattleshipGame


def main():
    """
    Demonstrates the usage of the BattleshipGame class by creating a
    game instance with a 10x10 board. This function showcases various
    game scenarios including adding battleships, attacking positions,
    and printing the current state of the game board.
    """

    # Initialize board game
    board_size = 10
    battleship_game = BattleshipGame(board_size)

    # Add battleships
    battleship_game.add_battleship(3, "A", "horizontal")  # Invalid position
    battleship_game.add_battleship(3, "A1", "invalid_orientation")  # Invalid input
    battleship_game.add_battleship(3, "I8", "vertical")  # Out of bounds
    battleship_game.add_battleship(3, "A3", "horizontal")  # In bounds
    battleship_game.add_battleship(3, "A5", "horizontal")  # Overlap
    battleship_game.add_battleship(3, "F3", "vertical")  # In bounds

    battleship_game.print_state_tracker()

    # Attack
    battleship_game.attack_position("A3")
    battleship_game.attack_position("B3")
    battleship_game.attack_position("A4")
    battleship_game.attack_position("A5")
    battleship_game.attack_position("F3")
    battleship_game.attack_position("G3")
    battleship_game.attack_position("H3")

    battleship_game.print_state_tracker()


if __name__ == "__main__":
    main()
