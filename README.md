<h1 align="center">🧠 GenAI Research Assistant</h1>

<p align="center">
  A visually polished AI assistant to summarize research papers, answer context-based questions, and challenge users with logic-based quizzes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20by-Gemini-ffca28?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-e74c3c?style=for-the-badge&logo=streamlit" />
</p>

---

## 🎬 Live Demo

[![Watch Demo](https://img.youtube.com/vi/YOUR_YOUTUBE_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID)

> 🔗 Click the thumbnail to watch a 2-minute walkthrough of the app in action.

---

## ✨ Features

- 📄 Auto-summary under 150 words when a document is uploaded
- 💬 Ask Anything mode with paragraph-level justification using `<support>` tagging
- 🧠 Challenge Me mode with logic-based AI-generated questions & contextual feedback
- 🌈 Responsive UI with custom CSS animations
- 🔁 Seamless tab switching without losing uploaded state

---

## 🏗️ Architecture Overview

```mermaid
flowchart TD
    A[User Uploads PDF/TXT] --> B[Extracted Text]
    B --> C[Text Chunking]
    C --> D[FAISS Vector Store]
    D --> E1[Ask Anything]
    D --> E2[Challenge Me]
    E1 --> F1[Gemini ↔ Answer + Justification]
    E2 --> F2[Gemini ↔ Generate Qs + Evaluate User Input]
