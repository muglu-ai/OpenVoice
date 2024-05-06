import streamlit as st
from together import Together
import json
import os


# Initialize Together client
client = Together(api_key="7fe79da4173eb6a1e411721dc28bd22d8e6d50f9c236594a37041fbda8256907")

def query(message):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": message}],
    )
    #store the response in a json file
    with open("response.json", "w") as f:
        f.write(response.choices[0].message.content)

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
    
    #remember the response and store it in a variable
    st.session_state.last_response = response
    # Display model response
    st.write("Muglu:", response)


#display the last response
if "last_response" in st.session_state:
    st.write("Muglu:", st.session_state.last_response)




# Add a background image to this page
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://source.unsplash.com/1600x900/?coffee");
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
