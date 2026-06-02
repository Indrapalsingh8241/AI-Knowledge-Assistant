import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)
if "loaded_source" not in st.session_state:
    st.session_state.loaded_source = None
# ----------------------------
# Session State
# ----------------------------

if "mode" not in st.session_state:
    st.session_state.mode = "chatbot"

if "chatbot_history" not in st.session_state:
    st.session_state.chatbot_history = []

if "youtube_history" not in st.session_state:
    st.session_state.youtube_history = []

if "pdf_history" not in st.session_state:
    st.session_state.pdf_history = []

if "website_history" not in st.session_state:
    st.session_state.website_history = []


def get_current_history():

    if st.session_state.mode == "chatbot":
        return st.session_state.chatbot_history

    elif st.session_state.mode == "youtube":
        return st.session_state.youtube_history

    elif st.session_state.mode == "pdf":
        return st.session_state.pdf_history

    return st.session_state.website_history

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("💬 History")

    history = get_current_history()

    if st.button("🗑️ Clear Current History"):

        history.clear()

        st.rerun()

    st.divider()

    for msg in reversed(history):

        if msg["role"] == "user":

            st.write(
                msg["content"][:40]
            )

# ----------------------------
# Title
# ----------------------------

st.title("🤖 AI Knowledge Assistant")

# ----------------------------
# Navigation Buttons
# ----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💬 Chatbot"):
        st.session_state.mode = "chatbot"

with col2:
    if st.button("🎥 YouTube"):
        st.session_state.mode = "youtube"

with col3:
    if st.button("📄 PDF"):
        st.session_state.mode = "pdf"

with col4:
    if st.button("🌐 Website"):
        st.session_state.mode = "website"

# =====================================================
# CHATBOT
# =====================================================

if st.session_state.mode == "chatbot":

    st.header("💬 Chatbot")

    for message in st.session_state.chatbot_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything...")

    if prompt:

        st.session_state.chatbot_history.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = requests.post(
            f"{BACKEND_URL}/chatbot/simple_chat",
            json={
                "question": prompt
            }
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

            st.session_state.chatbot_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        else:

            st.session_state.chatbot_history.append(
                {
                    "role": "assistant",
                    "content": response.text
                }
            )

        st.rerun()

# =====================================================
# YOUTUBE
# =====================================================

elif st.session_state.mode == "youtube":

    st.header("🎥 YouTube Chat")

    history = st.session_state.youtube_history

    # Display old messages
    for msg in history:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    video_url = st.text_input(
        "Enter YouTube URL",
        key="youtube_url"
    )
    import re
    def get_video_id(url):

     match = re.search(
        r"(?:v=)([A-Za-z0-9_-]{11})",
        url
    )

     if match:
        return match.group(1)

     return None

    if st.button("Load Video"):

        response = requests.post(
            f"{BACKEND_URL}/youtube/load-video",
            json={
                "video_url": video_url
            }
            
        )
        if video_url:

         video_id = get_video_id(video_url)

        if video_id:

         thumbnail_url = (
            f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        )

        col1, col2 = st.columns([1, 3])

        with col1:

            st.image(
                thumbnail_url,
                width=200,
                caption="Video Thumbnail"
            )

        if response.status_code == 200:

            st.success(
                response.json()["message"]
            )
            st.session_state.loaded_source = f"🎥 {video_url}"


            # Optional: Clear old video chat
            # st.session_state.youtube_history = []

        else:
            st.error(response.text)
    question = st.chat_input(
        "Ask about the video..."
    )

    if question:

        response = requests.post(
            f"{BACKEND_URL}/chat/ask",
            json={
                "question": question
            }
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

            history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()

        else:

            st.error(response.text)
# =====================================================
# PDF
# =====================================================

elif st.session_state.mode == "pdf":

    st.header("📄 PDF Chat")

    history = st.session_state.pdf_history

    # Display old chat
    for msg in history:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    pdf_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if st.button("Load PDF"):

        if pdf_file:

            files = {
                "file": (
                    pdf_file.name,
                    pdf_file,
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/pdfload",
                files=files
            )

            if response.status_code == 200:

                st.success("PDF Loaded Successfully")

                # Optional:
                # Start fresh when new PDF is loaded
                st.session_state.pdf_history = []

            else:

                st.error(response.text)

    question = st.chat_input(
        "Ask from PDF..."
    )

    if question:

        response = requests.post(
            f"{BACKEND_URL}/chat/ask",
            json={
                "question": question
            }
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

            history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()

        else:

            st.error(response.text)

# =====================================================
# WEBSITE
# =====================================================

elif st.session_state.mode == "website":

    st.header("🌐 Website Chat")

    history = st.session_state.website_history

    # Display old chat
    for msg in history:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    website_url = st.text_input(
        "Enter Website URL",
        key="website_url"
    )
    from urllib.parse import quote

    if website_url:

     screenshot_url = (
        f"https://image.thum.io/get/width/800/{website_url}"
    )

     st.image(
         screenshot_url,
        caption="Website Preview",
        width=350
     )


    if st.button("Load Website"):

        response = requests.post(
            f"{BACKEND_URL}/webload",
            json={
                "url": website_url
            }
        )

        if response.status_code == 200:

            st.success("Website Loaded Successfully")

            # Optional:
            # Start fresh when a new website is loaded
            st.session_state.website_history = []

        else:

            st.error(response.text)

    question = st.chat_input(
        "Ask from Website..."
    )

    if question:

        response = requests.post(
            f"{BACKEND_URL}/chat/ask",
            json={
                "question": question
            }
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

            history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()

        else:

            st.error(response.text)