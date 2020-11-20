''' Initialize & Connect to the E-mail Server '''

import logging

from mailsender.utility import LOG
from mailsender.server  import get_server, login_server
from mailsender.config  import read_config, write_config


class MailSender():
    ''' A Friendly Python E-mail Sending Tool '''

    def __init__(self, 
        account :str=None, 
        password:str=None, 
        server  :str="qq",
        logging_level:int=logging.INFO,
    ) -> None:
        LOG.setLevel(logging_level)
        config:dict = read_config()
        self.sender, psw, config = _parse_accpsw(account, password, config)

        try   : self.server = get_server(server, self.sender)
        except: raise RuntimeError("Fail to connect to server.")

        try   : self.server = login_server(self.server, self.sender, psw)
        except: raise RuntimeError("Fail to login to server.")

        write_config(config) # only write after successful connection


    def get_server(self): return self.server


def _parse_accpsw(acc:str, psw:str, config:dict) -> tuple:
    ''' Read Acc&Psw from Config File or User & Write them Back '''
    nothin_given:bool = acc is None and psw is None
    only_account:bool = acc is not None and psw is None
    both_given  :bool = acc is not None and psw is not None
    if nothin_given: 
        assert config, "Acc & psw must be given."
        acc:str = list(config.keys())[0]
        psw:str = config[acc]
    elif only_account:
        assert acc in config, f"Need the password of account: {acc}"
        psw:str = config[acc]
    elif both_given:
        if acc in config: 
            LOG.info(f"You don't need to specify the password of {acc}")
        config[acc] = psw # write it down
    return acc, psw, config