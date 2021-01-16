"API for Sending the Mail"

from typing import Optional, List

from email.mime.multipart import MIMEMultipart

from .init     import MailSender
from ..utility import LOG, get_mail, get_content, mail2str


class MailSender(MailSender):
    "A Friendly Python E-mail Sending Tool"


    def send(
        self,
        content:Optional[str]=None,
        to:List[str]=None,
        header:str = "A Mail Sent by Python",
        content_type:str="html",
    ) -> None:
        "Send the E-mail by Given Content, Header to Given Receivers"
        receivers:List[str] = self._get_receivers(to)
        mail:MIMEMultipart = get_mail(header, self.acc, receivers)
        msg :str = get_content(content, content_type)
        mail:str = mail2str(mail, msg, content_type)
        try: self.server.sendmail(self.acc, receivers, mail)
        except: raise RuntimeError(f"Fail to send e-mail: {header}")
        self._report(header, receivers)


    def _get_receivers(self, user:Optional[List[str]]) -> List[str]:
        "Collect & Report All Receivers"
        receivers:List[str] = [self.acc] # always send to sender himself
        if user is not None:
            if isinstance(user, str): user:List[str] = [user]
            else: assert isinstance(user, list)
            receivers += user
        msg:str = "Receivers: \n" if len(receivers) > 1 else "Receiver: \n"
        for receiver in receivers: msg += f"{receiver}\n"
        LOG.info(msg); return receivers


    def _report(self, title:str, to:List[str]) -> None:
        "Report the E-mail just Sent"
        if len(to) == 1: to_msg:str = f"myself ({self.acc})."
        else           : to_msg:str = f"{len(to)} receivers."
        LOG.info(f"Mail ({title}) sent to {to_msg}")
