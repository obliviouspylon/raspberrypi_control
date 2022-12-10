import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail, To
from time import sleep, time, strftime, localtime

API_KEY = ""

def sendEmail(recipientEmail,subject, body,recipientName, senderName = "RaspberryPi Notify"):

    sg = sendgrid.SendGridAPIClient(
        api_key=API_KEY)
    from_email = Email("",senderName)
    to_email = To(recipientEmail,recipientName)
    content = Content(
        "text/plain", body
    )
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    # The statements below can be included for debugging purposes
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)
