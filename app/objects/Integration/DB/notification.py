from app.objects.sendGrid import SendEmail

#Metodo para recuperar contrasena de los usuarios
def RequestNotification(purchaseRequest, userEmail, serverOutput):
    supervisorEmail = serverOutput['X-SUPERVISOR']
    requestID = serverOutput['X-RESQUEST_ID']
    if purchaseRequest == "4":
        body = 'Your request {0} has been rejected by {1}'.format(requestID, purchaseRequest.approver) + '' \
        '' \
        'PROQR' \
        '' \
        'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'

        SendEmail(sender='noreply@email.com', to=(userEmail, supervisorEmail), subject='Request Approval Confirmation',
                  body=body)

    elif purchaseRequest.status == "3":
        body = 'Your request {0} has been approved by {1}'.format(requestID, purchaseRequest.approver) + '' \
               '' \
               'PROQR' \
               '' \
               'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'

        SendEmail(sender='noreply@email.com', to= (userEmail) , subject='Request Approval Confirmation', body=body)

    elif purchaseRequest.status == "2":
        body = 'Your request {0} has been approved by {1}'.format(requestID, purchaseRequest.supervisor) + '' \
                '' \
                'PROQR' \
                '' \
                'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
        SendEmail(sender='noreply@email.com', to= (userEmail, supervisorEmail) , subject='Request Financial Approval Confirmation', body=body)

    elif purchaseRequest.status == "1":
        body = 'Your request {0} has been submitted successfully'.format(requestID) + '' \
               '' \
               'PROQR' \
               '' \
               'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
        SendEmail(sender='noreply@email.com', to=userEmail, subject='Request Submission Confirmation',
                  body=body)
