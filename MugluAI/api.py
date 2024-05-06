import os
from together import Together

client = Together(api_key="7fe79da4173eb6a1e411721dc28bd22d8e6d50f9c236594a37041fbda8256907")

def query(message):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content

#store this resposne in a function to print 
#print(query("Hello"))


# content = file.read()

# response = client.chat.completions.create(
#     model="meta-llama/Llama-3-8b-chat-hf",
#     messages=[{"role": "user", "content": content}],
# )
#make a function to provide the contetnt from the other file


# print(response.choices[0].message.content)