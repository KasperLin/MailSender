# Mail Sender

A Friendly Python E-mail Sending Tool. 

Simply a thin wrap of [`smtplib`](https://docs.python.org/3/library/smtplib.html) & [`email`](https://docs.python.org/3/library/email.html) , but hopefully it can make life a bit easier.  

- [Support servers](#server) include [Tencent Enterprise Mail（腾讯企业邮箱）](https://exmail.qq.com/) , [Outlook](https://exmail.qq.com/) , [iCloud](https://support.apple.com/en-us/HT201342) ... 
- Easy to customize for your own use case 
- Render your HTML e-mail by GitHub-style markdown CSS

> If you know Python's `smtplib` & `email` modules (or their alternatives) pretty well already, you can simply checkout [server](#server), which can get you going with the critical part of sending email by Python. 

# Getting Started

## Installation

1. Clone this repo : `git clone https://github.com/KasperLin/MailSender.git` 
2. Install :  `cd MailSender ; pip install .`   

## Basic Usage

Record your account & password in `~/.mailsender` for the first time:

```python
from mailsender import MailSender
MailSender(acc, psw, server="qq")
```

Once recorded, you can simply send your e-mail.

> Default to use the first configuration in `~/.mailsender`, but you can also specify which e-mail account to use. 

```python
MailSender().send(
	content = "Hi there !", 
	to      = ["one@host.com", "another@host.com"], 
	header  = "A Mail Sent by Python :)",
    content_type = "html", # can be 'html' or 'plain'
)
```

# Appendix

## Configuration

Your e-mail account & password info will be saved to `~/.mailsender` , so you don't need to type account & password every time. 

The config file can be easily modified by yourself, as long as it follows formats below : 

```
acc1@host.com:password1:server1
acc2@host.com:password2:server2
```

- Every time you use a new account, the info will be append to the tail of the config file
- If you don't specify any account & password, it will try to use the first account in the config 

## Server

E-mail servers available : 

| Server          | Host                                   | Port |
| --------------- | -------------------------------------- | ---- |
| `exmail.qq.com` | Tencent Enterprise Mail (腾讯企业邮箱)   | 465  |
| `office365.com` | Outlook                                | 587  |
| `mail.me.com`   | iCloud                                 | 587  |

> You probably needs an "app-specific password" as your password, instead of the actual password of the e-mail. 