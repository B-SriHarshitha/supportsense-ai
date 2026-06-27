# 🚀 SupportSense AI

An AI-powered Customer Support Assistant built using Streamlit and Groq LLM.

## Features

- 🤖 AI-powered customer support
- 🧠 Persistent customer memory
- ⚡ Smart model routing
- 📦 Order support
- 💰 Refund assistance
- 🚚 Shipping assistance
- 💬 Interactive chat interface

## Tech Stack

- Python 3.13
- Streamlit
- Groq API
- OpenAI Python SDK
- JSON Memory Storage
- Git & GitHub

## Project Structure

```
customer-support-agent/
│── app.py
│── memory.json
│── .env
│── requirements.txt
│── README.md
```

## Installation

Clone the repository

```bash
git clone https://github.com/B-SriHarshitha/supportsense-ai.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GROQ_API_KEY=your_api_key_here
```

Run

```bash
streamlit run app.py
```

## Example

Customer:
```
I want a refund.
```

AI:
```
Please provide your order number so I can help you with your refund.
```

## Future Improvements

- Database integration
- Authentication
- Admin dashboard
- Email notifications
- Analytics

## Author

B. Sri Harshitha