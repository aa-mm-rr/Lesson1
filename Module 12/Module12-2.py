import requests


def convert(kelvin):
    return kelvin - 273.15


def weatherdata(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None


def main():
    api_key = '84f5a0ba4b0b1cd1e738d8bb6006be01'
    city = input("Enter the name of the city: ")

    weather_data = weatherdata(city, api_key)
    if weather_data:
        try:
            temp_kelvin = weather_data["main"]["temp"]
            temp_celsius = convert(temp_kelvin)
            description = weather_data["weather"][0]["description"]

            print(f"\nWeather in {city.capitalize()}:")
            print(f"  Description: {description}")
            print(f"  Temperature: {temp_celsius:.2f} °C")
        except KeyError:
            print("Error: Unable to extract weather information. Please check the API response.")
    else:
        print("Could not fetch weather data. Please check the city name and your API key.")


if __name__ == "__main__":
    main()
