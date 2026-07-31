# Flask + PostgreSQL Docker Deployment

## Overview

A containerized Flask application deployed on AWS EC2 using Docker Compose.
The application uses PostgreSQL as the database and Nginx as a reverse proxy.

## Architecture

User
 |
 v
Nginx (Port 80)
 |
 v
Flask Application (Port 5000)
 |
 v
PostgreSQL Database


## Technologies

- Python Flask
- PostgreSQL
- Docker
- Docker Compose
- Nginx
- AWS EC2
- GitHub Actions


## Run Locally

Clone repository:

git clone <repository-url>

Start application:

docker compose up --build


## Deployment

Application deployed on AWS EC2.

Docker containers:

- nginx-proxy
- flask-app
- postgres-db


## Troubleshooting

Resolved Docker build failures caused by insufficient EC2 EBS storage by expanding the root volume and resizing the filesystem.
