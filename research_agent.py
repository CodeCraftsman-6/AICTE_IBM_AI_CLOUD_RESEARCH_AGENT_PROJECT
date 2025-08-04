import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def load_pdf(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    return splitter.split_documents(docs)

def create_vector_store(chunks, persist_dir="faiss_store"):
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(chunks, embeddings)
    vectordb.save_local(persist_dir)
    return vectordb

def load_vector_store(persist_dir="faiss_store"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(persist_dir, embeddings)

def ask_question(query, vectordb):
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
        retriever=retriever,
        return_source_documents=True
    )
    return chain.run(query)

if __name__ == "__main__":
    pdf_path = "sample_research_paper.pdf"
    if not os.path.exists("faiss_store"):
        print("Indexing documents...")
        chunks = load_pdf(pdf_path)
        vectordb = create_vector_store(chunks)
    else:
        print("Loading existing index...")
        vectordb = load_vector_store()

    print("Ask your research questions below (type 'exit' to quit):")
    while True:
        query = input("\nYour question: ")
        if query.lower() == "exit":
            break
        response = ask_question(query, vectordb)
        print("\nAnswer:", response)
