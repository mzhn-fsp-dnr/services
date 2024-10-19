FROM python:3.12-alpine3.20

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
# RUN apk update && apk add --no-cache \
#     gcc \
#     g++ \
#     make \
#     libffi-dev \
#     openssl-dev \
#     musl-dev 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ARG APP_PORT

CMD uvicorn src.main:app --host 0.0.0.0 --port $APP_PORT