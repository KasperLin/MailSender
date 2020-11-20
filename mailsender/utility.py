import logging

from pathlib              import Path
from email.header         import Header
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart

LOG:logging.Logger = logging.getLogger("MS")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    fmt     = '[%(asctime)s][MS %(levelname)s] %(message)s',
    datefmt = '%m-%d %H:%M',
)) ; LOG.addHandler(handler)


def get_HOME() -> str:
    ''' Get Home Directory (`~/`) Path '''
    return str(Path.home())


def get_Message() -> MIMEMultipart:
    ''' Get E-mail Message Object '''
    return MIMEMultipart()


def get_Header(title:str, encoding:str) -> str:
    ''' Get E-mail Header '''
    return Header(title, encoding).encode()


def get_Email(
    message:MIMEMultipart, content:str, dtype:str, encoding:str, 
) -> str:
    ''' Get the Whole E-mail in String '''
    message.attach(MIMEText(content, dtype, encoding))
    return message.as_string()