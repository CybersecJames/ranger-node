# Use Python 3 as the base image
FROM python:3.11-slim

# Install bash + tools
RUN apt-get update && apt-get install -y \
    bash curl vim less procps iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create data directory
RUN mkdir -p /app/data

# Copy local files into the container
COPY app.py .
COPY templates/ /app/templates/


# Install Flask
RUN pip install flask

# Run the app
CMD ["python", "app.py"]


