from flask import Flask, render_template,jsonify,request
import json
from datetime import datetime
import time
from dotenv import load_dotenv
from google import genai
app = Flask(__name__)
chat_history = []
import os
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

try:
    with open("chatbot.json", "r") as file:
        chat_history = json.load(file)
    print("History loaded from JSON file\n")   
except FileNotFoundError:
  print("No JSON file found")

client= genai.Client(api_key = API_KEY)    
response_cache = {}

@app.route("/", methods=["GET", "POST"])
def home():
    user_message = ""
    bot_reply = ""
    timestamp = ""

    if request.method == "POST":
        user_message = request.form["message"]
        bot_reply = chatbot_response(user_message)  
        timestamp = datetime.now().strftime("%H:%M:%S")

    chat_history.append({
        "user" : user_message,
        "bot_reply" : bot_reply,
        "timestamp" :timestamp
    })
    with open("chatbot.json", "w") as file:
        json.dump(chat_history, file, indent=4)
    print("\nSaved to json file\n") 

    return render_template(
        "index.html",
        user_message=user_message,
        bot_reply=bot_reply,
        chat_exit= user_message.strip().lower()== "bye"
    ) 


def chatbot_response(message): 
    predefined = { 
        "hello": "Welcome to your chatbot assistant. Ask me anything anytime !!!", 
        "hi":"Welcome to your chatbot assistant. Ask me anything anytime !!!",
        "hey":"Welcome to your chatbot assistant. Ask me anything anytime !!!",
        "help me with my studies": "I’d love to help you with your studies . Tell me the subject and topic you’re working on, and I’ll explain it step by step in a simple way.",
        "what is ai": "AI enables machines to simulate intelligence.", 
        "what are the important topics under ai": "The most important subfields include Machine Learning, Natural Language Processing (NLP), Computer Vision, and Robotics",
        "explain api": "An API (Application Programming Interface) is a set of rules and protocols that allows different software programs to communicate with each other.",
        "thank u for the information": "You are welcome",
        "bye" : "Goodbye!" 
    } 
 
    msg = message.strip().lower() 
    if msg in predefined:       
         return predefined[msg] 
    if msg in response_cache:
        return response_cache[msg]
    try:            
        response = client.models.generate_content(       
            model="gemini-2.5-flash",       
            contents=message    )  
        print("API VALID")
        return response.text
    except Exception as e:
        print("Invalid")
        print(e)
     
 
print("Simple Chatbot Started") 

if __name__ == "__main__":
    app.run(debug=True)


     