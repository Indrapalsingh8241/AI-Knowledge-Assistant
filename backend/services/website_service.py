from langchain_community.document_loaders import WebBaseLoader

def get_website_text(url):

    loader = WebBaseLoader(url)

    docs = loader.load()

    text = "\n".join(
        doc.page_content
        for doc in docs
    )

    return text