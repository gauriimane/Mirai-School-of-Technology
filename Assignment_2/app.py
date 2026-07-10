import os
import dotenv
import streamlit as st
import google.generativeai as genai

# -----------------------------
# Load Environment Variables
# -----------------------------
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API_KEY not found in .env file.")
    st.stop()

genai.configure(api_key=api_key)

# -----------------------------
# Streamlit Page
# -----------------------------
st.set_page_config(
    page_title="AI Multiverse",
    page_icon="🌌",
    layout="centered"
)

st.title("🌌 AI Multiverse")
st.caption("Choose an AI Universe and start chatting!")

# -----------------------------
# Persona Data
# -----------------------------
PERSONAS = {
    "Wise Sage": {
        "avatar": "🌿",
        "greeting": "Welcome, traveler. Sit beneath the ancient tree and ask what wisdom you seek today.",
        "prompt": (
            "You are an ancient wise sage. "
            "Speak calmly with wisdom, life lessons, metaphors, and peaceful guidance."
        )
    },

    "Sarcastic Robot": {
        "avatar": "🤖",
        "greeting": "System boot complete. Congratulations, you've activated the smartest robot in this galaxy.",
        "prompt": (
            "You are a sarcastic robot. "
            "Reply with dry humor, witty sarcasm, futuristic references, and playful arrogance."
        )
    },

    "Poet": {
        "avatar": "✍️",
        "greeting": "The stars whispered your arrival. Tell me your thoughts, and I'll turn them into poetry.",
        "prompt": (
            "You are a romantic poet. "
            "Answer using poetic language, vivid imagery, and emotional expression."
        )
    }
}

# -----------------------------
# Choose Persona
# -----------------------------
selected_persona = st.selectbox(
    "Choose your AI Universe",
    list(PERSONAS.keys())
)

avatar = PERSONAS[selected_persona]["avatar"]

# -----------------------------
# Session State
# -----------------------------
if "chat_histories" not in st.session_state:
    st.session_state.chat_histories = {}

if "greeted" not in st.session_state:
    st.session_state.greeted = {}

if selected_persona not in st.session_state.chat_histories:
    st.session_state.chat_histories[selected_persona] = []

# -----------------------------
# Show Greeting Once
# -----------------------------
if selected_persona not in st.session_state.greeted:

    greeting = PERSONAS[selected_persona]["greeting"]

    st.session_state.chat_histories[selected_persona].append(
        {
            "role": "assistant",
            "content": greeting
        }
    )

    st.session_state.greeted[selected_persona] = True

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.chat_histories[selected_persona]:

    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar=avatar):
            st.markdown(message["content"])

    else:
        with st.chat_message("user"):
            st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask your AI anything...")

if prompt:

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.chat_histories[selected_persona].append(
        {
            "role": "user",
            "content": prompt
        }
    )

    history = "\n".join(
        f"{msg['role'].capitalize()}: {msg['content']}"
        for msg in st.session_state.chat_histories[selected_persona]
    )

    full_prompt = f"""
{PERSONAS[selected_persona]['prompt']}

Conversation:

{history}

Assistant:
"""

    try:

        model = genai.GenerativeModel("gemini-2.5-flash")

        with st.chat_message("assistant", avatar=avatar):

            placeholder = st.empty()
            answer = ""

            response = model.generate_content(
                full_prompt,
                stream=True
            )

            for chunk in response:

                if chunk.text:
                    answer += chunk.text
                    placeholder.markdown(answer)

        st.session_state.chat_histories[selected_persona].append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        st.error(f"Gemini Error: {e}")

# -----------------------------
# Clear Chat
# -----------------------------
if st.button("🗑️ Clear Current Universe"):

    st.session_state.chat_histories[selected_persona] = []

    if selected_persona in st.session_state.greeted:
        del st.session_state.greeted[selected_persona]

    st.rerun()