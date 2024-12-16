import requests
import os
from dotenv import load_dotenv

load_dotenv()

def locate(location: str):
    params = {
        "text": location,
        "apiKey": os.getenv('GEO_API')
    }

    try:
        response = requests.get("https://api.geoapify.com/v1/geocode/search", params=params)
        data = response.json()

        if data["features"]:
            lat = data["features"][0]["geometry"]["coordinates"][1]
            lon = data["features"][0]["geometry"]["coordinates"][0]
            return {"lat": lat, "lon": lon}
        else:
            return None
    except requests.RequestException as e:
        print(f"Error type: {str(e)}")
        return None
            