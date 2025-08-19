# Chennai-Food-AI-Age

Love Language - Your Chennai Foodie Companion
Welcome to Love Language, an intelligent and charming conversational AI designed to help you discover the perfect dining experience in Chennai. Powered by Google's Gemini model, this chatbot acts as your personal foodie friend, offering personalized recommendations based on your cravings.

(Note: You can take a screenshot of your running app and upload it to a site like Imgur to get a URL to display an image here!)

Features
Conversational Search: Simply chat in natural language to find restaurants. No need to click through complex filters.

Personalized Recommendations: The chatbot learns your preferences from the conversation to suggest places you'll truly love.

Detailed Information: Get details on cuisine, location, specialty dishes, and price range for dozens of Chennai's best restaurants.

Engaging Persona: "Love Language" has a friendly, romantic-themed personality to make food discovery fun and engaging.

Tech Stack
Language: Python

AI Model: Google Gemini 1.5 Flash

Framework: Streamlit (for the interactive web interface)

Data Handling: Pandas

How It Works
This project uses a technique called Retrieval-Augmented Generation (RAG). In simple terms:

Retrieval: The chatbot has a knowledge base (chennai_restaurants.csv) containing factual data about restaurants in Chennai.

Augmentation: When you ask a question, the relevant data from the knowledge base is "augmented" or added to the prompt sent to the AI.

Generation: The LLM (Gemini) then uses this provided data and its own language capabilities to generate a creative, accurate, and in-character response. This prevents the AI from inventing incorrect information.

Getting Started
Follow these instructions to run the chatbot on your own local machine.

Prerequisites
Python 3.8 or higher installed.

A Google API Key for the Gemini model. You can get one from Google AI Studio.

Installation & Setup
Clone the repository:

git clone https://github.com/your-username/chennai-food-chatbot.git
cd chennai-food-chatbot

Install the required Python packages:

pip install -r requirements.txt

Set up your API Key:
The application is designed to ask for your API key in the interface. For a more permanent setup, you can use Streamlit's secrets management.

Running the Application
Open your terminal in the project directory.

Run the following command:

streamlit run app.py

The application will open in a new tab in your web browser.

File Structure
chennai-food-chatbot/
│
├── app.py                  # The main Streamlit application script
├── chennai_restaurants.csv # The knowledge base with restaurant data
├── requirements.txt        # List of Python dependencies
└── README.md               # This file
