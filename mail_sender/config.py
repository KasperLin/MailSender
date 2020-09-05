''' Configuration in `~/.mail_sender_config` '''

import os
import pathlib

from mail_sender.utility import LOG

CONFIG = os.path.join(str(pathlib.Path.home()), ".mail_sender_config")


def get_config(user:str=None):
    ''' Get configurations (acc & psw) from `~/.mail_sender_config` '''

    if not os.path.isfile(CONFIG): 
        LOG.info(f"Create file `~/.mail_sender_config` to save acc & psw.")
        with open(CONFIG, 'w') as f: f.write("")

    with open(CONFIG, 'r') as f: config:str = f.read()
    if "@" not in config: LOG.info(f"Empty config.") ; return dict()

    config:list = [x.split(":") for x in config.split("\n")]
    config:dict = {user: password for user, password in config}

    if user == "all": return config # shortcut for getting the whole config

    elif user is None: # read the first one as default
        user = list(config.keys())[0]
        LOG.info(f"Using default account: {user}")
        password = config[user]
    
    else: # use specified account
        assert isinstance(user, str) and user in config, \
            f"No config of account: {user}"
        password = config[user]

    return user, password


def to_config(user, password) -> None:
    ''' Write config to `~/.mail_sender_config` '''
    config = get_config("all")

    if user in config: LOG.warning(f"Config of {user} will be overwritten.")
    config[user] = password
    
    config:list = [[x, y] for x, y in zip(config.keys(), config.values())]
    config:str  = "\n".join([":".join(x) for x in config])
    with open(CONFIG, 'w') as f: f.write(config)