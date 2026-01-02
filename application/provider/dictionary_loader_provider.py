from domain.settings import get_settings
from services.logger.logger import get_logger
from services.dictionary_loader.s3_dictionary_loader import S3DictionaryLoader
from domain.dictionary_loader_interface.dictionary_loader_interface import DictionaryLoaderInterface

logger = get_logger()


def get_dictionary_loader() -> DictionaryLoaderInterface:
    settings = get_settings()
    if settings.dictionary_loader_implementation == "AWS_S3":
        return S3DictionaryLoader()
    return None
