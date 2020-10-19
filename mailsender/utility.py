import logging

LOG = logging.getLogger("MS")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    fmt     = '[%(asctime)s][MS %(levelname)s] %(message)s',
    datefmt = '%m-%d %H:%M',
)) ; LOG.addHandler(handler)