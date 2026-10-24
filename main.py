import argparse
import logging
import sys
import traceback
import uuid

from args import parse_arguments
import constants
from workflow import workflow

parser = argparse.ArgumentParser()
logger = logging.getLogger(__name__)

def main():
    args = [a for a in parse_arguments(parser)][0]
    handle_log_level(args)

    try:
        workflow()
    except Exception as e:
        logger.error(traceback.format_exception(e))
        traceback.print_exc()

def handle_log_level(args):
    if not args or not args.log_level:
        return

    run_sequence = uuid.uuid4().hex
    log_format = f"{run_sequence } %(asctime)s %(message)s"
    log = logging.getLogger(__name__)
    logging.basicConfig(
        format=log_format,
        level=args.log_level,
        handlers=[
            logging.FileHandler(constants.PROJECT_NAME + ".log"),
            logging.StreamHandler(sys.stdout)
        ]
    )


if __name__ == '__main__':
    main()