''' Connect to the E-mail Server Specified '''

import smtplib

from mailsender.utility import LOG

SERVER = {
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


def get_server(alias:str):
    ''' Get the E-mail server by its alias '''
    HOST = PORT = None
    for host in SERVER:
        if alias.lower() in SERVER[host]["ALIAS"]:
            HOST, PORT = host, SERVER[host]["PORT"]
            LOG.info(f"Server : {HOST}")
            return SERVER[host]["SMTP"](HOST, PORT)
    raise RuntimeError(f"Unrecognized server: {alias}")


def login_server(server, user, password):
    ''' Login to the E-mail server by given user name & password '''
    LOG.info(f"Sender : {user}")
    
    if isinstance(server, smtplib.SMTP_SSL):
        server.login(user, password)
    
    elif isinstance(server, smtplib.SMTP):
        server.ehlo() ; server.starttls() ; server.ehlo()
        server.login(user, password)
    
    return server