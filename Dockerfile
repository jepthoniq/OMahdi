FROM python:3.10-slim-buster
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git curl python3-pip ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/home/JoKeRUB/bin:$PATH"
CMD ["sh", "-c", "python3 ser.py & python3 -m JoKeRUB"]