# 🌦️ Weather App (Tkinter)

A simple and user-friendly Weather Application built with **Python**, **Tkinter**, and the **OpenWeatherMap API**. This desktop application allows users to search for real-time weather information for any city worldwide.

## Features

* Clean graphical user interface built with Tkinter
* Search weather by city name
* Display current temperature in Celsius
* Show weather conditions and descriptions
* Weather icons/emojis for better visualization
* Robust error handling for network and API issues
* Fast and lightweight desktop application

## Preview

![Weather App Screenshot](screenshot.png)

## Technologies Used

* Python 3.x
* Tkinter (GUI Framework)
* Requests Library
* OpenWeatherMap API

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/tkinter-weather-app.git
cd tkinter-weather-app
```

### Install Dependencies

```bash
pip install requests
```

> Tkinter comes pre-installed with most Python distributions.

### Get an OpenWeatherMap API Key

1. Sign up for a free account on OpenWeatherMap.
2. Generate an API key from your dashboard.
3. Open the Python file and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key:

```python
API_KEY = "your_api_key_here"
```

## Running the Application

```bash
python weather_app.py
```

## How It Works

1. Launch the application.
2. Enter a city name in the input field.
3. Click the **Get Weather** button.
4. View:

   * Current Temperature
   * Weather Description
   * Weather Icon/Emoji

## Example Output

```text
City: London

Temperature: 18°C
Condition: Broken Clouds
Emoji: ☁️
```

## Error Handling

The application handles common errors such as:

* Empty city input
* Invalid city names
* No internet connection
* API request timeout
* Unexpected API responses

## Project Structure

```text
tkinter-weather-app/
│
├── weather_app.py
├── README.md
├── screenshot.png
└── requirements.txt
```

## Future Enhancements

* 7-Day Weather Forecast
* Dynamic Weather Icons
* Auto-detect User Location
* Temperature Unit Conversion (°C / °F)
* Dark Mode Theme
* Search History
* Multiple Language Support

## API Reference

This project uses the OpenWeatherMap Current Weather API to fetch live weather data.

## License

This project is licensed under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## Author

Created using Python, Tkinter, and OpenWeatherMap API.
