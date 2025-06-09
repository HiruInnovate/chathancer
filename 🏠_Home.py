import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def get_base64_image(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

# Page config
st.set_page_config(
    page_title="ChatHancer",
    page_icon="🤖",
    layout="wide"
)

logo = Image.open("./chatHancer_logo.JPG")
encoded_logo = get_base64_image(logo)

st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{encoded_logo}" width="200"/>
    </div>
    """,
    unsafe_allow_html=True
)

# Title section
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🤖 ChatHancer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Supercharge your PDFs with AI-powered Q&A</h3>",
            unsafe_allow_html=True)
st.markdown("---")

# Hero description
st.markdown("""
<div style='text-align: center; font-size: 18px; color: #444;'>
Upload your PDF documents, embed their content into a smart vector database, and <br>
ask questions to get accurate, AI-generated answers directly from your data.
</div>
""", unsafe_allow_html=True)

st.markdown("")

# Features section
st.subheader("✨ What ChatHancer can do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("📄 **Upload PDFs**")
    st.markdown("Seamlessly upload documents for intelligent processing.")

with col2:
    st.markdown("🧠 **Embed with AI**")
    st.markdown("Break content into chunks and store embeddings in a vector DB.")

with col3:
    st.markdown("💬 **Ask Questions**")
    st.markdown("Interact with your documents through natural language queries.")

st.markdown("---")

# How to get started
st.subheader("🚀 Get Started")
st.markdown("""
1. Go to the **Embed** page and upload your PDFs.
2. Configure chunk size and overlap from the sidebar.
3. Head over to the **Chat** page to start asking questions!
""")

st.subheader("About the Developer")
st.markdown('''
👋 I am Hiranmoy Goswami, I am passionate about AI/ML/DL , Generative AI applications and their use in different domains, I also love to build web applications using Java, React, I have backend development experience with Java[Microservices]. For any work, you can reach out to me at...
''')
spacer1, col1, col2, spacer2 = st.columns([1, 2, 2, 1])

with col1:
    st.link_button(label="🐙 GitHub", url="https://github.com/HiruInnovate")

with col2:
    st.link_button(label="🔗 LinkedIn", url="https://www.linkedin.com/in/hiranmoy-goswami-1997-dev/")

st.markdown("---")

# Footer or tagline
st.markdown(
    "<div style='text-align: center; color: gray;'>Built with ❤️ using LangChain, Pinecone, and Streamlit</div>",
    unsafe_allow_html=True)
