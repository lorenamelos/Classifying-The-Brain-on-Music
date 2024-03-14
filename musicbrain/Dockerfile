FROM python:3.11.8-slim-bullseye

COPY musicbrain /musicbrain

COPY requirements_backend.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn musicbrain.api.fast:app --host 0.0.0.0