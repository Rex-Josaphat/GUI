from tkinter import *
import tkinter.font as font
import requests
from PIL import ImageTk, Image

HEIGHT = 480
WIDTH = 500


def text(entry):
    print('The entry is:', entry)


def get_weather(city):
    weather_key = 'beaae2dd3ab0e89755e44bbd9a6dd7c0'
    url = 'https://api.openweathermap.org/data/2.5/forecast'

    parameters = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=parameters)
    print(response.json())


root = Tk()
root.title('Weather App')

# Define font
myFont = font.Font(family='Times')

# Set UI resolution
canvas = Canvas(root, height=HEIGHT, width=WIDTH).pack()

# Insert backgroung image
back_img = PhotoImage(file='./images/unnamed.GIF')
back_label = Label(root, image=back_img).place(relwidth=1, relheight=1)

# Create the top frame
'''The top frame is where the user shall input the city where they want to retreive the weather'''
t_frame = Frame(root, bg='#80ff80', bd=3)
t_frame.place(relx=0.5, rely=0.1, relwidt=0.75, relheight=0.1, anchor='n')

# Create City input box
city = Entry(t_frame).place(relwidth=0.65, relheight=1)


# Create buton to view weather
def check():
    global label

    label = Label(l_frame, text='Button Clicked!', font=5)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label['font'] = myFont


check_btn = Button(t_frame, text='Get Weather', command=lambda: get_weather(entry.get()))
check_btn.place(relx=0.7, relheight=1, relwidth=0.3)
check_btn['font'] = myFont

# Create the bottom frame
'''This is where the weather results will be displayed'''
l_frame = Frame(root, bg='#80ff80', bd=3)
l_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Create wher the output data will be located
label = Label(l_frame)
label.place(relwidth=1, relheight=1)

# Exit app
quit = Button(root, text='Exit!', command=root.quit)
quit.pack(side='bottom')
quit['font'] = myFont
root.mainloop()
