import streamlit as st
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MEMORY_FILE = "memory.json"


# Load saved customer memory
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}


# Save customer memory
def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


memory = load_memory()

st.title("SupportSense AI")
st.subheader("AI Customer Support Agent with Memory & Smart Routing")

customer_id = st.text_input("Enter Customer ID")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.write(message)

user_input = st.chat_input("Ask support question...")

if user_input and customer_id:
    st.session_state.messages.append(("user", user_input))

    with st.chat_message("user"):
        st.write(user_input)

    # Load previous memory for this customer
    old_memory = memory.get(customer_id, [])
    memory_context = "\n".join(old_memory)

    # Smart model routing
    if len(user_input.split()) < 8:
        selected_model = "llama-3.1-8b-instant"
        routing_reason = "Fast model selected (simple query)"
    else:
        selected_model = "llama-3.3-70b-versatile"
        routing_reason = "Powerful model selected (complex query)"

    completion = client.chat.completions.create(
        model=selected_model,
        messages=[
            {
                "role": "system",
                "content": f"""
You are SupportSense AI, a helpful customer support assistant.

You help customers with:
- Order tracking
- Shipping
- Refunds
- Returns
- Complaints
- General support

Use the customer's previous conversation only if it exists.

IMPORTANT RULES:
- Never invent order numbers.
- Never invent tracking IDs.
- Never invent addresses.
- Never invent shipping status.
- Never invent customer details.
- Never claim an order exists unless the user has provided that information.
- If information is missing, politely ask the customer for it.
- If the customer asks what they asked earlier, answer using only the previous conversation stored below.

Customer History:
{memory_context}
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    reply = completion.choices[0].message.content

    # Save conversation memory
    if customer_id not in memory:
        memory[customer_id] = []

    memory[customer_id].append(f"User: {user_input}")
    memory[customer_id].append(f"Assistant: {reply}")

    save_memory(memory)

    st.session_state.messages.append(("assistant", reply))

    with st.chat_message("assistant"):
        st.write(reply)

    st.info(f"Model Used: {selected_model}")
    st.caption(routing_reason)
