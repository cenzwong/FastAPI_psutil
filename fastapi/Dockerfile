  
# docker build . -t cenzwong/sutil-fastapi:latest
# docker push cenzwong/fastapi-helloworld:latest
# docker run cenzwong/sutil-fastapi:latest -p 80:80

# set base image (host OS)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app
