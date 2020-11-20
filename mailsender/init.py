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

        try   : server, self.server = get_server(server, self.sender)
        except: raise RuntimeError("Fail to connect to server.")

        try   : self.server = login_server(self.server, self.sender, psw)
        except: raise RuntimeError("Fail to login to server.")

        config[self.sender]["server"] = server # record server
        write_config(config) # only write after successful connection


    def get_server(self): return self.server


def _parse_accpsw(acc:str, psw:str, config:dict) -> tuple:
    ''' Read Acc&Psw from Config File or User & Write them Back '''
    nothin_given:bool = acc is None and psw is None
    only_account:bool = acc is not None and psw is None
    both_given  :bool = acc is not None and psw is not None
    if   nothin_given: acc, psw = __use_first_account(config)
    elif only_account: acc, psw = __look_up_config(config, acc)
    elif both_given  : 
        if acc in config: LOG.info(f"(No need to specify password for {acc})")
        else            : config = __record_new(acc, psw, config)
    else: raise AssertionError
    return acc, psw, config

def __use_first_account(config:dict) -> tuple:
    ''' Send by the first account in the config if nothing given '''
    assert config, "Acc & psw must be given."
    acc:str = list(config.keys())[0]
    psw:str = config[acc]["psw"]; return acc, psw

def __look_up_config(config:dict, acc:str) -> tuple:
    ''' Look Up Config for Given Account if Only Acc is Given '''
    assert acc in config, f"Need the password of account: {acc}"
    psw:str = config[acc]["psw"]; return acc, psw

def __record_new(acc:str, psw:str, config:dict) -> dict:
    ''' Record New Acc&Psw in Config '''
    config[acc] = {"psw": psw, "server": ""}
    LOG.info(f"Record new account info: {acc}")
    return config