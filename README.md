# Hello K8s - FastAPI Microservice

🐳 A simple **FastAPI microservice** packaged with **Docker** and deployed on **Kubernetes**.  
This project is designed as a **practice setup** for learning K8s fundamentals like Deployments, Services, Probes, and (optionally) Ingress.

- REST API built with **FastAPI**
- Containerized with **Docker**
- Dependency management via **Pipenv**
- Kubernetes manifests for:
  - **Deployment** (with liveness/readiness probes)
  - **Service** (ClusterIP or LoadBalancer)

---

## 🚀 Getting Started

### 1️⃣ Local Development

```bash
pipenv install --dev
pipenv run fastapi dev api/main.py
```

### 2️⃣ Build & Run with Docker

```bash
docker build -t hello-k8s-api .
docker run -p 8000:8000 hello-k8s-api
```

### 3️⃣ Deploy on Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check pods

```bash
kubectl get pods
```
