# FastAPI Application with NGINX Reverse Proxy

## Overview
This project is a demonstration of a FastAPI application running behind an NGINX reverse proxy. The FastAPI application serves a simple RESTful API, and NGINX acts as a reverse proxy to forward requests to the FastAPI application.

## Architecture
The architecture consists of the following components:
- **FastAPI Application**: A Python web application built using the FastAPI framework. It includes endpoints for handling HTTP requests, as well as models, services, and dependencies.
- **NGINX**: A high-performance web server and reverse proxy server that forwards HTTP requests to the FastAPI application.

## Setup Instructions
### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the project repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-nginx-reverse-proxy.git
   cd fastapi-nginx-reverse-proxy
