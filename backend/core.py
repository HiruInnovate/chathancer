import os

from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from openai import AuthenticationError
from pinecone_plugins.inference.core.client.exceptions import NotFoundException

from typing import Any, Dict, List
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from logger.loggingUtil import get_logger
from consts import INDEX_NAME
from pinecone import Pinecone

logger = get_logger(__file__, log_file="main.log")
SOME_ERROR_OCCURRED_ = "Opps!! Some Error occurred!! "
load_dotenv()


def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    load_dotenv()
    try:
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        docsearch = PineconeVectorStore(index=pc.Index(INDEX_NAME), embedding=embeddings, text_key='text')
        chat = ChatOpenAI(verbose=True, temperature=0)

        rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")

        retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
        stuff_documents_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)

        history_aware_retriever = create_history_aware_retriever(
            llm=chat, retriever=docsearch.as_retriever(), prompt=rephrase_prompt
        )
        qa = create_retrieval_chain(
            retriever=history_aware_retriever, combine_docs_chain=stuff_documents_chain
        )
        logger.info("-->> QA INVOKING -->>>")

        result = qa.invoke(input={"input": query, "chat_history": chat_history})

    except NotFoundException as e:
        logger.error(f"Exception occurred while fetching data from pinecone :: Exception Details :: {e}")
        return SOME_ERROR_OCCURRED_
    except AuthenticationError as e:
        logger.error(f"Exception occurred while Authenticating OPen AI request :: Error Details :: {e}")
        return SOME_ERROR_OCCURRED_
    except Exception as e:
        logger.error(f"Exception occurred:: {e}")
        return SOME_ERROR_OCCURRED_

    logger.info(f"Information Retrieved :: Result :: {result} ")
    return result
