import tkinter as tk
from tkinter import messagebox
from weather import get_weather

def show_weather():
    city_name = city_entry.get()
    if city_name:
        weather_data = get_weather(city_name)
        messagebox.showinfo("Weather Information", weather_data)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

def create_gui():
    global city_entry
    root = tk.Tk()
    root.title("Weather App")

    # Create a label and entry to input the city name
    city_label = tk.Label(root, text="Enter City Name:")
    city_label.pack(pady=10)
    city_entry = tk.Entry(root, width=50)
    city_entry.pack(pady=5)

    # Create a button to fetch and display the weather information
    get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
    get_weather_button.pack(pady=20)

    # Run the application
    root.mainloop()
