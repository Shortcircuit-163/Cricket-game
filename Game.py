import tkinter as tk
from tkinter import END
from tkinter.ttk import *
from PIL import ImageTk, Image
import random
import csv

def start_game(bat_or_bowl, selected_players, overs, username, name):

    overs = int(overs)

    game = tk.Tk()
    game.title(f"Quicket-Singleplayer_{overs}-overs_{bat_or_bowl}")
    game.geometry('1400x620')
    game.resizable(False, False)

    game.configure(background='light grey')

    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    game.iconphoto(True, p1)

    bg_image = Image.open(r'images\game\bgg.png')
    backg_image = bg_image.resize((1400, 620), Image.Resampling.LANCZOS)
    background_image = ImageTk.PhotoImage(backg_image)
    # Create a label to display the image
    bg_label = tk.Label(game, image=background_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window
    
    def center_window(window, width, height):
        # Get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # Calculate x and y coordinates to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Set window size and position
        window.geometry(f"{width}x{height}+{x}+{y}")

    # Set window size and center it
    window_width = 1400
    window_height = 620
    center_window(game, window_width, window_height)
    
    game.columnconfigure(0, minsize=450)
    game.columnconfigure(1, minsize=500)
    game.columnconfigure(2, minsize=450)
    game.grid_columnconfigure(0, weight=1)
    game.grid_columnconfigure(1, weight=1)
    game.grid_columnconfigure(2, weight=1)

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
        game.after(2000, lambda: flash_label.config(text="----"))  # Reset after 2 seconds

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
    bowling_widgets = []
    earnings = 0
    player_win = False

    def save_data(runs_pc, wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs):
            nonlocal earnings, player_win

            rows = []
            with open(r'all_data\user_data.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)

                if runs >= runs_pc:
                    player_win = True

                if player_win == True:
                    earnings = (runs - runs_pc) * 10000
                else:
                    earnings = (runs_pc - runs) * 1000

                for i in rows:
                    if i[1] == username:
                        i[3] = float(i[3]) + earnings
                        i[8] = int(i[8]) + wickets
                        i[9] = int(i[9]) + runs
                        i[10] = round((float(i[10]) + float(economy)) / (float(i[14]) + float(Bowling_Overs)), 2)
                        i[11] = int(i[11]) + innings_completed
                        i[12] = round((float(i[12]) + float(Batting_Average)) / (float(i[13]) + float(Batting_Overs)), 2)
                        i[13] = round(float((i[13])) + float(Batting_Overs), 2)
                        i[14] = round(float((i[14])) + float(Bowling_Overs), 2)
                        i[15] = round(float(((i[15]))) + float(Total_Overs), 2)
                        i[16] = int(i[16]) + 1 if player_win else int(i[16])
                        break

            with open(r'all_data\user_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    
    def show_final_scores(player_batting_order, computer_batting_order):
        nonlocal earnings, runs, runs_pc, run_rate, run_rate_pc, wickets, wickets_pc, economy, economy_pc, Batting_Average, Batting_Average_pc, Batting_Overs, Bowling_Overs, Total_Overs, bat_or_bowl

        nonlocal player_win
        def center_window(window, width, height):
            # Get screen width and height
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            
            # Calculate x and y coordinates to center the window
            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)
            
            # Set window size and position
            window.geometry(f"{width}x{height}+{x}+{y}")

        # Set window size and center it
        window_width = 1400
        window_height = 670
        center_window(game, window_width, window_height)
        game.attributes('-alpha', 0.95)

        def restart_game():
            # Logic to reset game state or return to main menu
            msg = 'Choose to continue playing or quit the game.'
            top = tk.Toplevel(game)
            top.title("Game Over")
            top.geometry("350x150")

            message = tk.Label(top, text=msg)
            message.pack(pady=20)

            response = tk.StringVar(value="")

            def on_yes():
                response.set("yes")
                top.destroy()

            def on_no():
                response.set("no")
                top.destroy()

            button1 = tk.Button(top, text="Exit", command=on_yes, background='light grey')
            button1.pack(side=tk.LEFT, padx=20)

            button2 = tk.Button(top, text="Continue", command=on_no, background='light grey')
            button2.pack(side=tk.RIGHT, padx=20)

            top.wait_window()  # Wait for the user to make a selection
            if response.get() == "yes":
                game.destroy() # Close the window if confirmed            
            else:
                game.destroy()  # Go back to main menu if cancelled
                print("Restarting...")
                from Singleplayer_start import start_match_singleplayer as start
                start(name, username)
              
        
        game.protocol("WM_DELETE_WINDOW", restart_game)

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
            ('Earnings:', earnings, 'ꝏ'),
            ('Runs:', runs, runs_pc),
            ('Run Rate:', round(run_rate, 2), round(run_rate_pc, 2)),
            ('Wickets:', wickets, wickets_pc),
            ('Economy:', round(economy, 2), round(economy_pc, 2)),
            ('Batting Average:', round(Batting_Average, 2), round(Batting_Average_pc, 2)),
            ('Batting Overs:', Batting_Overs, Batting_Overs),
            ('Bowling Overs:', Bowling_Overs, Bowling_Overs),
            ('Total Overs:', Total_Overs, Total_Overs)
        ]

        total_rows = len(lst)
        total_columns = len(lst[0])

        colours = ['#F0FFF0', '#AFEEEE', '#F5FFFA', '#FFF0F5', '#F0FFF0', '#FFE4E1', '#FFFACD', '#FAFAD2', '#F0F8FF']
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
                            if player_win == True:
                                self.e = tk.Label(root, width=20, height=3, wraplength=300, background='#6e9827',
                                              font=('Arial', 16, 'bold'), anchor='w', padx=10)
                            else:
                                self.e = tk.Label(root, width=20, height=3, wraplength=300, background='#F08080',
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
        balls_faced_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        balls_faced_frame.config(background='#F0FFF0')
        balls_faced_label = tk.Label(balls_faced_frame, text=f"Balls Faced: {balls_faced}", font=('calibre', 20, 'bold'), background='#F0FFF0')
        balls_faced_label.pack()
        balls_faced_frame.grid(row=1, column=2, padx=20, pady=40, sticky='nsew')
        batting_widgets.append(balls_faced_frame)

        current_batsman_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        current_batsman_frame.config(background='#FFF0F5')
        current_batsman_label = tk.Label(current_batsman_frame, background='#FFF0F5', text=f"Current Batsman: {current_batsman}", font=('calibre', 20, 'bold'))
        current_batsman_label.pack()
        current_batsman_frame.grid(row=0, column=0, padx=20, pady=40, sticky='nsew')
        batting_widgets.append(current_batsman_frame)

        current_bowler_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        current_bowler_frame.config(background='#F0FFF0')
        current_bowler_label = tk.Label(current_bowler_frame, background='#F0FFF0', text=f"Current Bowler: {current_bowler}", font=('calibre', 20, 'bold'))
        current_bowler_label.pack()
        current_bowler_frame.grid(row=1, column=0, padx=20, pady=40, sticky='nsew')
        batting_widgets.append(current_bowler_frame)

        runs_label_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        runs_label_frame.config(background='#AFEEEE')
        runs_label = tk.Label(runs_label_frame, text=f"Runs: {runs}", font=('calibre', 20, 'bold'), background='#AFEEEE')
        runs_label.pack()
        runs_label_frame.grid(row=0, column=1, padx=20, pady=40, sticky='nsew')
        batting_widgets.append(runs_label_frame)

        run_rate_label_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        run_rate_label_frame.config(background='#FFE4E1')
        run_rate_label = tk.Label(run_rate_label_frame, text=f"Run Rate: {run_rate:.2f}", font=('calibre', 20, 'bold'), background='#FFE4E1')
        run_rate_label.pack()
        run_rate_label_frame.grid(row=0, column=2, padx=20, pady=40, sticky='nsew')
        batting_widgets.append(run_rate_label_frame)

        ball_type_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        ball_type_frame.config(background='#FAFAD2')
        ball_type_label = tk.Label(ball_type_frame, text="Ball Type:", font=('calibre', 20, 'bold'), background='#FAFAD2')
        ball_type_label.pack()
        ball_type_frame.grid(row=1, column=1, padx=20, pady=40, sticky='nsew')
        batting_widgets.append(ball_type_frame)

        flash_label_frame = tk.Frame(game, highlightbackground="red", highlightthickness=6, width=300, height=150)
        flash_label_frame.config(background='light grey')
        flash_label = tk.Label(flash_label_frame, text="----", font=('calibre', 40, 'bold'), fg='red', background='light grey')
        flash_label.pack()
        flash_label_frame.grid(row=2, column=1, padx=20, pady=40)
        batting_widgets.append(flash_label_frame)

        def get_ball_type():
            ball_type = random.choice(ball_types)
            ball_type_label.config(text=f"Ball Type: {ball_type}")
            return ball_type
        
        ball_type = get_ball_type()
        button_images_bat = [] # To prevent garbage collection of button images

        def update_batting_labels():
            # Update all live labels for batting
            runs_label.config(text=f"Runs: {runs}")
            balls_faced_label.config(text=f"Balls Faced: {balls_faced}")
            current_batsman_label.config(text=f"Current Batsman: {current_batsman}")
            run_rate_label.config(text=f"Run Rate: {run_rate:.2f}")
            current_bowler_label.config(text=f"Current Bowler: {current_bowler}")


        def submit_bat_choice(bat):

            nonlocal button_images_bat ,player_batting_order, computer_batting_order, runs, balls_faced, run_rate, current_batsman, current_batsman_rating, current_bowler, innings_completed, ball_type, wickets, wickets_pc, runs, economy, economy_pc, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs


            def bowl_now():
                nonlocal Batting_Average, Batting_Overs, runs, economy_pc

                Batting_Overs = float(balls_faced / 6)
                Batting_Average = float(runs / Batting_Overs)                
                economy_pc = float(runs / Batting_Overs)
                clear_widgets(batting_widgets)
                bowling()

            # Reset flash label immediately
            flash_label.config(text="----")


            if balls_faced % 6 == 0:
                if balls_faced == (overs * 6) / 2:
                    # Halfway through the innings
                    innings_completed += 1
                    if innings_completed == 2:
                        Batting_Overs = float(balls_faced / 6)
                        Batting_Average = float(runs / Batting_Overs)
                        economy_pc = float(runs / Batting_Overs)
                        Total_Overs = float(overs)
                        save_data(runs_pc, wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
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
                            save_data(runs_pc, wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
                            clear_widgets(batting_widgets)
                            tk.messagebox.showinfo("Game Over", "The game has ended. Thanks for playing!")
                            show_final_scores(player_batting_order, computer_batting_order)
                            return
                        else:
                            bowl_now()
                            tk.messagebox.showinfo("Innings over", "Your innings is over: ALL BATSMEN USED. Click OK to start bowling.")
                    
                    current_bowler = get_next_bowler_computer()[0]

            # # Reset flash label immediately
            # try:
            #     flash_label.config(text="----")
            # except tk.TclError:
                pass  # Suppress error if widget doesn't exist

            try:
            
                # Scale the rating to influence the probability (90+ gives a higher probability of success)
                rating_factor = 1 + ((float(current_batsman_rating) - 90.0)) / 10  # rating_factor > 1 if rating > 90

                selected_bat_type = bat
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
                        flash_score('-dot ball-', flash_label)
                    else:
                        flash_score(f'-{hit}-', flash_label)
                    
                    # Update all labels
                    update_batting_labels()
                
                else:
                    # Flash the score
                    flash_score('-OUT!-', flash_label)
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
                            save_data(runs_pc, wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
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
                
                # Disable all Bat buttons for 2 seconds
                for btn_name in [cut_btn, drive_btn, defend_btn, loft_btn, pull_btn]:
                    btn_name.config(state=tk.DISABLED)

                # After 2 seconds, re-enable all Bat buttons
                game.after(2000, lambda: [btn_name.config(state=tk.NORMAL) for btn_name in [cut_btn, drive_btn, defend_btn, loft_btn, pull_btn]])


            except tk.TclError:
                pass

        # Bat buttons
        bat_btns_frame = tk.Frame(game)
        bat_btns_frame.config(background='#D4EFE9', highlightbackground="black", highlightthickness=3)

        cut_shot_img = Image.open(r'images\game\bat_buttons\cut.png')
        cut_shot = ImageTk.PhotoImage(cut_shot_img)
        cut_btn = tk.Button(bat_btns_frame, image=cut_shot, background='#D4EFE9', command=lambda: submit_bat_choice('cut'), borderwidth=0, activebackground='#D4EFE9', )
        cut_btn.grid(row=0, column=0, sticky='nsew', pady=20)
        batting_widgets.append(ball_type_frame)
        button_images_bat.append(cut_shot)

        drive_shot_img = Image.open(r'images\game\bat_buttons\drive.png')
        drive_shot = ImageTk.PhotoImage(drive_shot_img)
        drive_btn = tk.Button(bat_btns_frame, image=drive_shot, background='#D4EFE9', command=lambda: submit_bat_choice('drive'), borderwidth=0, activebackground='#D4EFE9')
        drive_btn.grid(row=0, column=2, sticky='nsew', pady=20)
        batting_widgets.append(ball_type_frame)
        button_images_bat.append(drive_shot)

        defend_shot_img = Image.open(r'images\game\bat_buttons\defend.png')
        defend_shot = ImageTk.PhotoImage(defend_shot_img)
        defend_btn = tk.Button(bat_btns_frame, image=defend_shot, background='#D4EFE9', command=lambda: submit_bat_choice('defend'), borderwidth=0, activebackground='#D4EFE9')
        defend_btn.grid(row=1, column=1, sticky='nsew')
        batting_widgets.append(ball_type_frame)
        button_images_bat.append(defend_shot)

        loft_shot_img = Image.open(r'images\game\bat_buttons\loft.png')
        loft_shot = ImageTk.PhotoImage(loft_shot_img)
        loft_btn = tk.Button(bat_btns_frame, image=loft_shot, background='#D4EFE9', command=lambda: submit_bat_choice('loft'), borderwidth=0, activebackground='#D4EFE9')
        loft_btn.grid(row=1, column=0, sticky='nsew')
        batting_widgets.append(ball_type_frame)
        button_images_bat.append(loft_shot)

        pull_shot_img = Image.open(r'images\game\bat_buttons\pull.png')
        pull_shot = ImageTk.PhotoImage(pull_shot_img)
        pull_btn = tk.Button(bat_btns_frame, image=pull_shot, background='#D4EFE9', command=lambda: submit_bat_choice('pull'), borderwidth=0, activebackground='#D4EFE9')
        pull_btn.grid(row=1, column=2, sticky='nsew')
        batting_widgets.append(ball_type_frame)
        button_images_bat.append(pull_shot)

        bat_img = Image.open(r'images\game\bat_buttons\bat.png')
        bat_image = ImageTk.PhotoImage(bat_img)
        bat_label = tk.Label(bat_btns_frame, image=bat_image, background='#FFE9CD', highlightbackground="#DEB887", highlightthickness=3)
        bat_label.grid(row=0, column=1, sticky='nsew', pady=20)
        batting_widgets.append(bat_label)
        button_images_bat.append(bat_image)

        bat_btns_frame.grid(row=3, column=1, sticky='nsew')
        batting_widgets.append(bat_btns_frame)


    def bowling():
        balls_bowled = 0
        bat_type = '--'

        # If it's the start of the bowling phase
        current_batsman = computer_batting_order[0][0]
        current_bowler = player_bowling_order[0][0]
        current_bowler_rating = player_bowling_order[0][2]

        # Live labels for bowling
        balls_bowled_label_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        balls_bowled_label_frame.config(background='#F0FFF0')
        balls_bowled_label = tk.Label(balls_bowled_label_frame, text=f"Balls Bowled: {balls_bowled}", font=('calibre', 20, 'bold'))
        balls_bowled_label.pack()
        balls_bowled_label_frame.grid(row=1, column=2, padx=20, pady=40)
        bowling_widgets.append(balls_bowled_label_frame)

        current_batsman_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        current_batsman_frame.config(background='#FFF0F5')
        current_batsman_label = tk.Label(current_batsman_frame, text=f"Current Batsman: {current_batsman}", font=('calibre', 20, 'bold'), background='#FFF0F5')
        current_batsman_label.pack()
        current_batsman_frame.grid(row=0, column=0, padx=20, pady=40)
        bowling_widgets.append(current_batsman_frame)

        current_bowler_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        current_bowler_frame.config(background='#F0FFF0')
        current_bowler_label = tk.Label(current_bowler_frame, text=f"Current Bowler: {current_bowler}", font=('calibre', 20, 'bold'), background='#F0FFF0')
        current_bowler_label.pack()
        current_bowler_frame.grid(row=1, column=0, padx=20, pady=40)
        bowling_widgets.append(current_bowler_frame)

        runs_scored_label_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        runs_scored_label_frame.config(background='#AFEEEE')
        runs_scored_label = tk.Label(runs_scored_label_frame, text=f"Runs: {runs_pc}", font=('calibre', 20, 'bold') , background='#AFEEEE')
        runs_scored_label.pack()
        runs_scored_label_frame.grid(row=0, column=1, padx=20, pady=40)
        bowling_widgets.append(runs_scored_label_frame)

        run_rate_pc_label_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        run_rate_pc_label_frame.config(background='#FFE4E1')
        run_rate_pc_label_bowling = tk.Label(run_rate_pc_label_frame, text=f"Run Rate: {run_rate_pc:.2f}", font=('calibre', 20, 'bold'), background='#FFE4E1')
        run_rate_pc_label_bowling.pack()
        run_rate_pc_label_frame.grid(row=0, column=2, padx=20, pady=40)
        bowling_widgets.append(run_rate_pc_label_frame)

        bat_type_frame = tk.Frame(game, highlightbackground="black", highlightthickness=6, width=300, height=150)
        bat_type_frame.config(background='#FAFAD2')
        bat_type_label = tk.Label(bat_type_frame, text=f"Shot Played: {bat_type}", font=('calibre', 20, 'bold'), background='#FAFAD2')
        bat_type_label.pack()
        bat_type_frame.grid(row=1, column=1, padx=20, pady=40)
        bowling_widgets.append(bat_type_frame)

        flash_label_frame = tk.Frame(game, highlightbackground="red", highlightthickness=6, width=300, height=150)
        flash_label_frame.config(background='light grey')
        flash_label = tk.Label(flash_label_frame, text="----", font=('calibre', 40, 'bold'), fg='red')
        flash_label.pack()
        flash_label_frame.grid(row=2, column=1, padx=20, pady=40)
        bowling_widgets.append(flash_label_frame)

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
        button_images_ball = []  # To prevent garbage collection of button images

        def bowl_ball(ball_type):
            nonlocal button_images_ball, player_batting_order, computer_batting_order, runs_pc, run_rate_pc, balls_bowled, Batting_Average_pc, run_rate, current_batsman, current_bowler,current_bowler_rating, innings_completed, bat_type, wickets, runs, economy, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs

            def bat_now():

                nonlocal Bowling_Overs, economy, runs_pc, Batting_Average_pc
                Bowling_Overs = float(balls_bowled / 6)
                economy = float(runs_pc / Bowling_Overs)
                Batting_Average_pc = float(runs_pc / Bowling_Overs)

                clear_widgets(bowling_widgets)
                batting()

            # Reset flash label immediately
            flash_label.config(text="----")

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
                        save_data(runs_pc, wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
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
                            save_data(runs_pc, wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
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
                selected_ball_type = ball_type
                balls_bowled += 1

                # Scale the rating to influence the probability (90+ gives a higher probability of success)
                rating_factor = 1 + ((float(current_bowler_rating) - 90.0) / 10)  # rating_factor > 1 if rating > 90

                # Simulate the batsman's response based on probabilities
                probability = probabilities[selected_ball_type.lower()][bat_type.lower()]
                adjusted_probability = probability / rating_factor
                random_number = random.uniform(0, 1)

                # Determine if the computer batsman is out
                if random_number < adjusted_probability:
                    flash_score('-OUT!-', flash_label)
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
                            save_data(runs_pc, wickets, runs, economy, innings_completed, Batting_Average, Batting_Overs, Bowling_Overs, Total_Overs)
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
                        flash_score('-dot ball-', flash_label)
                    else:
                        flash_score(f'-{hit}-', flash_label)

                bat_type_label.config(text=f"Shot Played: {bat_type}")

                # Update all labels
                update_bowling_labels()

                # Get next bat type
                bat_type = get_bat_type()

                # Disable all Ball buttons for 2 seconds
                for btn_name in [fast_btn, spin_btn, swing_btn, bouncer_btn, yorker_btn]:
                    btn_name.config(state=tk.DISABLED)
                
                # After 2 seconds, re-enable all Ball buttons
                game.after(2000, lambda: [btn_name.config(state=tk.NORMAL) for btn_name in [fast_btn, spin_btn, swing_btn, bouncer_btn, yorker_btn]])
            
            except tk.TclError:
                pass

        # Ball buttons
        ball_btns_frame = tk.Frame(game)
        ball_btns_frame.config(background='#FFB19D', highlightbackground="black", highlightthickness=3)

        fast_ball_img = Image.open(r'images\game\ball_buttons\fast.png')
        fast_ball = ImageTk.PhotoImage(fast_ball_img)
        fast_btn = tk.Button(ball_btns_frame, image=fast_ball, background='#FFB19D', command=lambda: bowl_ball('fast'), borderwidth=0, activebackground='#FFB19D')
        fast_btn.grid(row=0, column=0, sticky='nsew', pady=20, padx=5)
        bowling_widgets.append(ball_btns_frame)
        button_images_ball.append(fast_ball)

        spin_ball_img = Image.open(r'images\game\ball_buttons\spin.png')
        spin_ball = ImageTk.PhotoImage(spin_ball_img)
        spin_btn = tk.Button(ball_btns_frame, image=spin_ball, background='#FFB19D', command=lambda: bowl_ball('spin'), borderwidth=0, activebackground='#FFB19D')
        spin_btn.grid(row=0, column=2, sticky='nsew', pady=20, padx=5)
        bowling_widgets.append(ball_btns_frame)
        button_images_ball.append(spin_ball)

        swing_ball_img = Image.open(r'images\game\ball_buttons\swing.png')
        swing_ball = ImageTk.PhotoImage(swing_ball_img)
        swing_btn = tk.Button(ball_btns_frame, image=swing_ball, background='#FFB19D', command=lambda: bowl_ball('swing'), borderwidth=0, activebackground='#FFB19D')
        swing_btn.grid(row=1, column=1, sticky='nsew', padx=5)
        bowling_widgets.append(ball_btns_frame)
        button_images_ball.append(swing_ball)

        bouncer_ball_img = Image.open(r'images\game\ball_buttons\bouncer.png')
        bouncer_ball = ImageTk.PhotoImage(bouncer_ball_img)
        bouncer_btn = tk.Button(ball_btns_frame, image=bouncer_ball, background='#FFB19D', command=lambda: bowl_ball('bouncer'), borderwidth=0, activebackground='#FFB19D')
        bouncer_btn.grid(row=1, column=0, sticky='nsew', padx=5)
        bowling_widgets.append(ball_btns_frame)
        button_images_ball.append(bouncer_ball)

        yorker_ball_img = Image.open(r'images\game\ball_buttons\yorker.png')
        yorker_ball = ImageTk.PhotoImage(yorker_ball_img)
        yorker_btn = tk.Button(ball_btns_frame, image=yorker_ball, background='#FFB19D', command=lambda: bowl_ball('yorker'), borderwidth=0, activebackground='#FFB19D')
        yorker_btn.grid(row=1, column=2, sticky='nsew', padx=5)
        bowling_widgets.append(ball_btns_frame)
        button_images_ball.append(yorker_ball)

        ball_img = Image.open(r'images\game\ball_buttons\bowling.png')
        ball_image = ImageTk.PhotoImage(ball_img)
        ball_label = tk.Label(ball_btns_frame, image=ball_image, background='#FFE9CD', highlightbackground="#D43D1A", highlightthickness=3)
        ball_label.grid(row=0, column=1, sticky='nsew', pady=20, padx=5)
        bowling_widgets.append(ball_label)
        button_images_ball.append(ball_image)

        ball_btns_frame.grid(row=3, column=1, sticky='nsew')
        bowling_widgets.append(ball_btns_frame)



    if bat_or_bowl == 'bat':
        batting()
    elif bat_or_bowl == 'bowl':
        bowling()

    game.mainloop()
