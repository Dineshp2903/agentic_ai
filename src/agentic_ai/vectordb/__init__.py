from abc import ABC, abstractmethod
from typing import List, Dict, Any
import faiss
import numpy as np


class AbstractVectorDB(ABC):

    @abstractmethod
    def add_documents(self, documents: List[Any]):
        """Add documents to the vector database."""
        pass

    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> List[Any]:
        """Search the database using a query and return the top_k results."""
        pass

    @abstractmethod
    def delete_document(self, doc_id: str):
        """Delete a document from the database using its ID."""
        pass

    @abstractmethod
    def get_document(self, doc_id: str) -> Any:
        """Retrieve a document by its ID."""
        pass

class FAISSVectorDB(AbstractVectorDB):

    def __init__(self,  embedding_dim: int):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents = {}  # Store doc_id -> text

    def load(self, documents: List[dict]):
        vectors = np.array([doc["vector"] for doc in documents], dtype="float32")
        self.index.add(vectors)
        for doc in documents:
            self.documents[doc["id"]] = doc["text"]

    def save(self, path: str, data: List[Dict[str, Any]]) -> None:
        return "FAISSVectorDB.save"

    def get(self, path: str) -> List[Dict[str, Any]]:
        return "FAISSVectorDB.get"

    def set(self, path: str, data: List[Dict[str, Any]]) -> None:
        return "FAISSVectorDB.set"