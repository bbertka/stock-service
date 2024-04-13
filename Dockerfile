# Use a smaller, more optimized base image for Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Define a build-time argument for the software version
ARG SOFTWARE_VERSION=latest

# Set it as an environment variable that the Flask app can access
ENV SOFTWARE_VERSION=$SOFTWARE_VERSION

# Copy only the requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies in a single layer and clean up in the same layer
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application files into the container
COPY src/ .

# Expose the port that the Flask application runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]