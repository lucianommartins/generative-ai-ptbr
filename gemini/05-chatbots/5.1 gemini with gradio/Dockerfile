
FROM python:3.8

EXPOSE 8080
WORKDIR /app

COPY . ./

EXPOSE 7860

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
