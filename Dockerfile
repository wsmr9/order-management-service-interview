FROM python:3.8
# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY . .

# Define arguments that will be environment variables
ARG DATABASE_URL
ENV DATABASE_URL=${DATABASE_URL}

# Command to run the application
CMD ["python", "run.py"]
