FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN flask db upgrade

CMD gunicorn 'app:create_app()'