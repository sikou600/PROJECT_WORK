FROM python:3.11-slim
WORKDIR /app

COPY app/app.py .
RUN pip install flask
RUN pip install flask prometheus_client
EXPOSE 8080
CMD ["python","app.py"]