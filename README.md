
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

## Project Structure

```
AgenticRAGProject/
├── app.py                  # Streamlit app entry point
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── src/
	└── langgraphagenticai/
		├── tools/          # Tool implementations (search, summarizer, etc.)
		├── nodes/          # Agent node logic
		├── graph/          # Graph builder and orchestration
		├── ui/             # Streamlit UI components
		└── ...
```

---

## License

This project is for educational and research purposes. See `LICENSE` for details if provided.

---
