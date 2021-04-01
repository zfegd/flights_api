FROM python:3.7
RUN pip install fastapi uvicorn
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
EXPOSE 80
COPY ./app/data /data
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
