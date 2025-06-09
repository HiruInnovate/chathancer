import os

from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone as PineconeLangchain
from pinecone import Pinecone, ServerlessSpec

from logger.loggingUtil import get_logger

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from consts import INDEX_NAME

logger = get_logger(__file__, log_file="main.log")


def ingest_docs(temp_file_path, chunk_size, chunk_overlap):
    load_dotenv()

    try:
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

        if not INDEX_NAME in pc.list_indexes():
            try:
                pc.create_index(
                    INDEX_NAME,
                    dimension=1536,
                    metric='dotproduct',
                    spec=ServerlessSpec(
                        cloud="aws",
                        region="us-east-1",
                    ))
                logger.info(f"Index created in Pinecone :: {INDEX_NAME}")

            except Exception as e:
                logger.error(f"Exception occurred while creating Index :: {e}")
                return "Error"

        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator="\n"
        )
        docs = text_splitter.split_documents(documents=documents)
        logger.info(f"loaded {len(docs)} documents")

        logger.info(f"Going to add {len(docs)} to Pinecone")
        PineconeLangchain.from_documents(docs, embeddings, index_name=INDEX_NAME)
        logger.info("Loading to vectorstore done.")
        return "Success"

    except Exception as e:
        logger.error(f"Error occurred while ingesting documents into vector database :: Error Details :: {e}")
        return "Error"
