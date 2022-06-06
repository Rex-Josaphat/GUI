from tkinter import *

root = Tk()
root.title('Python Slider')

'''When you want to set how big your window should be'''
root.geometry('640x500')

def get_val():
    l = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))  # set size of the screen depending on position of sliders

'''By using the scale widget  you can designate the direction.(Default is vertical)'''
# Define you slider and set the range

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

# Define a function to show the value when the button is clicked

btn = Button(root, text='View', command=get_val).pack()

quit = Button(root, text='Exit', command=root.quit).pack()
root.mainloop()