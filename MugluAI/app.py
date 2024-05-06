import streamlit as st
from together import Together
import json

# Initialize Together client
client = Together(api_key="7fe79da4173eb6a1e411721dc28bd22d8e6d50f9c236594a37041fbda8256907")

def query(message):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content

# Set page title
st.set_page_config(page_title="Muglu AI", page_icon="🧠")

# Streamlit UI
st.title("Muglu AI")

# Text input for user to type messages
message = st.text_input("You:", "")

if st.button("Send"):
    # Display user message
    st.write("You:", message)
    
    # Get response from the model
    response = query(message)

    #copy code to file
    response_dict = {"response": response}

    # Extract code block content
    code_block_start = response_dict['response'].find("```") + 3
    code_block_end = response_dict['response'].find("```", code_block_start)
    code_block_content = response_dict['response'][code_block_start:code_block_end]

    # Write code block content to a Python file
    with open("code.py", "w") as f:
        f.write(code_block_content)
    
    # Store the response in a JSON file
    with open("response.json", "w") as f:
        json.dump({"response": response}, f)
    
    

    
    # Display model response
    st.write("Muglu:", response)

# Display the last response
if st.button("Display Last Response"):
    try:
        with open("response.json", "r") as f:
            last_response = json.load(f)["response"]
            st.write("Last Response:", last_response)
    except FileNotFoundError:
        st.write("No response recorded yet.")
