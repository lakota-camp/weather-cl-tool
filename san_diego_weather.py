import requests
import os
from dotenv import load_dotenv
from utils import conversions

load_dotenv()

api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError("API key not found. Please add your API key to the .env file.")

def get_geo_location(city, state_code, country_code, api_key):
    """ Returns the geo location (latitude, longitude) of a given location.

    Args:
        city (String): City e.g. San Diego
        state_code (String): State e.g. CA
        country_code (String): Country e.g. US
        api_key (String)

    Returns:
        _type_: returns latitude and longitude
    """
    
    geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&limit=1&appid={api_key}'

    # GET request to API
    response = requests.get(geo_url)
    

    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0].get('lat')
            lon = data[0].get('lon')
            return lat, lon

    return None, None
def get_weather(lat, lon, api_key):
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
        data = requests.get(weather_url)
        
        if data.status_code == 200:
            return data.json()
        return None 
def display_data(weather_data, city, state_code):
    """Displays the weather data for given location

    Args:
        weather_data (Object): Object returned by weather API
        city (String): City e.g. San Diego
        state_code (String): State e.g. CA
    """
    if weather_data:      
        weather_desc = weather_data['weather'][0]['description']      
        # Temp
        temp = (weather_data['main']['temp'])
        temp_min = weather_data['main']['temp_min']
        temp_max = weather_data['main']['temp_max']
        temp_feels_like = weather_data['main']['feels_like']
                
        # Wind
        wind_speed = weather_data['wind']['speed']
                
        # Sunrise and sunset
        sunrise_time_timestamp = weather_data['sys']['sunrise']
        sunset_time_timestamp = weather_data['sys']['sunset']
                
        # Convert UTC time to local time
        sunrise_local_time = conversions.timestamp_convert(sunrise_time_timestamp, 'America/Los_Angeles')
        sunset_local_time = conversions.timestamp_convert(sunset_time_timestamp, 'America/Los_Angeles')
                
        # Display data
        print(f'Current Weather Forecast for {city}, {state_code}')
        print('-' * 45)
        print(f'{"Conditions:":<20} {weather_desc}')
        print(f'{"Temperature:":<20} {temp:.2f} °F')
        print(f'{"Feels Like:":<20} {temp_feels_like:.2f} °F')
        print(f'{"Min Temperature:":<20} {temp_min:.2f} °F')
        print(f'{"Max Temperature:":<20} {temp_max:.2f} °F')
        print(f'{"Wind Speed:":<20} {wind_speed:.2f} mph')
        print(f'{"Sunrise:":<20} {sunrise_local_time}')
        print(f'{"Sunset:":<20} {sunset_local_time}')
        print('-' * 45)
    else:
        print('No weather data available.')

    
def main():
    
    city = 'San Diego'
    state_code = 'CA'
    country_code = 'US'
    
    lat, lon = get_geo_location(city, state_code, country_code, api_key)
    if (lat is not None) and (lon is not None):
        weather_data = get_weather(lat, lon, api_key)
        display_data(weather_data, city, state_code)
    else:
        print(f'Failed to fetch geolocation data.')


if __name__ == '__main__':
    main()

