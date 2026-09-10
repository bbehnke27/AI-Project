import requests


class Conversation:

    def __init__(self):
        self.url = "http://localhost:11434/api/chat"
        self.model = "qwen3:8b"

        self.messages = []

    def ask(self, text):

        self.messages.append({
            "role": "user",
            "content": text
        })

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "messages": self.messages,
                "stream": False
            }
        )

        if not response.ok:
            print("Ollama error:")
            print(response.text)

        response.raise_for_status()

        data = response.json()

        reply = data["message"]["content"]

        self.messages.append({
            "role": "assistant",
            "content": reply
        })

        return reply