import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv
import random

def game(username, name, overs):
    game = tk.Tk()
    game.title("Quicket-Singleplayer")
    game.geometry('650x800')
    game.resizable(False, False)
    # sp.configure(background='light grey')
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    game.iconphoto(True, p1)

    info = f"Hello {name}, -- Current game: {str(overs)} match"
    heading = Label(game, text=info, font=('Times New Roman', 50, 'bold', 'underline'), background='light grey')
    heading.grid(row=0, column=0)

    player_status = ''
    
    toss_list = ['heads', 'tails']
    toss = random.choice(toss_list)
    print(f'Toss result: {toss}')
    if toss == 'heads':
        player_status = 




    game.mainloop()
    