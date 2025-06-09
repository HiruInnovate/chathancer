# 🤖 ChatHancer

**Supercharge your PDFs with AI-powered Q&A.**  
ChatHancer is a smart and modern application that lets you upload PDF documents, embed their content into a vector database, and ask natural language questions to retrieve precise, context-aware answers — powered by LangChain and LLMs.

![ChatHancer Logo](./chatHancer_logo.JPG) <!-- Replace with the actual path or URL -->

---

## 🚀 Features

- 📄 **PDF Upload**: Easily upload and manage your documents.
- 🧠 **Smart Embedding**: Convert document chunks into vector embeddings using powerful models.
- 💬 **Ask Questions**: Interact with your documents through a chat interface.
- 📦 **Vector Storage**: Uses Pinecone for storing and retrieving embeddings efficiently.
- ⚙️ **Custom Settings**: Configure chunk size and overlap for optimized embedding.
- 🌐 **Clean UI**: Built with Streamlit for a fast and responsive experience.

---

## 🛠️ Tech Stack

| Layer         | Technology              |
|---------------|-------------------------|
| UI/Frontend    | Streamlit              |
| Embeddings     | LangChain + OpenAI     |
| Backend        | Python                 |
| Vector Store   | Pinecone               |
| PDF Processing | PyPDF2                 |

---
### 1. Clone the repo

```bash
git clone https://github.com/HiruInnovate/chathancer.git
cd chathancer
```

## 🚀 Getting Started

### Set up Environment

```bash
pipenv shell
pipenv install
```
###  Set your environment variables

Create a .env file with your OpenAI API key and MySQL credentials:
```text
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
```
Go to Pinecone website and sign up, createa API key.
Same for OPEN AI, go to its website , sign up, add credits, create API key and putit in .env file to proceed.

### Run the app
```bash
streamlit run ./🏠_Home.py
```
# About me
I am `Hiranmoy Goswami`, I am passionate about `AI/ML/DL` , `Generative AI applications` and their use in different domains, I also love to build `web applications` using `Java, React`, I have backend development experience with Java[Microservices]. For any work, you can reach out to me at...

* [LinkedIn](https://www.linkedin.com/in/hiranmoy-goswami-1997-dev/)
* [Youtube](https://www.youtube.com/channel/UCzQ9e6BsI1XiBWD3wlBRfrQ)

