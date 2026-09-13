# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Prevent Python from generating .pyc files and force real-time logging.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /app

# Copy and install dependencies leveraging Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and tests
COPY ./app ./app
COPY ./tests ./tests

# Expose the standard FastAPI port
EXPOSE 8000

# Command to start Uvicorn listening for requests
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]