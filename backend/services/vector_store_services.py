from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


from langchain_huggingface import HuggingFaceEndpointEmbeddings
import os



embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

db = None

def create_vector_db(text):

    global db

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    db = FAISS.from_texts(
        chunks,
        embeddings
    )
    print(f"Total Chunks: {len(chunks)}")
    db.save_local("faiss_index")

    return True


def get_db():
    return db