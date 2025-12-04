FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port  (match the port Gunicorn will use)   
EXPOSE 8004

# Run Gunicorn with binding to all interfaces and a port
CMD ["gunicorn", "core.wsgi:application"]    