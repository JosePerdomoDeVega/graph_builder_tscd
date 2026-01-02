from domain.settings import get_settings
from services.graph_builder.neo4j_graph_builder import Neo4jGraphBuilder
from domain.graph_builder.graph_builder_interface import GraphBuilderInterface


def get_graph_builder() -> GraphBuilderInterface:
    settings = get_settings()
    if settings.graph_builder_implementation == "NEO4J":
        return Neo4jGraphBuilder()
    return None
