from tkinter import *

root = Tk()
root.title('PYTHON CALCULATOR')
a = Entry(root, width=35, borderwidth=5, bg='#353535', fg='#eeee00')
a.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(number):
    current = a.get()
    a.delete(0, END)
    a.insert(0, str(current) + str(number))
    return


def button_plus():
    first_number = a.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    a.delete(0, END)


def button_clean():
    a.delete(0, END)


def button_equal():
    sec_number = a.get()
    a.delete(0, END)

    if math == 'addition':
        a.insert(0, f_num + int(sec_number))

    if math == 'subtraction':
        a.insert(0, f_num - int(sec_number))

    if math == 'division':
        a.insert(0, f_num / int(sec_number))

    if math == 'multiplication':
        a.insert(0, f_num * int(sec_number))


def subtract():
    first_number = a.get()
    """We Create globals so that the updated variables can also work out of scope"""
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    a.delete(0, END)


def multiply():
    first_number = a.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    a.delete(0, END)


def divide():
    first_number = a.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    a.delete(0, END)


# define buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_add(1), fg='yellow', bg='#252525')
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_add(2), fg='yellow', bg='#252525')
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_add(3), fg='yellow', bg='#252525')
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_add(4), fg='yellow', bg='#252525')
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_add(5), fg='yellow', bg='#252525')
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_add(6), fg='yellow', bg='#252525')
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_add(7), fg='yellow', bg='#252525')
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_add(8), fg='yellow', bg='#252525')
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_add(9), fg='yellow', bg='#252525')
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_add(0), fg='yellow', bg='#252525')

# Final operation buttons
button_clear = Button(root, text='Clear', padx=79, pady=20, command=button_clean, fg='yellow', bg='#252525')
button_equals = Button(root, text='=', padx=91, pady=20, command=button_equal, fg='yellow', bg='#252525')

# Operation buttons
button_plus = Button(root, text='+', padx=38, pady=20, command=button_plus, fg='yellow', bg='#252525')
button_minus = Button(root, text='-', padx=39, pady=20, command=subtract, fg='yellow', bg='#252525')
button_times = Button(root, text='*', padx=42, pady=20, command=multiply, fg='yellow', bg='#252525')
button_divide = Button(root, text='/', padx=38, pady=20, command=divide, fg='yellow', bg='#252525')

button_quit = Button(root, text='Exit', padx=20, pady=20, command=root.quit, fg='yellow', bg='#252525')

# Align buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_plus.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_minus.grid(row=6, column=0)
button_times.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_quit.grid(row=7, column=1)

root.mainloop()
