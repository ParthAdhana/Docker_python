FROM python:3.10

WORKDIR /app

COPY app/server.py .

EXPOSE 3000

CMD ["python","server.py"]