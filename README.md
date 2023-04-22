[Whisper Python Docker]

https://github.com/openai/whisper


docker build -t whisper . --no-cache

docker run -v ~/whisper:/app -name whisper -d whisper

docker start whisper
