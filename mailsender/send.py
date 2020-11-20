''' Send the Mail by Server '''

from email.header         import Header
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart

from mailsender.utility import LOG
from mailsender.init    import MailSender
from mailsender.html    import HTML_HEAD, HTML_TAIL

ENCODING = "utf-8"


class MailSender(MailSender):
    ''' A Friendly Python E-mail Sending Tool '''

    def send(self,
		content      :str  = "This is a mail sent by Python.",
		to           :list = None,
		header       :str  = "A Mail Sent by Python",
		content_type :str  = "html",
	) -> bool:
        receivers:list = _get_receivers(self.sender, to)
        message:str = _get_message(
            title   = header, 
            from    = self.sender, 
            to      = receivers, 
            dtype   = content_type, 
            content = content, 
        )
        self.server.sendmail(self.sender, receivers, message)
        LOG.info(f"Mail ({header}) sent to {len(receivers)} users.")
        return True


def _get_receivers(sender, to:list) -> list:
	''' Collect receivers' emails & report them '''

	receivers = [sender] # always send to sender himself

	if to is not None:
		if isinstance(to, str): to = [to]
		else: assert isinstance(to, list)
		receivers += to

	msg = "Receivers: \n" if len(receivers) > 1 else "Receiver: \n"
	for receiver in receivers: msg += f"{receiver}\n"
	LOG.info(msg)

	return receivers


def _get_message(title:str, from:str, to:list, dtype:str, content:str) -> str:
    ''' Get E-mail Multipart Message '''
    message:MIMEMultipart = MIMEMultipart()

    message["Subject"] = Header(title, ENCODING).encode()
    message["From"]    = from
    message["To"]      = ','.join(to)

    if dtype == "html": # apply GitHub CSS for better style
        content = HTML_HEAD + content + HTML_TAIL

    message.attach(MIMEText(content, dtype, ENCODING))
    return message.as_string()