"Utilities for Handling Configuration for Mail Sender"

from typing import Dict


def str2dict(data:str) -> Dict[str, Dict[str, str]]:
    ''' Parse Raw Config File into Dict: {Acc: {psw, server}} '''
    if data == "": return dict() # empty config file
    data:list = [x.split(':') for x in data.split('\n')]
    # [[acc, psw, server], ...]
    data:dict = {x[0]: {"psw": x[1], "server": x[-1]} for x in data}
    # {acc: {"psw": psw, "server": server}, ...}
    return data


def dict2str(data:Dict[str, Dict[str, str]]) -> str:
    ''' Parse Config Dict Back to Str: acc:psw:server '''
    data:list = [[x, data[x]["psw"], data[x]["server"]] for x in data.keys()]
    # [[acc, psw, server], ...]
    data:str  = '\n'.join([':'.join(x) for x in data])
    # acc:psw:server\n...
    return data
