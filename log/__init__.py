import logging

import constants
import sensitive

filter_logger = logging.getLogger(__name__)

def get_logger():
    logger = logging.getLogger(__name__)
    logger.addFilter(TokenFilter())
    return logger

class TokenFilter(logging.Filter):
    def filter(self, record):
        token = sensitive.secrets[constants.TOKEN]
        if token in record.getMessage():
            record.message = record.getMessage().replace(token, "[REDACTED]")
            filter_logger.info(record.message)
            return False
        return True