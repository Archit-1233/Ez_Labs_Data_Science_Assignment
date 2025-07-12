<h1 align="center">🧠 GenAI Research Assistant</h1>

<p align="center">
  A beautifully designed AI assistant to summarize research papers, answer context-based questions, and challenge users with logic-based quizzes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20by-Gemini-ffca28?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-e74c3c?style=for-the-badge&logo=streamlit" />
</p>

## 🎬 Live Demo

[![Watch Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

> 🔗 Click the image above to watch a short demo walkthrough.

## ✨ Features

- 📄 **150-word Summary** auto-generated upon document upload
- 💬 **"Ask Anything"** mode with context-based responses and highlighted justifications
- 🧠 **"Challenge Me"** mode for AI-generated logic questions and feedback
- 🎨 Polished **animated UI** using CSS and gradients
- 🔄 Smooth mode switching without losing session state

## 🖼️ Screenshots

### 📥 Upload Document + Auto-Summary

<p align="center">
  <img src="<img width="1918" height="784" alt="Screenshot 2025-07-12 141713" src="https://github.com/user-attachments/assets/e4375ec2-d924-4957-83a2-6d4a5b38a357" />
" alt="Upload and Summary View" width="80%"/>
</p>

### 💬 Ask Anything with Justified Answer

<p align="center">
  <img src="<img width="1909" height="910" alt="Screenshot 2025-07-12 141802" src="https://github.com/user-attachments/assets/06a18b3a-346f-4108-a197-bd774c2f3750" />
" alt="Ask Anything Mode" width="80%"/>
</p>


### 🧠 Challenge Me: Questions

<p align="center">
  <img src="" alt="<img width="1426" height="380" alt="Screenshot 2025-07-12 142601" src="https://github.com/user-attachments/assets/7ee189b0-4800-4760-9ab1-5443a5c9fc8b" />
" width="80%"/>
</p>

<p align="center">
  <img src="" alt="<img width="1426" height="380" alt="<img width="1308" height="697" alt="Screenshot 2025-07-12 142642" src="https://github.com/user-attachments/assets/d541914b-830a-4434-bd1b-4ece29a427ac" />
" />
" width="80%"/>
</p>

<p align="center">
  <img src="" alt="<img width="1426" height="380" alt="<img width="1308" height="697"  alt="Screenshot 2025-07-12 142615" src="https://github.com/user-attachments/assets/a0fb6444-5c5c-4bc2-8066-641e6d3e297c" />
" />
" width="80%"/>
</p>

<p align="center">
  <img src="" alt="<img width="1426" height="380" alt="<img width="1308" height="697"  alt="Screenshot 2025-07-12 142655" src="https://github.com/user-attachments/assets/6465e637-ee7f-4aeb-8cda-17cf181af1eb" />
" />
" width="80%"/>
</p>





### 📚 Challenge Me: AI Feedback

<p align="center">
  <img src="screenshots/challenge_feedback.png" alt="Challenge Mode Feedback" width="80%"/>
</p>

---

## 🏗️ Architecture Overview

```mermaid
flowchart TD
    A[Upload PDF/TXT] --> B[Extracted Text]
    B --> C[Text Chunking]
    C --> D[FAISS Vector Store]
    D --> E1[Ask Mode]
    D --> E2[Challenge Mode]
    E1 --> F1[Gemini ↔ Answer + Justification]
    E2 --> F2[Gemini ↔ Questions + Evaluation]
