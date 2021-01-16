"Configuration of Mail Sender (~/.mailsender)"

import os

from pathlib import Path
from typing  import Dict, Optional, Tuple

from ..utility import LOG, get_server_name
from .parser   import str2dict, dict2str


class Configurator():
    "Handle Configuration for Mail Sender in ~/.mailsender"

    def __init__(self) -> None:
        "Settle File Path for Configuration (~/.mailsender)"
        self.path = os.path.join(str(Path.home()), ".mailsender")
    

    def read(self) -> Dict[str, Dict[str, str]]:
        "Read (or Create) & Parse Configuration"

        def create() -> dict:
            "Create Config File for the First Time"
            LOG.info("Create config on `~/.mailsender`.")
            return dict()
        
        def read() -> str:
            "Read Config File as String"
            with open(self.path) as f: return f.read()

        existed:bool = os.path.isfile(self.path)
        if not existed: return create()
        else          : return str2dict(read())
    

    def write(self, data:Dict[str, Dict[str, str]]) -> None:
        "Write Given Config Back to ~/.mailsender"
        with open(self.path, 'w') as f: f.write(dict2str(data))
    

    def first(self) -> Tuple[str]:
        "Get the First Pair of Acc, Psw & Server"
        data = self.read()
        assert data, "No config yet! Acc & Psw must be given."
        acc:str = list(data.keys())[0]
        psw:str = data[acc]["psw"]
        svr:str = data[acc]["server"]
        return acc, psw, svr
    

    def lookup(self, acc:str) -> Tuple[str]:
        "Look Up Config by Given Account"
        data = self.read()
        assert acc in data, f"Need the password of account: {acc}"
        psw:str = data[acc]["psw"]
        svr:str = data[acc]["server"]
        return acc, psw, svr
    

    def record(self, acc:str, psw:str, svr:Optional[str]=None) -> Tuple[str]:
        "Record Given Acc & Psw (& Server) Info in Config File"
        data = self.read()
        changed:bool = acc not in data
        changed     |= psw != data.get(acc, dict()).get("psw")
        changed     |= svr != data.get(acc, dict()).get("server")
        if changed: LOG.info(f"Overwrite account config: {acc}")
        else      : LOG.info(f"Record new account: {acc}")
        svr = get_server_name(acc, svr)
        data[acc] = {"psw": psw, "server": svr}; self.write(data)
        return acc, psw, svr
