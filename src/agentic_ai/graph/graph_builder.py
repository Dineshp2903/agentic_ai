from langgraph.graph import StateGraph,START,END,MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.agentic_ai.state.state import State
from src.agentic_ai.state.state import State
from src.agentic_ai.nodes.basic_chatbot_node import BasicChatBotNode
from src.agentic_ai.nodes.chatbot_with_toolnode import ChatBotWithToolNode
from src.agentic_ai.tools.search_tool import get_tools, create_tool_node



class GraphBuilder:

    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_grpah(self):
        """
        Create a basic chatbot node
        """
        self.chatbot_node = BasicChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def chatbot_with_tool_build_graph(self):
        """
        Create a chatbot with tool integration
        """

        tools = get_tools()

        tool_node = create_tool_node(tools)

        ###LLM
        llm = self.llm

        obj_chatbot_with_node = ChatBotWithToolNode(llm)

        create_chat_bot = obj_chatbot_with_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot",create_chat_bot)
        self.graph_builder.add_node("tools",tool_node)


        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")

        self.graph_builder.add_edge("chatbot",END)


    def setup_graph(self,usecase):
        """
        Setup the query
        """
        if usecase ==  "Basic Chatbot":
            self.basic_chatbot_build_grpah()

        if usecase == "Chatbot with Tool":
            # tools = get_tools()
            self.chatbot_with_tool_build_graph()

        return self.graph_builder.compile()
        