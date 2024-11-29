# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose port 5000 (or any other port if needed, update based on your app's requirements)
EXPOSE 5000

# Command to run the application
CMD ["python", "crypto.py"]

