
import ollama

response = ollama.generate(
    model="llama3.2:latest",
    prompt="tell me about dr ambedkar institute of technology banglore."
)

print(response.text)
