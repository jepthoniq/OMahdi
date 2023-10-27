FROM python:3.9.7-slim-buster
# Install requirements
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm@8.19.4
RUN pip3 install -U -r requirements.txt
CMD python3 ser.py & python3 -m JoKeRUB
