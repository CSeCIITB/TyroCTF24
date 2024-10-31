FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py flag.txt ./
COPY templates ./templates
COPY static ./static
USER nobody
EXPOSE 8000
CMD ["gunicorn", "-w8", "-t5", "--graceful-timeout", "0", "-b0.0.0.0", "app:app"]
