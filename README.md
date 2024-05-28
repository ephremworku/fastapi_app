# Asgi FastAPI Application with NGINX Reverse Proxy

## Overview
This project is a demonstration of a FastAPI application running behind an NGINX reverse proxy. The FastAPI application serves a simple RESTful API, and NGINX acts as a reverse proxy to forward requests to the FastAPI application.

## Architecture
This project is constructed by using a clean architecture and the folder structure will have the following structures:

fastapi_app/
├── app/                   # Main application directory  
│   ├── __init__.py        # Initialize the application package  
│   ├── main.py            # Entry point for the FastAPI application  
│   ├── api/               # Directory for API endpoints  
│   │   ├── __init__.py    # Initialize the API package  
│   │   ├── v1/            # API versioning directory  
│   │   │   ├── __init__.py    # Initialize version 1 package  
│   │   │   └── endpoints.py   # API endpoints for version 1  
│   ├── core/              # Core application functionality  
│   │   ├── __init__.py    # Initialize the core package  
│   │   ├── config.py      # Configuration settings  
│   │   └── database.py    # Database connection setup  
│   ├── models/            # Data models  
│   │   ├── __init__.py    # Initialize the models package  
│   │   └── user.py        # User data model  
│   ├── schemas/           # Pydantic schemas for request/response validation  
│   │   ├── __init__.py    # Initialize the schemas package  
│   │   └── user.py        # User Pydantic schema  
│   ├── services/          # Business logic services  
│   │   ├── __init__.py    # Initialize the services package  
│   │   └── user_service.py   # User service logic  
│   └── repositories/      # Data access layer  
│       ├── __init__.py    # Initialize the repositories package  
│       └── user_repository.py   # User repository for database interactions  
├── static/                # Static files directory  
│   └── index.html         # HTML file for the frontend  
└── requirements.txt       # Python dependencies  


The architecture consists of the following components:
- **FastAPI Application**: A Python web application built using the FastAPI framework. It includes endpoints for handling HTTP requests, as well as models, services, and dependencies.
- **NGINX**: A high-performance web server and reverse proxy server that forwards HTTP requests to the FastAPI application.

## Setup Instructions
### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the project repository:  
   ```sh
   git clone https://github.com/ephremworku/fastapi_app.git
    ``` 

3. Configuration

No additional configuration is required. However, you may customize the NGINX configuration if needed.
Running the Application

3. Build Docker images:

```sh
docker-compose build
```
Start Docker containers:
```sh
docker-compose up -d
```
4. to submit the form

```sh
http://localhost/register
```
by going the above link you can submit a form
