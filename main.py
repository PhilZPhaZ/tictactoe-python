import itertools
import sys
import time
import tkinter as tk
from tkinter import messagebox


class TicTacToeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.geometry("528x500")
        self.minsize(528, 500)
        self.maxsize(528, 500)
        self._cells = {}
        self._create_cells()
        self.turn = 0

        self.victories = [
            # Lignes
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Colonnes
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonales
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

    def _create_cells(self) -> None:
        for row, col in itertools.product(range(3), range(3)):
            button=tk.Button(
                self,
                text=None,
                padx=63,
                pady=63,
                command=lambda row=row, col=col: self.callback(row, col),
                font=('Helvetica', 27),
                height=1,
                width=1
            )

            self._cells[(row, col)] = button

            button.grid(
                row=row,
                column=col
            )

    def callback(self, row: int, col: int) -> None:
        button = self._cells[(row, col)]

        if button.cget('text'):
            pass
        else:
            if self.turn % 2 == 0:
                button.configure(text="X")
            else:
                button.configure(text="O")
            self.turn += 1

        self.update_idletasks()

        self.is_win()

    def is_win(self):
        for positions in self.victories:

            symboles = [self._cells[pos].cget('text') for pos in positions]

            if len(set(symboles)) == 1 and symboles[0] != "":
                self.win()

    def win(self):
        response = messagebox.askyesno("Gagné", "Bravo!")

        if response:
            self.reset()
            self.focus_set()
        else:
            sys.exit()

        self.focus_force()

    def reset(self):
        for button in self._cells.values():
            button.configure(text="")


game = TicTacToeGame()
game.mainloop()
