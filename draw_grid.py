from alphabet import AlphabetDrawer
import sys
from typing import List

START_X = 100
START_Y = 100
PUZZLE_WIDTH_PLOTTER_UNITS = 4995

class Square:
    def __init__(self, x: int, y: int, value: str):
        self.x = x
        self.y = y
        self.value = value

    def __str__(self):
        return f'{self.x}, {self.y}'

    __repr__ = __str__

class Puzzle:
    def __init__(
        self,
        black_squares: List[Square],
        letter_squares: List[Square],
        length_in_squares: int,
    ):
        self.black_squares: List[Square] = black_squares
        self.letter_squares: List[Square] = letter_squares
        self.length_in_squares: int = length_in_squares
        self.length_in_plotter_units: int = PUZZLE_WIDTH_PLOTTER_UNITS
        self.square_length_in_plotter_units: int = int(
            self.length_in_plotter_units / self.length_in_squares
        )

def draw_horizontal_lines(puzzle: Puzzle):
    increment = puzzle.square_length_in_plotter_units
    c = START_Y
    r = START_X + increment
    puzzle_edge_right = puzzle.length_in_plotter_units + START_Y

    while r < puzzle.length_in_plotter_units:
        # Move pen to r, c
        print(f'PA{r},{c};')

        # Set down pen
        print('PD;')

        # Draw all the way to the right edge of puzzle
        print(f'PA{r},{puzzle_edge_right};')

        # Pick up pen
        print('PU;')

        # Move down by <increment>
        r += increment

def draw_vertical_lines(puzzle: Puzzle):
    increment = puzzle.square_length_in_plotter_units
    r = START_X
    c = START_Y + increment
    puzzle_floor_y = puzzle.length_in_plotter_units + START_X

    while c < puzzle.length_in_plotter_units:
        # Move pen to r, c
        print(f'PA{r},{c};')

        # Set down pen
        print('PD;')

        # Draw all the way down to bottom of puzzle
        print(f'PA{puzzle_floor_y},{c};')

        # Pick up pen
        print('PU;')

        # Move to the right by <increment>
        c += increment

def draw_perimeter(puzzle: Puzzle):
    print(f'PA{START_X},{START_Y};')

    # Put down the pen (start drawing)
    print('PD;')

    # Top edge
    print(f'PA{START_X},{START_Y + puzzle.length_in_plotter_units};')

    # Right edge
    print(f'PA{START_X + puzzle.length_in_plotter_units},{START_Y + puzzle.length_in_plotter_units};')

    # Bottom edge
    print(f'PA{START_X + puzzle.length_in_plotter_units},{START_Y};')

    # Left edge
    print(f'PA{START_X},{START_Y};')

    # Pick up pen (stop drawing)
    print('PU;')

def draw_empty_grid(puzzle: Puzzle):
    # Initialize; select pen 1
    print('IN;SP1;')

    draw_perimeter(puzzle=puzzle)

    draw_vertical_lines(puzzle=puzzle)

    draw_horizontal_lines(puzzle=puzzle)

def fill_square__black(x: int, y: int, size: int):
    increment = int(size / 10)
    tmp_x = x
    direction = 1

    # Start on the right, slightly down
    print(f'PA{tmp_x + increment},{y + size};')
    print('PD;')

    while abs(x - tmp_x) < size - (2 * increment):
        if direction == 1:
            # Draw all the way to the left
            print(f'PA{tmp_x + increment},{y};')
            tmp_x += increment
            # Draw slightly down
            print('PU;')
            print(f'PA{tmp_x + increment},{y};')
            print('PD;')
        else:
            # Draw all the way to the right
            print(f'PA{tmp_x + increment},{y + size};')
            tmp_x += increment
            # Draw slightly down
            print('PU;')
            print(f'PA{tmp_x + increment},{y + size};')
            print('PD;')

        # Flip direction
        direction *= -1

    print('PU;')

def fill_black_squares(puzzle: Puzzle):
    # Fill in all black squares in the puzzle

    for square in puzzle.black_squares:
        # Determine starting location (upper left of square)
        start_x = int(square.x * puzzle.square_length_in_plotter_units) + START_X
        start_y = int(square.y * puzzle.square_length_in_plotter_units) + START_Y

        # Draw filled square of appropriate size
        fill_square__black(x=start_x, y=start_y, size=puzzle.square_length_in_plotter_units)

def fill_letters(puzzle: Puzzle):
    # Fill in all letters in the puzzle

    # Start slightly inset into the square
    offset = int(puzzle.square_length_in_plotter_units / 5)

    # Scale down letter size for readability
    scaled_square_size = int(puzzle.square_length_in_plotter_units * .6)

    # Initialize AlphabetDrawer
    alphabet_drawer = AlphabetDrawer(letter_height=scaled_square_size, letter_width=scaled_square_size)

    for square in puzzle.letter_squares:
        # Determine starting location (upper left of square, slightly offset inward)
        buffered_x = int(square.x * puzzle.square_length_in_plotter_units) + START_X + offset
        buffered_y = int(square.y * puzzle.square_length_in_plotter_units) + START_Y + offset

        # Draw filled square of appropriate size
        alphabet_drawer.draw_letter(s=square.value, x=buffered_x, y=buffered_y)

def parse_puzzle_file(path: str) -> Puzzle:
    black_squares: List[Square] = []
    letter_squares: List[Square] = []
    with open(path, 'r') as f:
        items = f.readline().split()
        boxes_across = int(items[0])
        row_index = 0
        for line in f:
            line = line.strip()
            for col_index in range(len(line)):
                if line[col_index] == '#':
                    # Black square
                    black_squares.append(Square(x=row_index, y=col_index, value=line[col_index]))
                elif line[col_index] == '.':
                    # Unfilled square, skip
                    pass
                else:
                    # Filled square
                    letter_squares.append(Square(x=row_index, y=col_index, value=line[col_index]))
            row_index += 1
    return Puzzle(
        black_squares=black_squares,
        letter_squares=letter_squares,
        length_in_squares=boxes_across,
    )

if __name__ == '__main__':
    
    puzzle_path = sys.argv[1]

    # Read puzzle file
    puzzle = parse_puzzle_file(path=puzzle_path)

    draw_empty_grid(puzzle=puzzle)

    fill_black_squares(puzzle=puzzle)

    fill_letters(puzzle=puzzle)

    print('SP0;')  # Put then pen back (select pen 0)
