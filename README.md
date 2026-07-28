# Chess Move Generator

A fully functional chess move generator implemented from scratch in Python as a learning project. The goal was to build a legal chess move engine without relying on external chess libraries, and to better understand how chess engines represent positions, generate moves, and validate legality.

## What this project does

This project includes:

- A chess board representation using FEN parsing
- Move generation for all standard piece types
- Legal move generation that filters out illegal moves
- Support for castling, en passant, and promotion
- Move application and undo support
- Check, checkmate, and stalemate detection
- Perft testing for move-generation correctness

## Project status

At this stage, the project is considered complete for its intended purpose. The move generator produces the expected standard Perft results for the initial position and the Kiwipete position, and the test suite passes.

## Why this project was built

This project was created primarily for learning and experimentation. It is aimed at practicing:

- Object-oriented design
- State management
- Recursive search and move generation
- Chess rules implementation
- Debugging complex logic

## Structure

The project is organized into modules for:

- game state
- board representation
- move generation
- move validation
- move application
- game rules
- perft testing

## Running the project

From the project root, run:

```bash
python3 main.py
```

To run the tests:

```bash
python3 -m pytest
```

## Notes

This is a learning-focused project rather than a production chess engine. The emphasis is on correctness, clarity, and understanding the underlying mechanics of chess move generation.
