from ollama import chat
from memory import Memory

memory = Memory()

print("AI Assistant Started \n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    # Load memory (last 5 chats)
    past = memory.load_recent()

    messages = [
        {"role": "system", "content": "You are a friendly AI assistant with memory."}
    ]

    # Add past memory
    for u, a in reversed(past):
        messages.append({"role": "user", "content": u})
        messages.append({"role": "assistant", "content": a})

    messages.append({"role": "user", "content": user})

    response = chat(
        model="qwen3:latest",
        messages=messages
    )

    reply = response["message"]["content"]

    print("SUSA:", reply)

    # Save memory
    memory.save(user, reply)