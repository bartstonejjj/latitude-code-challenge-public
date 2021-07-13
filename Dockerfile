FROM python:3.6-alpine

COPY . .

CMD ["python", "docker_run.py"]