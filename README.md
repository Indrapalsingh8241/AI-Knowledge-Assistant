
# 🤖 AI Knowledge Assistant

An AI-powered RAG application that allows users to chat with YouTube videos, PDFs, websites, and a general-purpose AI assistant through a unified interface.

Built with FastAPI, Streamlit, LangChain, FAISS, Groq LLM, HuggingFace Embeddings, and Retrieval-Augmented Generation (RAG).
🔗 Live Demo:
[https://lnkd.in/d3yyPF6v](https://ai-knowledge-assistant-emrvvzjeju4trs7abd7q6w.streamlit.app/)

---

# 🚀 Features

✅ AI Chatbot

✅ Chat with YouTube Videos

✅ Chat with PDF Documents

✅ Chat with Websites

✅ Retrieval-Augmented Generation (RAG)

✅ Semantic Search with FAISS

✅ Groq Llama 3 Integration

✅ HuggingFace Embeddings

✅ Separate Chat History for Each Mode

✅ YouTube Thumbnail Preview

✅ Modern ChatGPT-style Interface

✅ FastAPI Backend

✅ Streamlit Frontend

✅ Render Deployment Ready

---

# 🧠 How It Works

### YouTube Mode

1. User enters a YouTube URL
2. Transcript is extracted
3. Transcript is chunked
4. Embeddings are generated
5. FAISS index is created
6. Relevant chunks are retrieved
7. Groq LLM generates answers

### PDF Mode

1. User uploads a PDF
2. Text is extracted
3. Chunks are generated
4. Embeddings are created
5. FAISS index is built
6. Questions are answered using RAG

### Website Mode

1. User enters a website URL
2. Website content is extracted
3. Content is chunked
4. Embeddings are generated
5. FAISS index is created
6. Questions are answered from website content

### Chatbot Mode

1. User asks any question
2. Groq LLM generates a response directly

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* Python
* Requests

## Backend

* FastAPI
* LangChain
* FAISS
* Groq API
* HuggingFace Embeddings
* YouTube Transcript API
* BeautifulSoup
* PyPDF

---

# 📂 Project Structure

```text
chatbot/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Indrapalsingh8241/youtube-chatbot.git

cd youtube-chatbot
```

---

## Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend:

```text
http://localhost:8501
```

---

# 💡 Usage

### YouTube Chat

* Paste YouTube URL
* Load Video
* Ask Questions

### PDF Chat

* Upload PDF
* Load PDF
* Ask Questions

### Website Chat

* Enter Website URL
* Load Website
* Ask Questions

### AI Chatbot

* Ask General Questions
* Receive AI-generated Responses

---

# 🎯 Example Questions

### YouTube

* Summarize this video
* What are the key points?
* Explain this concept

### PDF

* Summarize the document
* Explain chapter 2
* Extract important points

### Website

* What services does this website provide?
* Summarize the content
* Give important information

### AI Chatbot Mode

1. User asks any general-purpose question
2. Question is sent directly to the Groq LLM
3. AI generates a conversational response
4. No document or website context is required

---

# 🚀 Future Improvements

* Source Citations
* Streaming Responses
* SQLite Chat History
* User Authentication
* Multi-Document RAG
* Notes Generation
* MCQ Generation
* PDF Export
* Conversation Memory
* Cloud Storage

---

# 🔒 Security

Never commit:

* .env
* API Keys
* FAISS Index Files
* Uploaded Files

Use:

* .env
* .gitignore

---

# 👨‍💻 Author

Indrapal Singh

Built with ❤️ using FastAPI, Streamlit, LangChain, FAISS, and Groq.

GitHub:
https://github.com/Indrapalsingh8241

