FROM python:3.10 

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
