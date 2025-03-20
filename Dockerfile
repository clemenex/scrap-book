# Use an official Python image as base
FROM python:3.10-slim  

# Set the working directory inside the container
WORKDIR /app  

# Copy the project files into the container
COPY . /app  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Command to run the scraper
CMD ["python", "book.py"]
