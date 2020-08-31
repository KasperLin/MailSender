''' Initialize & Connect to the E-mail Server '''

import os
import logging
import pathlib

from mail_sender.utility import LOG
from mail_sender.server  import get_server, login_server

CONFIG = os.path.join(str(pathlib.Path.home()), ".mail_sender_config")


class MailSender():

    def __init__(
        self, sender:str=None, password:str=None, server:str=None,
        logging_level:int=logging.INFO,
    ) -> None:
        self.set_logging_level(logging_level)

        user, password = self.config(sender, password)

        if server is None: server = user.split("@")[-1].split(".")[0]
        self.server = get_server(server)

        self.sender = user
        self.server = login_server(self.server, self.sender, password)


    def set_logging_level(self, level:int) -> None:
        ''' Set the logging level of the module '''
        LOG.setLevel(int(level))


    def get_config(self) -> dict:
        ''' Get configurations (acc & psw) from `~/.mail_sender_config` '''
        if not os.path.isfile(CONFIG): 
            LOG.info(f"Create `~/.mail_sender_config` config file.")
            with open(CONFIG, 'w') as f: f.write("")
        with open(CONFIG, 'r') as f: config:str = f.read()
        if "@" not in config: LOG.info(f"Empty config.") ; config = dict()
        else:
            config:list = [x.split(":") for x in config.split("\n")]
            config:dict = {user: password for user, password in config}
        return config


    def get_config_user_password(self, user:str=None) -> tuple:
        config = self.get_config()

        if user is None:
            user = list(config.keys())[0]
            LOG.info(f"Using default config: {user}")
            password = config[user]

        else:
            assert isinstance(user, str)
            assert user in config, f"No config of {user}"
            password = config.get(user, None)

        return user, password


    def config(self, user:str, password:str) -> None:
        ''' Save e-mail account & password to `~/.mail_sender_config` '''
        if password is None:
            user, password = self.get_config_user_password(user)
        else:
            assert isinstance(user, str), "User must be given."
            self.to_config(user, password)
        return user, password


    def to_config(self, user, password) -> None:
        ''' Write config to `~/.mail_sender_config` '''
        config = self.get_config()
        config[user] = password
        config:list = [[x, y] for x, y in zip(config.keys(), config.values())]
        config:str  = "\n".join([":".join(x) for x in config])
        with open(CONFIG, 'w') as f: f.write(config)


    def get_server(self): return self.server