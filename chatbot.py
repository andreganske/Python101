import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the pre-trained model and tokenizer from Hugging Face
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set up the Streamlit app
st.title("Hugging Face Chatbot with Streamlit")
st.write("This is a simple chatbot using the DialoGPT model.")

# Initialize the conversation history
if 'chat_history_ids' not in st.session_state:
    st.session_state['chat_history_ids'] = None
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

# Function to handle input and generate responses
def generate_response(user_input):
    # Encode the new user input, add the eos_token, and return a tensor in PyTorch
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append the new user input tokens to the chat history
    bot_input_ids = torch.cat([st.session_state['chat_history_ids'], new_input_ids], dim=-1) if st.session_state['chat_history_ids'] is not None else new_input_ids

    # Generate a response
    st.session_state['chat_history_ids'] = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode the generated response
    response = tokenizer.decode(st.session_state['chat_history_ids'][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Save the past user input and the response for display purposes
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(response)

# User input
user_input = st.text_input("You: ", "")

if user_input:
    generate_response(user_input)

# Display conversation history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])):
        st.write(f"You: {st.session_state['past'][i]}")
        st.write(f"Bot: {st.session_state['generated'][i]}")
