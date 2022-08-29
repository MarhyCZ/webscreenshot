import base64
import csv
from datetime import date
from postmarker.core import PostmarkClient

import os

from common.types import Attachment
postmark = PostmarkClient(server_token=os.environ['POSTMARK_TOKEN'])


def send_mail(attachments: list[Attachment]):
    current_date = date.today().strftime("%d-%m-%Y")
    postmark_attachments = []
    for attachment in attachments:
        base64_bytes = base64.b64encode(attachment.content.encode('ascii'))
        base64_content = base64_bytes.decode('ascii')
        postmark_attachments.append({"Name": attachment.filename,
                                     "Content": base64_content, "ContentType": attachment.mimetype})
    postmark.emails.send(
        From='michal.marhan@o2.cz',
        To=['michal.marhan@o2.cz'],
        Subject='Selenium Test - Cookies',
        HtmlBody=f'<html><body><p><strong>Ahoj,</strong> Posílám výstup cookies z {current_date}.</p><p>Toto je automaticky poslaná zpráva.</p></body></html>',
        Attachments=postmark_attachments
    )
