import whisper

model = whisper.load_model("small")

result = model.transcribe(
    "How GOOD was Brock Lesnar Actually.m4a"
)

print(result["text"])

with open("transcription.txt", "w", encoding="utf-8") as file:
    file.write(result["text"])

print("Saved to transcription.txt")