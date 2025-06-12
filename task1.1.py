import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Configuration
API_KEY = "5857e967f3a44771b835f22da49ee11e"  # Your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
DEFAULT_CITY = "London"
UNITS = "metric"

def fetch_weather_data(city_name, units=UNITS):
    """Fetch 5-day forecast data from OpenWeatherMap API."""
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": units
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"🚨 Error fetching data for '{city_name}': {e}")
        return None

def process_weather_data(data):
    """Convert API data into a structured DataFrame."""
    records = []
    for forecast in data["list"]:
        records.append({
            "datetime": datetime.fromtimestamp(forecast["dt"]),
            "temp": forecast["main"]["temp"],
            "feels_like": forecast["main"]["feels_like"],
            "humidity": forecast["main"]["humidity"],
            "wind_speed": forecast["wind"]["speed"],
            "weather": forecast["weather"][0]["main"],
        })
    return pd.DataFrame(records)

def create_visualizations(df, city_name):
    """Generate a weather dashboard with 4 subplots."""
    plt.figure(figsize=(15, 10))
    plt.suptitle(f"5-Day Weather Forecast for {city_name}", fontweight="bold")

    # Plot 1: Temperature
    plt.subplot(2, 2, 1)
    plt.plot(df["datetime"], df["temp"], label="Actual Temp", color="red", linewidth=2)
    plt.plot(df["datetime"], df["feels_like"], label="Feels Like", color="orange", linestyle="--")
    plt.xlabel("Date/Time")
    plt.ylabel(f"Temperature (°{'C' if UNITS == 'metric' else 'F'})")
    plt.legend()
    plt.grid(alpha=0.3)

    # Plot 2: Humidity
    plt.subplot(2, 2, 2)
    plt.bar(df["datetime"], df["humidity"], color="royalblue", alpha=0.7)
    plt.xlabel("Date/Time")
    plt.ylabel("Humidity (%)")
    plt.grid(alpha=0.3)

    # Plot 3: Wind Speed
    plt.subplot(2, 2, 3)
    plt.plot(df["datetime"], df["wind_speed"], color="green", marker="o")
    plt.xlabel("Date/Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.grid(alpha=0.3)

    # Plot 4: Weather Conditions
    plt.subplot(2, 2, 4)
    weather_counts = df["weather"].value_counts()
    plt.pie(weather_counts, 
            labels=weather_counts.index, 
            autopct="%1.1f%%", 
            colors=["gold", "lightcoral", "lightblue"])
    plt.title("Weather Conditions")

    plt.tight_layout()
    plt.savefig("weather_dashboard.png", dpi=120, bbox_inches="tight")
    plt.show()

def main():
    # Get clean city input
    try:
        city = input(f"Enter city name (default: {DEFAULT_CITY}): ").strip()
    except:
        city = DEFAULT_CITY
    
    if not city:
        city = DEFAULT_CITY
    
    print(f"🌍 Fetching weather for: {city}")
    data = fetch_weather_data(city)
    
    if data:
        df = process_weather_data(data)
        print("\n✅ Sample data:")
        print(df.head(3))
        create_visualizations(df, city)
        print("\n📊 Dashboard saved as 'weather_dashboard.png'")

if __name__ == "__main__":
    main()