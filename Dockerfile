# Use the official Python slim image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose port 5000 for web traffic
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "app.py"]

