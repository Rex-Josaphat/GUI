"""Used to define sections in a document"""

from tkinter import *

root = Tk()
root.title('Python Frames')

frame = LabelFrame(root, text='Rex Frame............', padx=25, pady=25)
frame.pack(padx=10, pady=10)

b = Button(frame, text='Click Me', command=frame.quit)
b.pack()



root.mainloop()