from abc import ABC, abstractmethod
from langchain_community import PyPDFLoader



class doc_loader(ABC):
    @abstractmethod
    def load(self, path):
        pass

    @abstractmethod
    def save(self, path, data):
        pass

    @abstractmethod
    def get(self, path):
        pass

    @abstractmethod
    def set(self, path, data):
        pass

class PDFLoader(doc_loader):
    def load(self, path):
        loader = PyPDFLoader(path)
        pages = loader.load()
        return pages

    def save(self, path, data):
        return "PDFLoader.save"

    def get(self, path):
        return "PDFLoader.get"

    def set(self, path, data):
        return "PDFLoader.set"
