from configparser import ConfigParser


class Config:
    def __init__(self,config_file="./src/agentic_ai/ui/uiconfigfile.ini"):
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(self.config_file)

    def get_llm_options(self):
        """
        Get the LLM options from the config file
        """
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_use_case_options(self):
        """
        Get the use case options from the config file
        """
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_options(self):
        """
        Get the GROQ options from the config file
        """
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        """
        """
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
