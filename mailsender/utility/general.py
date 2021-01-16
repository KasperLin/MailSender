"General Utilities for Project Mail Sender"

import logging


def _get_LOG() -> logging.Logger:
    "Get Logger for Mail Sender called 'MS'"
    LOG:logging.Logger = logging.getLogger("MS")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        fmt = '[%(asctime)s][MS %(levelname)s] %(message)s', 
        datefmt = '%m-%d %H:%M', 
    )); LOG.addHandler(handler)
    return LOG


LOG:logging.Logger = _get_LOG()
