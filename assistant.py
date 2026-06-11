from ollama import chat

class Assistant:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are a friendly AI assistant."
                    "Respond naturally and clearly."
                ),
            }
        ]

    def ask(self, user_message):
        self.messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        response = chat(
            model="qwen3:latest",
            messages=self.messages,
        )

        assistant_reply = response["message"]["content"]

        self.messages.append(
            {
                "role": "assistant",
                "content": assistant_reply,
            }
        )

        return assistant_reply