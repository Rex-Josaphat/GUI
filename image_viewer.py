from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('PYTHON IMAGE VIEWER')

# Loading Images
img_1 = ImageTk.PhotoImage(Image.open('images/rex.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('images/a.png'))
img_3 = ImageTk.PhotoImage(Image.open('images/b.png'))
img_4 = ImageTk.PhotoImage(Image.open('images/c.png'))


img_list = [img_1, img_2, img_3, img_4]

# Adding status bar
""" 'sticky' is used to stretch towards a certain side, 'Anchor' is used to align'"""

status = Label(root, text='Image 1 of' + str(len(img_list)), bd=3, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# Defining image label
image = Label(image=img_1)
image.grid(row=0, column=0, columnspan=3)


def forward(img_index):
    '''Create globals so that the updated variables can also work out of scope'''
    global image
    global button_next
    global button_previous

    """forget the value that was there and get ready to receive another status"""
    image.grid_forget()
    image = Label(image=img_list[img_index - 1])
    button_next = Button(root, text='-->>', borderwidth=4, fg='#ffff00', bg='#000000',
                         command=lambda: forward(img_index + 1))
    button_previous = Button(root, text='<<--', borderwidth=4, fg='#ffff00', bg='#000000',
                             command=lambda: backward(img_index - 1))

    if img_index == len(img_list):
        button_next = Button(root, text='-->>', borderwidth=4, fg='#ffff00', bg='#000000', state=DISABLED)

    image.grid(row=0, column=0, columnspan=3)
    button_previous.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    # Update status bar
    status = Label(root, text='Image' + str(img_index) + 'of' + str(len(img_list)), bd=3, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def backward(img_index):
    # Create globals so that the updated variables can also work out of scope
    global image
    global button_next
    global button_previous

    image.grid_forget()
    image = Label(image=img_list[img_index - 1])
    button_next = Button(root, text='-->>', borderwidth=4, fg='#ffff00', bg='#000000',
                         command=lambda: forward(img_index + 1))
    button_previous = Button(root, text='<<--', borderwidth=4, fg='#ffff00', bg='#000000',
                             command=lambda: backward(img_index - 1))

    if img_index == 1:
        button_previous = Button(root, text='<<--', borderwidth=4, fg='#ffff00', bg='#000000', state=DISABLED)

    image.grid(row=0, column=0, columnspan=3)
    button_previous.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    status = Label(root, text='Image' + str(img_index) + 'of' + str(len(img_list)), bd=3, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_quit = Button(root, text='Exit', borderwidth=4, fg='#ffff00', bg='#000000', command=root.quit, padx=30, pady=10)
button_previous = Button(root, text='<<--', borderwidth=4, fg='#ffff00', bg='#000000', command=backward,
                         state=DISABLED)  # Button state disabled because its the first image you can't ove back
button_next = Button(root, text='-->>', borderwidth=4, fg='#ffff00', bg='#000000', command=lambda: forward(2))

button_next.grid(row=1, column=2)
button_previous.grid(row=1, column=0)
button_quit.grid(row=1, column=1)

root.mainloop()
