import logging
import mailsender as ms

from mailsender.utility import LOG
from mailsender.send    import MailSender # entry point

__version__ = "0.2.4.2"

LOG.setLevel(logging.INFO)
LOG.info(f"<<< Mail Sender {ms.__version__} >>>")