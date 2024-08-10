import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image

def home():


    def exit_and_open_singleplayer():
        win.destroy()
        from Singleplayer import open_singleplayer
        open_singleplayer()

    win = tk.Tk()
    win.title("Quicket")
    win.geometry('500x750')
    win.resizable(False, False)
    win.configure(background='light grey')
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    win.iconphoto(True, p1)

    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=1)
    win.grid_columnconfigure(2, weight=1)
    win.grid_rowconfigure(0, weight=1)
    win.grid_rowconfigure(1, weight=1)
    win.grid_rowconfigure(2, weight=1)
    win.grid_rowconfigure(3, weight=1)
    win.grid_rowconfigure(4, weight=1)


    heading = Label(win, text="Quicket", background='light grey', font=('Times New Roman', 50, 'bold'))
    heading.grid(row=0, column=1)

    quicket_image = Image.open(r'images\home\quicket_bg.png')
    quicket_image_resized = quicket_image.resize((250,250))
    quicket_resized = ImageTk.PhotoImage(quicket_image_resized)
    quicket_image_label = Label(win, image=quicket_resized)
    quicket_image_label.grid(row=1, column=1)

    play_mode = Label(win, text='-Choose Game Mode-', background='light grey', font=('Century Gothic', 30, 'underline'))
    play_mode.grid(row=2, column=1)

    photo1 = tk.PhotoImage(file=r'images\home\singleplayer.png')
    btn1 = Button(win, image=photo1, style='A.TButton', command=exit_and_open_singleplayer)
    btn1.grid(row=3, column=1)

    photo2 = tk.PhotoImage(file=r'images\home\multiplayer.png')
    btn2 = Button(win, image=photo2, style='B.TButton', command=None)
    btn2.grid(row=4, column=1)

    win.mainloop()

home()