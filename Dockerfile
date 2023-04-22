FROM python:3.10-slim

WORKDIR /app

RUN apt-get update
RUN pip3 install -U openai-whisper
RUN apt-get install -y ffmpeg

VOLUME /app

CMD ["python","handle.py"]
