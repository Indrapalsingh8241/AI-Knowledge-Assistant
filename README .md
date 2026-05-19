# 🎥 YouTube AI RAG Chatbot

An AI-powered chatbot that lets you chat with any YouTube video using Retrieval-Augmented Generation (RAG).

Built with Flask, LangChain, FAISS, Groq LLM, and YouTube Transcript API.

---

# 🚀 Live Demo

👉 Add your deployed Render link here

Example:

https://your-app-name.onrender.com

---

# ✨ Features

✅ Chat with any YouTube video  
✅ Automatic transcript extraction  
✅ AI-generated answers using Groq Llama 3.1  
✅ Semantic search with FAISS  
✅ Clean chatbot UI  
✅ Retrieval-Augmented Generation (RAG)  
✅ Fast responses  
✅ Render deployment ready  
✅ Chrome extension ready  

---

# 🧠 How It Works

1. Paste a YouTube video URL
2. Transcript is fetched automatically
3. Transcript is split into chunks
4. Embeddings are created
5. FAISS vector database is generated
6. User asks questions
7. Relevant context is retrieved
8. Groq LLM generates final answer

---

# 🛠️ Tech Stack

- Python
- Flask
- LangChain
- FAISS
- Groq API
- HuggingFace Embeddings
- YouTube Transcript API
- HTML/CSS/JavaScript

---

# 📂 Project Structure

```text
youtube-rag-chatbot/
│
├── app.py
├── requirements.txt
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/youtube-rag-chatbot.git

cd youtube-rag-chatbot
```

---

## 2️⃣ Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv myenv

source myenv/bin/activate
```

### Windows

```bash
python -m venv myenv

myenv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Packages

```txt
flask
flask-cors
gunicorn
langchain
langchain-community
langchain-huggingface
sentence-transformers
faiss-cpu
langchain-groq
youtube-transcript-api
pytube
```

---

# 🔑 Setup Groq API Key

Get API key from:

https://console.groq.com/keys

---

## Mac/Linux

```bash
export GROQ_API_KEY="your_groq_api_key"
```

---

## Windows

```bash
set GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Project

```bash
python app.py
```

Open:

```text
http://localhost:5001
```

---

# 🎬 Example YouTube Video

```text
https://www.youtube.com/watch?v=aircAruvnKk
```

---

# 💡 Example Questions

- What is a transformer?
- Explain neural networks
- Summarize the video
- What are the key concepts discussed?

---

# 🚀 Deploy on Render

## Build Command

```bash
pip install -r requirements.txt
```

---

## Start Command

```bash
gunicorn app:app
```

---

# 🌐 Future Improvements

- Timestamp-based answers
- Chrome Extension
- PDF export
- Video summarization
- Playlist chatbot
- Voice interaction
- Multi-video memory
- Dark mode

---

# 🤝 Contributing

Pull requests are welcome.

If you'd like to improve the project, feel free to fork the repository and submit a PR.



---

# 👨‍💻 Author

Indrapal Singh

Made with ❤️ using Flask + LangChain + Groq
