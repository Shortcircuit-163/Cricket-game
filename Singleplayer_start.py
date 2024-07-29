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
        from Shop import shop
        shop(name, username)

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

    all = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    all.config(background="grey")
    all.grid(row=0, column=3, pady = 20)
    all_rounders = Label(all, text='All Rounders', background='grey', font=('Times New Roman', 20, 'bold'))
    all_rounders.grid(row=0, column=0)
    all_rounders_value = Label(all, text=all_rounders_owned, background='grey', font=('Times New Roman', 30, 'bold'))
    all_rounders_value.grid(row=1, column=0)

    wice = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    wice.config(background="light grey")
    wice.grid(row=0, column=4, pady = 20)
    wickets_label = Label(wice, text='Wickets', background='light grey', font=('Times New Roman', 20, 'bold'))
    wickets_label.grid(row=0, column=0)
    wickets_value = Label(wice, text=wickets, background='light grey', font=('Times New Roman', 30, 'bold'))
    wickets_value.grid(row=1, column=0)

    run = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    run.config(background="grey")
    run.grid(row=1, column=0, pady = 20)
    runs_label = Label(run, text='Runs', background='grey', font=('Times New Roman', 20, 'bold'))
    runs_label.grid(row=0, column=0)
    runs_value = Label(run, text=runs, background='grey', font=('Times New Roman', 30, 'bold'))
    runs_value.grid(row=1, column=0)

    eco = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    eco.config(background="light grey")
    eco.grid(row=1, column=1)
    economy_label = Label(eco, text='Net R.R.', background='light grey', font=('Times New Roman', 20, 'bold'))
    economy_label.grid(row=0, column=0)
    economy_value = Label(eco, text=economy, background='light grey', font=('Times New Roman', 30, 'bold'))
    economy_value.grid(row=1, column=0)

    tot = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    tot.config(background="grey")
    tot.grid(row=1, column=2)
    total_overs_label = Label(tot, text='Total Overs', background='grey', font=('Times New Roman', 20, 'bold'))
    total_overs_label.grid(row=0, column=0)
    total_overs_value = Label(tot, text=total_overs, background='grey', font=('Times New Roman', 30, 'bold'))
    total_overs_value.grid(row=1, column=0)

    batt = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    batt.config(background="light grey")
    batt.grid(row=1, column=3)
    batting_avg = Label(batt, text='Games Won', background='light grey', font=('Times New Roman', 20, 'bold'))
    batting_avg.grid(row=0, column=0)
    batting_avg_value = Label(batt, text=batting_average, background='light grey', font=('Times New Roman', 30, 'bold'))
    batting_avg_value.grid(row=1, column=0)

    bowl = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    bowl.config(background="grey")
    bowl.grid(row=1, column=4)
    bowling_avg = Label(bowl, text='Games lost', background='grey', font=('Times New Roman', 20, 'bold'))
    bowling_avg.grid(row=0, column=0)
    bowling_avg_value = Label(bowl, text=bowling_average, background='grey', font=('Times New Roman', 30, 'bold'))
    bowling_avg_value.grid(row=1, column=0)

    inn = tk.Frame(player_info, highlightbackground="black", highlightthickness=6)
    inn.config(background="light grey")
    inn.grid(row=2, column=2)
    innings_label = Label(inn, text='Matches', background='light grey', font=('Times New Roman', 20, 'bold'))
    innings_label.grid(row=0, column=0)
    innings_value = Label(inn, text=innings, background='light grey', font=('Times New Roman', 30, 'bold'))
    innings_value.grid(row=1, column=0)

    game_start = tk.Frame(sm)
    game_start.grid(row=2, column=1)

    overs_var=tk.StringVar()


    name_label = tk.Label(game_start, text = 'Select number of overs:', font=('calibre',21, 'bold'))
    name_label.grid(row=0, column=0, padx=20)
    over_options = [2, 3, 4]
    over_select = Combobox(game_start, textvariable=overs_var, values=over_options, state="readonly", font=('calibre',21,'bold'))
    over_select.grid(row=0, column=1, padx=20)

    start_img = tk.PhotoImage(file=r'images\singleplayer_start\start.png')
    login_button=tk.Button(game_start,image=start_img, command = None, borderwidth=0) #button to open game
    login_button.grid(row=0, column=2)

    sm.mainloop()
