
# 🌤️ Weather Dashboard - Multi-Service Microservices Architecture (Railway Edition)

This repository contains a containerized, production-ready microservices application designed for high performance, high availability, and low memory consumption. 

Originally architected for AWS (EKS, Terraform, ArgoCD, Helm), this version was optimized and deployed on **Railway** using modern DevOps practices to eliminate hardware bottlenecks and leverage native Cloud GitOps.

---

## 🏗️ Architecture Overview

The system consists of three independent microservices and a managed caching layer:

1. **Frontend UI (Flask)**: A web interface allowing users to select cities and view live weather statistics.
2. **Weather Backend (Flask API)**: Fetches live weather metrics via OpenWeatherMap API and triggers tracking events.
3. **Weather Tracker (Gunicorn/Flask)**: An event-driven analytics service that records search history.
4. **Redis Cache**: A high-performance, in-memory data store managing search counters.

---

## 🚀 Native GitOps Workflow on Railway

Instead of managing heavy infrastructure overhead (like ArgoCD/EKS control planes on limited hardware), this deployment utilizes **Railway's Native Orchestrator**:
* **Automatic Builds**: Every `git push` triggers an automatic multi-stage Docker build based on directory context.
* **Environment Isolation**: Configured with dynamic, isolated environments (`development` vs `production`) mapped to specific GitHub branches.
* **Service Discovery**: Microservices communicate internally using Railway's secure private networking protocol (`*.railway.internal`).

---

## 💻 Local Development & Testing

To test the entire architecture locally using a configuration identical to production, run:

```bash
# 1. Export your API Key
export OPENWEATHER_API_KEY="your_api_key_here"

# 2. Spin up the cluster locally
docker compose up --build -d

Port Mappings (Local):
Frontend UI: http://localhost:8081

Backend API: http://localhost:8080

Tracker Service: http://localhost:8082

Developed by Moti Levi - DevOps & Cloud Infrastructure Project.