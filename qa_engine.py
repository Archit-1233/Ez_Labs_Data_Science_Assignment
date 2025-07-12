from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
import google.generativeai as genai
import re
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def chunk_text(text,chunk_size=1000,chunk_overlap=100):
    splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    return splitter.split_text(text)

def build_vectorstore(chunks,savepath="vectorstoreindex"):
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))
    vectorstore = FAISS.from_texts(chunks, embedding=embedding_model)
    vectorstore.save_local(savepath)
    return savepath

def load_vectorstore(save_path="vectorstore_index"):
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))
    return FAISS.load_local(save_path, embedding_model, allow_dangerous_deserialization=True)

def get_relevant_chunks(query, vectorstore, k=3):
    results = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in results])

def ask_question_with_gemini(question, context):
    prompt = f"""
You are an intelligent assistant. Based *only* on the provided context, answer the user's question in clear and concise bullet points (● or -). Avoid long paragraphs. Structure your response so it's easy to read and understand. After the bullet points, wrap the justification paragraph(s) inside <support> tags.

Document:
\"\"\"
{context}
\"\"\"

Question: {question}
"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def generate_logic_questions(context):
    prompt = f"""
Read the following document and create 3 logic-based, inference-heavy questions.

Document:
\"\"\"
{context}
\"\"\"
Only output the questions as a list.
"""
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    return model.generate_content(prompt).text.strip().split("\n")

def evaluate_user_answer(question, answer, context):
    prompt = f"""
Document:
\"\"\"
{context}
\"\"\"

Question: {question}
User's Answer: {answer}

Tell whether it's correct. Give feedback and justify with references.
"""
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    return model.generate_content(prompt).text.strip()


def evaluate_user_answer(question, answer, context):
    prompt = f"""
You are an expert evaluator.

Evaluate the following user answer based ONLY on the document context.

1. Provide feedback in bullet points.
2. Mention if the answer is correct or not.
3. Include supporting justification (from which paragraph or section).
4. Wrap the supporting content inside <support>...</support> tags.

Document:
\"\"\"{context}\"\"\"

Question: {question}
User Answer: {answer}
"""
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    result = model.generate_content(prompt).text

    support_match = re.search(r"<support>(.*?)</support>", result, re.DOTALL)
    support_text = support_match.group(1).strip() if support_match else "No reference found."
    clean_feedback = re.sub(r"<support>.*?</support>", "", result, flags=re.DOTALL).strip()

    return clean_feedback, support_text




