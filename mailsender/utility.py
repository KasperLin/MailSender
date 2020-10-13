import logging

LOG = logging.getLogger("MS")
handler = logging.StreamHandler(); handler.setFormatter(logging.Formatter(
    fmt='[%(asctime)s][MS %(levelname)s] %(message)s',
    datefmt='%b %d %I:%M',
)) ; LOG.addHandler(handler)