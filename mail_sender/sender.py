''' Send the Mail '''

from email.header         import Header
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart

from mail_sender.init    import MailSender
from mail_sender.utility import LOG

ENCODING = "utf-8"


class MailSender(MailSender):

	def send(
		self,
		to           : list = None,
		header       : str  = "A Mail Sent by Python",
		content      : str  = "This is a mail sent by Python.",
		content_type : str  = "html",
	) -> bool:

		receivers = self.get_receivers(to)

		message = MIMEMultipart()

		message["Subject"] = Header(header, ENCODING).encode()
		message["From"]    = self.sender
		message["To"]      = ','.join(receivers)

		message.attach(MIMEText(content, content_type, ENCODING))

		self.server.sendmail(self.sender, receivers, message.as_string())

		LOG.info(f"Mail ({header}) sent to {len(receivers)} users.")
		return True


	def get_receivers(self, to:list) -> list:
		''' Collect receivers' emails & report them '''

		receivers = [self.sender] # always send to myself

		if to is not None:
			if isinstance(to, str): to = [to]
			else: assert isinstance(to, list)
			receivers += to

		msg = f"Receivers: \n"
		for receiver in receivers: msg += f"{receiver}\n"
		LOG.info(msg)

		return receivers    