DevOps Project 03 – Dockerized Microservices (React + FastAPI + MongoDB)

📌 Overview

This third project in my DevOps Project Series evolves a monolith into a multi-service setup. It runs a React frontend, a Python FastAPI backend, and MongoDB, all orchestrated with Docker Compose. It demonstrates service isolation, persistent storage, and CI/CD with Jenkins.

| Component        | Technology               |
| ---------------- | ------------------------ |
| Frontend         | React                    |
| Backend API      | Python (FastAPI)         |
| Database         | MongoDB                  |
| Containerization | Docker, Docker Compose   |
| CI/CD            | Jenkins + GitHub Webhook |
| Version Control  | GitHub                   |

🔧 Services & Ports

- Frontend (React, served via `serve`): http://localhost:3000
- Backend (FastAPI via `uvicorn`): http://localhost:8000 (Swagger UI at `/docs`)
- MongoDB: container-only (no host port exposed), persistent volume `mongo_data`

🧩 Data & Networking

- MongoDB connection string used by backend: `mongodb://mongodb:27017/<database>`
- Internal Docker network: `app-network` (services resolve by name, e.g., `backend`, `mongodb`)
- Data persistence: volume `mongo_data` mounted to `/data/db` in the `mongo` container

⚙️ Environment Variables

The backend expects the environment variable `MONGODB_URL`.

Example value for local Compose networking:

```
MONGODB_URL=mongodb://mongodb:27017/task_management
```

Note: Ensure your Compose file sets `MONGODB_URL` (not `MONGO_URL`) for the backend service so the application connects correctly.

🚀 Quick Start

```
# Build and run all services (detached)
docker compose up -d --build

# View logs for a specific service
docker compose logs -f backend

# Stop and remove containers, networks, volumes (named volumes persist by default)
docker compose down
```

Once running:

- Frontend: `http://localhost:3000`
- API root: `http://localhost:8000/`
- API docs: `http://localhost:8000/docs`

🧪 CI/CD (Jenkins)

- GitHub webhook triggers the Jenkins pipeline on push
- Lints/tests for React and Python
- Builds Docker images and can push to a registry (Docker Hub)
- Deploys with `docker compose` on the target environment

To push images manually, tag and push according to your registry naming (example):

```
# Example only — replace with your registry/name:tag
docker compose build
docker tag devops-project-03-frontend:latest <dockerhub-username>/react-frontend:v1
docker tag devops-project-03-backend:latest <dockerhub-username>/python-backend:v1
docker push <dockerhub-username>/react-frontend:v1
docker push <dockerhub-username>/python-backend:v1
```

📈 What You’ll Learn

- Multi-container orchestration with Docker Compose
- Service isolation with Docker networking
- Persistent storage for stateful services (MongoDB)
- CI/CD integration with Jenkins + GitHub Webhooks
- Preparing multi-service apps for production-ready deployment

🧭 Next Steps

- Project 4: Advanced Docker – Private Registry, Image Scanning (Trivy), Optimized CI/CD
- Project 5: Kubernetes deployment with Helm + ArgoCD

👤 Author

Mahendravarma

💻 DevOps Engineer | Jenkins | Docker | Kubernetes | CI/CD | Cloud

🔗 Related Projects

- Project 1 – Monolithic Next.js App with Jenkins CI https://github.com/iam-mahendravarma/Devops-Project-01-Monolithic.git
- Project 2 – Dockerized Monolithic Next.js App https://github.com/iam-mahendravarma/Devops-Project-02-Dockerized-Monolithic.git

🏷️ Tags

#DevOpsEngineer #DockerCompose #MultiServiceArchitecture #React #Python #MongoDB #JenkinsPipeline #DockerHub #CI_CD #DevOpsProjects #LearningInPublic #TechPortfolio
