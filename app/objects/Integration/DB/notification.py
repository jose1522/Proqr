from app.objects.sendGrid import SendEmail

#Metodo para enviar los correos de notificacion basado en el status del request
def RequestNotification(purchaseRequest, userEmail, serverOutput):
    supervisorEmail = serverOutput['EMAIL_SUP']
    approverEmail = serverOutput['EMAIL']
    requestID = serverOutput['ID']
    if purchaseRequest == "4":
        body = """Your request {0} has been rejected.
        
        Link to Request: 
        http://127.0.0.1:5000/purchase/{0}
        
        This e-mail message has been delivered from a send-only address. Please do not reply to this message
        """.format(requestID, purchaseRequest.approver)

        SendEmail(sender='noreply@email.com', to=(userEmail, supervisorEmail, approverEmail), subject='Request Rejected',
                  body=body)

    elif purchaseRequest.status == "3":
        body = 'Request {0} has been approved by {1}'.format(requestID, approverEmail) + '' \
               '' \
               'PROQR' \
               '' \
               'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'

        SendEmail(sender='noreply@email.com', to= (userEmail, approverEmail), subject='Request Financial Approval Confirmation', body=body)

    elif purchaseRequest.status == "2":
        body = 'Request {0} has been approved by {1} and it awaiting for financial approval'.format(requestID, supervisorEmail) + '' \
                '' \
                'PROQR' \
                '' \
                'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
        SendEmail(sender='noreply@email.com', to= (userEmail, supervisorEmail, approverEmail) , subject='Request Approval Confirmation', body=body)

    elif purchaseRequest.status == "1":
        body = 'Your request {0} has been submitted successfully and awaiting for approval'.format(requestID) + '' \
               '' \
               'PROQR' \
               '' \
               'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
        SendEmail(sender='noreply@email.com', to=(userEmail, supervisorEmail), subject='Request Submission Confirmation',
                  body=body)