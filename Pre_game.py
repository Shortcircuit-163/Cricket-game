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
            player_composition = []
            # Check and gather the selections
            selected_indices_bat = listbox_bat.curselection()
            selected_players_bat = [listbox_bat.get(i) for i in selected_indices_bat]
            if len(selected_players_bat) != 4:
                player_composition.append('not_ok')
            else:
                player_composition.append('ok')

            selected_indices_bowl = listbox_bowl.curselection()
            selected_players_bowl = [listbox_bowl.get(i) for i in selected_indices_bowl]
            if len(selected_players_bowl) != 3:
                player_composition.append('not_ok')
            else:
                player_composition.append('ok')

            selected_indices_wk = listbox_wk.curselection()
            selected_players_wk = [listbox_wk.get(i) for i in selected_indices_wk]
            if len(selected_players_wk) != 1:
                player_composition.append('not_ok')
            else:
                player_composition.append('ok')

            selected_indices_alr = listbox_ar.curselection()
            selected_players_alr = [listbox_ar.get(i) for i in selected_indices_alr]
            if len(selected_players_alr) != 3:
                player_composition.append('not_ok')
            else:
                player_composition.append('ok')

            # Validation check
            if 'not_ok' in player_composition:
                messagebox.showwarning("Selection Error", "You must select exactly 11 players: 4 batsmen, 3 bowlers, 1 wicketkeeper, and 3 all-rounders.")
            else:
                selected_players = []
                selected_players.append(selected_players_bat)
                selected_players.append(selected_players_bowl)
                selected_players.append(selected_players_alr)
                selected_players.append(selected_players_wk)
                for widget in all_widgets:
                    widget.destroy()
                pre_game.destroy()
                from Game import start_game
                start_game(bat_or_bowl, selected_players, overs)

        batsmen = []
        bowlers = []
        wicketkeepers = []
        allrounders = []
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
                if role == 'bat':
                    batsmen.append(player)
                elif role == 'bowl':
                    bowlers.append(player)
                elif role == 'wk':
                    wicketkeepers.append(player)
                elif role == 'alr':
                    allrounders.append(player)

        all_widgets = []

        # Headings for each listbox
        tk.Label(toss_frame, text="Batsmen", font=('calibre', 15, 'bold')).grid(row=0, column=0, sticky='w')
        tk.Label(toss_frame, text="Bowlers", font=('calibre', 15, 'bold')).grid(row=0, column=2, sticky='w')
        tk.Label(toss_frame, text="Wicketkeepers", font=('calibre', 15, 'bold')).grid(row=0, column=4, sticky='w')
        tk.Label(toss_frame, text="All-rounders", font=('calibre', 15, 'bold')).grid(row=0, column=6, sticky='w')

        # Listbox for batsmen
        listbox_bat = tk.Listbox(toss_frame, selectmode=tk.MULTIPLE, height=15, font=('calibre', 15), exportselection=False)
        for batsman in batsmen:
            listbox_bat.insert(tk.END, batsman)
        listbox_bat.grid(row=1, column=0, sticky='w', pady=10, padx=10)
        all_widgets.append(listbox_bat)

        # Scrollbar for batsmen
        scrollbar_bat = tk.Scrollbar(toss_frame, orient="vertical")
        scrollbar_bat.grid(row=1, column=1, sticky='ns')
        listbox_bat.config(yscrollcommand=scrollbar_bat.set)
        scrollbar_bat.config(command=listbox_bat.yview)
        all_widgets.append(scrollbar_bat)

        # Listbox for bowlers
        listbox_bowl = tk.Listbox(toss_frame, selectmode=tk.MULTIPLE, height=15, font=('calibre', 15), exportselection=False)
        for bowler in bowlers:
            listbox_bowl.insert(tk.END, bowler)
        listbox_bowl.grid(row=1, column=2, sticky='w', pady=10, padx=10)
        all_widgets.append(listbox_bowl)

        # Scrollbar for bowlers
        scrollbar_bowl = tk.Scrollbar(toss_frame, orient="vertical")
        scrollbar_bowl.grid(row=1, column=3, sticky='ns')
        listbox_bowl.config(yscrollcommand=scrollbar_bowl.set)
        scrollbar_bowl.config(command=listbox_bowl.yview)
        all_widgets.append(scrollbar_bowl)

        # Listbox for wicketkeepers
        listbox_wk = tk.Listbox(toss_frame, selectmode=tk.MULTIPLE, height=15, font=('calibre', 15), exportselection=False)
        for wicketkeeper in wicketkeepers:
            listbox_wk.insert(tk.END, wicketkeeper)
        listbox_wk.grid(row=1, column=4, sticky='w', pady=10, padx=10)
        all_widgets.append(listbox_wk)

        # Scrollbar for wicketkeepers
        scrollbar_wk = tk.Scrollbar(toss_frame, orient="vertical")
        scrollbar_wk.grid(row=1, column=5, sticky='ns')
        listbox_wk.config(yscrollcommand=scrollbar_wk.set)
        scrollbar_wk.config(command=listbox_wk.yview)
        all_widgets.append(scrollbar_wk)

        # Listbox for all-rounders
        listbox_ar = tk.Listbox(toss_frame, selectmode=tk.MULTIPLE, height=15, font=('calibre', 15), exportselection=False)
        for allrounder in allrounders:
            listbox_ar.insert(tk.END, allrounder)
        listbox_ar.grid(row=1, column=6, sticky='w', pady=10, padx=10)
        all_widgets.append(listbox_ar)

        # Scrollbar for all-rounders
        scrollbar_ar = tk.Scrollbar(toss_frame, orient="vertical")
        scrollbar_ar.grid(row=1, column=7, sticky='ns')
        listbox_ar.config(yscrollcommand=scrollbar_ar.set)
        scrollbar_ar.config(command=listbox_ar.yview)
        all_widgets.append(scrollbar_ar)

        # Submit button
        submit_button = tk.Button(toss_frame, text="Submit Selection", command=submit_selection, font=('calibre', 15, 'bold'))
        submit_button.grid(row=2, column=3, columnspan=2, pady=20)
        all_widgets.append(submit_button)

    choice_var = tk.StringVar()

    def toss_outcome():
        global bat_or_bowl
        
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

        # bat_or_bowl = 'bowl' # For testing purposes
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

pre_game('user_1', 'Rishi', 4)
