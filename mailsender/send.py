''' Send the Mail '''

from email.header         import Header
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart

from mailsender.utility import LOG
from mailsender.init    import MailSender
from mailsender.html    import HTML_HEAD, HTML_TAIL

ENCODING = "utf-8"


class MailSender(MailSender):

	def send(
		self,
		content      : str  = "This is a mail sent by Python.",
		to           : list = None,
		header       : str  = "A Mail Sent by Python",
		content_type : str  = "html",
	) -> bool:

		receivers = get_receivers(self.sender, to)

		message = MIMEMultipart()

		message["Subject"] = Header(header, ENCODING).encode()
		message["From"]    = self.sender
		message["To"]      = ','.join(receivers)

		if content_type == "html": # apply GitHub CSS for better style 
			content = HTML_HEAD + content + HTML_TAIL

		message.attach(MIMEText(content, content_type, ENCODING))
		self.server.sendmail(self.sender, receivers, message.as_string())

		LOG.info(f"Mail ({header}) sent to {len(receivers)} users.")
		return True


def get_receivers(sender, to:list) -> list:
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