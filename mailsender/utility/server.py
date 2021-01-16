"Utilities for Handling E-mail Servers"

import smtplib

from typing import Optional, Union

from .general import LOG

SERVERS:dict = {
    "smtp.exmail.qq.com": {
        "PORT" : 465, 
        "SMTP" : smtplib.SMTP_SSL, 
        "ALIAS": ["exmail.qq.com", "exmail", "exmail.qq", "tencent", "qq"], 
    }, 
    "smtp.office365.com": {
        "PORT" : 587, 
        "SMTP" : smtplib.SMTP, 
        "ALIAS": ["office365.com", "office365", "outlook", "microsoft", "ms"], 
    }, 
    "smtp.mail.me.com": {
        "PORT" : 587, 
        "SMTP" : smtplib.SMTP, 
        "ALIAS": ["mail.me.com", "icloud", "apple", "mail.me"], 
    }
}


def get_server_name(address:str, alias:Optional[str]=None) -> str:
    "Get ACTUAL Server Name by Address (Or Alias)"
    if alias is None: alias:str = address.split('@')[-1].split('.')[0]
    alias:str = alias.lower() # all aliases are in lower case
    for name in SERVERS:
        if alias in SERVERS[name]["ALIAS"]: 
            LOG.info(f"Server of {address}: {name}")
            return name
    raise RuntimeError(f"Unrecognized server: {address} ({alias})")


def get_server(name:str) -> Union[smtplib.SMTP, smtplib.SMTP_SSL]:
    "Get the Actual Server by Given Server Name"
    method = SERVERS[name]["SMTP"]
    port   = SERVERS[name]["PORT"]
    return method(name, port)
