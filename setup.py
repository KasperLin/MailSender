from mailsender.__init__ import __version__
from setuptools          import find_packages, setup

setup(
    name        = "mailsender", 
    version     = __version__, 
    description = "A Friendly Python E-mail Sender", 
    packages    = find_packages(), 
)
