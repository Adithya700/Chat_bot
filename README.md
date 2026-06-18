# AI Chatbot using Flask and Gemini API

A simple AI-powered chatbot built using Flask and Google's Gemini API. The chatbot provides predefined responses for common questions and uses the Gemini model to generate intelligent responses for other queries. It also maintains chat history by storing conversations in a JSON file.

---

## Features

* Web-based chatbot interface using Flask
* Integration with Google's Gemini API
* Predefined responses for common questions
* AI-generated responses for custom queries
* Chat history persistence using JSON
* Environment variable support using `.env`
* Response caching to avoid repeated API calls for identical queries
* Timestamp for each conversation
* Exit functionality using the `bye` command

---

## Technologies Used

* Python 3
* Flask
* Google Gemini API
* python-dotenv
* JSON
* HTML Templates

---

## Project Structure

```text
Chat_bot/
│
├── chatbot.py
├── chatbot.json
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## How It Works

### Predefined Responses

The chatbot provides instant responses for common queries such as:

* Hello
* Hi
* Hey
* What is AI?
* Explain API
* Help me with my studies
* Thank you
* Bye

These responses are served locally without making API requests.

---

### AI Responses

For queries that are not predefined, the chatbot sends the user's message to the Gemini API:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=message
)
```

The generated response is then displayed in the chat interface.

---

### Response Caching

The application maintains a dictionary cache:

```python
response_cache = {}
```

If a user sends the same message again, the cached response can be returned instead of making another API call, reducing API usage and response time.

---

### Chat History

Every conversation is stored in `chatbot.json`:

```json
[
    {
        "user": "Hello",
        "bot_reply": "Welcome to your chatbot assistant. Ask me anything anytime !!!",
        "timestamp": "14:32:10"
    }
]
```

The history is automatically loaded when the application starts and updated after each conversation.

---

## Environment Variables

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_gemini_api_key
```

The application loads the API key securely using:

```python
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Adithya700/Chat_bot.git
cd Chat_bot
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python chatbot.py
```

The application runs at:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser and start chatting with the AI assistant.

---

## Requirements

* Python 3.x
* Flask
* google-genai
* python-dotenv

Example:

```bash
pip install flask google-genai python-dotenv
```

---

## Learning Objectives

This project was developed to practice:

* Flask web development
* Building AI-powered applications
* Integrating external APIs
* Environment variable management
* File handling with JSON
* Response caching
* Template rendering using Flask
* Exception handling and error management

---

## Author

**Adithya K.S.**

This project was created as a practice project to strengthen Flask development skills and gain hands-on experience in building AI-powered web applications using Google's Gemini API.
