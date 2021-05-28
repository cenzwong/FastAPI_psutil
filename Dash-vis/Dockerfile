# docker build .
# docker run kjlahfkljsd -p 8050:80
# docker build -t cenzwong/dash-util-fastapi:latest .
# docker run -p 8087:80 -d cenzwong/dash-util-fastapi

FROM python:3.8-slim-buster

# WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app
WORKDIR /app
RUN chmod +x gunicorn.sh

ENTRYPOINT ["/app/gunicorn.sh"]

## docker run -p 8050:80 cenzwong/covidhk
## docker run -p 8899:80 cenzwong/covidhk
# gunicorn -w 2 -b 0.0.0.0:8050 main:server --chdir ./app
