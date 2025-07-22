async function getWeather() {
  const city = document.getElementById("cityInput").value;
  const result = document.getElementById("weatherResult");

  if (!city) {
    result.textContent = "Please enter a city name.";
    return;
  }

  try {
    const response = await fetch(`http://127.0.0.1:8000/weather?city=${city}`);
    const data = await response.json();
    result.textContent = data;
  } catch (error) {
    result.textContent = "Error fetching weather data.";
    console.error(error);
  }
}
