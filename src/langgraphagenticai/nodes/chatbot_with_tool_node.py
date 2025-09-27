from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Process the input state and generates a response with tool integration
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # Simulate tool specific logic
        tool_response = f"Tool response for input: '{user_input}'"

        return {"messages": [llm_response, tool_response]}
    
    def create_chatbot(self, tools):
        llm_with_tools = self.llm.bind_tools(tools)
        def node(state):
            return self.chatbot_node(state, llm_with_tools)
        return node

    def chatbot_node(self, state, llm_with_tools):
        """
        chatbot logic for processing the input state and returning a response
        """
        return {"messages": [llm_with_tools.invoke(state["messages"])]}
          
    