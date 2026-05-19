# 🌤️ Weather Station - Multi-Service Microservices Architecture

This repository contains a fully containerized, production-ready microservices application built with Python (Flask) and optimized for high performance, low footprint, and secure inner-network communication.

This project serves as a comprehensive DevOps portfolio showcase, demonstrating two core implementation patterns:
1. **Rapid Cloud Deployment & Service Discovery** via **Railway**.
2. **Enterprise GitOps & Automated CI/CD Pipelines** via **GitHub Actions**, **Docker Hub**, and **Helm Charts** (targeted for AWS Kubernetes/ArgoCD infrastructure).

---

## 🏗️ Architecture & Component Overview

The application is decomposed into three decoupled microservices and a high-speed caching layer:

1. **Frontend UI (`/frontend`)**: A modern web interface built with Flask, styled using state-of-the-art **Glassmorphism (Dark Mode)** and FontAwesome metrics visualization.
2. **Weather Backend API (`/backend`)**: A RESTful API that handles business logic, sanitizes user queries, fetches real-time telemetry from the OpenWeatherMap API, and asynchronously updates the tracking system.
3. **Weather Tracker (`/tracker`)**: An event-driven analytics engine running under a production-grade **Gunicorn** server that ingests search metrics.
4. **Redis Cache / Database**: An in-memory data structure store used by the Tracker to maintain lightning-fast atomic counters for searched locations.

---

## 🚀 Enterprise CI/CD & GitOps Workflow

The repository is equipped with an automated, context-aware **GitHub Actions Pipeline** (`.github/workflows/ci-cd.yml`) executing a true GitOps lifecycle:

```text
       [ Developer Push to main/dev branch ]
                        │
                        ▼
       ┌─────────────────────────────────┐
       │     GitHub Actions Runner       │
       ├─────────────────────────────────┤
       │ 1. Evaluates changed folders    │
       │ 2. Compiles multi-stage Docker  │
       │ 3. Pushes tags to Docker Hub    │
       └────────────────┬────────────────┘
                        │
                        ▼
       ┌─────────────────────────────────┐
       │   Automated Manifest Update     │
       ├─────────────────────────────────┤
       │ Clones deployment Helm Repo &   │
       │ updates image tags dynamically  │
       └─────────────────────────────────┘

       Targeted Builds: The pipeline utilizes git differential analysis to build and push images only for the specific microservices containing code modifications.

Image Registry: Builds are securely shipped to Docker Hub under motinet/<service-name>.

State Synchronization: Upon a successful build, the pipeline automatically clones the central infrastructure repository (moti-art/weather-gitops), updates environment-specific values (values-dev.yaml or values-prod.yaml), and commits back, triggering ArgoCD reconciliations on the Kubernetes side.

☁️ Production Cloud Environment (Railway)
For live monitoring and validation, the services are orchestrated on Railway leveraging cloud-native configurations:

Service Discovery: Internal communications bypass public networks entirely using secure DNS routing (http://weather-backend.railway.internal:5000).

Environment Variables: Managed securely through injecting credentials (OPENWEATHER_API_KEY, BACKEND_URL, TRACKER_URL) dynamically without hardcoding values.

💻 Local Development & Infrastructure Replication
To replicate the entire microservices mesh locally with configurations identical to production, ensure Docker Desktop is running and execute:

Bash
# 1. Provide your live OpenWeatherMap API Token
export OPENWEATHER_API_KEY="your_secret_api_key_here"

# 2. Boot the entire stack in detached mode
docker compose up --build -d
🎛️ Local Port Mappings:
Frontend Dashboard UI: http://localhost:5001

Weather Core Backend API: http://localhost:5000

Analytics Tracker Service: http://localhost:5002

Developed with 💻 and ☕ by Moti Levi - Cloud Infrastructure & DevOps Specialist.