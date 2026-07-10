# 🌌 AI Multiverse

**AI Multiverse** is an interactive Streamlit application that lets users chat with multiple AI personalities powered by **Google Gemini 2.5 Flash**. Each AI Universe has its own unique personality, greeting, conversation history, and communication style, providing a fun and immersive conversational experience.

Built using **Python**, **Streamlit**, **Google Generative AI**, and **python-dotenv**, this project demonstrates how prompt engineering can be used to create distinct AI personalities while maintaining separate chat sessions for each universe.

---

## 🚀 Features

- 🌿 **Multiple AI Universes**
  - Wise Sage
  - Sarcastic Robot
  - Poet

- 💬 **Independent Chat Histories**
  - Each persona maintains its own conversation history.
  - Switching between universes preserves previous conversations.

- 👋 **Dynamic Persona Greetings**
  - Every AI introduces itself with a unique welcome message.

- 🎭 **Unique AI Personalities**
  - Each universe responds with its own tone, style, and behavior using customized system prompts.

- ⚡ **Real-Time Streaming Responses**
  - Gemini responses are streamed live for a smooth chat experience.

- 🎨 **Persona Avatars**
  - Each AI universe has its own emoji avatar for better user experience.

- 🗑️ **Clear Chat**
  - Reset the conversation for the currently selected AI universe.

- 🔐 **Secure API Key Management**
  - Uses `.env` file to securely store the Google Gemini API key.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit**
- **Google Gemini 2.5 Flash**
- **google-generativeai**
- **python-dotenv**

---

## 📂 Project Structure

```
AI-Multiverse/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Multiverse.git
```

Or download the project folder.

---

### 2. Create a Virtual Environment (Optional)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` File

Create a file named `.env` in the project directory.

```env
API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your Google Gemini API key.

---

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🎭 Available AI Universes

### 🌿 Wise Sage

A calm philosopher who answers with wisdom, life lessons, and thoughtful metaphors.

---

### 🤖 Sarcastic Robot

A futuristic robot that responds with witty sarcasm, humor, and playful arrogance.

---

### ✍️ Poet

A romantic poet who transforms conversations into expressive and imaginative poetry.

---

## 💡 How It Works

1. Select an AI Universe from the dropdown menu.
2. Receive a personalized greeting from the selected persona.
3. Start chatting with the AI.
4. Responses are generated using **Google Gemini 2.5 Flash**.
5. Each universe stores its own conversation history.
6. Switch between universes anytime without losing previous chats.
7. Use the **Clear Current Universe** button to reset the active conversation.

---

## 📋 Requirements

```
streamlit
google-generativeai
python-dotenv
```

Or install manually:

```bash
pip install streamlit google-generativeai python-dotenv
```

---

## 🔒 Environment Variables

The application requires the following environment variable:

| Variable | Description |
|----------|-------------|
| `API_KEY` | Google Gemini API Key |

---

## 🎯 Learning Objectives

This project demonstrates:

- Prompt Engineering
- AI Persona Design
- Streamlit Chat Interface
- Session State Management
- Google Gemini API Integration
- Environment Variable Management
- Streaming AI Responses
- Multi-Persona Conversation Handling

---

## 👩‍💻 Author

**Gauri Mane**

B.Tech Computer Science Engineering (AI & ML)

---

## 📄 License

This project is developed for educational and learning purposes as part of the **MirAI School of Technology – Virtual Summer Internship 2026**.
