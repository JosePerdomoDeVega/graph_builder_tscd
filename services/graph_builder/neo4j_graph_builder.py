from neo4j import GraphDatabase
from domain.graph_builder.graph_builder_interface import GraphBuilderInterface
from domain.settings import get_settings
from services.logger.logger import get_logger
from typing import List, override

logger = get_logger()
settings = get_settings()


class Neo4jGraphBuilder(GraphBuilderInterface):
    def __init__(self):
        uri = settings.neo4j_uri
        user = settings.neo4j_user
        password = settings.neo4j_password
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    @override
    def close_conn(self):
        self.driver.close()

    @staticmethod
    def one_letter_diff(word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        diff = sum(c1 != c2 for c1, c2 in zip(word1, word2))
        return diff == 1

    @override
    def build_graph(self, words: List[str]):
        edges = 0
        try:
            with self.driver.session() as session:
                for word in words:
                    session.run("MERGE (w:Word {value: $value})", value=word)

                for i, word1 in enumerate(words):
                    for word2 in words[i + 1:]:
                        if self.one_letter_diff(word1, word2):
                            session.run(
                                """
                                MATCH (a:Word {value: $w1}), (b:Word {value: $w2})
                                MERGE (a)-[:CONNECTED]->(b)
                                """,
                                w1=word1, w2=word2
                            )
                            edges += 1
        except Exception as e:
            logger.error("Error while building graph", error=str(e))
        logger.info(f"Graph successfully built with {len(words)} nodes and {edges} edges")
