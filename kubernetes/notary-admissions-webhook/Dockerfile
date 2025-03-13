
# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY admission-webhook.py .

# Install required dependencies
RUN pip install flask

# Expose the webhook port
EXPOSE 8080

# Run the webhook
CMD ["python", "admission-webhook.py"]
