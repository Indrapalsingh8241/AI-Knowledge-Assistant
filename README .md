# ✨ YouTube AI RAG Chatbot

An AI-powered YouTube chatbot that allows users to chat with any YouTube video using Retrieval-Augmented Generation (RAG).

Built with Flask, LangChain, FAISS, Groq LLM, HuggingFace Embeddings, and YouTube Transcript API.

---

# 🚀 Features

✅ Chat with any YouTube video  
✅ Automatic transcript extraction  
✅ AI-powered answers using Groq Llama 3  
✅ Semantic search using FAISS  
✅ Retrieval-Augmented Generation (RAG)  
✅ Chrome Extension support  
✅ Auto-detect current YouTube tab  
✅ Modern glassmorphism UI  
✅ Fast response generation  
✅ YouTube Shorts support  
✅ Render deployment ready  

---

# 🧠 How It Works

1. Open any YouTube video
2. Transcript is fetched automatically
3. Transcript is split into chunks
4. Embeddings are generated
5. FAISS vector database is created
6. User asks questions
7. Relevant chunks are retrieved
8. Groq LLM generates final response

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Chrome Extension API

## Backend
- Flask
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq API
- YouTube Transcript API

---

# 📂 Project Structure

```text
youtube-chatbot/
│
├── app.py
├── requirements.txt
├── manifest.json
├── popup.html
├── popup.js
├── style.css
├── icon.png
├── README.md
├── .gitignore
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Indrapalsingh8241/youtube-chatbot.git

cd youtube-chatbot
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
langchain-groq
sentence-transformers
faiss-cpu
youtube-transcript-api
pytube
```

---

# 🔑 Setup Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Mac/Linux

```bash
export GROQ_API_KEY="your_groq_api_key"
```

---

## Windows CMD

```bash
set GROQ_API_KEY=your_groq_api_key
```

---

## Windows PowerShell

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

---

# ▶️ Run Backend

```bash
python app.py
```

Backend runs on:

```text
http://127.0.0.1:5001
```

---

# 🧩 Load Chrome Extension

1. Open Chrome
2. Go to:

```text
chrome://extensions/
```

3. Enable:
- Developer Mode

4. Click:
- Load Unpacked

5. Select project folder

---

# 💡 Usage

1. Open any YouTube video
2. Click the Chrome extension
3. Video loads automatically
4. Ask questions about the video

---

# 🎬 Example Questions

- Summarize this video
- What are the key points?
- Explain this concept simply
- What does the speaker mean?
- Give notes from this video

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

- Streaming AI responses
- Timestamp-based answers
- Voice interaction
- Chat history
- Multi-video memory
- PDF export
- Playlist chatbot
- Mobile app support

---

# 🔒 Security

Never hardcode API keys.

Use:
- `.env`
- `.gitignore`

---

# 🤝 Contributing

Pull requests are welcome.

Feel free to fork the repository and improve the project.

---

# 👨‍💻 Author

Indrapal Singh

Made with ❤️ using Flask + LangChain + Groq

GitHub:
https://github.com/Indrapalsingh8241
