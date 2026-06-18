AI Chatbot 

This is a simple AI chatbot web application built using Flask and Google Gemini API.
It allows users to chat with an AI assistant through a web interface.

Features
Simple chat UI using HTML
AI responses using Gemini API
Custom predefined responses (greetings, bye, etc.)
Chat history stored in JSON file
Exit chat by typing "bye"

Technologies Used
Python
Flask
HTML/CSS
Google Gemini API
JSON (for storing chat history)

Project Structure
project/
│
├── app.py
├── chatbot.json
├── chatbot.py
├── templates/
     └── index.html


Implementation
The chatbot is built using Flask as the backend and Gemini API for AI responses.
The user enters a message in the HTML input box.
The message is sent to Flask using a POST request.
Flask receives the message in the / route.
The message is passed to chatbot_response() function.
Inside the function:
First, it checks if the message matches any predefined responses.
If yes, it returns the custom response.
Otherwise, it sends the message to the Gemini API.
The AI-generated response is returned back to Flask.
Flask renders the response in the HTML page.
The conversation is saved in chatbot.json.     


Usage
Open browser and go to:
http://127.0.0.1:5000
Type a message and press Send
Type bye to end chat

Example Conversation
User: hello
Bot: Hi! How can I help you?

User: what is AI
Bot: AI enables machines to simulate intelligence.

User: bye
Bot: Goodbye!

Author
Made by Adithya K.S
