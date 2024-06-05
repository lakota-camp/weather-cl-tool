# Weather Forecast Application

This project fetches and displays the current weather forecast for a specified location using the OpenWeatherMap API.

## Features

- Fetches geolocation data for a city
- Retrieves current weather data for the location
- Displays weather conditions, temperature, wind speed, sunrise, and sunset times
- Converts temperatures from Kelvin to Fahrenheit
- Converts Unix timestamps to local time
- Handles error cases for API requests and data retrieval

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/lakotcamp/weather-cl-tool.git
    cd weather-cl-tool
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your OpenWeatherMap API key:

    ```plaintext
    API_KEY=your_api_key_here
    ```

5. Run the application:

    ```bash
    python san_diego_weather.py  # or python weather.py for the general script
    ```

## CLI Command Alias Setup

To simplify running the weather forecast scripts, you can set up command aliases in your shell configuration file (`.bashrc`, `.zshrc`, etc.). Follow these steps:

1. Open your shell configuration file in a text editor. For example:

    ```bash
    nano ~/.bashrc  # or ~/.zshrc depending on your shell
    ```

2. Add the following alias definitions to the file:

    ```bash
    alias weather-sd='source /path/to/dir/.venv/bin/activate && python3 /path/to/dir/san_diego_weather.py'
    alias weather='source /path/to/dir/.venv/bin/activate && python3 /path/to/dir/weather.py'
    ```

3. Save and close the file (e.g., `Ctrl+O`, `Enter`, `Ctrl+X` in nano).

4. Apply the changes by sourcing the configuration file:

    ```bash
    source ~/.bashrc  # or ~/.zshrc depending on your shell
    ```

5. Now you can use the aliases to run the scripts:

    ```bash
    weather-sd
    weather
    ```

## Dependencies

- `requests`
- `python-dotenv`
- `pytz`

## Additional Information

- **Error Handling**: The application includes basic error handling for API requests and data retrieval, ensuring that meaningful messages are displayed in case of failures.
- **Temperature Conversion**: The application converts temperatures from Kelvin to Fahrenheit for easier interpretation.
- **Time Conversion**: Unix timestamps for sunrise and sunset times are converted to local time for the specified location.

## License

This project is licensed under the MIT License.
