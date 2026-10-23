import argparse
import logging

import constants

def parse_arguments(parser: argparse.ArgumentParser):
    create_arguments(parser)
    yield parser.parse_args()


def create_arguments(parser):
    parser.add_argument("--log-level", choices=[str(l) for l in logging.getLevelNamesMapping()], default=logging.INFO)



