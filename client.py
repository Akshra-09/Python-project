# from openai import OpenAI
#
# print(completion.choices[0].message.content)

# import os
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ]
)

print(response["message"]["content"])
# import os

# api_key = os.getenv("OPENAI_API_KEY")
