# Use the official Python image as a base image
FROM python:3.9-slim
# Set the working directory inside the container
WORKDIR /app
# Copy the Python quiz app files into the container
COPY . /app
# Install Flask
RUN pip install Flask
# Expose port 5000 for web traffic
EXPOSE 5000
# Run the Flask app when the container starts
CMD ["python", "app.py"]
