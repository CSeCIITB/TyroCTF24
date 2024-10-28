FROM --platform=linux/amd64 python:3.9-slim
WORKDIR /app
COPY request_taker_5o5344534n.py /app/
RUN pip install flask flask_cors requests
EXPOSE 4000
CMD ["python", "request_taker_5o5344534n.py"]
