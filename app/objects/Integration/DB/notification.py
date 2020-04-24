from app.objects.sendGrid import SendEmail

#Metodo para recuperar contrasena de los usuarios
def RequestNotification(purchaseRequest, userEmail, serverOutput):
    values = serverOutput.keys()
    supervisorEmail = (serverOutput['X-SUPERVISOR']) if 'X-SUPERVISOR' in values else ''
    requestID = (serverOutput['X-REQUEST_ID']) if 'X-REQUEST_ID' in values else ''
    approverEmail = (serverOutput['X-APPROVER']) if 'X-APPROVER' in values else ''

    if purchaseRequest.status == '4':
        body = 'Your request {0} has been rejected by {1}'.format(requestID, purchaseRequest.approver) + '' \
        '' \
        'PROQR' \
        '' \
        'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'

        SendEmail(sender='noreply@email.com', to=(userEmail, supervisorEmail, approverEmail), subject='Request Approval Confirmation',
                  body=body)

    elif purchaseRequest.status == '3':
        body = 'Your request {0} has been approved by {1}'.format(requestID, purchaseRequest.approver) + '' \
               '' \
               'PROQR' \
               '' \
               'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'

        SendEmail(sender='noreply@email.com', to= (userEmail, approverEmail) , subject='Request Approval Confirmation', body=body)

    elif purchaseRequest.status == '2':
        body = 'Your request {0} has been approved by {1}'.format(requestID, purchaseRequest.supervisor) + '' \
                '' \
                'PROQR' \
                '' \
                'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
        SendEmail(sender='noreply@email.com', to= (userEmail, supervisorEmail, approverEmail) , subject='Request Financial Approval Confirmation', body=body)

    elif purchaseRequest.status == '1':
        body = 'Your request {0} has been submitted successfully'.format(requestID) + '' \
               '' \
               'PROQR' \
               '' \
               'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
        SendEmail(sender='noreply@email.com', to=(userEmail, supervisorEmail), subject='Request Submission Confirmation',
                  body=body)
