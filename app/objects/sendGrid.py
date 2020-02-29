from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.objects.Integration.DB.readKey import readSendGridKey

#Método se encarga de enviar el email. Recibe el from, el to, el subject y el body del correo
#Utiliza sendGrid por lo que necesita un key
#Utiliza tambien el API de sendGrid, es el vehículo para mandarlo

def SendEmail(sender,to,subject,body):
    key= readSendGridKey()
    message = Mail(
        from_email= sender,
        to_emails= to,
        subject= subject,
        html_content='<p>{0}</p>'.format(body)
    )
    sg = SendGridAPIClient(key)
    response = sg.send(message)
    return response