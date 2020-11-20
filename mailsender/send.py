''' Send the Mail by Server '''

from mailsender.init    import MailSender
from mailsender.CSS     import HTML_HEAD, HTML_TAIL
from mailsender.utility import LOG, get_Email, get_Header, get_Message


class MailSender(MailSender):
    ''' A Friendly Python E-mail Sending Tool '''

    def send(self,
		content      :str  = "This is a mail sent by Python.",
		to           :list = None,
		header       :str  = "A Mail Sent by Python",
		content_type :str  = "html",
	) -> None:
        receivers:list = _get_receivers(self.sender, to)
        message  :str  = _get_message(header, self.sender, receivers,
                                      content_type, content)
        self.server.sendmail(self.sender, receivers, message)
        LOG.info(f"Mail ({header}) sent to {len(receivers)} users.")


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


def _get_message(
    title  :str,
    sender :str,
    to     :list,
    dtype  :str,
    content:str,
) -> str:
    ''' Get E-mail Multipart Message '''
    ENCODING = "utf-8"

    message            = get_Message()
    message["Subject"] = get_Header(title, ENCODING)
    message["From"]    = sender
    message["To"]      = ','.join(to)

    # Apply CSS for better styling.
    if dtype == "html": content = HTML_HEAD + content + HTML_TAIL

    return get_Email(message, content, dtype, ENCODING)