# Use the official Python image as a base image
FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y net-tools procps

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY backend /app/backend

# Copy the frontend HTML file into the container
COPY static/index.html /app/static/index.html
COPY tyroCTF{gr3at_g0in7g_ch8mp} /app/tyroCTF{gr3at_g0in7g_ch8mp}

# Copy the watchdog script
COPY watchdog.sh /app/watchdog.sh

# Make the script executable
RUN chmod +x /app/watchdog.sh

# Create logs directory and files
RUN mkdir -p /app && \
    touch /app/watchdog.log && \
    touch /app/uvicorn.log && \
    touch /app/user_input.log && \
    chmod 777 /app/*.log

ENV LOG_FILE_1=/app/user_input.log

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the watchdog script
CMD ["/bin/bash", "-c", "/app/watchdog.sh"]
