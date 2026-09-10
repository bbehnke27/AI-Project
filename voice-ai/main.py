from audio.microphone import record_audio
from speech.transcriber import Transcriber
from speech.speaker import Speaker
from brain.conversation import Conversation


def main():

    print("Starting voice AI...\n")

    transcriber = Transcriber()
    conversation = Conversation()
    speaker = Speaker()

    print("\nVoice AI ready!")

    while True:

        input("\nPress ENTER to speak...")

        # Record
        audio = record_audio()

        # Speech to text
        print("Transcribing...")

        text = transcriber.transcribe(audio)

        if not text:
            print("I didn't hear anything.")
            continue

        print(f"\nYou: {text}")

        # Text to Qwen
        print("Thinking...")

        response = conversation.ask(text)

        print(f"\nAI: {response}")

        # Text to speech
        print("Speaking...")

        speaker.speak(response)


if __name__ == "__main__":
    main()