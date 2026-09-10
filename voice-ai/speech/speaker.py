import torch
import sounddevice as sd
import soundfile as sf
from qwen_tts import Qwen3TTSModel


class Speaker:

    def __init__(self):
        print("Loading Qwen3-TTS...")

        self.model = Qwen3TTSModel.from_pretrained(
            "Qwen/Qwen3-TTS-12Hz-0.6B-Base",
            device_map="cpu",
            dtype=torch.bfloat16,
        )

        print("Qwen3-TTS ready.")

    def speak(self, text):
        wavs, sample_rate = self.model.generate_voice_clone(
            text=text,
            language="English",
            ref_audio="blake.wav",
            ref_text="Hello. My name is Blake. I work at Audio-Technica. I am a test engineer for the product management team.",
        )
        sf.write("response.wav", wavs[0], sample_rate)
        
        sd.play(wavs[0], sample_rate)
        sd.wait()