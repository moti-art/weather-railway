# 🖥️ Weather Station - Frontend UI Microservice

This is the user-facing web interface for the Weather Station application. Built with **Python (Flask)**, it serves a highly optimized, responsive **Dark Mode (Glassmorphism)** dashboard that visualizes real-time weather metrics fetched from the Backend API.

## ⚙️ Requirements & Environment Variables
The application expects the following runtime configuration:
* `PORT`: The internal port for the Flask server to listen on (Default: `5001`).
* `BACKEND_URL`: The fully qualified endpoint or DNS name of the Weather Backend microservice (Default: `http://localhost:5000`).

## 🛠️ Local Development (Standalone)
To build and run this specific microservice manually without orchestrators:

```bash
# Build the localized image
docker build -t motinet/weather-frontend:dev .

# Run the container with custom backend binding
docker run -d \
  -p 5001:5001 \
  -e PORT=5001 \
  -e BACKEND_URL="http://localhost:5000" \
  --name weather-ui \
  motinet/weather-frontend:dev