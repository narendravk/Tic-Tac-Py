# Portfolio Project - Tic Tac Toe
#TODO : Imports
from art import startup,thanks
from games import TicTacToe
import os

#TODO : Runtime
print(startup)
print("Welcome!")
name1=(input("Please enter name of Player 1: ")).title()
name2=(input("Please enter name of Player 2: ")).title()
keep_playing=True

while keep_playing==True:
    os.system('cls')
    game = TicTacToe(name1, name2)
    game.play_game()
    print(game.score)
    continue_game = input("Do you want to continue playing? Type 'yes' or 'no':")
    if continue_game.lower()=="yes":
        keep_playing=True
    else:
        keep_playing=False

print(thanks)
print("For more visit me at http://narendrakashikar.life")
print()