''' Command Line Arguments of Mail Sender '''

import argparse

args = argparse.ArgumentParser()

args.add_argument(
    "command", type=str, default="send", 
    help="Command, `config` for configure acc & psw, "
    "any other commands will send the mail.", 
)
args.add_argument(
    "--user", "-u", type=str, default=None, 
    help="E-mail account user name.", 
)
args.add_argument(
    "--password", "-p", type=str, default=None, 
    help="E-mail account password.", 
)
args.add_argument(
    "-to", type=str, default=None, 
    help="E-mail account(s) to send to.", 
)
args.add_argument(
    "--server", type=str, default=None, 
    help="E-mail host server.", 
)
args.add_argument(
    "--subject", type=str, default="A Mail Sent by Python", 
    help="The header of this mail.", 
)
args.add_argument(
    "--content", "-c", type=str, default="Content of the mail.", 
    help="The content of this mail.", 
)
args.add_argument(
    "--content_type", "-t", type=str, default="plain", 
    help="Content type of this mail (plain or html).", 
)

args = args.parse_args()

if isinstance(args.to, str) and ("[" in args.to and "]" in args.to):
    args.to = args.to.split("[")[-1].split("]")[0].split(",")