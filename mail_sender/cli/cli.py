''' Command Line Interface of Mail Sender '''

from mail_sender import MailSender

from mail_sender.cli.args import args


def run() -> None:

    if args.command == "config": MailSender(
        sender   = args.user, 
        password = args.password, 
        server   = args.server, 
    )

    elif args.command == "send": MailSender(
        sender   = args.user, 
        password = args.password, 
        server   = args.server, 
    ).send(
        to           = args.to, 
        header       = args.subject, 
        content      = args.content, 
        content_type = args.content_type, 
    )

    else: raise NotImplementedError