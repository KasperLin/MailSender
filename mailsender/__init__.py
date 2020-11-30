import logging

import mailsender as ms
from mailsender.send import MailSender  # entry point
from mailsender.utility import LOG

__version__ = "0.2.7.2"

LOG.setLevel(logging.INFO)
LOG.info(f"<<< Mail Sender {ms.__version__} >>>")
