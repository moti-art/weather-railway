`backend/README.md`
```markdown
# ⚙️ Weather Station - Core Backend API Microservice

This is the centralized business logic microservice. It exposes an upstream RESTful API that handles user parameters, establishes asynchronous downstream integration with the Analytics Tracker service, and proxies sanitized metrics directly from the **OpenWeatherMap external API**.

## 🔌 API Endpoints
* `GET /weather/<location_key>` - Fetches parsed, metric-unit JSON weather profiles (Temperature, Humidity, Wind Speed, Conditions).

## ⚙️ Requirements & Environment Variables
The application requires the following environment mappings to spin up:
* `PORT`: Internal listening port for Flask (Default: `5000`).
* `OPENWEATHER_API_KEY`: A valid authorization token from OpenWeatherMap.
* `TRACKER_URL`: Downstream analytic endpoint targeting the event tracker (Default: `http://localhost:5002/track`).

## 🛠️ Local Development (Standalone)
```bash
# Build the backend image
docker build -t motinet/weather-backend:dev .

# Run the API proxy container
docker run -d \
  -p 5000:5000 \
  -e PORT=5000 \
  -e OPENWEATHER_API_KEY="your_api_key_here" \
  -e TRACKER_URL="http://localhost:5002/track" \
  --name weather-api \
  motinet/weather-backend:dev