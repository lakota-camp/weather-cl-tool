import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

api_key = os.getenv('API_KEY')

# Check if API Key is found in .evn file
if not api_key:
    raise ValueError("API key not found. Please add your API key to the .env file.")

# Function to make API request
def make_api_request(url):
    """Returns dict response if an API GET request is successful.

    Args:
        url (String): API Endpoint

    Returns:
        dict or None: Python dictionary representation of the JSON response from API, or None if request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
        return None

# Function to get geo location from an API end point, given: City, State Code, Country Code, and API Key. Uses the make_api_request function created previously.
def get_geo_location(city, state_code, country_code, api_key):
    """ Returns the geo location (latitude, longitude) of a given location.

    Args:
        city (str): City e.g. San Diego
        state_code (str): State e.g. CA
        country_code (str): Country e.g. US
        api_key (str): OpenWeather API Key

    Returns:
        float: returns latitude (lat) and longitude (lon)
    """
    
    geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&limit=1&appid={api_key}'

    # GET request to API
    data = make_api_request(geo_url)
    
    if data:
        lat = data[0].get('lat')
        lon = data[0].get('lon')
        return lat, lon
    
    return None, None

# Function to fetch the weather data given a latitude, longitude, and API Key. Uses the make_api_request function created previously.
def get_weather(lat, lon, api_key):
    """Returns weather data for a given latitude and longitude.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        api_key (str): OpenWeatherAPI key.

    Returns:
        dict or None: Python dictionary representation of the weather data for the given location, or None if request fails.
    """
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
        
    return make_api_request(weather_url)

# Function to elegantly dipslay the data in the terminal
def display_data(weather_data, city, state_code):
    """Displays the weather data for given location

    Args:
        weather_data (dict): Object returned by weather API
        city (str): City e.g. San Diego
        state_code (str): State e.g. CA
    Returns:
        None
    """
    
    # Check if weather data is present
    if weather_data:
        # Weather description   
        weather_desc = weather_data['weather'][0]['description']   
           
        # Temp
        temp = (weather_data['main']['temp'])
        temp_min = weather_data['main']['temp_min']
        temp_max = weather_data['main']['temp_max']
        temp_feels_like = weather_data['main']['feels_like']
                
        # Wind
        wind_speed = weather_data['wind']['speed']
                
        # Sunrise and sunset
        sunsrise_time_timestamp = weather_data['sys']['sunrise']
        sunset_time_timestamp = weather_data['sys']['sunset']
        
        # Convert to appropriate timezone
        timezone_offset = timedelta(seconds=weather_data['timezone'])
        print(timezone_offset)
                    
        # Convert UTC time to local time
        sunrise_local_time = (datetime.fromtimestamp(sunsrise_time_timestamp, timezone.utc) + timezone_offset).time()
        sunset_local_time = (datetime.fromtimestamp(sunset_time_timestamp, timezone.utc) + timezone_offset).time()
                
        # Display data
        print(f'Current Weather Forecast for {city}, {state_code}')
        print('-' * 45)
        print(f'{"Conditions:":<20} {weather_desc}')
        print(f'{"Temperature:":<20} {temp:.2f} °F')
        print(f'{"Feels Like:":<20} {temp_feels_like:.2f} °F')
        print(f'{"Min Temperature:":<20} {temp_min:.2f} °F')
        print(f'{"Max Temperature:":<20} {temp_max:.2f} °F')
        print(f'{"Wind Speed:":<20} {wind_speed:.2f} mph')
        print(f'{"Sunrise:":<20} {sunrise_local_time.strftime('%I:%M %p')}')
        print(f'{"Sunset:":<20} {sunset_local_time.strftime('%I:%M %p')}')
        print('-' * 45)
        
    else:
        print('No weather data available.')

def main():
    while True:
        city = input('Enter a city (e.g. San Diego): ')
        state_code = input('Enter a state (e.g. CA): ')
        country_code = input('Enter a country (e.g. US): ')
        print()
        # Fetch lat and lon
        lat, lon = get_geo_location(city, state_code, country_code, api_key)
        
        # Conditional to check if lat and lon is present
        if (lat is not None) and (lon is not None):
            # Fetch data given the lat, lon, and API Key
            weather_data = get_weather(lat, lon, api_key)
            # Display data using function
            display_data(weather_data, city, state_code)
        else:
            print(f'Failed to fetch geolcation data.')
        
        print()
        # Prompt to check to see if another weather check wants to be made
        check = input('Would you like to check the weather for another location? \n(Enter Y to continue)\n(Enter any key other to exit): ')
        if check.lower() != 'y':
            print()
            print('-' * 25)
            print('Weather check complete!')
            print('-' * 25)
            print()
            break


if __name__ == '__main__':
    main()
