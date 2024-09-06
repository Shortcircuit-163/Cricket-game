import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import random

def start_game(bat_or_bowl, selected_players, overs):
    game = tk.Tk()
    game.title(f"Quicket-Singleplayer_{overs}-overs_{bat_or_bowl}")
    game.geometry('1400x800')
    game.resizable(False, False)
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    game.iconphoto(True, p1)

    # Example data
    current_batsman = "Nairit"
    current_bowler = "Krish"
    runs = 0
    balls_faced = 0
    balls_bowled = 0
    run_rate = 0.0

    # omkaar

    # List of types of balls for computer (random) and user (choice)
    ball_types = ['Fast', 'Spin', 'Swing', 'Bouncer', 'Yorker']
    bat_types = ['Pull', 'Drive', 'Defend', 'Loft', 'Cut']  # List of bat types

    def flash_score(score, flash_label):
        flash_label.config(text=str(score))
        game.after(1000, lambda: flash_label.config(text=""))  # Reset after 1 second

    def batting():
        nonlocal runs, balls_faced, run_rate, current_bowler
        
        # Live labels for batting
        runs_label = tk.Label(game, text=f"Runs: {runs}", font=('calibre', 20, 'bold'))
        runs_label.pack()
        balls_faced_label = tk.Label(game, text=f"Balls Faced: {balls_faced}", font=('calibre', 20, 'bold'))
        balls_faced_label.pack()
        current_batsman_label = tk.Label(game, text=f"Current Batsman: {current_batsman}", font=('calibre', 20, 'bold'))
        current_batsman_label.pack()
        run_rate_label = tk.Label(game, text=f"Run Rate: {run_rate:.2f}", font=('calibre', 20, 'bold'))
        run_rate_label.pack()
        current_bowler_label = tk.Label(game, text=f"Current Bowler: {current_bowler}", font=('calibre', 20, 'bold'))
        current_bowler_label.pack()
        ball_type_label = tk.Label(game, text="Ball Type:", font=('calibre', 20, 'bold'))
        ball_type_label.pack()
        flash_label = tk.Label(game, text="", font=('calibre', 40, 'bold'), fg='red')
        flash_label.pack()

        def update_batting_labels():
            # Update all live labels for batting
            runs_label.config(text=f"Runs: {runs}")
            balls_faced_label.config(text=f"Balls Faced: {balls_faced}")
            current_batsman_label.config(text=f"Current Batsman: {current_batsman}")
            run_rate_label.config(text=f"Run Rate: {run_rate:.2f}")
            current_bowler_label.config(text=f"Current Bowler: {current_bowler}")

        def submit_bat_choice():
            nonlocal runs, balls_faced, run_rate

            # Simulate the result based on the bat type (random for now)
            selected_bat_type = bat_type_var.get()
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

            # Disable Bat button until next ball is bowled
            bat_button.config(state=tk.DISABLED)

        def bowl_ball():
            nonlocal runs, balls_faced, run_rate

            # Reset flash label immediately
            flash_label.config(text="")

            # Random ball type from the computer
            ball_type = random.choice(ball_types)
            ball_type_label.config(text=f"Ball Type: {ball_type}")

            # Disable Bat button initially
            bat_button.config(state=tk.DISABLED)

            # After 3 seconds, enable Bat button and allow player to choose shot
            game.after(3000, lambda: bat_button.config(state=tk.NORMAL))

        # Drop-down to select bat type
        bat_type_var = tk.StringVar()
        bat_type_dropdown = Combobox(game, textvariable=bat_type_var, values=bat_types, state="readonly", font=('calibre', 20, 'bold'))
        bat_type_dropdown.pack()

        # Button to submit the bat choice
        bat_button = tk.Button(game, text="Bat", command=submit_bat_choice, font=('calibre', 20, 'bold'), state=tk.DISABLED)
        bat_button.pack()

        # Button to simulate bowling a ball
        bowl_button = tk.Button(game, text="Bowl", command=bowl_ball, font=('calibre', 20, 'bold'))
        bowl_button.pack()

    def bowling():
        nonlocal balls_bowled, current_batsman, current_bowler

        # Live labels for bowling
        balls_bowled_label = tk.Label(game, text=f"Balls Bowled: {balls_bowled}", font=('calibre', 20, 'bold'))
        balls_bowled_label.pack()
        current_batsman_label = tk.Label(game, text=f"Current Batsman: {current_batsman}", font=('calibre', 20, 'bold'))
        current_batsman_label.pack()
        current_bowler_label = tk.Label(game, text=f"Current Bowler: {current_bowler}", font=('calibre', 20, 'bold'))
        current_bowler_label.pack()
        ball_type_label = tk.Label(game, text="Ball Type:", font=('calibre', 20, 'bold'))
        ball_type_label.pack()
        flash_label = tk.Label(game, text="", font=('calibre', 40, 'bold'), fg='red')
        flash_label.pack()

        def update_bowling_labels():
            # Update all live labels for bowling
            balls_bowled_label.config(text=f"Balls Bowled: {balls_bowled}")
            current_batsman_label.config(text=f"Current Batsman: {current_batsman}")
            current_bowler_label.config(text=f"Current Bowler: {current_bowler}")

        def bowl_ball():
            nonlocal balls_bowled

            # Reset flash label immediately
            flash_label.config(text="")

            # User selects ball type
            selected_ball_type = ball_type_var.get()
            ball_type_label.config(text=f"Ball Type: {selected_ball_type}")
            balls_bowled += 1

            # Simulate the batsman's response (random for now)
            hit = random.choice([0, 1, 2, 3, 4, 6])

            # Flash the score

            flash_score(hit, flash_label)

            # Update all labels
            update_bowling_labels()

        # Drop-down to select ball type
        ball_type_var = tk.StringVar()
        ball_type_dropdown = Combobox(game, textvariable=ball_type_var, values=ball_types, state="readonly", font=('calibre', 20, 'bold'))
        ball_type_dropdown.pack()

        # Button to simulate bowling a ball
        bowl_button = tk.Button(game, text="Bowl", command=bowl_ball, font=('calibre', 20, 'bold'))
        bowl_button.pack()

    if bat_or_bowl == 'bat':
        batting()
    elif bat_or_bowl == 'bowl':
        bowling()

    game.mainloop()

# Example call to start the game
start_game('bowl', [], 2)

