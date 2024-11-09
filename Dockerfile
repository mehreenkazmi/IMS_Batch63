# Dockerfile

# Base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . /app/

# Command to run the main application
CMD ["python", "main.py"]