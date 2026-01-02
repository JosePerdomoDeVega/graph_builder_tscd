from abc import ABC, abstractmethod
from typing import List


class GraphBuilderInterface(ABC):

    @abstractmethod
    def close_conn(self):
        pass

    @abstractmethod
    def build_graph(self, words: List[str]):
        pass
