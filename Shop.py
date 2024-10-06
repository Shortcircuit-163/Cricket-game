import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import csv
import time

def shop_scr(name, username):
    from Singleplayer_start import start_match_singleplayer

    class ScrollBar:
        def __init__(self):
            self.shp = tk.Tk()
            self.shp.title("Shop")
            self.shp.resizable(False, False)
            self.shp.configure(background='light grey')
            ph1 = tk.PhotoImage(file=r'images\home\quicket.png')
            self.shp.iconphoto(True, ph1)

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
            window_width = 600
            window_height = 800
            center_window(self.shp, window_width, window_height)

            style = ttk.Style()
            style.configure('TNotebook.Tab', padding=[20, 10])

            def go_to_singleplayer():
                self.shp.destroy()
                start_match_singleplayer(name, username)


            #BUYING THE PLAYER
            def buy_player(username, player_name, player_price, player_role, bat, bowl):

                playerdata = r'all_data\users\player_data_' + username + '.csv'
                with open(playerdata, 'r') as f:
                    player_reader = csv.reader(f, delimiter=',')
                    for row in player_reader:
                        if row[0] == 'players':
                            continue
                        else:
                            if row[0] == player_name:
                                print("player already exists in team")
                                tk.messagebox.showerror("Purchase Error", "Player already exists in team")
                                return
                
                #convert from 'M' or 'K' to integer
                def convert_currency_num(value):
                    if value.endswith('M'):
                        return int(float(value[:-1]) * 1_000_000)
                    elif value.endswith('K'):
                        return int(float(value[:-1]) * 1_000)
                    else:
                        return int(value)
                    
                #convert from integer to 'M' or 'K'
                def convert_currency_back(value):
                        if value >= 1_000_000:
                            return f"{value / 1_000_000:.2f}M"
                        elif value >= 1_000:
                            return f"{value / 1_000}K"
                        else:
                            return str(value)
                
                converted_player_price = convert_currency_num(player_price)
                    
                # Read all data from the CSV file
                with open(r'all_data\user_data.csv', 'r', newline='') as file:
                    balance_reader = csv.reader(file)
                    rows = list(balance_reader)

                # Open the CSV file for writing
                with open(r'all_data\user_data.csv', 'w', newline='') as file:
                    balance_writer = csv.writer(file)
                    
                    for row in rows:
                        if row[1] == username:
                            current_balance = row[3]
                            if current_balance == 'inf':
                                converted_current_balance = float('inf')
                            else:
                                converted_current_balance = convert_currency_num(current_balance)

                            if converted_current_balance >= converted_player_price:
                                #changing the price
                                converted_current_balance -= converted_player_price
                                if converted_current_balance == float('inf'):
                                    row[3] = 'inf'
                                else:
                                    converted_current_balance_reset = convert_currency_back(converted_current_balance)
                                    row[3] = str(converted_current_balance_reset)

                                #adding the player name to owned players list
                                if player_role == 'bat':
                                    role_index = 4
                                elif player_role == 'bowl':
                                    role_index = 5
                                elif player_role == 'alr':
                                    role_index = 7
                                elif player_role == 'wk':
                                    role_index = 6
                                
                                p_no = int(row[role_index])
                                row[role_index] = str(p_no + 1)

                                path = r'all_data\users\player_data_' + username + '.csv'
                                with open(path, 'a', newline='') as players:
                                    writer = csv.writer(players)
                                    writer.writerow([player_name, player_role, bat, bowl])
                                
                                print(f"Bought {player_name} for {player_price}")
                            else:
                                print("Insufficient balance to buy the player.")
                                tk.messagebox.showerror("balance error", "Insufficient funds to buy the player")
                        # Write each row back to the file
                        balance_writer.writerow(row)


            # Function to get player names and prices
            def get_names_pstats(img_no, ptype):
                file_path = ''
                if ptype == 'batsmen':
                    file_path = r'all_data\batsmen_data.csv'
                elif ptype == 'bowlers':
                    file_path = r'all_data\bowlers_data.csv'
                elif ptype == 'all_rounders':
                    file_path = r'all_data\all_rounders_data.csv'
                elif ptype == 'wk_keepers':
                    file_path = r'all_data\wk_keepers_data.csv'

                with open(file_path) as p_names:
                    names_reader = csv.reader(p_names, delimiter=',')
                    iterate_count = -1
                    for row in names_reader:
                        if iterate_count == img_no:
                            p_name = row[0]
                            p_price = row[4]
                            p_role = row[1]
                            p_bat=row[2]
                            p_bowl=row[3]
                            return p_name, p_price, p_role, p_bat, p_bowl
                        iterate_count += 1

            tabControl = ttk.Notebook(self.shp)

            tab1 = ttk.Frame(tabControl) 
            tab2 = ttk.Frame(tabControl)
            tab3 = ttk.Frame(tabControl)
            tab4 = ttk.Frame(tabControl) 
            
            tabControl.add(tab1, text='Batsmen') 
            tabControl.add(tab2, text='Bowlers') 
            tabControl.add(tab3, text='All Rounders') 
            tabControl.add(tab4, text='WK Keepers') 
            tabControl.pack(expand=1, fill='both') 

            # Function to create a tab
            def create_tab(tab, path, ptype):

                canvas = Canvas(tab, background='light grey')
                canvas.pack(side=LEFT, fill=BOTH, expand=True)
                
                scrollbar = Scrollbar(tab, orient=VERTICAL, command=canvas.yview)
                scrollbar.pack(side=RIGHT, fill=Y)
                
                canvas.configure(yscrollcommand=scrollbar.set)
                canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
                
                scr_frame = tk.Frame(canvas, background='light grey')
                canvas.create_window((0, 0), window=scr_frame, anchor="nw")

                photo4 = tk.PhotoImage(file=r'images\shop\back.png')                
                btn3 = tk.Button(scr_frame, image=photo4, command=go_to_singleplayer, borderwidth=0, background='light grey')
                btn3.photo = photo4  # Keep a reference to avoid garbage collection
                btn3.grid(row=0, column=0, sticky=W, padx=10, pady=10)

                balance_frame = tk.Frame(scr_frame, background='light grey')
                balance_frame.grid(row=0, column=1)
                balance_label = tk.Label(balance_frame, text='Balance:', background='dark grey', font=('Times New Roman', 20, 'bold'))
                balance_label.grid(row=0, column=0)
                balance = tk.Label(balance_frame, text='actual balance', background='dark grey', font=('Times New Roman', 20, 'bold'))
                balance.grid(row=0, column=1)


                 # Function to update the balance label
                def update_balance():
                    try:
                        with open(r'all_data\user_data.csv', 'r', newline='') as file:
                            balance_reader = csv.reader(file)
                            for row in balance_reader:
                                if row[1] == username:
                                    current_balance = row[3]
                                    if current_balance == 'inf':
                                        current_balance = '∞'
                                    balance.config(text=current_balance)
                                    break
                    except Exception as e:
                        print(f"Error reading balance: {e}")

                    # Check if the window is still open before scheduling the next update
                    if self.shp.winfo_exists():
                        self.shp.after(200, update_balance)  # Update every 0.2 second
                    else:
                        return

                # Call the update_balance function to start updating the balance label
                # win_exists = 1
                update_balance()

                dir_list = os.listdir(path)

                images = []
                buttons = []
                for player in dir_list:
                    img_path = os.path.join(path, f'{player}')
                    if os.path.exists(img_path):
                        img = Image.open(img_path)
                        img_resized = img.resize((150, 200))  # Resize images to 150x200
                        img_tk = ImageTk.PhotoImage(img_resized)
                        images.append(img_tk)


                img_no = 0

                for idx, img_tk in enumerate(images):
                    row = (idx // 3) + 1  # Start placing images from row 1 to avoid overlapping with the home button
                    col = idx % 3

                    frame = tk.Frame(scr_frame, background='light grey')
                    frame.grid(row=row, column=col, padx=10, pady=10)

                    label = Label(frame, image=img_tk, background='light grey')
                    label.image = img_tk
                    label.pack()

                    name, price, role, bat, bowl = get_names_pstats(img_no, ptype)
                    purchase_text = Label(frame, text=name, font=('Roboto Mono', 10, 'bold'), background='light grey')
                    purchase_text.pack()

                    price_text = Label(frame, text=price, font=('Roboto Mono', 10, 'bold'), background='light grey')
                    price_text.pack()

                    buy_photo = tk.PhotoImage(file=r'images\shop\buy.png')
                    buy_btn = Button(frame, image=buy_photo, style='A.TButton', command=lambda u=username, n=name, p=price, r=role, b=bat, bo=bowl: buy_player(u, n, p, r,b,bo))
                    buy_btn.image = buy_photo  # Keep a reference to avoid garbage collection
                    buy_btn.pack()

                    buttons.append(buy_btn)

                    img_no += 1

            create_tab(tab1, r'images\shop\batsmen', 'batsmen')
            create_tab(tab2, r'images\shop\bowlers', 'bowlers')
            create_tab(tab3, r'images\shop\all rounders', 'all_rounders')
            create_tab(tab4, r'images\shop\wk keepers', 'wk_keepers')

            self.shp.mainloop()

    scr = ScrollBar()
