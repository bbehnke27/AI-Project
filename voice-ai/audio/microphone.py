import sounddevice as sd


SAMPLE_RATE = 16000


def record_audio(duration=5):
    print("Listening...")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    print("Finished listening.")

    return audio