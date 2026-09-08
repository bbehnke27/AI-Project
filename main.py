import requests

MODEL = "qwen3:8b"

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        break

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "think" : False,
            "stream": False
        }
    )

    data = response.json()

    print("AI:", data["message"]["content"])