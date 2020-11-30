from setuptools import find_packages, setup

from mailsender.__init__ import __version__

setup(
    name        = "mailsender", 
    version     = __version__, 
    description = "A Friendly Python E-mail Sender", 
    packages    = find_packages(exclude=["test"]), 
)
