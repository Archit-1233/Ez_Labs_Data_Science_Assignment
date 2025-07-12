import streamlit as st
import os
import hashlib
import re
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
from document_parser import extract_text
from qa_engine import (
    chunk_text, build_vectorstore, load_vectorstore,
    get_relevant_chunks, ask_question_with_gemini,
    generate_logic_questions, evaluate_user_answer
)

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Smart Assistant for Research Summarization", layout="wide")

# Google Fonts and custom CSS
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Poppins:wght@400;700&display=swap" rel="stylesheet">
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: #f7faff;
    color: #1a1a1a;
}
.header-title {
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(to right, #007cf0, #00dfd8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-top: 1rem;
    animation: fadeInDown 1s ease-in-out;
}
.header-subtitle {
    font-size: 1.25rem;
    text-align: center;
    color: #555;
    margin-bottom: 2rem;
    animation: fadeIn 2s ease;
}
.card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 8px 30px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
    animation: fadeIn 1s ease-in-out;
}
.context-snippet-box {
    background-color: #fefce8;
    border-left: 6px solid #facc15;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    white-space: pre-wrap;
    font-size: 0.95rem;
    font-family: 'Courier New', monospace;
}
.support-highlight {
    color: #b45309;
    font-weight: bold;
    margin-top: 1rem;
    font-size: 1rem;
}
button[data-baseweb="tab"] {
    background: white !important;
    border-radius: 8px !important;
    font-weight: bold;
    padding: 10px 20px;
}
@keyframes fadeInDown {
    0% {opacity: 0; transform: translateY(-30px);}
    100% {opacity: 1; transform: translateY(0);}
}
@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-title">Smart Assistant for Research Summarization</div>
<p class='header-subtitle'>Upload research papers and choose your interaction mode: Ask Questions or Take a Challenge</p>
""", unsafe_allow_html=True)

st.sidebar.header("📤 Upload Document")

def hash_file(file):
    file.seek(0)
    file_hash = hashlib.md5(file.read()).hexdigest()
    file.seek(0)
    return file_hash

def convert_markdown_to_html_list(text):
    lines = text.split("\n")
    html_lines = []
    inside_list = False
    for line in lines:
        if line.strip().startswith("* "):
            if not inside_list:
                html_lines.append("<ul>")
                inside_list = True
            html_lines.append(f"<li>{line.strip()[2:].strip()}</li>")
        else:
            if inside_list:
                html_lines.append("</ul>")
                inside_list = False
            if line.strip():
                html_lines.append(f"<p>{line}</p>")
    if inside_list:
        html_lines.append("</ul>")
    return "\n".join(html_lines)

uploaded_file = st.sidebar.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    file_hash = hash_file(uploaded_file)
    doc_id = file_hash

    if f'vectorstore_{doc_id}' not in st.session_state:
        with st.spinner("🔍 Processing document..."):
            text = extract_text(uploaded_file)
            context_for_summary = text[:3000]
            summary = ask_question_with_gemini("Summarize this in under 150 words", context_for_summary)
            chunks = chunk_text(text)
            vectorstore_path = os.path.join("indexes", doc_id)
            os.makedirs("indexes", exist_ok=True)
            build_vectorstore(chunks, savepath=vectorstore_path)
            st.session_state[f'vectorstore_{doc_id}'] = vectorstore_path
            st.session_state[f'summary_{doc_id}'] = summary
            st.session_state['current_doc_id'] = doc_id
    else:
        vectorstore_path = st.session_state[f'vectorstore_{file_hash}']
        summary = st.session_state[f'summary_{file_hash}']
        st.session_state['current_doc_id'] = file_hash

    st.markdown(f"""
    <div class='card'>
        <h4>📄 Auto-Summary</h4>
        <p>{summary}</p>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["💬 Ask Assistant", "🧠 Challenge Me"])
    db = load_vectorstore(st.session_state['vectorstore_' + st.session_state['current_doc_id']])

    # Ask Mode
    with tabs[0]:
        st.subheader("Ask any question about your document")
        query = st.text_input("🔍 Enter your question:", placeholder="What’s the main objective?")
        if query:
            with st.spinner("Thinking..."):
                context = get_relevant_chunks(query, db)
                prompt = f"""
You are an assistant that must answer based only on the given context.
- Provide a concise answer.
- Then extract only the paragraph(s) that justify the answer.
- Wrap those supporting paragraphs in <support>...</support> tags.

Context:
{context}

Question:
{query}
"""
                model = GenerativeModel("gemini-1.5-flash-latest")
                result = model.generate_content(prompt).text
                support_match = re.search(r"<support>(.*?)</support>", result, re.DOTALL)
                support_text = support_match.group(1).strip() if support_match else "No justification found."
                clean_answer = re.sub(r"<support>.*?</support>", "", result, flags=re.DOTALL).strip()
                formatted_answer = convert_markdown_to_html_list(clean_answer)
                formatted_support = convert_markdown_to_html_list(support_text)

            st.markdown(f"""
            <div class='card'>
                <h4>💡 Answer</h4>
                {formatted_answer}
                <div class='support-highlight'>📌 Justification</div>
                <div class='context-snippet-box'>{formatted_support}</div>
            </div>
            """, unsafe_allow_html=True)

    # Challenge Mode
    with tabs[1]:
        st.subheader("Test your understanding with AI-generated questions")
        full_context = get_relevant_chunks("overview and logic", db, k=10)
        if st.button("🎲 Generate Questions"):
            with st.spinner("Crafting challenging questions..."):
                raw_questions = generate_logic_questions(full_context)
                questions = [q.strip(" -•1234567890. ").strip() for q in raw_questions if q.strip()]
                questions = [q for q in questions if len(q.split()) > 5]
                st.session_state["challenge_questions"] = questions[:3]
                st.session_state["challenge_answers"] = ["" for _ in range(len(questions[:3]))]
                st.session_state["feedback_ready"] = False

        if "challenge_questions" in st.session_state:
            for i, q in enumerate(st.session_state["challenge_questions"]):
                st.markdown(f"**Q{i+1}:** {q}")
                st.session_state["challenge_answers"][i] = st.text_area(
                    f"Your Answer to Q{i+1}", value=st.session_state["challenge_answers"][i], key=f"ans_{i}")

            if st.button("✅ Submit Answers"):
                st.session_state["feedback_ready"] = True

        if st.session_state.get("feedback_ready"):
            st.markdown("<h4>📚 AI Feedback</h4>", unsafe_allow_html=True)
            for i, (q, a) in enumerate(zip(st.session_state["challenge_questions"], st.session_state["challenge_answers"])):
                if a.strip():
                    with st.spinner(f"Evaluating answer {i+1}..."):
                        feedback_text, support_text = evaluate_user_answer(q, a, full_context)
                        formatted_feedback = convert_markdown_to_html_list(feedback_text)
                        formatted_support = convert_markdown_to_html_list(support_text)

                    with st.expander(f"📘 Feedback for Q{i+1}"):
                        st.markdown(f"**Your Answer:** {a}")
                        st.markdown("**AI Feedback:**", unsafe_allow_html=True)
                        st.markdown(formatted_feedback, unsafe_allow_html=True)
                        st.markdown("<div class='support-highlight'>📌 Justification</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='context-snippet-box'>{formatted_support}</div>", unsafe_allow_html=True)
else:
    st.info("📄 Please upload a document to begin.")
