from faster_whisper import WhisperModel


class Transcriber:

    def __init__(self):
        print("Loading Whisper...")

        self.model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper ready.")

    def transcribe(self, audio):
       
        audio = audio.flatten()

        segments, info = self.model.transcribe(audio)

        text = "".join(segment.text for segment in segments).strip()

        return text