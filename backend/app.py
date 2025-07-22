from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from weather_api import get_weather

app = FastAPI()

# Allow frontend access (from any domain for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "WeatherWhiz API is running 🚀"}

@app.get("/weather")
def weather(city: str):
    result = get_weather(city)
    return result