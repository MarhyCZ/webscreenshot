# syntax=docker/dockerfile:1
FROM python:3-alpine
WORKDIR /
RUN apk add --no-cache gcc libffi-dev musl-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "./main.py"]