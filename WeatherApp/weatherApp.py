from tkinter import *
from configparser import ConfigParser
import requests


url ='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))

    if result.status_code == 200:  # Check if the request was successful (status code 200)
        print(result.json())  # Use result.json() to parse the response as JSON
    else:
        print("Error:", result.status_code)
        return None

# Example usage
get_weather("London")
def Search():
    pass

app = Tk()
app.title("Weather App")
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search Weather', width=12, command=Search)
search_btn.pack()

location_lbl = Label(app, text='Location', font=('bold',20))
location_lbl.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text='Temperature')
temp_lbl.pack()


weather_lbl = Label(app, text='Weather')
weather_lbl.pack()





app.mainloop()