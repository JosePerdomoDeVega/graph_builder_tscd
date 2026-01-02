from abc import ABC, abstractmethod


class DictionaryLoaderInterface(ABC):

    @abstractmethod
    def pull_dictionary(self, file_name):
        """
        Get file from dictionary repository.
        """
        pass
