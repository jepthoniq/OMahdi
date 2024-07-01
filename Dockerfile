FROM python:3.10-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN python3 -m pip install --upgrade pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN npm i -g npm@8.19.4
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV PATH="/home/JoKeRUB/bin:$PATH"
CMD python3 ser.py & python3 -m JoKeRUB