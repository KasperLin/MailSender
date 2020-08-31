# Mail Sender

A Friendly Python E-mail Sending Tool. 

Simply a thin wrap of [`smtplib`](https://docs.python.org/3/library/smtplib.html) & [`email`](https://docs.python.org/3/library/email.html) , but hopefully it can make life a bit easier.  

- [Support servers](#server) include [Tencent Enterprise Mail（腾讯企业邮箱）](https://exmail.qq.com/) , [Outlook](https://exmail.qq.com/) , [iCloud](https://support.apple.com/en-us/HT201342) ... 
- Support both console scripting & python interactive environments
- Easy to customize for your own use case 

# Getting Started

## Installation

1. Clone this repo : `git clone https://github.com/KasperLin/MailSender.git` 
2. Install :  `cd MailSender ; pip install .`   

## Basic Usage

### Interactive

```python
from mail_sender import MailSender
MailSender(
	user     = "mymail@somewhere.com" , 
	password = my_email_password, 
    # server = "icloud",
).send(
	to      = ["someone@somewhere.com", "another@somewhere.com"], 
	header  = "A Mail Sent by Python :)",
	content = "Hi there !", 
    # content_type = "html",
)
```

### Scripting

```bash
$ send-mail config -u mymail@somewhere.com -p mypassword --server myserver
$ send-mail send -to someone@somewhere.com --subject "Hey!" --content "How r u?"
```

# Appendix

## Configuration

Your e-mail account & password info will be saved to `~/.mail_sender_config` , so you don't need to type account & password every time. 

The config file can be easily modified by yourself, as long as it follows formats below : 

```
acc1@host.com:password1
acc2@host.com:password2
```

- Every time you use a new account, the info will be append to the tail of the config file
- If you don't specify any account & password, it will try to use the first account in the config 

## Server

E-mail servers available : 

| Server          | Host                                   | Port |
| --------------- | -------------------------------------- | ---- |
| `exmail.qq.com` | Tencent Enterprise Mail (腾讯企业邮箱) | 465  |
| `office365.com` | Outlook                                | 587  |
| `mail.me.com`   | iCloud                                 | 587  |

> You probably needs an "app-specific password" as your password. 