import tkinter as tk
from tkinter import Entry, END
from tkinter.ttk import *
from PIL import ImageTk, Image
import random
import csv

def start_game(bat_or_bowl, selected_players, overs, username):

    overs = int(overs)

    game = tk.Tk()
    game.title(f"Quicket-Singleplayer_{overs}-overs_{bat_or_bowl}")
    game.geometry('1100x600')
    game.resizable(False, False)
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    game.iconphoto(True, p1)

    # setting batting and bowling order for computer
    computer_batsmen_unpicked = []
    computer_bowlers_unpicked = []
    computer_alr_unpicked = []
    computer_wk_unpicked = []

    with open(r'all_data\batsmen_data.csv', 'r') as bat_data:
        reader = csv.reader(bat_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_batsmen_unpicked.append([row[0], row[2]])
    with open(r'all_data\bowlers_data.csv', 'r') as bowl_data:
        reader = csv.reader(bowl_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_bowlers_unpicked.append([row[0], row[2]])
    with open(r'all_data\all_rounders_data.csv', 'r') as alr_data:
        reader = csv.reader(alr_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_alr_unpicked.append([row[0], row[2]])
    with open(r'all_data\wk_keepers_data.csv', 'r') as wk_data:
        reader = csv.reader(wk_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_wk_unpicked.append([row[0], row[2]])
    
    # Randomly select 11 players for computer
    # Randomly select 4 batsmen
    computer_batsmen = random.sample(computer_batsmen_unpicked, 4)
    # Randomly select 3 bowlers
    computer_bowlers = random.sample(computer_bowlers_unpicked, 3)
    # Randomly select 3 all-rounders
    computer_alr = random.sample(computer_alr_unpicked, 3)
    # Randomly select 1 wicket-keeper
    computer_wk = random.sample(computer_wk_unpicked, 1)
    # print(computer_batsmen, computer_bowlers, computer_alr, computer_wk)
    

    player_batsmen = selected_players[0]
    player_bowlers = selected_players[1]
    player_alr = selected_players[2]
    player_wk = selected_players[3]
    
    random.shuffle(player_batsmen)
    random.shuffle(player_alr)
    random.shuffle(player_wk)
    random.shuffle(player_bowlers)

    player_batting_order = player_batsmen + player_alr + player_wk + player_bowlers
    player_bowling_order = player_bowlers + player_alr

    computer_batting_order = computer_batsmen + computer_alr + computer_wk + computer_bowlers
    computer_bowling_order = computer_bowlers + computer_alr

    # omkaar
    
    innings_completed = 0  # Track the number of completed innings

    # List of types of balls for computer (random) and user (choice)
    ball_types = ['Fast', 'Spin', 'Swing', 'Bouncer', 'Yorker']
    bat_types = ['Pull', 'Drive', 'Defend', 'Loft', 'Cut']  # List of bat types

    probabilities = {
    'fast': {'defend': 0.1, 'drive': 0.2, 'loft': 0.3, 'cut': 0.4, 'pull': 0.5},
    'spin': {'defend': 0.1, 'drive': 0.2, 'cut': 0.3, 'loft': 0.4, 'pull': 0.5},
    'swing': {'defend': 0.1, 'pull': 0.2, 'drive': 0.3, 'loft': 0.4, 'cut': 0.5},
    'bouncer': {'pull': 0.1, 'loft': 0.2, 'cut': 0.3, 'defend': 0.4, 'drive': 0.5},
    'yorker': {'defend': 0.1, 'drive': 0.2, 'loft': 0.3, 'cut': 0.4, 'pull': 0.5}
    }

    def get_next_batsman_player():
        nonlocal player_batting_order
        try:
            return player_batting_order.pop(0)
        except IndexError:
            return ['All out', 0, 0]
    
    def get_next_bowler_player():
        nonlocal player_bowling_order
        return player_bowling_order.pop(0)
    
    
    def get_next_batsman_computer():
        nonlocal computer_batting_order
        try:
            return computer_batting_order.pop(0)
        except IndexError:
            return ['All out',0, 0]
    
    def get_next_bowler_computer():
        nonlocal computer_bowling_order
        return computer_bowling_order.pop(0)


    def flash_score(score, flash_label):
        flash_label.config(text=str(score))
        game.after(1500, lambda: flash_label.config(text=""))  # Reset after 1.5 second

    def clear_widgets(widget_list):
            """Clear all widgets in the provided list."""
            for widget in widget_list:
                widget.destroy()
            widget_list.clear()

    runs = 0
    runs_pc = 0
    run_rate = 0.0
    run_rate_pc = 0.0
    economy = 0.0
    economy_pc = 0.0
    wickets = 0
    wickets_pc = 0
    Batting_Average = 0.0
    Batting_Average_pc = 0.0
    Batting_Overs = 0.0
    Bowling_Overs = 0.0
    Total_Overs = 0.0
    batting_widgets = []

    def save_data(wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs):
            rows = []
            with open(r'all_data\user_data.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)

                for i in rows:
                    if i[1] == username:
                        i[8] = int(i[8]) + wickets
                        i[9] = int(i[9]) + runs
                        i[10] = (float(i[10]) + float(economy)) / (float(i[14]) + float(Bowling_Overs))
                        i[11] = int(i[11]) + innings_completed
                        i[12] = (float(i[12]) + float(Batting_Average)) / (float(i[13]) + float(Batting_Overs))
                        i[13] = float((i[13])) + float(Batting_Overs)
                        i[14] = float((i[14])) + float(Bowling_Overs)
                        i[15] = float(((i[15]))) + float(Total_Overs)
                        break

            with open(r'all_data\user_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    
    def show_final_scores(player_batting_order, computer_batting_order):
        nonlocal runs, runs_pc, run_rate, run_rate_pc, wickets, wickets_pc, economy, economy_pc, Batting_Average, Batting_Average_pc, Batting_Overs, Bowling_Overs, Total_Overs, bat_or_bowl

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



    def batting():
        
        balls_faced = 0

        current_batsman = player_batting_order[0][0]
        current_bowler = computer_bowling_order[0][0]
        current_batsman_rating = player_batting_order[0][1]

        # Live labels for batting
        balls_faced_label = tk.Label(game, text=f"Balls Faced: {balls_faced}", font=('calibre', 20, 'bold'))
        balls_faced_label.pack()
        batting_widgets.append(balls_faced_label)
        current_batsman_label = tk.Label(game, text=f"Current Batsman: {current_batsman}", font=('calibre', 20, 'bold'))
        current_batsman_label.pack()
        batting_widgets.append(current_batsman_label)
        current_bowler_label = tk.Label(game, text=f"Current Bowler: {current_bowler}", font=('calibre', 20, 'bold'))
        current_bowler_label.pack()
        batting_widgets.append(current_bowler_label)
        runs_label = tk.Label(game, text=f"Runs: {runs}", font=('calibre', 20, 'bold'))
        runs_label.pack()
        batting_widgets.append(runs_label)
        run_rate_label = tk.Label(game, text=f"Run Rate: {run_rate:.2f}", font=('calibre', 20, 'bold'))
        run_rate_label.pack()
        batting_widgets.append(run_rate_label)
        ball_type_label = tk.Label(game, text="Ball Type:", font=('calibre', 20, 'bold'))
        ball_type_label.pack()
        batting_widgets.append(ball_type_label)
        flash_label = tk.Label(game, text="", font=('calibre', 40, 'bold'), fg='red')
        flash_label.pack()
        batting_widgets.append(flash_label)

        def get_ball_type():
            ball_type = random.choice(ball_types)
            ball_type_label.config(text=f"Ball Type: {ball_type}")
            return ball_type
        
        ball_type = get_ball_type()


        def update_batting_labels():
            # Update all live labels for batting
            runs_label.config(text=f"Runs: {runs}")
            balls_faced_label.config(text=f"Balls Faced: {balls_faced}")
            current_batsman_label.config(text=f"Current Batsman: {current_batsman}")
            run_rate_label.config(text=f"Run Rate: {run_rate:.2f}")
            current_bowler_label.config(text=f"Current Bowler: {current_bowler}")


        def submit_bat_choice():

            nonlocal player_batting_order, computer_batting_order, runs, balls_faced, run_rate, current_batsman, current_batsman_rating, current_bowler, innings_completed, ball_type, wickets, wickets_pc, runs, economy, economy_pc, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs


            def bowl_now():
                nonlocal Batting_Average, Batting_Overs, runs, economy_pc

                Batting_Overs = float(balls_faced / 6)
                Batting_Average = float(runs / Batting_Overs)                
                economy_pc = float(runs / Batting_Overs)
                clear_widgets(batting_widgets)
                bowling()


            if balls_faced % 6 == 0:
                if balls_faced == (overs * 6) / 2:
                    # Halfway through the innings
                    innings_completed += 1
                    if innings_completed == 2:
                        Batting_Overs = float(balls_faced / 6)
                        Batting_Average = float(runs / Batting_Overs)
                        economy_pc = float(runs / Batting_Overs)
                        Total_Overs = float(overs)
                        save_data(wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
                        clear_widgets(batting_widgets)
                        tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                        show_final_scores(player_batting_order, computer_batting_order)
                        return
                    else:
                        bowl_now()
                        tk.messagebox.showinfo("Innings over", "Your innings is over. Click OK to start bowling.")
                else:
                    current_batsman_and_rating = get_next_batsman_player()
                    current_batsman, current_batsman_rating = current_batsman_and_rating[0], current_batsman_and_rating[1]

                    if current_batsman == 'All out':
                        # All out
                        innings_completed += 1
                        if innings_completed == 2:
                            Batting_Overs = float(balls_faced / 6)
                            Batting_Average = float(runs / Batting_Overs)
                            economy_pc = float(runs / Batting_Overs)
                            Total_Overs = float(overs)
                            save_data(wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
                            clear_widgets(batting_widgets)
                            tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                            show_final_scores(player_batting_order, computer_batting_order)
                            return
                        else:
                            bowl_now()
                            tk.messagebox.showinfo("Innings over", "Your innings is over: ALL BATSMEN USED. Click OK to start bowling.")
                    
                    current_bowler = get_next_bowler_computer()[0]

            # Reset flash label immediately
            try:
                flash_label.config(text="")
            except tk.TclError:
                pass                            # Suppress error if widget doesn't exist

            try:
                # Disable Bat button for 2 secs
                bat_button.config(state=tk.DISABLED)

                # After 2 seconds, enable Bat button and allow player to choose shot
                game.after(2000, lambda: bat_button.config(state=tk.NORMAL))
            
                # Scale the rating to influence the probability (90+ gives a higher probability of success)
                rating_factor = 1 + ((float(current_batsman_rating) - 90.0)) / 10  # rating_factor > 1 if rating > 90

                selected_bat_type = bat_type_var.get()
                probability = probabilities[ball_type.lower()][selected_bat_type.lower()]
                adjusted_probability = probability / rating_factor
                random_number = random.uniform(0, 1)

                if random_number > adjusted_probability:
                    if selected_bat_type.lower() == 'defend':
                        hit = random.choice([0, 1])
                    else:
                        hit = random.choice([0, 1, 4, 6])
                    runs += hit
                    balls_faced += 1
                    run_rate = (runs / balls_faced) * 6

                    # Flash the score
                    if hit == 0:
                        flash_score('dot ball', flash_label)
                    else:
                        flash_score(hit, flash_label)
                    
                    # Update all labels
                    update_batting_labels()
                
                else:
                    # Flash the score
                    flash_score('OUT', flash_label)
                    wickets_pc += 1
                    balls_faced += 1
                    runs += 0
                    run_rate = (runs / balls_faced) * 6

                    # Get next batsman
                    current_batsman_and_rating = get_next_batsman_player()
                    current_batsman, current_batsman_rating = current_batsman_and_rating[0], current_batsman_rating[1]
                    if current_batsman == 'All out':
                        # All out
                        innings_completed += 1
                        if innings_completed == 2:
                            Batting_Overs = float(balls_faced / 6)
                            Batting_Average = float(runs / Batting_Overs)
                            Total_Overs = float(overs)
                            economy_pc = float(runs / Batting_Overs)
                            save_data(wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
                            clear_widgets(batting_widgets)
                            tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                            show_final_scores(player_batting_order, computer_batting_order)
                            return
                        else:
                            bowl_now()
                            tk.messagebox.showinfo("Innings over", "Your innings is over: ALL OUT. Click OK to start bowling.")
                            return

                # Update all labels
                update_batting_labels()

                ball_type = get_ball_type()

                # Disable Bat button for 2 secs
                bat_button.config(state=tk.DISABLED)

                # After 2 seconds, enable Bat button and allow player to choose shot
                game.after(2000, lambda: bat_button.config(state=tk.NORMAL))

            except tk.TclError:
                pass

        # Drop-down to select bat type
        bat_type_var = tk.StringVar()
        bat_type_dropdown = Combobox(game, textvariable=bat_type_var, values=bat_types, state="readonly", font=('calibre', 20, 'bold'))
        bat_type_dropdown.pack()
        batting_widgets.append(bat_type_dropdown)

        # Button to submit the bat choice
        bat_button = tk.Button(game, text="Bat", command=submit_bat_choice, font=('calibre', 20, 'bold'))
        bat_button.pack()
        batting_widgets.append(bat_button)
    

    def bowling():
        balls_bowled = 0
        bat_type = '--'
        bowling_widgets = []

        # If it's the start of the bowling phase
        current_batsman = computer_batting_order[0][0]
        current_bowler = player_bowling_order[0][0]
        current_bowler_rating = player_bowling_order[0][2]

        # Live labels for bowling
        balls_bowled_label = tk.Label(game, text=f"Balls Bowled: {balls_bowled}", font=('calibre', 20, 'bold'))
        balls_bowled_label.pack()
        bowling_widgets.append(balls_bowled_label)
        current_batsman_label = tk.Label(game, text=f"Current Batsman: {current_batsman}", font=('calibre', 20, 'bold'))
        current_batsman_label.pack()
        bowling_widgets.append(current_batsman_label)
        current_bowler_label = tk.Label(game, text=f"Current Bowler: {current_bowler}", font=('calibre', 20, 'bold'))
        current_bowler_label.pack()
        bowling_widgets.append(current_bowler_label)
        runs_scored_label = tk.Label(game, text=f"Runs: {runs_pc}", font=('calibre', 20, 'bold'))
        runs_scored_label.pack()
        bowling_widgets.append(runs_scored_label)
        run_rate_pc_label_bowling = tk.Label(game, text=f"Run Rate: {run_rate_pc:.2f}", font=('calibre', 20, 'bold'))
        run_rate_pc_label_bowling.pack()
        bowling_widgets.append(run_rate_pc_label_bowling)
        bat_type_label = tk.Label(game, text=f"Bat Type: {bat_type}", font=('calibre', 20, 'bold'))
        bat_type_label.pack()
        bowling_widgets.append(bat_type_label)
        flash_label = tk.Label(game, text="", font=('calibre', 40, 'bold'), fg='red')
        flash_label.pack()
        bowling_widgets.append(flash_label)

        def update_bowling_labels():
            # Update all live labels for bowling
            current_batsman_label.config(text=f"Current Batsman: {current_batsman}")
            current_bowler_label.config(text=f"Current Bowler: {current_bowler}")
            balls_bowled_label.config(text=f"Balls Bowled: {balls_bowled}")
            runs_scored_label.config(text=f"Runs: {runs_pc}")
            run_rate_pc_label_bowling.config(text=f"Run Rate: {run_rate_pc:.2f}")

        def get_bat_type():
            bat_type = random.choice(bat_types)
            return bat_type
        
        bat_type = get_bat_type()

        def bowl_ball():
            nonlocal player_batting_order, computer_batting_order, runs_pc, run_rate_pc, balls_bowled, Batting_Average_pc, run_rate, current_batsman, current_bowler,current_bowler_rating, innings_completed, bat_type, wickets, runs, economy, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs

            def bat_now():

                nonlocal Bowling_Overs, economy, runs_pc, Batting_Average_pc
                Bowling_Overs = float(balls_bowled / 6)
                economy = float(runs_pc / Bowling_Overs)
                Batting_Average_pc = float(runs_pc / Bowling_Overs)

                clear_widgets(bowling_widgets)
                batting()

            # Reset flash label immediately
            flash_label.config(text="")

            # Check if innings are over
            if balls_bowled % 6 == 0:
                if balls_bowled == (overs * 6) / 2:
                    # End of innings
                    innings_completed += 1
                    if innings_completed == 2:
                        Bowling_Overs = float(balls_bowled / 6)
                        Total_Overs = float(overs)
                        economy = float(runs_pc / Bowling_Overs)
                        Batting_Average_pc = float(runs_pc / Bowling_Overs)
                        save_data(wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
                        clear_widgets(bowling_widgets)
                        tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                        show_final_scores(player_batting_order, computer_batting_order)
                        return
                    else:
                        bat_now()
                        tk.messagebox.showinfo("Innings Over", "Your innings is over. Click OK to start batting.")
                        return
                else:
                    current_batsman = get_next_batsman_computer()[0]
                    current_bowler_and_rating = get_next_bowler_player()
                    current_bowler, current_bowler_rating = current_bowler_and_rating[0], current_bowler_and_rating[2]

                    if current_batsman == 'All out':
                        innings_completed += 1
                        if innings_completed == 2:
                            Bowling_Overs = float(balls_bowled / 6)
                            Total_Overs = float(overs)
                            economy = float(runs_pc / Bowling_Overs)
                            Batting_Average_pc = float(runs_pc / Bowling_Overs)
                            save_data(wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
                            clear_widgets(bowling_widgets)
                            tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                            show_final_scores(player_batting_order, computer_batting_order)
                            return
                        else:
                            bat_now()
                            tk.messagebox.showinfo("Innings Over", "Your innings is over: ALL BATSMEN USED. Click OK to start batting.")
                            return

            try:

                # User selects ball type
                selected_ball_type = ball_type_var.get()
                balls_bowled += 1

                # Scale the rating to influence the probability (90+ gives a higher probability of success)
                rating_factor = 1 + ((float(current_bowler_rating) - 90.0) / 10)  # rating_factor > 1 if rating > 90

                # Simulate the batsman's response based on probabilities
                probability = probabilities[selected_ball_type.lower()][bat_type.lower()]
                adjusted_probability = probability / rating_factor
                random_number = random.uniform(0, 1)

                # Determine if the computer batsman is out
                if random_number < adjusted_probability:
                    flash_score('OUT', flash_label)
                    wickets += 1
                    run_rate_pc = (runs_pc / balls_bowled) * 6
                    current_batsman = get_next_batsman_computer()[0]
                    if current_batsman == 'All out':
                        innings_completed += 1
                        if innings_completed == 2:
                            Bowling_Overs = float(balls_bowled / 6)
                            economy = runs_pc / Bowling_Overs
                            Total_Overs = float(overs)
                            Batting_Average_pc = float(runs_pc / Bowling_Overs)
                            save_data(wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
                            clear_widgets(bowling_widgets)
                            tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                            show_final_scores(player_batting_order, computer_batting_order)
                            return
                        else:
                            bat_now()
                            tk.messagebox.showinfo("Innings Over", "Your innings is over: ALL OUT. Click OK to start batting.")
                            return
                else:
                    if bat_type.lower() == 'defend':
                        hit = random.choice([0, 1])
                    else:
                        hit = random.choice([0, 1, 4, 6])
                    runs_pc += hit
                    run_rate_pc = (runs_pc / balls_bowled) * 6
                    if hit == 0:
                        flash_score('dot ball', flash_label)
                    else:
                        flash_score(hit, flash_label)

                bat_type_label.config(text=f"Bowl countered with: {bat_type}")

                # Update all labels
                update_bowling_labels()

                # Get next bat type
                bat_type = get_bat_type()

                # Disable Bowl button for 3 seconds
                bowl_button.config(state=tk.DISABLED)
                game.after(2000, lambda: bowl_button.config(state=tk.NORMAL))
            
            except tk.TclError:
                pass

        # Drop-down to select ball type
        ball_type_var = tk.StringVar()
        ball_type_dropdown = Combobox(game, textvariable=ball_type_var, values=ball_types, state="readonly", font=('calibre', 20, 'bold'))
        ball_type_dropdown.pack()
        bowling_widgets.append(ball_type_dropdown)

        # Button to simulate bowling a ball
        bowl_button = tk.Button(game, text="Bowl", command=bowl_ball, font=('calibre', 20, 'bold'))
        bowl_button.pack()
        bowling_widgets.append(bowl_button)

    if bat_or_bowl == 'bat':
        batting()
    elif bat_or_bowl == 'bowl':
        bowling()

    game.mainloop()
