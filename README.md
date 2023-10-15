# battleships-state-tracker

## Description

The task is to implement a Battleship state-tracker for a single player that must support the following logic:

- Create a board.
- Add a battleship to the board.
- Take an “attack” at a given position, and report back whether the attack resulted in a hit or a miss.
- Return whether the player has lost the game yet (i.e. all battleships are sunk).

Application should not implement the entire game, just the state tracker. No UI or
persistence layer is required.

## Getting started

**Install dependencies**: `pip install -r requirements.txt`

**Run tests:** `pytest tests/`

**Run app:** `python src/main.py`

## Explainer

I made the decision to track the game state rather using a dictionary rather than implementing a 2D grid as a board. My rationals are that:

- Using a dictionary to track the game state is more memory-efficient as we only store information for non-empty cases.
- A dictionary generally offers better time complexity.
- A dictionary is easier to consume as the key-value structure allows for quick retrieval and modification of data.
