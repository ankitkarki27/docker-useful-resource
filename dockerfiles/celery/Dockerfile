FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# cmd celery
# CMD ["celery -A core worker -l INFO"]  
CMD ["celery", "-A", "core", "worker", "-l", "INFO"]     