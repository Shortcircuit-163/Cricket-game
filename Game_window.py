import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv

def game(username, overs):
    game = tk.Tk()
    game.title("Quicket-Singleplayer")
    game.geometry('650x800')
    game.resizable(False, False)
    # sp.configure(background='light grey')
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    game.iconphoto(True, p1)

    info = username + str(overs)
    heading = Label(game, text=info, font=('Times New Roman', 50, 'bold', 'underline'))
    heading.grid(row=0, column=1)

    game.mainloop()
    