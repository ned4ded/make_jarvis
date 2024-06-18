import wave
import struct
import os
from datetime import datetime

import pvporcupine
from pvrecorder import PvRecorder

from src.config import settings

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

try:
    is_writing = False
    wav_file = None

    while True:
        pcm = recorder.read()
        result = porcupine.process(pcm)

        if wav_file is not None and is_writing:
            wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))

        if result >= 0:
            print("[%s] Detected %s" % (str(datetime.now()), "Эй-Конь"))
            is_writing = not is_writing

            if is_writing:
                print("Enabling recorder")
                if os.path.exists(settings.output_path):
                    os.remove(settings.output_path)
                    print(f"The old file '{settings.output_path}' has been removed.")
                wav_file = wave.open(settings.output_path, "w")
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(16000)
            else:
                print("Disabling recorder")
                if wav_file is not None:
                    wav_file.close()

except KeyboardInterrupt:
    print("Stopping ...")
finally:
    recorder.delete()
    porcupine.delete()
    if wav_file is not None:
        wav_file.close()
