FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENV AUTHOR="kolyan"

ENTRYPOINT ["uvicorn", "echo_server:app", "--host", "127.0.0.1", "--port", "8000"]