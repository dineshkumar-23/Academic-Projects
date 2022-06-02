FROM python:3.8-slim-buster

COPY ./Voice-search ./speechrec

WORKDIR /speechrec

RUN pip3 install -r requirements.txt

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc libsndfile1 

#ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["python", "app.py"]