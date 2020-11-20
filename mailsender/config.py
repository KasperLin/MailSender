''' Read & Write Configuration in `~/.mailsender_config` '''

import os

from pathlib import Path

PATH:str = os.path.join(str(Path.home()), ".mailsender_config")


def read_config() -> dict:
    ''' Read `~/.mailsender_config` '''
    if not os.path.isfile(PATH): data = dict()
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