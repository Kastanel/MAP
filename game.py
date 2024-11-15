from tkinter import Tk, Label, Button
from tkinter import messagebox
import random

root = Tk()

root.title("Rock/Paper/Scissors")
root.geometry("300x300")

total_plays = player_wins = computer_wins = equalities = 0

CHOICES = [
    {"type": "ROCK", "wins": "SCISSORS", "looses": "PAPER"},
    {"type": "PAPER", "wins": "ROCK", "looses": "SCISSORS"},
    {"type": "SCISSORS", "wins": "PAPER", "looses": "ROCK"},
]


def play_game(player_choice):
    computer_choice = random.choice(CHOICES)
    global total_plays, player_wins, computer_wins, equalities
    total_plays += 1

    if computer_choice["looses"] == player_choice:
        result = "YOU WON!"
        player_wins += 1
    elif computer_choice["wins"] == player_choice:
        result = "YOU LOST!"
        computer_wins += 1
    else:
        equalities += 1
        result = "EQUALITY!"
    messagebox.showinfo(
        "RESULT",
        f"{result}\n"
        f"you chose: {player_choice}\n"
        f"computer chose: {computer_choice['type']}",
    )
    player_win_rate_label.config(
        text=f"Your win rate is: {(player_wins / total_plays)*100:.2f}%"
    )
    equality_rate_label.config(
        text=f"Equality rate is: {(equalities / total_plays)*100:.2f}%"
    )
    computer_win_rate_label.config(
        text=f"Computer win rate is: {(computer_wins / total_plays)*100:.2f}%"
    )


rules = (
    "Game rules are:\n"
    "Rock   VS Paper    --> Paper\n"
    "Rock   VS Scissors --> Rock\n"
    "Paper  VS Scissors --> Scissors"
)
for col in range(3):
    root.columnconfigure(col, weight=1)

rules_label = Label(
    root, text=rules, justify="left", font=("Cascadia Code", 12, "bold")
)
rules_label.grid(row=0, columnspan=3, sticky="w", padx=10, pady=5)

rock_button = Button(root, text="ROCK", command=lambda: play_game("ROCK"))
rock_button.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
paper_button = Button(root, text="PAPER", command=lambda: play_game("PAPER"))
paper_button.grid(row=1, column=1, sticky="ew")
scissors_button = Button(root, text="SCISSORS", command=lambda: play_game("SCISSORS"))
scissors_button.grid(row=1, column=2, sticky="ew", padx=10, pady=5)

player_win_rate_label = Label(
    root,
    text=f"Your win rate is: 0.00%",
    justify="left",
    font=("Cascadia Code", 12, "bold"),
)
player_win_rate_label.grid(row=2, columnspan=3, sticky="w", padx=10)

equality_rate_label = Label(
    root,
    text=f"Equality rate is: 0.00%",
    justify="left",
    font=("Cascadia Code", 12, "bold"),
)
equality_rate_label.grid(row=3, columnspan=3, sticky="w", padx=10)

computer_win_rate_label = Label(
    root,
    text=f"Computer win rate is: 0.00%",
    justify="left",
    font=("Cascadia Code", 12, "bold"),
)
computer_win_rate_label.grid(row=4, columnspan=3, sticky="w", padx=10)

root.mainloop()
