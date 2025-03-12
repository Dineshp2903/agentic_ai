from src.agentic_ai.state.state import State

class ChatBotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """
    def init(self,model):
        self.llm = model

    def process(self,state:State) -> dict:
        """
        Process the input state and generate the response
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role":"user","content":user_input}])
        tools_response = f"Tools Integration for :{user_input}"

        return {"messages":[llm_response,tools_response]}
    
    def create_chatbot(self,tools):
        """
        Create a chatbot with tool integration
        """
        llm_with_tools = self.llm.bind_tools(tools)
        def chatbot_node(state:State):
            return {"messages":llm_with_tools.invoke(state["messages"])}
        
        return chatbot_node