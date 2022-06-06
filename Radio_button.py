from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio buttons')

# Defining the kinter variable
# r = IntVar()
# r.set('2')

img_1 = ImageTk.PhotoImage(Image.open('images/rex.jpg'))

var = StringVar()
var.set('boy')
l = Label(root, bg='white', width=20, text='Select an option!')
l.pack()
 
options = [('mom', 'Mom'), ('boy', 'Boy'), ('cousin', 'Cousin')]

def print_selection():
    l.config(text=var.get())

for opt,val in options:
    r = Radiobutton(root, text=opt, activeforeground='red', variable=var, value=val).pack(anchor=W)

r1 = Radiobutton(root, text='image', activeforeground='red', variable=var, value=img_1).pack(anchor=W)

button = Button(root, text='Select_', borderwidth=4, fg='#ffff00', bg='#000000', command= print_selection).pack()
 
   
   
# label = Label(root, text=person.get())
# label.pack()

# Defining the radio buttons
# Radiobutton(root, text='Option1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option2', variable=r, value=2, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option3', variable=r, value=3, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option4', variable=r, value=4, command=lambda: clicked(r.get())).pack()


button_quit = Button(root, text='Exit', borderwidth=4, fg='#ffff00', bg='#000000', command=root.quit)
button_quit.pack()
root.mainloop()