#!/bin/bash
set -e

# Build the coreapp image
podman build -t coreapp ./coreapp

# Run the coreapp container
podman run -dit \
  --name coreapp \
  --network appnet \
  --replace \
  -p 5000:5000 \
  coreapp

