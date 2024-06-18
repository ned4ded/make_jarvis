import whisper

print("Loading whisper...")
w_model = whisper.load_model("large")
print("Whisper is loaded.")


def transcribe(audio_np):
    return w_model.transcribe(audio_np)
