import tkinter as tk
import os
import json
import api as api

def send_message():
    message = entry.get()
    # Process the message and generate a response
    response = generate_response(message)
    # Display the response in the chat window
    chat_text.insert(tk.END, f"You: {message}\n")
    chat_text.insert(tk.END, f"Muglu: {response}\n")
    # Clear the input field
    entry.delete(0, tk.END)

def generate_response(message):
    # Check local storage for responses
    response = check_local_storage(message)
    if response:
        return response
    else:
        # If response not found locally, query the API
        return api_query(message)

def check_local_storage(query):
    # Load stored responses from a JSON file
    responses = load_responses("responses.json")
    # Check if the query exists in the responses
    if query.lower() in responses:
        return responses[query.lower()]
    else:
        return None

def load_responses(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {}

def api_query(query2):
    # Call your API function here
    # For demonstration purposes, simply return a placeholder response
    response = api.query(query2)
    chat_text.insert(tk.END, f"Muglu: {response}\n")
    return response


# Create the main window
window = tk.Tk()
window.title("Muglu AI")

# Create the chat window
chat_text = tk.Text(window, width=50, height=20)
chat_text.pack()

# Create the input field
entry = tk.Entry(window, width=50)
entry.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start the main loop
window.mainloop()
