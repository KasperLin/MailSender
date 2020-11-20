''' Connect to the E-mail Server Specified '''

import smtplib

from mailsender.utility import LOG

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


def get_server(alias:str, address:str):
    ''' Get the E-mail server by its alias '''
    alias:str = _get_server_alias(alias, address)
    for name in SERVERS:
        server:dict = SERVERS[name]
        if alias in server["ALIAS"]:
            LOG.info(f"Server : {name}")
            method   = server["SMTP"]
            port:int = server["PORT"]
            return method(name, port)
    raise RuntimeError(f"Unrecognized server: {alias}")


def _get_server_alias(alias:str, address:str) -> str:
    ''' Get Server Name by Alias or Address '''
    # Guess server by <user>@<server>.com
    if alias is None: alias:str = address.split('@')[-1].split('.')[0]
    return alias.lower()


def login_server(server, acc, psw):
    ''' Login to the E-mail server by given acc & psw '''
    LOG.info(f"Sender : {acc}")
    if   isinstance(server, smtplib.SMTP_SSL): server.login(acc, psw)
    elif isinstance(server, smtplib.SMTP)    : server=_login(server, acc, psw)
    return server


def _login(server, acc, psw):
    ''' Login to a SMTP server '''
    server.ehlo() ; server.starttls() ; server.ehlo()
    server.login(acc, psw); return server