FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 as base
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app/data /data
COPY ./app /app
ENV PYTHONPATH /app/app

FROM base as test
COPY ./requirements-test.txt /requirements-test.txt
RUN pip install -r /requirements-test.txt

FROM base as loadtest
COPY ./requirements-loadtest.txt /requirements-loadtest.txt
RUN pip install -r /requirements-loadtest.txt
