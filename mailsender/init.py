''' Initialize & Connect to the E-mail Server '''

import logging

import mailsender as ms

from mailsender.utility import LOG
from mailsender.config  import get_config, to_config
from mailsender.server  import get_server, login_server


class MailSender():

    def __init__(
        self, sender:str=None, password:str=None, server:str="qq",
        logging_level:int=logging.INFO,
    ) -> None:
        self.set_logging_level(logging_level)

        LOG.info(f"<<< Mail Sender {ms.__version__} >>>")

        user, password = self.config(sender, password)

        if server is None: server = user.split("@")[-1].split(".")[0]
        try   : self.server = get_server(server)
        except: raise RuntimeError("Fail to connect to server.")

        self.sender = user
        try   : self.server = login_server(self.server, self.sender, password)
        except: raise RuntimeError("Fail to login to server.")

    def set_logging_level(self, level:int) -> None: LOG.setLevel(int(level))


    def config(self, user:str, password:str) -> None:
        ''' Fetch (& save) e-mail account & password '''
        config = get_config("all")

        # Without a password, we can only read config
        if password is None: user, password = get_config(user)

        # If a password is given, there must be a user as well.
        else:
            if user in config: LOG.warning(f"""
            Account {user} is already in the config, 
            you should use it without passing password explicitly.
            """)
            assert isinstance(user, str) and user, \
                "User must be given when password is given."
            # Save to config since it maybe a new one.
            to_config(user, password)

        return user, password


    def get_server(self): return self.server