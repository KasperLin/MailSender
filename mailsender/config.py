''' Read & Write Configuration in `~/.mailsender_config` '''

import os

from mailsender.utility import get_HOME, LOG

PATH:str = os.path.join(get_HOME(), ".mailsender_config")


def read_config() -> dict:
    ''' Read `~/.mailsender_config` Config Dict '''
    if not os.path.isfile(PATH): 
        data = dict()
        LOG.info("Create `~/.mailsender_config` config file.")
    else:
        with open(PATH) as f: data:str = f.read()
        if data == "": data = dict() # empty config file
        else: data:dict = _str2dict(data)
    return data


def write_config(data:dict) -> None:
    ''' Write Config Back to `~/.mailsender_cofig` '''
    data:str = _dict2str(data)
    with open(PATH, 'w') as f: f.write(data)


def _str2dict(data:str) -> dict:
    ''' Parse Raw Config File into Dict: {Acc: {psw, server}} '''
    data:list = [x.split(':') for x in data.split('\n')]
    # [[acc, psw, server], ...]
    data:dict = {x[0]: {"psw": x[1], "server": x[-1]} for x in data}
    # {acc: {"psw": psw, "server": server}, ...}
    return data

def _dict2str(data:dict) -> str:
    ''' Parse Config Dict Back to Str: acc:psw:server '''
    data:list = [[x, data[x]["psw"], data[x]["server"]] for x in data.keys()]
    # [[acc, psw, server], ...]
    data:str  = '\n'.join([':'.join(x) for x in data])
    # acc:psw:server\n...
    return data