import ollama
message=[{
    "role": "system",
    "content": "tell me about Dr RAjkumar kannada industry"
},
{


    "role": "user",
    "content": "tell me about AI"
}]

modelname="llama3.2:latest"
response = ollama.chat(
    model=modelname,
    messages=message
)
print(response["message"]["content"])