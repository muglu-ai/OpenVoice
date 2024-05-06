# import streamlit as st
# import api as api

# def send_message():
#     global chat_text, entry  # Declare chat_text and entry as global to modify them inside the function
#     message = entry
#     # Display the user message in the chat window
#     chat_text += f"\nYou: {message}\n"
#     # Process the message and generate a response
#     response = generate_response(message)
#     # Display Muglu's response in the chat window
#     chat_text += f"Muglu: {response}\n\n"
#     # Clear the input field after sending the message
#     entry = ""

# def generate_response(message):
#     # Implement your logic to generate a response based on the message
#     # For example, you can use a machine learning model or predefined responses
#     return api.query(message)

# # Set the app title
# st.title("AI")

# # Create the chat window
# chat_text = st.text_area("Chat", height=200)

# # Create the input field
# entry = st.text_input("Enter message")

# # Create the send button
# send_button = st.button("Send", on_click=send_message)

# # Start the app
# st.run()

import streamlit as st

def send_message():
    # Implement your logic to generate a response based on the message
    message = entry
    response = generate_response(message)
    chat_text = f"{chat_text}\nUser: {message}\nMuglu: {response}\n"
    return chat_text

# Create the chat window
chat_text = st.text_area("Chat", value="", height=200)

# Create the input field
entry = st.text_input("Enter message")

# Create the send button
if st.button("Send"):
    chat_text = send_message()

st.text_area("Chat", value=chat_text, height=200)