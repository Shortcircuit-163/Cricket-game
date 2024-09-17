import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import csv


def squad_scr(name, username):
    from Singleplayer_start import start_match_singleplayer

    class ScrollBar:
        def __init__(self):
            self.sqd = tk.Tk()
            self.sqd.title("My Squad")
            self.sqd.geometry('600x800')
            self.sqd.resizable(False, False)
            self.sqd.configure(background='light grey')
            ph1 = tk.PhotoImage(file=r'images\home\quicket.png')
            self.sqd.iconphoto(True, ph1)

            style = ttk.Style()
            style.configure('TNotebook.Tab', padding=[20, 10])

            def go_to_singleplayer():
                self.sqd.destroy()
                start_match_singleplayer(name, username)

            # Function to get player names
            def get_names(img_no, ptype):
                batsmen_list = []
                bowlers_list = []
                all_rounders_list = []
                wk_keepers_list = []

                if ptype == 'batsmen':
                    for i in range(len(roles_list)):
                        if i == 'bat':
                            batsmen_list.append([owned_players_list[i]])
                            return batsmen_list[img_no]
                elif ptype == 'bowlers':
                    for i in range(len(roles_list)):
                        if i == 'bowl':
                            bowlers_list.append([owned_players_list[i]])
                            return bowlers_list[img_no]
                elif ptype == 'all_rounders':
                    for i in range(len(roles_list)):
                        if i == 'alr':
                            all_rounders_list.append([owned_players_list[i]])
                            return all_rounders_list[img_no]
                elif ptype == 'wk_keepers':
                    for i in range(len(roles_list)):
                        if i == 'wk':
                            wk_keepers_list.append([owned_players_list[i]])
                            return wk_keepers_list[img_no]

                # with open(file_path) as p_names:
                #     names_reader = csv.reader(p_names, delimiter=',')
                #     iterate_count = -1
                #     for row in names_reader:
                #         if iterate_count == img_no:
                #             p_name = row[0]
                #             return p_name
                #         iterate_count += 1

            tabControl = ttk.Notebook(self.sqd)

            tab1 = ttk.Frame(tabControl) 
            tab2 = ttk.Frame(tabControl)
            tab3 = ttk.Frame(tabControl)
            tab4 = ttk.Frame(tabControl) 
            
            tabControl.add(tab1, text='Batsmen') 
            tabControl.add(tab2, text='Bowlers') 
            tabControl.add(tab3, text='All Rounders') 
            tabControl.add(tab4, text='WK Keepers') 
            tabControl.pack(expand=1, fill='both') 

            
            owned_players_list = []
            roles_list = []
            with open(r'all_data\users\player_data_' + username + '.csv', 'r') as owned_players:
                owned_reader = csv.reader(owned_players, delimiter=',')
                for row in owned_reader:
                    if row[1] == ('players'):
                        continue
                    else:
                        owned_players_list.append(row[0])
                        roles_list.append(row[1])

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

                photo4 = tk.PhotoImage(file=r'images\singleplayer_start\home1.png')                
                btn3 = tk.Button(scr_frame, image=photo4, command=go_to_singleplayer, borderwidth=0, background='light grey')
                btn3.photo = photo4  # Keep a reference to avoid garbage collection
                btn3.grid(row=0, column=0, sticky=W, padx=10, pady=10)

                balance_label = tk.Label(scr_frame, text='MY SQUAD', background='light grey', font=('Times New Roman', 20, 'bold'))
                balance_label.grid(row=0, column=1, padx=10, pady=10, sticky=NSEW)

                dir_list = os.listdir(path)

                images = []
                for player in dir_list:
                    if str(player[:-4]) in owned_players_list:
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

                    name1 = get_names(img_no, ptype)
                    purchase_text = Label(frame, text=name1, font=('Roboto Mono', 10, 'bold'), background='light grey')
                    purchase_text.pack()

                    img_no += 1

            create_tab(tab1, r'images\shop\batsmen', 'batsmen')
            create_tab(tab2, r'images\shop\bowlers', 'bowlers')
            create_tab(tab3, r'images\shop\all rounders', 'all_rounders')
            create_tab(tab4, r'images\shop\wk keepers', 'wk_keepers')

            self.sqd.mainloop()

    scr = ScrollBar()
