import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv
import random

def pre_game(username, name, overs):
    pre_game = tk.Tk()
    pre_game.title("Quicket-Singleplayer")
    pre_game.geometry('1000x600')
    pre_game.resizable(False, False)
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    pre_game.iconphoto(True, p1)

    def toss_handle(toss_status):
        options_list = ['bat', 'bowl']
        if toss_status == 'can_choose':
            toss_msg = 'You have won the toss! Please choose to bat or bowl.'
            top = tk.Toplevel(pre_game)
            top.title("Toss result")
            top.geometry("350x150")

            message = tk.Label(top, text=toss_msg)
            message.pack(pady=20)

            response = tk.StringVar(value="")

            def on_bat():
                response.set("bat")
                top.destroy()

            def on_bowl():
                response.set("bowl")
                top.destroy()

            button1 = tk.Button(top, text="Bat", command=on_bat, background='light grey')
            button1.pack(side=tk.LEFT, padx=20)

            button2 = tk.Button(top, text="Bowl", command=on_bowl, background='light grey')
            button2.pack(side=tk.RIGHT, padx=20)

            top.wait_window()  # Wait for the user to make a selection
            return response.get()

        elif toss_status == 'cannot_choose':
            computer_select = random.choice(options_list)
            player_select = options_list[0] if computer_select == options_list[1] else options_list[1]
            toss_msg = f'''You have lost the toss! The computer has chosen to {computer_select}.
            You will be {player_select}ing first.'''

            tk.messagebox.showinfo("Toss result", toss_msg)
            return player_select

    def players_select():

        def submit_selection():
            selected_indices = listbox.curselection()
            selected_players = [listbox.get(i) for i in selected_indices]
            
            if len(selected_players) != 11:
                messagebox.showwarning("Selection Error", "You must select exactly 11 players.")
            else:
                print("Selected Players:", selected_players)
                listbox.destroy()
                scrollbar.destroy()
                submit_button.destroy()
                pre_game.destroy()
                from Game import start_game
                start_game(bat_or_bowl, selected_players, overs) # FIX: SELECTED PLAYERS LIST IS EMPTY

        players = []
        path = r'Data\users\player_data_' + username + '.csv'
        with open(path, 'r') as p_names:
            player_names = csv.reader(p_names)
            for row in player_names:
                if row[0] == 'players':
                    continue
                player = row[0]
                role = row[1]
                players.append(f"{player} ----- {role}")

        # Create a Listbox with MULTIPLE selection mode
        listbox = tk.Listbox(toss_frame, selectmode=tk.MULTIPLE, height=15, font=('calibre', 15))
        for i in players:
            listbox.insert(tk.END, i)
        listbox.grid(row=1, column=0, sticky='w', pady=10, padx=10)

        # Add a Scrollbar
        scrollbar = tk.Scrollbar(toss_frame, orient="vertical")
        scrollbar.grid(row=1, column=1, sticky='ns')
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Button to submit the selection
        submit_button = tk.Button(toss_frame, text="Submit Selection", command=submit_selection, font=('calibre', 15, 'bold'))
        submit_button.grid(row=2, column=0, columnspan=2, pady=20)

    choice_var = tk.StringVar()

    def toss_outcome():
        global bat_or_bowl
        global selected_players_lst  # Access the global variable
        
        choice = choice_var.get()
        toss = random.choice(toss_list)
        print(f'User chose: {choice}')
        print(f'Toss result: {toss}')
        if toss == choice:
            toss_status = 'can_choose'
            bat_or_bowl = toss_handle(toss_status)
        else:
            toss_status = 'cannot_choose'
            bat_or_bowl = toss_handle(toss_status)

        # Destroy the selection box and button after the toss
        choice_entry_label.destroy()
        choice_dropdown.destroy()
        choose_button.destroy()

        print(f"User is {bat_or_bowl}ing")
        players_select()

    info = f"Hello {name}, -- Current game: {str(overs)} match"
    heading = Label(pre_game, text=info, font=('Times New Roman', 50, 'bold', 'underline'), background='light grey')
    heading.grid(row=0, column=0, pady=20)

    toss_frame = tk.Frame(pre_game, background='light grey')
    toss_frame.grid(row=1, column=0, sticky='w')

    choice_entry_label = tk.Label(toss_frame, text='Choose heads or tails:', font=('calibre', 20, 'bold'), background='light grey')
    choice_entry_label.grid(row=0, column=0, sticky='w')

    toss_list = ['heads', 'tails']
    choice_dropdown = Combobox(toss_frame, textvariable=choice_var, values=toss_list, state="readonly", font=('calibre', 19, 'bold'), background='light grey')
    choice_dropdown.grid(row=0, column=1, sticky='w')

    choose = tk.PhotoImage(file=r'images\game_window\tick.png')
    choose_button = tk.Button(toss_frame, image=choose, command=toss_outcome, borderwidth=0, background='light grey')
    choose_button.grid(row=0, column=2, pady=20)

    pre_game.mainloop()

pre_game('user_1', 'Rishi', 2)
