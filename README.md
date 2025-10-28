# DevOps Lab 4

![CI/CD Pipeline](https://github.com/USERNAME/REPO/actions/workflows/main.yml/badge.svg)
![Kubernetes Deploy](https://github.com/USERNAME/REPO/actions/workflows/k8s-deploy.yml/badge.svg)

## Features

- Click counter with persistent state (PostgreSQL)
- Multi-container setup with docker-compose
- Health checks for both services
- Production-ready with Gunicorn
- Multi-stage Docker build for optimized image size
- Volume persistence for database
- Network isolation between containers

## Endpoints

- `/` - Main application
- `/click` - POST endpoint to increment counter
- `/health` - Health check endpoint

## Architecture

- **Web Service**: Flask application with Gunicorn WSGI server
- **Database**: PostgreSQL 16 with Alpine Linux
- **Network**: Bridge network for inter-container communication
- **Volumes**: Persistent storage for PostgreSQL data

## Tech Stack

- Python 3.11
- Flask 3.0.0
- PostgreSQL 16
- psycopg2 (PostgreSQL adapter)
- Gunicorn (WSGI server)
- Docker multi-stage build
- Docker Compose
- Kubernetes manifests with auto-scaling
- GitHub Actions CI/CD with K8s deployment
- Automated rollback on failure