<h1 align="center">🧠 GenAI Research Assistant</h1>

<p align="center">
  A beautifully designed AI assistant to summarize research papers, answer context-based questions, and challenge users with logic-based quizzes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20by-Gemini-ffca28?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-e74c3c?style=for-the-badge&logo=streamlit" />
</p>

---

## 🎬 Live Demo

[![Watch Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

> 🔗 Click the image above to watch a 2–3 min walkthrough video.

---

## ✨ Features

- 📄 **Auto-Summarization**: Generates a concise 150-word summary instantly upon upload.
- 💬 **Ask Anything**: Pose questions with AI-generated answers and highlighted justifications.
- 🧠 **Challenge Me**: Get logic-based questions from the document and receive smart feedback.
- 🎨 **Elegant UI**: Animated, intuitive interface with gradient visuals and smooth transitions.
- 🔄 **Switch Modes Seamlessly**: Move between "Ask" and "Challenge" without session loss.

---

## 🖼️ Screenshots

### 📥 Upload Document + Auto-Summary

<p align="center">
  <img src="https://github.com/user-attachments/assets/e4375ec2-d924-4957-83a2-6d4a5b38a357" alt="Upload and Summary View" width="100%"/>
</p>

---

### 💬 Ask Anything with Justified Answer

<p align="center">
  <img src="https://github.com/user-attachments/assets/06a18b3a-346f-4108-a197-bd774c2f3750" alt="Ask Anything Mode" width="100%"/>
</p>

---

### 🧠 Challenge Me: Logic-Based Questions

<p align="center">
  <img src="https://github.com/user-attachments/assets/7ee189b0-4800-4760-9ab1-5443a5c9fc8b" alt="Challenge Question 1" width="100%"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/d541914b-830a-4434-bd1b-4ece29a427ac" alt="Challenge Question 2" width="100%"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/a0fb6444-5c5c-4bc2-8066-641e6d3e297c" alt="Challenge Question 3" width="100%"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/6465e637-ee7f-4aeb-8cda-17cf181af1eb" alt="Challenge Question 4" width="100%"/>
</p>

---

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
