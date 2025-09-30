from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.arxiv import ArxivAPIWrapper
from langchain_community.tools.arxiv.tool import ArxivQueryRun

def get_tools():
    """
    Return the list of tools to be used in the chatbot.
    """
    tools = [TavilySearchResults(max_results=2), WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()), ArxivQueryRun(api_wrapper=ArxivAPIWrapper())]
    return tools

def create_tool_node(tools):
    """
    Creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools) 