import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Predefined intents and responses (expand this for more capabilities)
intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello! How can I help you?", "Hi there!", "Hey! What's up?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "exit"],
        "responses": ["Goodbye! Have a great day!", "See you later!", "Bye!"]
    },
    "name": {
        "patterns": ["what is your name", "who are you", "tell me about yourself"],
        "responses": ["I'm a simple chatbot built with NLTK. What's your name?", "You can call me Navin's assistant. Nice to meet you!"]
    },
    "help": {
        "patterns": ["help", "what can you do", "assist me"],
        "responses": ["I can answer basic questions, chat, or provide info. Try asking about the weather or my name!", "How can I assist you today?"]
    },
    "weather": {
        "patterns": ["weather", "how is the weather", "is it raining"],
        "responses": ["I'm not connected to real-time data, but I hope it's sunny!", "Weather's great in my digital world!"]
    },
    "about":{
        "patterns":["Creater","about your creater","who is your creater"],
        "responses":["My creater is Navin who is pursuing B.tech from jnct & He is very intellegent and dedicated person "]
    },
    "purpose":{
        "patterns":["who are you ", "purpose of creating",],
        "responses":["Navin created me for his internship at codech company😁"]
    },
       
    "default": {
        "responses": ["I'm not sure I understand. Can you rephrase?", "Sorry, I don't know that. Ask me something else!"]
    }
    
        
    
}

# Function to preprocess user input
def preprocess_input(user_input):
    # Tokenize and lemmatize
    tokens = word_tokenize(user_input.lower())
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized

# Function to match intent based on keywords
def get_intent(lemmatized_input):
    for intent, data in intents.items():
        if intent == "default":
            continue
        for pattern in data["patterns"]:
            pattern_words = preprocess_input(pattern)
            # Check if most words in pattern match input (simple keyword matching)
            if all(word in lemmatized_input for word in pattern_words):
                return intent
    return "default"

# Function to get a random response for an intent
def get_response(intent):
    responses = intents[intent]["responses"]
    return random.choice(responses)

# Main chatbot loop
def chatbot():
    print("ChatBot: Hello! I'm here to chat. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        
        # Preprocess input
        lemmatized = preprocess_input(user_input)
        
        # Get intent
        intent = get_intent(lemmatized)
        
        # Get response
        response = get_response(intent)
        
        print(f"ChatBot: {response}")
        
        # Exit condition
        if intent == "goodbye":
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()