from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message boxes')

def popup():
    response = messagebox.askokcancel('This is my popup', 'Read Timeout!')
    # Label(root, text=response).pack()
    
    if response == 1:
        a = Label(root, text='Approved').pack()

    else: 
        a = Label(root, text='Canceled').pack()

button = Button(root, text='click', command=popup).pack()

button_quit = Button(root, text='Exit', borderwidth=4, fg='#ffff00', bg='#000000', command=root.quit)
button_quit.pack()
root.mainloop()