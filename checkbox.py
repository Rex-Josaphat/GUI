from tkinter import *

root = Tk()
root.title('Python Checkbox')

var = StringVar()
c = Checkbutton(root, text='Click, Here!', variable=var, onvalue='off', offvalue='on')
c.deselect()
c.pack()

def check():
    l = Label(root, text=var.get()).pack()
    
    if var.get() == 0:
        lab = Label(root, text='Box Not Checked!').pack()

btn = Button(root, text='Show', command=check).pack()

quit = Button(root, text='Exit', command=root.quit).pack()
root.mainloop()