FROM python:latest
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . app
WORKDIR /app
EXPOSE 5000
CMD ["python", "run.py"]