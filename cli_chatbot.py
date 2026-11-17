
import ollama

# 1. Select our local model
MODEL = "llama3.2:latest"

# 2. Store conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI assistant."
    }
]

print("================================")
print("       MY AI CHATBOT")
print("================================")
print("Type 'exit' to stop chatting.\n")

# 3. Start conversation
while True:

    user_input = input("You: ").strip()

    # 4. Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day!")
        break

    if not user_input:
        continue

    # 5. Add user message to history
    messages.append({
        "role": "user",
        "content": user_input
    })

    # 6. Get response from Ollama
    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    # 7. Extract AI response
    assistant_reply = response["message"]["content"]

    # 8. Display response
    print("\nBot:", assistant_reply)

    # 9. Save assistant response
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })