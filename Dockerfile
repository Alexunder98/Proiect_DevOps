FROM python:3-alpine3.15

WORKDIR /app

COPY ./flask_app /app

RUN pip install -r requirments.txt

EXPOSE 80

CMD python ./app.py
