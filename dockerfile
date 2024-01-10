FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev mariadb-dev && \
pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]
