import re
from enum import Enum
from pprint import pprint


class BattleshipGame:
    """
    A class representing a Battleship game state tracker for a single player.

    Attributes:
        board_size (int): The size of the game board.
        state_tracker (dict): A dictionary to track the game state.
    """

    class ShipStatus(Enum):
        """
        An enumeration representing ship statuses.
        """

        OCCUPIED = "Occupied"
        HIT = "Hit"
        MISS = "Miss"

    class Orientation(Enum):
        """
        An enumeration representing ship orientations.
        """

        HORIZONTAL = "horizontal"
        VERTICAL = "vertical"

    HIT = ShipStatus.HIT.value
    OCCUPIED = ShipStatus.OCCUPIED.value
    MISS = ShipStatus.MISS.value
    HORIZONTAL = Orientation.HORIZONTAL.value
    VERTICAL = Orientation.VERTICAL.value

    def __init__(self, board_size) -> None:
        self.board_size = board_size
        self.state_tracker = {}

    def add_battleship(self, ship_size, position, orientation) -> None:
        """
        Add a battleship to the game board.

        Args:
            ship_size (int): The size of the battleship.
            position (str): The starting position of the battleship (e.g., "A1").
            orientation (str): The orientation of the battleship ("horizontal" or "vertical").

        Raises:
            InvalidInput: If the input is invalid.
            InvalidPosition: If the position format is invalid.
            OutboundException: If the position is out of bounds.
            OverlapException: If the space is already occupied.
        """
        try:
            head_row, head_col = self._position_to_coord(position)

            self._place_ship(ship_size, head_row, head_col, orientation)

        except (
            InvalidInput,
            InvalidPosition,
            OutboundException,
            OverlapException,
        ) as exc:
            print(exc)

    def attack_position(self, position) -> None:
        """
        Perform an attack at the specified position.

        Args:
            position (str): The position to attack (e.g., "A1").
        """
        try:
            attack_position = self._position_to_coord(position)

            if attack_position in self.state_tracker:
                self.state_tracker[attack_position] = BattleshipGame.HIT
                print(f"Position {position} is a hit!")
                self.is_game_over()
            else:
                self.state_tracker[attack_position] = BattleshipGame.MISS
                print(f"No ship at position {position}.")
        except InvalidPosition as exc:
            print(exc)

    def is_game_over(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over; False otherwise.
        """
        if self.state_tracker and not any(
            value == BattleshipGame.OCCUPIED for value in self.state_tracker.values()
        ):
            print("Game over.")
            return True
        return False


    def print_state_tracker(self):
        """
        Print the current game board state.
        """
        pprint(self.state_tracker)


    def _position_to_coord(self, position) -> tuple[int, int]:
        # Convert a valid position string to row and column coordinates

        if not self._is_valid_position(position):
            raise InvalidPosition("Invalid position format.")

        # Row index calculation based on the first uppercase character in 'position'.
        row = ord(position[0].upper()) - ord("A")

        # Column index calculation from the numeric part of 'position',adjusted for 0-based indexing.
        col = int(position[1:]) - 1

        return row, col

    def _is_valid_position(self, position) -> bool:
        # Check if the position format is valid.

        # Regex checks if string starts with 1 letter and ends with 1 to 2 digits
        pattern = re.compile(r"^[A-Za-z]{1}\d{1,2}$")
        return bool(pattern.match(position))

    def _is_valid_input(self, ship_size, orientation) -> bool:
        # Check if the input values when adding a battleship are valid.
        return isinstance(ship_size, int) and orientation in [
            BattleshipGame.HORIZONTAL,
            BattleshipGame.VERTICAL,
        ]

    def _is_outbound(self, ship_size, head_row, head_col, orientation) -> bool:
        # Check if the battleship is out of bounds.

        if orientation == BattleshipGame.HORIZONTAL:
            # Check if ship's head column is out of bounds
            # Check if last column of the ship is out of bounds
            # Check if ship's head row is out of bounds
            return (
                not 0 <= head_col < self.board_size
                or not 0 <= head_col + ship_size - 1 < self.board_size
                or not 0 <= head_row < self.board_size
            )
        if orientation == BattleshipGame.VERTICAL:
            # Check if ship's head row is out of bounds
            # Check if last row of the ship is out of bounds
            # Check if ship's head column is out of bounds
            return (
                not 0 <= head_row < self.board_size
                or not 0 <= head_row + ship_size - 1 < self.board_size
                or not 0 <= head_col < self.board_size
            )
        return False

    def _is_overlapping(self, ship_size, row, col, orientation) -> bool:
        # Check if the space is already occupied by a battleship.

        if orientation == BattleshipGame.HORIZONTAL:
            for i in range(ship_size):
                check_position = (row, col + i)
                if (
                    check_position in self.state_tracker
                    and self.state_tracker[check_position] == BattleshipGame.OCCUPIED
                ):
                    return True
        elif orientation == BattleshipGame.VERTICAL:
            for i in range(ship_size):
                check_position = (row + i, col)
                if (
                    check_position in self.state_tracker
                    and self.state_tracker[check_position] == BattleshipGame.OCCUPIED
                ):
                    return True
        return False

    def _place_ship(self, ship_size, head_row, head_col, orientation) -> None:
        # Place a battleship on the gameboard.

        if not self._is_valid_input(ship_size, orientation):
            raise InvalidInput("Invalid input.")
        
        if self._is_outbound(ship_size, head_row, head_col, orientation):
            raise OutboundException("Position is out of bounds.")

        if self._is_overlapping(ship_size, head_row, head_col, orientation):
            raise OverlapException("Space is already occupied.")
        
        for i in range(ship_size):
            if orientation == BattleshipGame.HORIZONTAL:
                self.state_tracker[(head_row, head_col + i)] = BattleshipGame.OCCUPIED
            elif orientation == BattleshipGame.VERTICAL:
                self.state_tracker[(head_row + i, head_col)] = BattleshipGame.OCCUPIED


class OutboundException(Exception):
    """
    Exception raised for outbound position errors.
    """


class InvalidInput(Exception):
    """
    Exception raised for invalid input errors.
    """


class InvalidPosition(Exception):
    """
    Exception raised for invalid position format errors.
    """


class OverlapException(Exception):
    """
    Exception raised for overlap errors.
    """
