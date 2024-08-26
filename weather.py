import requests

def get_weather(api_key, location):
    """Fetch the current weather for the specified location."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    """Display weather information."""
    if weather_data.get("cod") != 200:
        print(f"Error: {weather_data.get('message', 'Unable to fetch weather data.')}")
        return
    
    city = weather_data.get("name")
    temp = weather_data["main"].get("temp")
    humidity = weather_data["main"].get("humidity")
    weather_description = weather_data["weather"][0].get("description")
    
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_description.capitalize()}")

def main():
    print("Welcome to the Weather App!")
    
    # Get the API key and location from the user
    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter the location (city or ZIP code): ")

    try:
        # Fetch and display the weather data
        weather_data = get_weather(api_key, location)
        display_weather(weather_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "__main__":
    main()
