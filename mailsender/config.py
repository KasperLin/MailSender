''' Read & Write Configuration in `~/.mailsender_config` '''

import os

from pathlib import Path

PATH:str = os.path.join(str(Path.home()), ".mailsender_config")


def read_config() -> dict:
    ''' Read `~/.mailsender_config` '''
    with open(PATH) as f: data:str = f.read()
    if data == "": data = dict() # empty config file
    else: data:dict = _str2dict(data)
    return data


def write_config(data:dict) -> None:
    ''' Write Config Back to `~/.mailsender_cofig` '''
    data:str = _dict2str(data)
    with open(PATH, 'w') as f: f.write(data)


def _str2dict(data:str) -> dict:
    ''' Parse Raw Config File into Dict: {Acc: Psw} '''
    # Config format : acc@host.com:psw \n ...
    data:list = [x.split(':') for x in data.split('\n')]
    data:dict = {acc: psw for acc, psw in data}
    return data

def _dict2str(data:dict) -> str:
    ''' Parse Config Dict Back to Str: acc:psw '''
    data:list = [[x, y] for x, y in zip(data.keys(), data.values())]
    data:str  = '\n'.join([':'.join(x) for x in data])
    return data


# def get_config(acc:str, psw:str=None) -> tuple:
#     ''' Read/Write Acc&Psw Info in `~/.mailsender_config` '''
#     config:dict = _read() if os.path.isfile(PATH) else dict()
#     if acc is None:
#         if not config: raise AssertionError("No account config yet.")
#         acc:str = list(config.keys())[0] # read the first one as default
#         psw:str = config[acc]
#     else:
#         assert acc in config, f"No config of account: {acc}"
#         psw:str = config[acc]
#     return acc, psw


# def get_accpsw_from_config(user:str, password:str) -> tuple:
#     ''' Fetch (& save) e-mail account & password '''
#     config = get_config("all")

#     # Without a password, we can only read config
#     if password is None: user, password = get_config(user)

#     # If a password is given, there must be a user as well.
#     else:
#         if user in config: LOG.warning(f"""
#         Account {user} is already in the config,
#         you should use it without passing password explicitly.
#         """)
#         assert isinstance(user, str) and user, \
#             "User must be given when password is given."
#         # Save to config since it maybe a new one.
#         to_config(user, password)

#     return user, password


# def get_config(user:str=None):
#     ''' Get configurations (acc & psw) from `~/.mailsender_config` '''

#     if not os.path.isfile(PATH):
#         LOG.info(f"Create file `~/.mailsender_config` to save acc & psw.")
#         with open(PATH, 'w') as f: f.write("")

#     with open(PATH, 'r') as f: config:str = f.read()
#     if "@" not in config: LOG.info(f"Empty config.") ; return dict()

#     config:list = [x.split(":") for x in config.split("\n")]
#     config:dict = {user: password for user, password in config}

#     if user == "all": return config # shortcut for getting the whole config

#     elif user is None: # read the first one as default
#         user = list(config.keys())[0]
#         LOG.info(f"Using default account: {user}")
#         password = config[user]

#     else: # use specified account
#         assert isinstance(user, str) and user in config, \
#             f"No config of account: {user}"
#         password = config[user]

#     return user, password


# def to_config(user, password) -> None:
#     ''' Write config to `~/.mailsender_config` '''
#     config = get_config("all")

#     if user in config: LOG.warning(f"Config of {user} will be overwritten.")
#     config[user] = password

#     config:list = [[x, y] for x, y in zip(config.keys(), config.values())]
#     config:str  = "\n".join([":".join(x) for x in config])
#     with open(PATH, 'w') as f: f.write(config)