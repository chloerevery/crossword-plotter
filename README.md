## About

Crossword Plotter is a tool for transcribing crossword puzzles - filled, unfilled, or partially filled - using a plotter machine.

It is designed for use with a HP7440A plotter (old model from the 80s without support for many commands), but should work with any plotter that accepts [HPGL](https://en.wikipedia.org/wiki/HP-GL) files.

<img src="https://user-images.githubusercontent.com/6632604/73477136-a6f23000-4361-11ea-9d6e-d19ceecae86b.jpg" width="300">

## How to Use

The tool takes in a `.puzzle` file and outputs an `.hpgl` file that can be fed into a plotter machine.

`.puzzle` format files have the following structure:

First line: `<puzzle_width> <puzzle_height>`
Each subsequent line represents a row in the crossword puzzle, where `#` indicates a black square, `.` indicates an unfilled square, and any other character indicates a square filled with that character.

### Example

(A partially-filled puzzle)
```
5 5
..L.#
ALEUT
..T..
LOGAN
#.O..
```

If you'd like to visualize what the final result will look like beforehand, I highly recommend the `viz` tool in this [excellent collection of plotter tools](https://github.com/WesleyAC/plotter-tools).

## Build & Run Instructions

`python3 draw_grid.py path/to/puzzle/file`
