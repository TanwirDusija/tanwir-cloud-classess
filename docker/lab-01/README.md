# Docker Web Application

## Objective
Build and run a simple Python web application using Docker and Docker Compose.

## Technologies
- Python
- Docker
- Docker Compose
- Ubuntu

## Project Files
- app.py: Python web application
- Dockerfile: Instructions to build the image
- compose.yaml: Compose service configuration

## Build the Image
docker build -t tanwir-docker-web:v1 .

## Run with Docker Compose
docker compose up -d --build

## Verify the Application
Open http://localhost:8080

## View Logs
docker compose logs

## Stop and Remove Containers
docker compose down
