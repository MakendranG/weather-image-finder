import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# API Keys (Replace with your own keys)
OPENWEATHER_API_KEY = "your_openweather_api_key"
UNSPLASH_ACCESS_KEY = "your_unsplash_access_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather_image', methods=['POST'])
def get_weather_image():
    city = request.form.get('city', '')

    if not city:
        return jsonify({"error": "City is required"}), 400

    # Step 1: Fetch weather data from OpenWeather API
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    weather_response = requests.get(weather_url)
    if weather_response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), 500

    weather_data = weather_response.json()
    weather_condition = weather_data['weather'][0]['description']

    # Step 2: Fetch image data from Unsplash API
    unsplash_url = f"https://api.unsplash.com/search/photos?query={weather_condition}&client_id={UNSPLASH_ACCESS_KEY}"
    unsplash_response = requests.get(unsplash_url)
    if unsplash_response.status_code != 200:
        return jsonify({"error": "Failed to fetch image data"}), 500

    image_data = unsplash_response.json()
    if not image_data['results']:
        return jsonify({"error": "No images found for the weather condition"}), 404

    # Step 3: Return weather and image data
    image_url = image_data['results'][0]['urls']['regular']
    return jsonify({
        "city": city,
        "weather_condition": weather_condition,
        "image_url": image_url
    })

if __name__ == '__main__':
    app.run(debug=True)
