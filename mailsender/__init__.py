"Import API, Set Logging Level as Info & Self-Introduce"

from .core import MailSender

__version__ = "0.3.0"


def _self_introduce() -> None:
    "Set Logging Level as Info & Report Current Version"
    import logging; from .utility import LOG
    LOG.setLevel(logging.INFO)
    LOG.info(f"<<< Mail Sender {__version__} >>>")


_self_introduce()
