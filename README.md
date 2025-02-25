# Funny Press: Web Service

## Overview
Funny Press is a project aimed at detecting humorous press article titles. This repository contains the code for a web service, built with Python and FastAPI, that evaluates whether a given article title is funny or not. It is part of the broader Funny Press project, which is still a work in progress, with ongoing improvements to the humor detection model.

## Requirements
- Docker

## Installation
For development purposes, a Docker image is available.

1. Build the Docker image:
   ```sh
   docker build -t funnypress-ws-dev -f Dockerfile.dev .
   ```

2. Run the web service in a Docker container:
   ```sh
   docker run --name funnypress-ws-dev -it --rm -p 8000:8000 -v $(pwd)/app:/app funnypress-ws-dev
   ```

## Usage
Once the web service is running, access it via `http://localhost:8000`.

- API documentation (Swagger UI) is available at:
  ```
  http://localhost:8000/docs
  ```
- Refer to the API documentation for details on how to evaluate article titles for humor.

