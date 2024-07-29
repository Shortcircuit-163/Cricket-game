import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import csv

def shop(name, username):
    class ScrollBar:
        def __init__(self):
            shp = tk.Tk()
            shp.title("Shop")
            shp.geometry('800x600+100+200')
            shp.resizable(False, False)
            ph1 = tk.PhotoImage(file=r'images\home\quicket.png')
            shp.iconphoto(True, ph1)

            style = ttk.Style()
            style.configure('TNotebook.Tab', padding=[20, 10])

            # ---------------------------------------------------------- Getting names from required path
            def get_names_price(img_no, ptype):
                if ptype == 'batsmen':
                    with open(r'Data\batsmen_data.csv') as p_names:
                        names_reader = csv.reader(p_names, delimiter=',')
                        iterate_count = -1
                        for row in names_reader:
                            if iterate_count == img_no:
                                p_name = row[0]
                                p_price = row[3]
                                return [p_name, p_price]
                            iterate_count += 1
                elif ptype == 'bowlers':
                    with open(r'Data\bowlers_data.csv') as p_names:
                        names_reader = csv.reader(p_names, delimiter=',')
                        iterate_count = -1
                        for row in names_reader:
                            if iterate_count == img_no:
                                p_name = row[0]
                                p_price = row[3]
                                return [p_name, p_price]
                            iterate_count += 1
                elif ptype == 'all_rounders':
                    with open(r'Data\all_rounders_data.csv') as p_names:
                        names_reader = csv.reader(p_names, delimiter=',')
                        iterate_count = -1
                        for row in names_reader:
                            if iterate_count == img_no:
                                p_name = row[0]
                                p_price = row[3]
                                return [p_name, p_price]
                            iterate_count += 1
                elif ptype == 'wk_keepers':
                    with open(r'Data\wk_keepers_data.csv') as p_names:
                        names_reader = csv.reader(p_names, delimiter=',')
                        iterate_count = -1
                        for row in names_reader:
                            if iterate_count == img_no:
                                p_name = row[0]
                                return p_name
                            iterate_count += 1

            tabControl = ttk.Notebook(shp)

            tab1 = ttk.Frame(tabControl) 
            tab2 = ttk.Frame(tabControl)
            tab3 = ttk.Frame(tabControl)
            tab4 = ttk.Frame(tabControl) 
            
            tabControl.add(tab1, text='Batsmen') 
            tabControl.add(tab2, text='Bowlers') 
            tabControl.add(tab3, text='All Rounders') 
            tabControl.add(tab4, text='WK Keepers') 
            tabControl.pack(expand=1, fill='both') 

            # ---------------------------------------------------------------- 1st tab - batsmen
            canvas1 = Canvas(tab1)
            canvas1.pack(side=LEFT, fill=BOTH, expand=True)
            
            scrollbar1 = Scrollbar(tab1, orient=VERTICAL, command=canvas1.yview)
            scrollbar1.pack(side=RIGHT, fill=Y)
            
            canvas1.configure(yscrollcommand=scrollbar1.set)
            canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
            
            scr_tab1 = Frame(canvas1)
            canvas1.create_window((0, 0), window=scr_tab1, anchor="nw")

            path = r'images\shop\batsmen'
            dir_list = os.listdir(path)
            print("Files and directories in '", path, "' :")
            print(dir_list)

            # Load images and add to grid
            images1 = []
            buttons1 = []
            for player in dir_list:  # Iterate over players
                img_path = os.path.join(path, f'{player}')
                if os.path.exists(img_path):
                    img = Image.open(img_path)
                    img_resized = img.resize((150, 200))  # Resize images to 150x150
                    img_tk1 = ImageTk.PhotoImage(img_resized)
                    images1.append(img_tk1)

            img_no = 0

            for idx1, img_tk1 in enumerate(images1):
                row1 = idx1 // 3 * 2  # 3 images per row, double the row index to leave space for buttons
                col1 = idx1 % 3
                label1 = Label(scr_tab1, image=img_tk1)
                label1.grid(row=row1, column=col1, padx=10, pady=10)

                purchase_frame1 = Frame(scr_tab1)
                purchase_frame1.grid(row=row1 + 1, column=col1, padx=10, pady=10, sticky=NSEW)

                info = get_names_price(img_no, 'batsmen')

                purchase_text1 = Label(purchase_frame1, text=info[0], background='', font=('Times New Roman', 30, 'bold'))
                purchase_text1.grid(row=0, column=0)

                buy_photo = tk.PhotoImage(file=r'images\shop\buy.png')

                buy_btn = Button(purchase_frame1, image=buy_photo, style='A.TButton', command=None)
                buy_btn.image = buy_photo  # Keep a reference to avoid garbage collection
                buy_btn.grid(row=0, column=1)

                # Add button to the list for reference
                buttons1.append(buy_btn)

                img_no += 1
            
            for i in range(3):
                scr_tab1.grid_columnconfigure(i, weight=1)

            shp.mainloop()

    scr = ScrollBar()

# call to the function
shop('name', 'username')