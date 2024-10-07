#!/bin/bash

# Build the docker container image
docker build -t excel_ai .

# Run the Docker container with the image excel_ai
docker run -d -p 8000:8000 excel_ai

# Check if the container is running
if [ $? -eq 0 ]; then
    echo "Docker container for excel_ai is running on port 8000."
else
    echo "Failed to start the Docker container for excel_ai."
fi