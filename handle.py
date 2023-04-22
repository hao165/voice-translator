import whisper
import time

model = whisper.load_model("medium")
result = model.transcribe("audio.ogg", fp16=False)
text = result["text"]

timestamp = int(time.time())
with open(f'{timestamp}.txt', 'w') as f:
    f.write(text)

print(text)
