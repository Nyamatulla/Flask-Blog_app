# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory to /app
WORKDIR /flask-app

# Copy the current directory contents into the container at /app
COPY . /flask-app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "flask-app/run.py"]
