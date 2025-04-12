# Weather-Based Image Finder

This project connects two APIs—[OpenWeather API](https://openweathermap.org/api) and [Unsplash API](https://unsplash.com/developers)—to create a web application. The app fetches the current weather for a user-specified city and displays an image matching the weather condition.

---

## Features
- Fetches weather data using the OpenWeather API.
- Retrieves matching images using the Unsplash API.
- Displays both the weather information and a corresponding image.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MakendranG/weather-image-finder.git
   cd weather-image-finder
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

3. Add your API keys:
   - Open `app.py` and replace `your_openweather_api_key` and `your_unsplash_access_key` with your API keys.

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## Contributions
Feel free to fork the repository and submit pull requests for improvements.

---

## License
This project is licensed under the MIT License.
