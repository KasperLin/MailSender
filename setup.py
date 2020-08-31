from setuptools import setup, find_packages

from mail_sender.__init__ import __version__

setup(
    name         = "mail_sender", 
    version      = __version__, 
    description  = "A Python E-mail Sender", 
    packages     = find_packages(exclude=["test"]), 
    entry_points = {"console_scripts": ["send-mail=mail_sender.cli.cli:run"]}, 
)