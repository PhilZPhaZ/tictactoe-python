import contextlib
import itertools
import sys
import tkinter as tk
from tkinter import messagebox


class TicTacToeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.geometry("500x500")
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
        for row in range(3):
            self.grid_rowconfigure(row, weight=1)
            for col in range(3):
                self.grid_columnconfigure(col, weight=1)
                button=tk.Button(
                    self,
                    text=None,
                    command=lambda row=row, col=col: self.callback(row, col),
                    font=('Helvetica', 40),
                    width=10, 
                    height=2
                )

                self._cells[(row, col)] = button

                button.grid(
                    row=row,
                    column=col,
                    sticky="nsew"
                )

    def callback(self, row: int, col: int) -> None:
        button = self._cells[(row, col)]

        if not button.cget('text'):
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

        if all(button.cget('text') for button in self._cells.values()):
            self.tie()

    def win(self):
        if response := messagebox.askyesno("Gagné! ", "Voulez vous recommencer ?!"):
            self.reset()
            self.focus_set()
        else:
            sys.exit()

        self.focus_force()

    def tie(self):
        if response := messagebox.askyesno("Egalité", "Voulez vous recommencer ?"):
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
