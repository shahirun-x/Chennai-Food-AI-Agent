import streamlit as st
import pandas as pd
import google.generativeai as genai

# --- Page Configuration ---
st.set_page_config(
    page_title="Love Language ❤️",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Love Language - Your Chennai Foodie Companion")
st.caption("Find the food you'll fall in love with in Chennai")

# --- API Key and Model Configuration ---
# A safer way to get the API key in Streamlit
try:
    # This is for Streamlit Community Cloud deployment, but works locally too
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    # A fallback for local development
    api_key = st.text_input("Enter your Google API Key:", type="password", help="Get your key from https://aistudio.google.com/app/apikey")

if not api_key:
    st.info("Please enter your Google API Key to continue.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Data Loading ---
# The @st.cache_data decorator tells Streamlit to be smart.
# It will only run this function once and cache the result.
# This prevents reloading the big CSV file every time the user types a message.
@st.cache_data
def load_data(filepath):
    """Loads the restaurant data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file '{filepath}' was not found. Please make sure it's in the same folder as app.py.")
        return None

df = load_data('chennai_restaurants.csv')

# Stop the app if data loading failed
if df is None:
    st.stop()

# Convert the dataframe to a string for the prompt
restaurants_data_string = df.to_string()

# --- Chat History Management ---
# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages from the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input and Response Generation ---
if prompt := st.chat_input("What are you craving today?"):
    # Add user's message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user's message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Prepare the Prompt for the AI ---
    # We build a history for the AI to have context, but keep it simple for now
    # We will send the full rules and data every time for this prototype
    full_prompt = f"""
    You are 'Love Language,' a friendly and romantic-themed conversational agent for a food app in Chennai. Your goal is to help users find food they will fall in love with.

    **RULES:**
    - Use ONLY the restaurant data provided below to answer the user's question.
    - Do not make up any information or restaurants.
    - Be friendly, a little poetic, and charming.
    - If the user asks a question unrelated to food or Chennai restaurants, politely decline and steer the conversation back to food.

    **RESTAURANT DATA:**
    {restaurants_data_string}

    **CURRENT CONVERSATION:**
    {st.session_state.messages}

    **USER'S LATEST QUESTION:**
    {prompt}

    **YOUR RESPONSE:**
    """
    
    # --- Generate and Display AI Response ---
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking... ❤️")
        
        try:
            response = model.generate_content(full_prompt)
            ai_response = response.text
            message_placeholder.markdown(ai_response)
            
            # Add AI's response to chat history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
        except Exception as e:
            st.error(f"An error occurred: {e}")