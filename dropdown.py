from tkinter import *
import tkinter.ttk as tk
root = Tk()
root.title('Dropdown menu')
root.geometry('400x400')


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
var = StringVar(root)
var.set(days[0])

drop = OptionMenu(root, var, *days)
drop.pack()
dropdown = var.get()
print(dropdown)
exit = Button(root, text='Exit!', command=root.quit).pack()
root.mainloop()