# Weather Forecast CLI Application

This command-line application fetches and displays the current weather forecast for a specified location using the OpenWeatherMap API.

## 🌟 Features

- Retrieves geolocation data for any city
- Fetches current weather data for the specified location
- Displays weather conditions, temperature, wind speed, sunrise, and sunset times
- Converts temperatures from Kelvin to Fahrenheit for easy interpretation
- Converts Unix timestamps to local time for the specified location
- Robust error handling for API requests and data retrieval

## 🚀 Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/lakota-camp/weather-cl-tool.git
    cd weather-cl-tool
    ```

2. **Set up a virtual environment and activate it:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Add your OpenWeatherMap API key:**

    Create a `.env` file in the root directory and add your API key:

    ```plaintext
    API_KEY=your_api_key_here
    ```

5. **Run the application:**

    ```bash
    python3 weather.py  # or python3 san_diego_weather.py for San Diego weather (Incase the weather sucks where you live)
    ```

## 🛠️ CLI Command Alias Setup

To simplify running the weather forecast scripts, you can set up command aliases in your shell configuration file (`.bashrc`, `.zshrc`, etc.):

1. Open your shell configuration file:

    ```bash
    nano ~/.zshrc # or ~/.bashrc depending on your shell
    ```

2. Add the following alias definitions:

    ```bash
    alias weather-sd='source /path/to/dir/.venv/bin/activate && python3 /path/to/dir/san_diego_weather.py'
    alias weather='source /path/to/dir/.venv/bin/activate && python3 /path/to/dir/weather.py'
    ```

3. Save and close the file.

4. Apply the changes:

    ```bash
    source ~/.bashrc  # or ~/.zshrc depending on your shell
    ```

Now, you can use the aliases `weather-sd` and `weather` to run the scripts.

## 📦 Dependencies

- `requests`
- `python-dotenv`

## 📝 Additional Information

- **Error Handling**: The application includes basic error handling for API requests and data retrieval, ensuring that meaningful messages are displayed in case of failures.
- **Temperature Conversion**: The application converts temperatures from Kelvin to Fahrenheit for easier interpretation.
- **Time Conversion**: Unix timestamps for sunrise and sunset times are converted to local time for the specified location.

## 📄 License

This project is licensed under the MIT License.
