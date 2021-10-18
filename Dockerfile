FROM python:3.9

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN pip3 install psycopg2
WORKDIR /app
ADD requirements.txt ./
RUN pip3 install -r requirements.txt
ADD /app ./
EXPOSE 5000
ENTRYPOINT python app.py