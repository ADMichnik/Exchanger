# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Add empty environmental variable
ENV API_KEY=""

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Docker
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

# Copy the application code
COPY . .

# Set the command to run the application
CMD ["python", "main.py", "-a", "1000", "-b", "USD", "-t", "PLN"]
