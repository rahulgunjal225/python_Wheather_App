from tkinter import *
from tkinter import ttk
import requests

def data_get():
    try:
        city = city_name.get()
        api_key = "d8f6e2a66ed7523a5744fb79ab2bc045"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        data = requests.get(url).json()

        # Update weather data in labels
        W1_label.config(text=data["weather"][0]["main"])
        Wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + "°C")
        Per_label1.config(text=str(data["main"]["pressure"]) + " hPa")

    except KeyError:
        # Handle case where city name is invalid or API returns an error
        W1_label.config(text="N/A")
        Wb_label1.config(text="Invalid city name")
        temp_label1.config(text="N/A")
        Per_label1.config(text="N/A")
    except Exception as e:
        # Handle other unexpected errors
        W1_label.config(text="Error")
        Wb_label1.config(text=str(e))
        temp_label1.config(text="N/A")
        Per_label1.config(text="N/A")

# Initialize Tkinter window
win = Tk()
win.title("RG Weather App")
win.config(bg="blue")
win.geometry("500x500")

# App title
name_label = Label(win, text="RG WEATHER APP", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

# City selection dropdown
city_name = StringVar()
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
    "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
    "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
]
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Weather info labels
W_label = Label(win, text="Weather Climate", font=("Times New Roman", 10))
W_label.place(x=25, y=250, height=40, width=200)

W1_label = Label(win, text="", font=("Times New Roman", 10))
W1_label.place(x=250, y=250, height=40, width=200)

Wb_label = Label(win, text="Weather Description", font=("Times New Roman", 10))
Wb_label.place(x=25, y=300, height=40, width=200)

Wb_label1 = Label(win, text="", font=("Times New Roman", 10))
Wb_label1.place(x=250, y=300, height=40, width=200)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 10))
temp_label.place(x=25, y=350, height=40, width=200)

temp_label1 = Label(win, text="", font=("Times New Roman", 10))
temp_label1.place(x=250, y=350, height=40, width=200)

Per_label = Label(win, text="Pressure", font=("Times New Roman", 10))
Per_label.place(x=25, y=400, height=40, width=200)

Per_label1 = Label(win, text="", font=("Times New Roman", 10))
Per_label1.place(x=250, y=400, height=40, width=200)

# Button to fetch weather data
done_button = Button(win, text="DONE", font=("Times New Roman", 20, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()
