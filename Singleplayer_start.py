import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv


def start_match_singleplayer(name, username):

    sm = tk.Tk()
    sm.title("Quicket-Start Match")
    sm.geometry('1000x650')
    # sm.resizable(False, False)
    # sm.configure(background='light grey')
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    sm.iconphoto(True, p1)
    

    sm.grid_columnconfigure(0, weight=1)
    sm.grid_columnconfigure(1, weight=1)
    sm.grid_columnconfigure(2, weight=1)

    greeting = "Hello " + name + "!"
    heading = Label(sm, text=greeting, background='', font=('Times New Roman', 50, 'bold'))
    heading.grid(row=0, column=1)

    def go_home():
        sm.destroy()
        from Home_screen import home
        home()
    
    def shop():
        sm.destroy()
        #shop window call

    photo3 = tk.PhotoImage(file=r'images\singleplayer_start\home1.png')
    btn3 = tk.Button(sm, image=photo3, command=go_home, borderwidth=0)
    btn3.grid(row=0, column=0, padx = 0)

    photo4 = tk.PhotoImage(file=r'images\singleplayer_start\shop.png')
    btn4 = tk.Button(sm, image=photo4, command=shop, borderwidth=0)
    btn4.grid(row=0, column=3, pady = 10)

    player_info = tk.Frame(sm)
    player_info.grid(row=1, column=1, pady = 50)

    def return_playerdata():
        data_path = r'Data\user_data.csv'
        with open(data_path) as player_data:
            user_reader = csv.reader(player_data, delimiter=',')
            for row in user_reader:
                if row[0] == name:
                    batsmen_owned = row[3]
                    bowlers_owned = row[4]
                    wicket_keepers_owned = row[5]
                    all_rounders_owned = row[6]
                    wickets = row[7]               
                    runs = row[8]              
                    economy = row[9]              
                    innings = row[10]               
                    batting_average = row[11]               
                    bowling_average = row[12]              
                    batting_overs = row[13]               
                    bowling_overs = row[14]              
                    total_overs = row[15]
                    all_data = [batsmen_owned, bowlers_owned, wicket_keepers_owned, all_rounders_owned, wickets, runs, economy, innings, batting_average, bowling_average, batting_overs, bowling_overs, total_overs]
                    return all_data

    
    batsmen_owned, bowlers_owned, wicket_keepers_owned, all_rounders_owned, wickets, runs, economy, innings, batting_average, bowling_average, batting_overs, bowling_overs, total_overs = return_playerdata()[0], return_playerdata()[1], return_playerdata()[2], return_playerdata()[3], return_playerdata()[4], return_playerdata()[5], return_playerdata()[6], return_playerdata()[7], return_playerdata()[8], return_playerdata()[9], return_playerdata()[10], return_playerdata()[11], return_playerdata()[12]

    bat = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    bat.config(background="light grey")
    bat.grid(row=0, column=0, pady = 20)
    batsmen = Label(bat, text='Batsmen', background='light grey', font=('Times New Roman', 20, 'bold'))
    batsmen.grid(row=0, column=0)
    batsmen_value = Label(bat, text=batsmen_owned, background='light grey', font=('Times New Roman', 30, 'bold'))
    batsmen_value.grid(row=1, column=0)

    bow = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    bow.config(background="grey")
    bow.grid(row=0, column=1, pady = 20)
    bowlers = Label(bow, text='Bowlers', background='grey', font=('Times New Roman', 20, 'bold'))
    bowlers.grid(row=0, column=0)
    bowlers_value = Label(bow, text=bowlers_owned, background='grey', font=('Times New Roman', 30, 'bold'))
    bowlers_value.grid(row=1, column=0)

    wic = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    wic.config(background="light grey")
    wic.grid(row=0, column=2, pady = 20, padx = 20)
    wicket_keepers = Label(wic, text='Wkt Keepers', background='light grey', font=('Times New Roman', 20, 'bold'))
    wicket_keepers.grid(row=0, column=0)
    wicket_keepers_value = Label(wic, text=wicket_keepers_owned, background='light grey', font=('Times New Roman', 30, 'bold'))
    wicket_keepers_value.grid(row=1, column=0)


    sm.mainloop()
