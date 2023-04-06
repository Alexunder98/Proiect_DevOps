FROM python:3-alpine3.15

WORKDIR /app

COPY ./flask_app /app

RUN pip install -r requirments.txt

EXPOSE 5001

CMD python ./app.py
