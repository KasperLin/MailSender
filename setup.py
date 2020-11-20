from setuptools import setup, find_packages
from mailsender.__init__ import __version__

setup(
    name         = "mailsender", 
    version      = __version__, 
    description  = "A Python E-mail Sender", 
    packages     = find_packages(exclude=["test"]), 
)