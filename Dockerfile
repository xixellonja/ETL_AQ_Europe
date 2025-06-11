# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Install pandas
RUN pip install pandas

# Create cleaned_data folder in container
RUN mkdir -p cleaned_data

# Set default command to run the ETL
CMD ["python", "etl.py"]