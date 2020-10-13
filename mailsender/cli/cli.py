''' Command Line Interface of Mail Sender '''

from mailsender import MailSender

from mailsender.cli.args import args


def run() -> None:

    if args.command == "config": MailSender(
        sender   = args.user, 
        password = args.password, 
        server   = args.server, 
    )

    else: MailSender(
        sender   = args.user, 
        password = args.password, 
        server   = args.server, 
    ).send(
        to           = args.to, 
        header       = args.subject, 
        content      = args.content, 
        content_type = args.content_type, 
    )