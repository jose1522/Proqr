from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.objects.Integration.DB.readKey import readSendGridKey

def SendEmail(sender,to,subject,body):
    key= readSendGridKey()
    message = Mail(
        from_email= sender,
        to_emails= to,
        subject= subject,
        html_content='<p>{0}</p>'.format(body)
    )
    sg = SendGridAPIClient(
        key
    )
    response = sg.send(message)
    return response