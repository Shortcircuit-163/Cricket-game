import tkinter as tk
from tkinter import Entry, END
from tkinter.ttk import *
from PIL import ImageTk, Image
import random
import csv


game = tk.Tk()
game.title(f"Quicket - Cricket Scorecard")
game.geometry('1100x600')
game.resizable(False, False)
p1 = tk.PhotoImage(file=r'images\home\quicket.png')
game.iconphoto(True, p1)

def show_final_scores(player_batting_order, computer_batting_order):

        win_player = ''
        win_pc = ''

        # Determine the winner
        if runs >= runs_pc:
            if bat_or_bowl == 'bowl':
                win_player = f'You have won by {11 - len(player_batting_order)} wickets!'
                win_pc = f'Lost. Player beat the target with {11 - len(player_batting_order)} wickets remaining!'
            else:
                win_player = f'You have won by {runs - runs_pc} runs!'
                win_pc = f'Lost. Fell short of {runs - runs_pc} runs!'
        else:
            if bat_or_bowl == 'bowl':
                win_player = f'Lost. You fell short of {runs_pc - runs} runs!'
                win_pc = f'Won by {runs_pc - runs} runs!'
            else:
                win_player = f'Lost. Computer beat your target with {11 - len(computer_batting_order)} wickets remaining!'
                win_pc = f'Won by {11 - len(computer_batting_order)} wickets!'

        # List for table data
        lst = [
            ('STATS', 'PLAYER', 'COMPUTER'),
            ('WINNER:', win_player, win_pc),
            ('Runs:', runs, runs_pc),
            ('Run Rate:', run_rate, run_rate_pc),
            ('Wickets:', wickets, wickets_pc),
            ('Economy:', economy, economy_pc),
            ('Batting Average:', Batting_Average, Batting_Average_pc),
            ('Batting Overs:', Batting_Overs, Batting_Overs),
            ('Bowling Overs:', Bowling_Overs, Bowling_Overs),
            ('Total Overs:', Total_Overs, Total_Overs)
        ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        colours = ['#AFEEEE', '#F5FFFA', '#FFF0F5', '#F0FFF0', '#FFE4E1', '#FFFACD', '#FAFAD2', '#F0F8FF']
        #'Light_Coral' : '#F08080' taken for 1st row

        # Table class
        class Table:
            def __init__(self, root):
                x = -2
                for i in range(total_rows):
                    for j in range(total_columns):
                        colour = colours[x]
                        if i == 0:  # For the header
                            self.e = tk.Label(root, width=20, height=3, foreground='white', background='dark grey',
                                              font=('Arial', 20, 'bold'), anchor='w', padx=10)
                        elif i == 1:  # For the row with the win/loss messages
                            self.e = tk.Label(root, width=20, height=2, wraplength=300, background='#F08080',
                                              font=('Arial', 16, 'bold'), anchor='w', padx=10)
                        else:
                            self.e = tk.Label(root, width=20, height=2, background=colour, font=('Arial', 16), anchor='w', padx=10)
                        
                        self.e.grid(row=i, column=j, sticky='nsew')  # sticky option to stretch widgets
                        self.e.config(text=lst[i][j])
                
                    x += 1

        # Create the table in the 'game' window
        table = Table(game)



runs, runs_pc = 250, 230
run_rate, run_rate_pc = 5.5, 4.8
wickets, wickets_pc = 6, 9
economy, economy_pc = 4.5, 5.0
Batting_Average, Batting_Average_pc = 40.0, 35.0
Batting_Overs, Bowling_Overs, Total_Overs = 50, 50, 50
bat_or_bowl = 'bowl'
player_batting_order = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6']
computer_batting_order = ['Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5']

# Show the final scores
show_final_scores(player_batting_order, computer_batting_order)

game.mainloop()