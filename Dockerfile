FROM python:latest
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . app

# Define arguments that will be environment variables
ARG DATABASE_URL
ENV DATABASE_URL=${DATABASE_URL}

WORKDIR /app
EXPOSE 5000
CMD ["python", "run.py"]