"Initialize The Mail Sender Class"

import logging
import smtplib

from typing import Optional, Tuple

from ..config  import Configurator
from ..utility import LOG, get_server


class MailSender():
    "A Friendly Python E-mail Sending Tool"

    def __init__(
        self,
        account :str = None,
        password:str = None,
        server  :str = None, 
        logging_level:int=logging.INFO
    ) -> None:
        "Set Logging Level, Acc, Psw & Server, Create & Login to Server"
        LOG.setLevel(logging_level)
        self.acc, self.psw, self.svr = self._get_account_password_server \
            (account, password, server)
        try   : self.server = get_server(self.svr)
        except: raise RuntimeError(f"Fail to connect to server: {self.svr}")
        try   : self._login()
        except: raise RuntimeError(f"Fail to login ({self.svr}): {self.acc}")


    @staticmethod
    def _get_account_password_server(
        acc:Optional[str], 
        psw:Optional[str], 
        svr:Optional[str], 
    ) -> Tuple[str]:
        "Get E-Mail Account from User/Config"
        all_none = lambda check: all(x is None for x in check)
        nothing_given = all_none((acc, psw, svr))
        given_account = acc is not None and all_none((psw, svr))
        both_given    = acc is not None and psw is not None
        config = Configurator()
        if   nothing_given: acc, psw, svr = config.first()
        elif given_account: acc, psw, svr = config.lookup(acc)
        elif both_given   : acc, psw, svr = config.record(acc, psw, svr)
        else: raise NotImplementedError("""
        Either:
        * Pass nothing to use the first config as default
        * Pass e-mail account & look-up in the config file
        * Pass both e-mail account & password (& server) to record in config
        """)
        return acc, psw, svr
    

    def _login(self) -> None:
        "Login `self.server` by Given Acc & Psw"
        over_SSL:bool = isinstance(self.server, smtplib.SMTP_SSL)
        is_SMTP :bool = isinstance(self.server, smtplib.SMTP)
        if   over_SSL: self.server.login(self.acc, self.psw)
        elif is_SMTP : self._login_smtp(self.server, self.acc, self.psw)
    

    @staticmethod
    def _login_smtp(server, acc:str, psw:str) -> None:
        "Log-in Given Server Via SMTP by Given Acc & Psw"
        server.ehlo(); server.starttls(); server.ehlo()
        server.login(acc, psw)
