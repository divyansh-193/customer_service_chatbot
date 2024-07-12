import streamlit as st
import pandas as pd
import ollama

# Load the CSV data
data = pd.read_csv('prepared_data.csv')

# Prepare training data from CSV
training_data = []
for index, row in data.iterrows():
    training_data.append({'role': 'user', 'content': row['input']})
    training_data.append({'role': 'assistant', 'content': row['response']})

st.write("Training data prepared.")

# Streamlit UI
st.title("Customer Service Chatbot")

# Initialize the session state if not already done
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to display the chatbox
def display_chatbox():
    chat_history = ""
    for message in st.session_state.messages:
        if message['role'] == 'user':
            chat_history += f"<div style='text-align: right; color: blue;'>{message['content']}</div><br>"
        else:
            chat_history += f"<div style='text-align: left; color: green;'>{message['content']}</div><br>"
    st.markdown(f"<div style='height: 400px; overflow-y: auto; padding: 10px; border: 1px solid #ccc; border-radius: 5px;'>{chat_history}</div>", unsafe_allow_html=True)

# User input form
with st.form(key='user_input_form', clear_on_submit=True):
    user_input = st.text_input("Enter your prompt (or type 'exit' to quit):")
    submit_button = st.form_submit_button(label='Send')

    if submit_button:
        if user_input.lower() == 'exit':
            st.write("Exiting the chat.")
        else:
            pre_prompt = "Assume you are a customer service executive, you are professional, humble, and fun to talk to. You can clearly explain complex things in simple language. It's effortless for customers to get their queries sorted as you provide precise on-point responses. Customer is saying: "
            final_prompt = pre_prompt + user_input

            # Add user message to the messages list
            st.session_state.messages.append({'role': 'user', 'content': user_input})

            # Display "Waiting for response..." message
            st.session_state.messages.append({'role': 'assistant', 'content': 'Waiting for response...'})
            display_chatbox()
            st.session_state.messages.pop()

            # Create a list of messages for the chat request
            chat_messages = [{'role': 'user', 'content': pre_prompt}]
            chat_messages.extend(st.session_state.messages)

            stream = ollama.chat(
                model='llama3',
                messages=chat_messages,
                stream=True,
            )

            response = ""
            for chunk in stream:
                response += chunk['message']['content']

            # Add bot response to the messages list
            st.session_state.messages.append({'role': 'assistant', 'content': response})

            # Refresh the chatbox to display the new message
            st.experimental_rerun()

# Display the chatbox again to ensure it is updated
display_chatbox()