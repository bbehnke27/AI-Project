from audio.microphone import record_audio
from speech.transcriber import Transcriber
from brain.conversation import Conversation


def main():

    print("Starting voice AI...\n")

    transcriber = Transcriber()
    conversation = Conversation()

    print("\nVoice AI ready!")

    while True:

        input("\nPress ENTER to speak...")

        # Record
        audio = record_audio()

        # Speech → text
        print("Transcribing...")

        text = transcriber.transcribe(audio)

        if not text:
            print("I didn't hear anything.")
            continue

        print(f"\nYou: {text}")

        # Text → Qwen
        print("Thinking...")

        response = conversation.ask(text)

        print(f"\nAI: {response}")


if __name__ == "__main__":
    main()