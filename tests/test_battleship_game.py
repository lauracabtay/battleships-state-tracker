class TestBattleshipGame():
    def test_add_battleship_valid(self, game_with_ship):
        game = game_with_ship
        assert game.state_tracker == {
            (0, 0): "Occupied",
            (0, 1): "Occupied",
            (0, 2): "Occupied",
        }

    def test_add_battleship_invalid_position(self, capsys, game_with_invalid_position):
        game = game_with_invalid_position
        captured = capsys.readouterr()

        assert "Invalid position format." in captured.out
        assert not game.state_tracker

    def test_add_battleship_invalid_input(self, capsys, game_with_invalid_input):
        game = game_with_invalid_input
        captured = capsys.readouterr()

        assert "Invalid input." in captured.out
        assert not game.state_tracker

    def test_add_battleship_outbound(self, capsys, game_with_outbound_position):
        game = game_with_outbound_position
        captured = capsys.readouterr()

        assert "Position is out of bounds." in captured.out
        assert not game.state_tracker
        
    def test_add_battleship_overlap(self, capsys, game_with_ship):
        game = game_with_ship
        game.add_battleship(3, "A2", "horizontal")
        captured = capsys.readouterr()

        assert "Space is already occupied." in captured.out
        assert game.state_tracker == {
            (0, 0): "Occupied",
            (0, 1): "Occupied",
            (0, 2): "Occupied",
        }

    def test_attack_position_hit(self, capsys, game_with_ship):
        game = game_with_ship
        game.attack_position("A1")
        captured = capsys.readouterr()

        assert "Position A1 is a hit!" in captured.out
        assert game.state_tracker == {
            (0, 0): "Hit",
            (0, 1): "Occupied",
            (0, 2): "Occupied",
        }

    def test_attack_position_miss(self, capsys, game_with_ship):
        game = game_with_ship
        game.attack_position("B2")
        captured = capsys.readouterr()

        assert "No ship at position B2." in captured.out
        assert game.state_tracker == {
            (0, 0): "Occupied",
            (0, 1): "Occupied",
            (0, 2): "Occupied",
            (1, 1): "Miss"
        }

    def test_attack_position_invalid_position(self, capsys, game):
        game.attack_position("A#1")
        captured = capsys.readouterr()

        assert "Invalid position format." in captured.out
        assert not game.state_tracker
    
    def test_is_game_over_empty_board(self, game):
        result = game.is_game_over()

        assert not result

    def test_is_game_over_with_ships(self, game_with_ship):
        game = game_with_ship
        game.attack_position("A3")
        result = game.is_game_over()

        assert not result

    def test_is_game_over_all_ships_sunk(self, capsys, game_with_ship):
        game = game_with_ship

        for i in range(3):
            game.attack_position(f"A{i + 1}")
            
        result = game.is_game_over()
        captured = capsys.readouterr()

        assert result
        assert "Game over." in captured.out

    def test_print_state_tracker(self, capsys, game_with_ship):
        game = game_with_ship
        game.print_state_tracker()
        captured = capsys.readouterr()

        assert "{(0, 0): 'Occupied', (0, 1): 'Occupied', (0, 2): 'Occupied'}" in captured.out
