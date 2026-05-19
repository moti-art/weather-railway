`tracker/README.md`
```markdown
# 📊 Weather Station - Analytics Tracker Service

This is an isolated, high-performance tracking and ingestion microservice. Built with Flask and served using an enterprise-grade **Gunicorn WSGI server**, it records asynchronous state changes (search inquiries) and stores atomic operational counters into a **Redis caching database**.

## 🔌 API Endpoints
* `POST /track` - Ingests JSON payload tracking events `{"city": "CityName"}`.
* `GET /stats` - Aggregates and yields complete historical location search frequency data.

## ⚙️ Requirements & Environment Variables
* `PORT`: Internal listening port for Gunicorn (Default: `5002`).
* `REDIS_URL`: The operational network connection string linking to the Redis database (Default: `redis://localhost:6379`).

## 🛠️ Local Development (Standalone)
```bash
# Build the tracker engine
docker build -t motinet/weather-tracker:dev .

# Run the container connected to a local Redis instance
docker run -d \
  -p 5002:5002 \
  -e PORT=5002 \
  -e REDIS_URL="redis://host.docker.internal:6379" \
  --name weather-tracker \
  motinet/weather-tracker:dev