
# Multipurpose Agentic AI 

A modular, agentic application built with LangChain, LangGraph, and Streamlit. This project enables advanced conversational AI using Groq either with a basic chatbot or with tool-augmented capabilities, including web search, Wikipedia, Arxiv, and more. 

---

## 🚀 Live Demo

Access the deployed app here:  
**[https://multipurpose-agentic-ai-juoua4sc9dhn5uga2qqopg.streamlit.app/](https://multipurpose-agentic-ai-juoua4sc9dhn5uga2qqopg.streamlit.app/)**

---

## Features

- **Basic Chatbot**: LLM-powered conversational agent.
- **Chatbot with Tools**: Enhanced with search tools (Tavily, Wikipedia, Arxiv, etc.).
- **Streamlit UI**: Interactive chat interface with tool call transparency.
- **LangGraph Integration**: Modular graph-based agent orchestration.
- **Groq LLM Support**: Easily switch between Groq models.

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/AshutoshSingh1028/Multipurpose-Agentic-AI.git
cd AgenticAIWorkspace/AgenticRAGProject
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the App Locally
```bash
streamlit run app.py
```

---

## Configuration

- **API Keys:**
	- **Groq**: Required for LLM access.
	- **Tavily**: Required for search tool integration.
	Enter these in the Streamlit sidebar when prompted.

- **Model & Use Case Selection:**
	Choose your preferred LLM and use case (Basic Chatbot or Chatbot with Tool) from the sidebar.

---

## How It Works

- The app uses a modular graph-based approach to orchestrate agentic workflows.
- For the "Chatbot with Tool" use case, it integrates external tools (search, Wikipedia, Arxiv) into the conversation flow.
- The UI is built with Streamlit for interactive chat and tool transparency.
