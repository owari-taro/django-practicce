from django.core.files.uploadedfile import UploadedFile

from logging import getLogger

logger=getLogger(__name__)

def message(text:str):
    logger.info(text)
    logger.debug(text)
    logger.critical(text)