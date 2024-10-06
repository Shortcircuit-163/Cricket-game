import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv
import random

def signup_window():

    sgnp = tk.Tk()
    sgnp.title("Quicket-Signup")
    sgnp.resizable(False, False)
    sgnp.configure(background='light grey')
    ph1 = tk.PhotoImage(file=r'images\home\quicket.png')
    sgnp.iconphoto(True, ph1)

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
    window_width = 800
    window_height = 600
    center_window(sgnp, window_width, window_height)

    sgnp.grid_columnconfigure(0, weight=1)
    sgnp.grid_columnconfigure(2, weight=1)

    heading = Label(sgnp, text="Create quicket account", font=('Times New Roman', 50, 'bold', 'underline'), background='light grey')
    heading.grid(row=0, column=1, pady = 50)

    signup_frame = tk.Frame(sgnp, background='light grey')
    signup_frame.grid(row=1, column=1, pady = 100)

    def go_home():
        sgnp.destroy()
        from Home_screen import home
        home()

    name_var=tk.StringVar()
    username_var=tk.StringVar()
    passw_var=tk.StringVar()

    def signup_append():
        name = name_var.get()
        username = username_var.get()
        password = passw_var.get()


        def check_username_taken():
            with open(r'all_data\user_data.csv', 'a+') as add_user:
                add_user.seek(0)
                user_reader = csv.reader(add_user, delimiter=',')
                for row in user_reader:
                    if row[1] == username:
                        print("Username already taken")
                        tk.messagebox.showerror("Username taken", "Please try again")
                        return True
                
                return False
        
        if check_username_taken() == False:

            new_player_credentials = [name, username, password, 0, 4, 3, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            append_player_data =  open(r'all_data\user_data.csv', 'a', newline='')
            datawriter = csv.writer(append_player_data)
            datawriter.writerow(new_player_credentials)
            append_player_data.close()

            #starterpack------------------------------------

                #batsment--------------------------------
            batsmen_list = []
            with open(r'all_data\batsmen_data.csv', 'r', newline='') as starter_bats:
                reader1 = csv.reader(starter_bats)
                for row1 in reader1:
                    if row1[0] == 'name':
                        continue
                    else:
                        batsmen_list.append([row1[0], row1[2], row1[3]])

                # Randomly select 4 batsmen from the list
                selected_items1 = random.sample(batsmen_list, 4)
                # Print the selected items
                print(selected_items1)

                #bowlers----------------------------------
            bowlers_list = []
            with open(r'all_data\bowlers_data.csv', 'r', newline='') as starter_bowls:
                reader2 = csv.reader(starter_bowls)
                for row2 in reader2:
                    if row2[0] == 'name':
                        continue
                    else:
                        bowlers_list.append([row2[0], row2[2], row2[3]])

                # Randomly select 3 bowlers from the list
                selected_items2 = random.sample(bowlers_list, 3)
                # Print the selected items
                print(selected_items2)   

                #wk_keepers--------------------------------
            wk_list = []
            with open(r'all_data\wk_keepers_data.csv', 'r', newline='') as starter_wk:
                reader3 = csv.reader(starter_wk)
                for row3 in reader3:
                    if row3[0] == 'name':
                        continue
                    else:
                        wk_list.append([row3[0], row3[2], row3[3]])

                # Randomly select 1 wk keeper from the list
                selected_items3 = random.sample(wk_list, 1)
                # Print the selected items
                print(selected_items3)
                
                # all_rounders--------------------------------
            alr_list = []
            with open(r'all_data\all_rounders_data.csv', 'r', newline='') as starter_alr:
                reader4 = csv.reader(starter_alr)
                for row4 in reader4:
                    if row4[0] == 'name':
                        continue
                    else:
                        alr_list.append([row4[0], row4[2], row4[3]])

                # Randomly select 3 allrounders from the list
                selected_items4 = random.sample(alr_list, 3)
                # Print the selected items
                print(selected_items4)

                path = r'all_data\users\player_data_' + username + '.csv'
                with open(path, 'w', newline='') as players:
                    player_data_writer = csv.writer(players)
                    player_data_writer.writerows([['players', 'role', 'bat', 'bowl'],
                                                [selected_items1[0][0], 'bat', selected_items1[0][1], selected_items1[0][2]],
                                                [selected_items1[1][0], 'bat', selected_items1[1][1], selected_items1[1][2]],
                                                [selected_items1[2][0], 'bat', selected_items1[2][1], selected_items1[2][2]],
                                                [selected_items1[3][0], 'bat', selected_items1[3][1], selected_items1[3][2]],
                                                [selected_items2[0][0], 'bowl', selected_items2[0][1], selected_items2[0][2]],
                                                [selected_items2[1][0], 'bowl', selected_items2[1][1], selected_items2[1][2]],
                                                [selected_items2[2][0], 'bowl', selected_items2[2][1], selected_items2[2][2]],
                                                [selected_items3[0][0], 'wk', selected_items3[0][1], selected_items3[0][2]],
                                                [selected_items4[0][0], 'alr', selected_items4[0][1], selected_items4[0][2]],
                                                [selected_items4[1][0], 'alr', selected_items4[1][1], selected_items4[1][2]],
                                                [selected_items4[2][0], 'alr', selected_items4[2][1], selected_items4[2][2]]
                                                ])
            
            go_home()

                    
                    #ADD STARTERPACK HERE
            
            #----------------------------------------------------------------

            # sgnp.destroy()
            # cap = cv2.VideoCapture(r"images\cricvideo.mp4")
            # ret, frame = cap.read()
            # while(1):
            #     ret, frame = cap.read()
            #     cv2.imshow('frame',frame)
            #     if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
            #         cap.release()
            #         cv2.destroyAllWindows()
            #         break
            #     cv2.imshow('frame',frame)
            # from Home_screen import home
            # home()
            

    name_entry_label = tk.Label(signup_frame, text = 'Enter your name:', font = ('calibre',20,'bold'), background='light grey')
    name_entry_label.grid(row=0, column=0)
    
    name_entry = tk.Entry(signup_frame, textvariable = name_var, font = ('calibre',20,'normal'))
    name_entry.grid(row=0, column=1)

    username_label = tk.Label(signup_frame, text = 'Enter username:', font = ('calibre',20,'bold'), background='light grey')
    username_label.grid(row=1, column=0)

    username_entry = tk.Entry(signup_frame, textvariable = username_var, font = ('calibre',20,'normal'))
    username_entry.grid(row=1, column=1)

    passw_label = tk.Label(signup_frame, text = 'Enter password:', font = ('calibre',20,'bold'), background='light grey')
    passw_label.grid(row=2, column=0)

    passw_entry=tk.Entry(signup_frame, textvariable = passw_var, font = ('calibre',20,'normal'), show = '*')
    passw_entry.grid(row=2, column=1)

    signup = tk.PhotoImage(file=r'images\singleplayer\signup.png')
    signup_btn = signup.subsample(2, 2)
    signup_button=tk.Button(signup_frame,image=signup_btn, command = signup_append, borderwidth=0, background='light grey')
    signup_button.grid(row=3, column=1, pady=30)    


    sgnp.mainloop()