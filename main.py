from domain.settings import get_settings
from services.logger.logger import get_logger
from application.provider.graph_builder_provider import get_graph_builder
from application.provider.dictionary_loader_provider import get_dictionary_loader

if __name__ == '__main__':
    settings = get_settings()
    logger = get_logger()

    with logger.span("Building new Words Graph"):
        dictionary_loader = get_dictionary_loader()
        logger.info(f"Pulling last version of dictionary with {settings.dictionary_loader_implementation}")
        graph_builder = get_graph_builder()
        logger.info(f"Building new Words Graph with {settings.graph_builder_implementation}")


        dictionary = dictionary_loader.pull_dictionary(settings.dictionary_file_last_version)
        graph_builder.build_graph(dictionary)
