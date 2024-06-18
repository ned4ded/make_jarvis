import struct
from datetime import datetime
import numpy as np
import os

import whisper
import pvporcupine
from pvrecorder import PvRecorder

from src.config import settings
from src.agent.llm import ask

print("Loading whisper...")
w_model = whisper.load_model("large")
print("Whisper is loaded.")

try:
    porcupine = pvporcupine.create(
        access_key=settings.picovoice_access_key,
        keyword_paths=["models/Эй-Конь_ru_mac_v3_0_0.ppn"],
        model_path="models/porcupine_params_ru.pv",
    )
except pvporcupine.PorcupineInvalidArgumentError as e:
    print("One or more arguments provided to Porcupine is invalid: ")
    print(e)
    raise e
except pvporcupine.PorcupineActivationError as e:
    print("AccessKey activation error")
    raise e
except pvporcupine.PorcupineActivationLimitError as e:
    print(
        "AccessKey '%s' has reached it's temporary device limit"
        % settings.picovoice_access_key
    )
    raise e
except pvporcupine.PorcupineActivationRefusedError as e:
    print("AccessKey '%s' refused" % settings.picovoice_access_key)
    raise e
except pvporcupine.PorcupineActivationThrottledError as e:
    print("AccessKey '%s' has been throttled" % settings.picovoice_access_key)
    raise e
except pvporcupine.PorcupineError as e:
    print("Failed to initialize Porcupine")
    raise e

for i, device in enumerate(PvRecorder.get_available_devices()):
    print("Device %d: %s" % (i, device))

recorder = PvRecorder(frame_length=porcupine.frame_length, device_index=0)
recorder.start()


print("Listening ... (press Ctrl+C to exit)")


def say(t: str):
    os.system(f"say {t}")


try:
    is_writing = False
    wav_file = None
    audio_data = bytearray(b"")

    while True:
        pcm = recorder.read()
        result = porcupine.process(pcm)

        if is_writing:
            audio_data.extend(struct.pack("h" * len(pcm), *pcm))

        if result >= 0:
            print("[%s] Detected %s" % (str(datetime.now()), "Эй-Конь"))
            is_writing = not is_writing

            if is_writing:
                print("Enabling recorder")
            else:
                print("Disabling recorder")
                print("Transcribing...")
                audio_np = (
                    np.frombuffer(audio_data, dtype=np.int16).astype(np.float32)
                    / 32768.0
                )
                result = w_model.transcribe(audio_np)
                print("Asking LLM...")
                answer = ask(result["text"])
                print(answer)
                say(answer)
                audio_data = bytearray(b"")
                print("End")

except KeyboardInterrupt:
    print("Stopping ...")
finally:
    recorder.delete()
    porcupine.delete()
