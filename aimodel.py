import whisper

model = whisper.load_model("small")


def vv():
    result = model.transcribe(
        "voice.ogg"
    )

    return result["text"]

# print(result["text"])

# with open("transcription.txt", "w", encoding="utf-8") as file:
#     file.write(result["text"])

# print("Saved to transcription.txt")