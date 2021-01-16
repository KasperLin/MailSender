"Utilities of Python email Module"

from datetime import datetime
from typing   import List, Optional

from email.header         import Header
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart

from .css import HTML_HEAD, HTML_TAIL

ENCODING:str = "utf-8"


def get_mail(header:str, from_:str, to:List[str]) -> MIMEMultipart:
    "Get E-Mail Object & Set Header, From & To"
    mail = MIMEMultipart()
    mail["Subject"] = Header(header, ENCODING).encode()
    mail["From"]    = from_
    mail["To"]      = ','.join(to)
    return mail


def get_content(data:Optional[str], dtype:str) -> str:
    "Get Plain Text / HTML E-Mail Content in String"
    if data is None: 
        now :str = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        data:str = f"Hi! This is a mail sent by Python on {now}" 
    if dtype == "html": data = HTML_HEAD + data + HTML_TAIL
    return data    


def mail2str(mail:MIMEMultipart, content:str, str_type:str) -> str:
    "Parse Mail & Content into String"
    mail.attach(MIMEText(content, str_type, ENCODING))
    return mail.as_string()
