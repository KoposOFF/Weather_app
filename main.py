from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import httpx
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Загрузка и обработка CSV-файла
file_path = 'cities.csv'
df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
cities = df[["Город", "Широта", "Долгота"]].dropna().to_dict(orient='records')

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    city_names = [city["Город"] for city in cities]
    return templates.TemplateResponse("index.html", {"request": request, "cities": city_names})

@app.post("/", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    city_data = next((item for item in cities if item["Город"].lower() == city.lower()), None)

    if city_data:
        lat = city_data["Широта"]
        lon = city_data["Долгота"]
    else:
        city_names = [city["Город"] for city in cities]
        return templates.TemplateResponse("index.html", {"request": request, "error": "Город не найден", "cities": city_names})

    API_URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "current_weather": True
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
        data = response.json()

    current_weather = data.get("current_weather", {})

    city_names = [city["Город"] for city in cities]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "city": city,
        "temperature": current_weather.get("temperature"),
        "wind_speed": current_weather.get("windspeed"),
        "weather_code": current_weather.get("weathercode"),
        "cities": city_names
    })