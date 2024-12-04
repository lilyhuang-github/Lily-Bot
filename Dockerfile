FROM python:3.11

WORKDIR /lbot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 5100

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5100"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["python", "app.py"]
