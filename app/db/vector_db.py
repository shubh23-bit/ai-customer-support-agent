from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_db():
    #load pdf
    loader=PyPDFLoader("../../data/company.pdf")
    documents=loader.load()

    #split text into chunks
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50

    )
    docs=text_splitter.split_documents(documents)
    print(docs)

    #create embedding
    embedding_model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    #store in chromadb
    vectorstore=Chroma.from_documents(
        docs,
        embedding_model,
        persist_directory="chroma_db"
    )
    print("\n vector db created sucessfully")
    return vectorstore
if __name__ == "__main__":
    create_vector_db()
