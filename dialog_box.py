from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Dialog Box')
# Navigate through the files

def open():
    global img
    global btn
    root.filename = filedialog.askopenfilename(initialdir='/Users/Home/PycharmProjects/GUI/images', title='Choose', filetypes=(('png files','*.jpg'),('All files','*.*')))
    l = Label(root, text=root.filename).pack()  # Help to get path to any file
    img = ImageTk.PhotoImage(Image.open(root.filename))
    imge = Label(image=img).pack()

    btn = Button(root, text='Open', command=open, state=DISABLED).pack()    




btn = Button(root, text='Open', command=open).pack()

quit = Button(root, text='Exit', command=root.quit).pack()
root.mainloop()