# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port on which the app will run
EXPOSE 8000

# Command to run the FastAPI app with your custom command
# CMD ["fastapi", "dev", "main.py"]
CMD ["uvicorn", "main:app", "--reload", "--port=8000", "--host=0.0.0.0"]