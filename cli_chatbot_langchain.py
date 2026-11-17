
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 1. Initialize the local LLM
llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.7
)

# 2. Store conversation history
messages = [
    SystemMessage(
        content="You are a helpful and friendly AI assistant."
    )
]

print("\n==============================")
print("    LANGCHAIN CLI CHATBOT")
print("==============================")
print("Type 'exit' to stop chatting.\n")

# 3. Start chatbot loop
while True:

    user_input = input("You: ").strip()

    # 4. Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day!")
        break

    if not user_input:
        continue

    # 5. Add user message
    messages.append(
        HumanMessage(content=user_input)
    )

    # 6. Get response from LangChain
    response = llm.invoke(messages)

    # 7. Extract AI response
    assistant_reply = response.content

    print("\nBot:", assistant_reply)

    # 8. Save AI response
    messages.append(
        AIMessage(content=assistant_reply)
    )
