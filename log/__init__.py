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
        client_id = sensitive.CLIENT_ID
        if token in record.getMessage() or client_id in record.getMessage():
            record.message = record.getMessage().replace(token, "[REDACTED]")
            record.message = record.message.replace(client_id, "[REDACTED]")
            filter_logger.info(record.message)
            return False
        return True