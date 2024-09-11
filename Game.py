import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import random
import csv
import time

def start_game(bat_or_bowl, selected_players, overs):

    game = tk.Tk()
    game.title(f"Quicket-Singleplayer_{overs}-overs_{bat_or_bowl}")
    game.geometry('1000x600')
    game.resizable(False, False)
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    game.iconphoto(True, p1)

    # setting batting and bowling order for computer
    computer_batsmen_unpicked = []
    computer_bowlers_unpicked = []
    computer_alr_unpicked = []
    computer_wk_unpicked = []

    with open(r'Data\batsmen_data.csv', 'r') as bat_data:
        reader = csv.reader(bat_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_batsmen_unpicked.append(row[0])
    with open(r'Data\bowlers_data.csv', 'r') as bowl_data:
        reader = csv.reader(bowl_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_bowlers_unpicked.append(row[0])
    with open(r'Data\all_rounders_data.csv', 'r') as alr_data:
        reader = csv.reader(alr_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_alr_unpicked.append(row[0])
    with open(r'Data\wk_keepers_data.csv', 'r') as wk_data:
        reader = csv.reader(wk_data)
        for row in reader:
            if row[0] == 'name':
                continue
            else:
                computer_wk_unpicked.append(row[0])
    
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
    'fast': {'defend': 0.1, 'drive': 0.25, 'loft': 0.3, 'cut': 0.5, 'pull': 0.7},
    'spin': {'defend': 0.1, 'drive': 0.25, 'cut': 0.3, 'loft': 0.5, 'pull': 0.7},
    'swing': {'defend': 0.1, 'pull': 0.25, 'drive': 0.3, 'loft': 0.5, 'cut': 0.7},
    'bouncer': {'pull': 0.1, 'loft': 0.25, 'cut': 0.3, 'defend': 0.5, 'drive': 0.7},
    'yorker': {'defend': 0.1, 'drive': 0.25, 'loft': 0.3, 'cut': 0.5, 'pull': 0.7}
    }


    def get_next_batsman_player():
        nonlocal player_batting_order
        try:
            return player_batting_order.pop(0)
        except IndexError:
            return 'All out'
    
    def get_next_bowler_player():
        nonlocal player_bowling_order
        return player_bowling_order.pop(0)
    
    def get_next_batsman_computer():
        nonlocal computer_batting_order
        try:
            return computer_batting_order.pop(0)
        except IndexError:
            return 'All out'
    
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

    def batting():

        runs = 0
        balls_faced = 0
        run_rate = 0.0
        batting_widgets = []
        

        current_batsman = player_batting_order[0]
        current_bowler = computer_bowling_order[0]

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

            def bowl_now():
                time.sleep(2.1)
                clear_widgets(batting_widgets)
                bowling()


            nonlocal runs, balls_faced, run_rate, current_batsman, current_bowler, innings_completed, ball_type

            if balls_faced % 6 == 0:
                if balls_faced == (overs * 6) / 2:
                    # Halfway through the innings
                    innings_completed += 1
                    if innings_completed == 2:
                        tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                        game.quit()
                        return
                    else:
                        tk.messagebox.showinfo("Innings over", "Your innings is over. Click OK to start bowling.")
                        bowl_now()
                else:
                    current_batsman = get_next_batsman_player()
                    current_bowler = get_next_bowler_computer()
                    if current_batsman == 'All out':
                        # All out
                        tk.messagebox.showinfo("Innings over", "Your innings is over: ALL BATSMEN USED. Click OK to start bowling.")
                        bowl_now()

            # Reset flash label immediately
            flash_label.config(text="")

            # Disable Bat button for 3 secs
            bat_button.config(state=tk.DISABLED)

            # After 3 seconds, enable Bat button and allow player to choose shot
            game.after(2000, lambda: bat_button.config(state=tk.NORMAL))

            selected_bat_type = bat_type_var.get()
            probability = probabilities[ball_type.lower()][selected_bat_type.lower()]
            random_number = random.uniform(0, 1)

            if random_number > probability:
                if selected_bat_type.lower() == 'defend':
                    hit = random.choice([0, 1])
                else:
                    hit = random.choice([0, 1, 4, 6])
                runs += hit
                balls_faced += 1
                run_rate = (runs / balls_faced) * 6

                # Flash the score
                if hit == 0:
                    flash_score('dot ball', flash_label) # Flash 'dot ball' if no runs scored
                    print(ball_type, selected_bat_type, 'dot ball') # Print the ball type and the shot
                else:
                    flash_score(hit, flash_label) # Flash the runs scored
                    print(ball_type, selected_bat_type, hit) # Print the ball type and the shot
                
                # Update all labels
                update_batting_labels()
            
            else:
                # Flash the score
                flash_score('OUT', flash_label)
                balls_faced += 1
                runs += 0
                run_rate = (runs / balls_faced) * 6

                current_batsman = get_next_batsman_player()
                if current_batsman == 'All out':
                    # All out
                    bowl_now()
                    tk.messagebox.showinfo("Innings over", "Your innings is over: ALL OUT. Click OK to start bowling.")
                    return

                # Update all labels
            update_batting_labels()

            ball_type = get_ball_type()

                # Disable Bat button for 3 secs
            bat_button.config(state=tk.DISABLED)

                # After 3 seconds, enable Bat button and allow player to choose shot
            game.after(3000, lambda: bat_button.config(state=tk.NORMAL))

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
        runs = 0
        balls_bowled = 0
        run_rate = 0.0
        bowling_widgets = []

        # If it's the start of the bowling phase
        current_batsman =computer_batting_order[0]
        current_bowler = player_bowling_order[0]

        # Live labels for bowling
        balls_bowled_label = tk.Label(game, text=f"Balls Bowled: 0", font=('calibre', 20, 'bold'))
        balls_bowled_label.pack()
        bowling_widgets.append(balls_bowled_label)
        current_batsman_label = tk.Label(game, text=f"Current Batsman: {current_batsman}", font=('calibre', 20, 'bold'))
        current_batsman_label.pack()
        bowling_widgets.append(current_batsman_label)
        current_bowler_label = tk.Label(game, text=f"Current Bowler: {current_bowler}", font=('calibre', 20, 'bold'))
        current_bowler_label.pack()
        bowling_widgets.append(current_bowler_label)
        runs_scored_label = tk.Label(game, text=f"Runs: 0", font=('calibre', 20, 'bold'))
        runs_scored_label.pack()
        bowling_widgets.append(runs_scored_label)
        run_rate_label_bowling = tk.Label(game, text=f"Run Rate: 0.0", font=('calibre', 20, 'bold'))
        run_rate_label_bowling.pack()
        bowling_widgets.append(run_rate_label_bowling)
        bat_type_label = tk.Label(game, text=f"Bat Type: ----", font=('calibre', 20, 'bold'))
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
            runs_scored_label.config(text=f"Runs: {runs}")
            run_rate_label_bowling.config(text=f"Run Rate: {run_rate:.2f}")

        bat_type = ''
        def get_bat_type():
            nonlocal bat_type
            bat_type = random.choice(bat_types)
            return bat_type
        
        bat_type = get_bat_type()

        def bowl_ball():
            nonlocal runs, balls_bowled, run_rate, current_batsman, current_bowler, innings_completed, bat_type

            def bat_now():
                time.sleep(2.1)
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
                        tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                        game.quit()
                        return
                    else:
                        tk.messagebox.showinfo("Innings Over", "Your innings is over. Click OK to start batting.")
                        bat_now()
                        return
                else:
                    current_batsman = get_next_batsman_computer()
                    current_bowler = get_next_bowler_player()
                    if current_batsman == 'All out':
                        innings_completed += 1
                        if innings_completed == 2:
                            tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                            game.quit()
                            return
                        else:
                            tk.messagebox.showinfo("Innings Over", "Your innings is over: ALL BATSMEN USED. Click OK to start batting.")
                            bat_now()
                            return

            # User selects ball type
            selected_ball_type = ball_type_var.get()
            balls_bowled += 1

            # Simulate the batsman's response based on probabilities
            probability = probabilities[selected_ball_type.lower()][bat_type.lower()]
            random_number = random.uniform(0, 1)

            # Determine if the computer batsman is out
            if random_number < probability:
                flash_score('OUT', flash_label)
                runs += 0
                run_rate = (runs / balls_bowled) * 6
                current_batsman = get_next_batsman_computer()
                if current_batsman == 'All out':
                    innings_completed += 1
                    if innings_completed == 2:
                        tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                        game.quit()
                        return
                    else:
                        tk.messagebox.showinfo("Innings Over", "Your innings is over: ALL OUT. Click OK to start batting.")
                        bat_now()
                        return
            else:
                if bat_type.lower() == 'defend':
                    hit = random.choice([0, 1])
                else:
                    hit = random.choice([0, 1, 4, 6])
                runs += hit
                run_rate = (runs / balls_bowled) * 6
                if hit == 0:
                    flash_score('dot ball', flash_label)
                    print(selected_ball_type, bat_type, 'dot ball') # Print the ball type and the shot 
                else:
                    flash_score(hit, flash_label)
                    print(selected_ball_type, bat_type, hit) # Print the ball type and the shot

            # Update all labels
            update_bowling_labels()

            bat_type_label.config(text=f"Ball Countered with: {bat_type}")

            # Get next bat type
            bat_type = get_bat_type()

            # Disable Bowl button for 3 seconds
            bowl_button.config(state=tk.DISABLED)
            game.after(3000, lambda: bowl_button.config(state=tk.NORMAL))

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



# Example call to start the game
# start_game('bat', [], 2)

