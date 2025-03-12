from src.agentic_ai.state.state import State


class BasicChatBotNode:
    def __init__(self,model):
        self.llm = model

    def process(self,state:State) -> dict:
        """
        Process the input state and generate the response
        
        """
        return {"messages":self.llm.invoke(state["messages"])}