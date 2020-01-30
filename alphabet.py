from typing import Any, Dict

class AlphabetDrawer:

    def __init__(self, letter_width: int, letter_height: int):
        self.letter_width = letter_width
        self.letter_height = letter_height

    def draw_letter(self, s: str, x: int, y: int):
        LETTER_TO_CALLABLE: Dict[str, Any] = {
            'A': self.A,   
            'B': self.B,
            'C': self.C,
            'D': self.D, 
            'E': self.E, 
            'F': self.F, 
            'G': self.G, 
            'H': self.H, 
            'I': self.I, 
            'J': self.J, 
            'K': self.K, 
            'L': self.L, 
            'M': self.M, 
            'N': self.N, 
            'O': self.O, 
            'P': self.P, 
            'Q': self.Q, 
            'R': self.R, 
            'S': self.S, 
            'T': self.T, 
            'U': self.U, 
            'V': self.V, 
            'W': self.W, 
            'X': self.X, 
            'Y': self.Y, 
            'Z': self.Z, 
        }
        LETTER_TO_CALLABLE[s](s, x, y)

    def A(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width / 2)};')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')

        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width * 1/5)};')
        print('PD;')
        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width * 4/5)};')
        print('PU;')

    def B(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height * 1/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 2/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 3/6)},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height * 4/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 5/6)},{y + self.letter_width};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + self.letter_height},{y};')
        print(f'PA{x},{y};')
        print('PU;')

        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width * 5/6)};')
        print('PD;')
        print(f'PA{x + int(self.letter_height / 2)},{y};')
        print('PU;')

    def C(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + int(self.letter_height * 1/5)},{y + self.letter_width};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x},{y + int(self.letter_width * 1/5)};')
        print(f'PA{x + int(self.letter_height * 1/5)},{y};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 1/5)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y + self.letter_width};')
        print('PU;')

    def D(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + int(self.letter_height * 1/5)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y + self.letter_width};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + self.letter_height},{y};')
        print(f'PA{x},{y};')
        print('PU;')

    def E(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y + self.letter_width};')
        print('PD;')
        print(f'PA{x},{y};')
        print(f'PA{x + self.letter_height},{y};')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')

        print(f'PA{x + int(self.letter_height / 2)},{y};')
        print('PD;')
        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width * 2/3)};')
        print('PU;')

    def F(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y + self.letter_width};')
        print('PD;')
        print(f'PA{x},{y};')
        print(f'PA{x + self.letter_height},{y};')
        print('PU;')

        print(f'PA{x + int(self.letter_height / 2)},{y};')
        print('PD;')
        print(f'PA{x + int(self.letter_height / 2)},{y + self.letter_width};')
        print('PU;')

    def G(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + int(self.letter_height * 1/6)},{y + self.letter_width};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x},{y + int(self.letter_width * 1/5)};')
        print(f'PA{x + int(self.letter_height * 1/5)},{y};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 1/5)};')

        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height * 5/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height / 2)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width * 2/3)};')
        print('PU;')

    def H(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y};')
        print('PU;')

        print(f'PA{x},{y + self.letter_width};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')

        print(f'PA{x + int(self.letter_height / 2)},{y};')
        print('PD;')
        print(f'PA{x + int(self.letter_height / 2)},{y + self.letter_width};')
        print('PU;')

    def I(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')

        print('PU;')
        print(f'PA{x},{y + int(self.letter_width / 2)};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width / 2)};')
        print('PU;')

    def J(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

        print(f'PA{x},{y + int(self.letter_width * 2/3)};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 2/3)};')
        print(f'PA{x + self.letter_height},{y};')
        print(f'PA{x + int(self.letter_height * 2/3)},{y};')
        print('PU;')

    def K(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y};')
        print('PU;')
        print(f'PA{x},{y + self.letter_width};')
        print('PD;')
        print(f'PA{x + int(self.letter_height / 2)},{y};')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')

    def L(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y + int(self.letter_width * 1/6)};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 1/6)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 5/6)};')
        print('PU;')

    def M(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x},{y};')
        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width / 2)};')
        print(f'PA{x},{y + self.letter_width};')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')

    def N(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x},{y};')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

    def O(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y + int(self.letter_width * 1/5)};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + int(self.letter_height * 1/5)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y + self.letter_width};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 1/5)};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y};')
        print(f'PA{x + int(self.letter_height * 1/5)},{y};')
        print(f'PA{x},{y + int(self.letter_width * 1/5)};')
        print('PU;')

    def P(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x},{y};')
        print(f'PA{x},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height * 1/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 2/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 3/6)},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height / 2)},{y};')
        print('PU;')

    def Q(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y + int(self.letter_width * 1/5)};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + int(self.letter_height * 1/5)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y + self.letter_width};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 1/5)};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y};')
        print(f'PA{x + int(self.letter_height * 1/5)},{y};')
        print(f'PA{x},{y + int(self.letter_width * 1/5)};')
        print('PU;')

        print(f'PA{x + int(self.letter_height * (2/3))},{y + int(self.letter_width * (2/3))};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')

    def R(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x},{y};')
        print(f'PA{x},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height * 1/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 2/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height/2)},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height/2)},{y};')
        print('PU;')

        print(f'PA{x + int(self.letter_height/2)},{y + int(self.letter_width * 3/5)};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')

    def S(self, s: str, x: int, y: int) -> None:
        print(f'PA{x + int(self.letter_height * 1/6)},{y + self.letter_width};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 5/6)};')
        print('PD;')
        print(f'PA{x},{y + int(self.letter_width * 1/6)};')
        print(f'PA{x + int(self.letter_height * 1/6)},{y};')
        print(f'PA{x + int(self.letter_height * 2/6)},{y};')
        print(f'PA{x + int(self.letter_height/2)},{y + int(self.letter_width * 1/6)};')
        print(f'PA{x + int(self.letter_height/2)},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + int(self.letter_height * 4/6)},{y + self.letter_width};')
        print(f'PA{x + int(self.letter_height * 5/6)},{y + self.letter_width};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 5/6)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 1/6)};')
        print(f'PA{x + int(self.letter_height * 5/6)},{y};')

        print('PU;')

    def T(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')
        print(f'PA{x},{y + int(self.letter_width / 2)};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width / 2)};')
        print('PU;')

    def U(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x + int(self.letter_height * 4/5)},{y};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 1/5)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * 4/5)};')
        print(f'PA{x + int(self.letter_height * 4/5)},{y + self.letter_width};')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

    def V(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width / 2)};')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

    def W(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * (1/3))};')
        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width / 2)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width * (2/3))};')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

    def X(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')
        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

    def Y(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width / 2)};')
        print(f'PA{x + self.letter_height},{y + int(self.letter_width / 2)};')
        print('PU;')
        print(f'PA{x + int(self.letter_height / 2)},{y + int(self.letter_width / 2)};')
        print('PD;')
        print(f'PA{x},{y + self.letter_width};')
        print('PU;')

    def Z(self, s: str, x: int, y: int) -> None:
        print(f'PA{x},{y};')
        print('PD;')
        print(f'PA{x},{y + self.letter_width};')
        print(f'PA{x + self.letter_height},{y};')
        print('PD;')
        print(f'PA{x + self.letter_height},{y + self.letter_width};')
        print('PU;')
