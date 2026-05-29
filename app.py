from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    
    if request.method == "POST":
        city = request.form.get("city")
        print(f"User entered: {city}")
        
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            print(f"URL: {url}")  # Check this URL works in browser
            
            response = requests.get(url)
            data = response.json()
            print(f"API Response: {data}")  # << Check this!
            
            if data.get("cod") != 200:
                print(f"Error: {data.get('message')}")
                data = None
            else:
                # Convert wind speed
                wind_ms = data["wind"]["speed"]
                data["wind"]["speed"] = round(wind_ms * 3.6, 2)

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)