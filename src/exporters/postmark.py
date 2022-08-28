import base64
import csv
from datetime import date
from pprint import pprint
from postmarker.core import PostmarkClient

import os
postmark = PostmarkClient(server_token=os.environ['POSTMARK_TOKEN'])


def send_mail(csv_attachments: list[tuple[str, str]]):
    current_date = date.today().strftime("%d-%m-%Y")
    postmark_attachments = []

    for attachment in csv_attachments:
        name, contents = attachment
        base64_bytes = base64.b64encode(contents.encode('ascii'))
        base64_message = base64_bytes.decode('ascii')
        postmark_attachments.append({"Name": f"name_{current_date}.csv",
                                     "Content": base64_message, "ContentType": "text/csv"})

    # postmark.emails.send(
    #     From = 'michal.marhan@o2.cz',
    #     To = ['michal.marhan@o2.cz', 'ondrej.slama@o2.cz'],
    #     Subject = 'Selenium Test - Cookies',
    #     HtmlBody = f'<html><body><p><strong>Ahoj,</strong> Posílám výstup cookies z {current_date}.</p><p>Toto je automaticky poslaná zpráva.</p></body></html>',
    #     Attachments = postmark_attachments
    # )
