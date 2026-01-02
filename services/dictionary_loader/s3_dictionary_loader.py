import boto3
from typing import override
from domain.dictionary_loader_interface.dictionary_loader_interface import DictionaryLoaderInterface
from domain.settings import get_settings
from services.logger.logger import get_logger

settings = get_settings()
logger = get_logger()


class S3DictionaryLoader(DictionaryLoaderInterface):

    def __init__(self):

        self.bucket_name = settings.aws_bucket_name
        self.s3_client = boto3.client("s3", region_name=settings.aws_region)


    @override
    def pull_dictionary(self, file_name: str):
        """
        Persist a record in S3 using a date-based prefix.
        """
        dictionary = None
        try:
            dictionary = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=file_name
            )['Body'].read().decode().split()

            logger.info("File successfully pulled from Bucket", bucket=self.bucket_name, key=file_name)

        except Exception as e:
            logger.error("Error while getting S3 object", error=str(e))

        return dictionary
