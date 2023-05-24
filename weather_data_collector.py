from datetime import datetime
import requests

DIRECTIONS = {
    "N": (337.5, 22.5),
    "NNE": (22.5, 67.5),
    "NE": (67.5, 112.5),
    "ENE": (112.5, 157.5),
    "E": (157.5, 202.5),
    "ESE": (202.5, 247.5),
    "SE": (247.5, 292.5),
    "SSE": (292.5, 337.5),
    "S": (337.5, 22.5)
}

def main():
    print("\n[Welcome to Weather Data Collector]")
    
    # ask the necessary data
    api_key = input("\nEnter your valid OpenWeatherMap API key: ").strip()
    
    if not api_key:
        print(" - Sorry, go to OpenWeatherMap.org to generate your API key.")
        return

    API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    while 1:
        print("\nWhat location do you want to request?")
        try:
            lat = float(input(" Latitude:\t"))
            lon = float(input(" Longitude:\t"))
        except:
            break

        URL = f"{API_BASE_URL}?units=metric&lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(URL)
        
        # Status Code 200 is OK/Success
        if (response.status_code != 200):
            print(f"\nError in accessing the URL: {URL}")
            break
        
        # Get the JSON representation of the response
        weather = response.json()
        
        # Parse the Weather Data to get the values
        location = weather["name"]
        country = weather["sys"]["country"]
        weather_description = weather["weather"][0]["description"].title()
        clouds = weather["clouds"]["all"]
        temperature = weather["main"]["temp"]
        temperature_feels_like = weather["main"]["feels_like"]
        temperature_min = weather["main"]["temp_min"]
        temperature_max = weather["main"]["temp_max"]
        humidity = weather["main"]["humidity"]
        pressure = weather["main"]["pressure"]
        
        wind_speed = weather["wind"]["speed"]
        wind_degrees = weather["wind"]["deg"]
        wind_direction = get_wind_direction(wind_degrees)
        
        weather_datetime = get_formatted_datetime(weather["dt"], "%Y-%m-%d")
        
        sunrise_timestamp = weather["sys"]["sunrise"]
        sunrise = get_formatted_datetime(sunrise_timestamp, "%I:%S %p")
        sunset_timestamp = weather["sys"]["sunset"]
        sunset = get_formatted_datetime(sunset_timestamp, "%I:%S %p")
        
        print(f"\nWeather Data in {location}, {country}")
        print(f" - Date:          \t{weather_datetime}")
        print(f" - Weather:       \t{weather_description}")
        print(f" - Cloud cover:   \t{clouds}%")
        print(f" - Temperature:   \t{temperature}°C (feels like {temperature_feels_like}°C)")
        print(f"     Min and Max: \t{temperature_min} | {temperature_max}°C")
        print(f" - Rel. Humidity: \t{humidity}%")
        print(f" - Wind:          \t{wind_speed} km/h {wind_direction}")
        print(f" - Atm. Pressure: \t{pressure} Pa")
        print(f" - Sunrise:       \t{sunrise}")
        print(f" - Sunset:        \t{sunset}")

    print("\nGoodbye!")

def get_formatted_datetime(timestamp, formatting):
    return datetime.fromtimestamp(timestamp).strftime(formatting)

def get_wind_direction(degrees):
    for direction, (lower, upper) in DIRECTIONS.items():
        if lower <= degrees < upper:
            return direction
    return "N/A"

if __name__ == "__main__":
    main()