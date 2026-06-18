import tkinter as tk
from tkinter import messagebox
import requests


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Title
        self.city_label = tk.Label(
            root,
            text="Enter City Name:",
            font=("Calibri", 20, "italic")
        )
        self.city_label.pack(pady=10)

        # Input
        self.city_entry = tk.Entry(
            root,
            font=("Calibri", 18),
            justify="center"
        )
        self.city_entry.pack(pady=10)

        # Button
        self.weather_button = tk.Button(
            root,
            text="Get Weather",
            font=("Calibri", 16, "bold"),
            command=self.get_weather
        )
        self.weather_button.pack(pady=10)

        # Output Labels
        self.temperature_label = tk.Label(
            root,
            font=("Calibri", 40)
        )
        self.temperature_label.pack(pady=10)

        self.emoji_label = tk.Label(
            root,
            font=("Segoe UI Emoji", 60)
        )
        self.emoji_label.pack()

        self.description_label = tk.Label(
            root,
            font=("Calibri", 24)
        )
        self.description_label.pack(pady=10)

    def get_weather(self):
        api_key = "YOUR_API_KEY_HERE"

        city = self.city_entry.get().strip()

        if not city:
            messagebox.showwarning(
                "Input Error",
                "Please enter a city name."
            )
            return

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}&units=metric"
        )

        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            if response.status_code == 200:
                self.display_weather(data)
            else:
                message = data.get("message", "Unknown Error")
                messagebox.showerror(
                    "Error",
                    message.title()
                )

        except requests.exceptions.ConnectionError:
            messagebox.showerror(
                "Connection Error",
                "Check your internet connection."
            )

        except requests.exceptions.Timeout:
            messagebox.showerror(
                "Timeout Error",
                "The request timed out."
            )

        except requests.exceptions.RequestException as e:
            messagebox.showerror(
                "Request Error",
                str(e)
            )

    def display_weather(self, data):
        temperature = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"].title()

        self.temperature_label.config(
            text=f"{temperature:.0f}°C"
        )

        self.emoji_label.config(
            text=self.get_weather_emoji(weather_id)
        )

        self.description_label.config(
            text=description
        )

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return "🌍"


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
