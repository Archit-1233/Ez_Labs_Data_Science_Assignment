<h1 align="center">🧠 GenAI Research Assistant</h1>

<p align="center">
  A beautifully designed AI assistant to summarize research papers, answer context-based questions, and challenge users with logic-based quizzes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20by-Gemini-ffca28?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-e74c3c?style=for-the-badge&logo=streamlit" />
</p>

## 📸 Overview of the App

<p align="center">
  <img width="100%" src="https://github.com/user-attachments/assets/da985324-28c5-4334-b500-e357277cfec7" alt="Overview Screenshot" />
</p>

## 🎬 Live Demo

<p align="center">
  <a href="https://drive.google.com/file/d/1OdmuD3efuyYuXGxLmhkx3xfq8Y55RGKJ/view?usp=sharing" target="_blank">
    <img width="70%" src="https://github.com/user-attachments/assets/e4375ec2-d924-4957-83a2-6d4a5b38a357" alt="Click to Watch Demo Video"/>
  </a>
</p>

> 🔗 Click the image above to watch a 2–3 min walkthrough video hosted on Google Drive.

## ✨ Features

- 📄 **Auto-Summarization**: Instantly generates a ~150-word summary on upload  
- 💬 **Ask Anything**: Ask deep questions with AI-generated answers + highlighted justifications  
- 🧠 **Challenge Me**: Test yourself with logic-based AI questions and get smart feedback  
- 🎨 **Elegant UI**: Animated, gradient-rich, and cleanly styled layout  
- 🔄 **Switch Seamlessly**: Switch modes without losing your session data  

## 🧠 Architecture Overview

```mermaid
flowchart TD
    Upload["📥 Upload PDF / TXT"] --> OCR["🔍 Text Extraction (Mistral OCR)"]
    OCR --> Chunk["🧩 Text Chunking"]
    Chunk --> Embed["📐 Generate Embeddings"]
    Embed --> VectorDB["🗂️ FAISS Vector Store"]

    VectorDB --> AskMode["💬 Ask Mode"]
    VectorDB --> ChallengeMode["🧠 Challenge Mode"]

    AskMode --> Retrieval["📥 Retrieve Relevant Chunks"]
    Retrieval --> Gemini["🔮 Gemini LLM (Answer + Justification)"]
    Gemini --> Answer["📑 Return Answer & Supporting Paragraphs"]

    ChallengeMode --> Retrieval
    Retrieval --> QAgen["❓ Generate Logical Questions"]
    QAgen --> Eval["📚 Evaluate User Answers"]
```

## 🖼️ Screenshots

### 📥 Upload Document + Auto-Summary
<p align="center">
  <img src="https://github.com/user-attachments/assets/e4375ec2-d924-4957-83a2-6d4a5b38a357" alt="Upload and Summary View" width="100%"/>
</p>

### 💬 Ask Anything with Justified Answer
<p align="center">
  <img src="https://github.com/user-attachments/assets/06a18b3a-346f-4108-a197-bd774c2f3750" alt="Ask Anything Mode" width="100%"/>
</p>

### 🧠 Challenge Me: Logic-Based Questions
<p align="center">
  <img src="https://github.com/user-attachments/assets/7ee189b0-4800-4760-9ab1-5443a5c9fc8b" alt="Challenge Question 1" width="100%"/>
</p>

### 🧠 Challenge Me: AI Feedback
<p align="center">
  <img src="https://github.com/user-attachments/assets/d541914b-830a-4434-bd1b-4ece29a427ac" alt="Challenge Question 2" width="100%"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/a0fb6444-5c5c-4bc2-8066-641e6d3e297c" alt="Challenge Question 3" width="100%"/>
</p>

### 🧠 Challenge Me: AI Feedback
<p align="center">
  <img src="https://github.com/user-attachments/assets/6465e637-ee7f-4aeb-8cda-17cf181af1eb" alt="Challenge Question 4" width="100%"/>
</p>
