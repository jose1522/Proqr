import requests
import json
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.purchaseRequest import PurchaseRequest


#Metodo que trae los datos de la base de datos de los usuarios ya registrados en la aplicacion.
#Trae desde la base de datos todos los requests

class RequestList:

    def __init__(self, userRole=1, userID=0, action=open):
        self.purchases = []
        self.userRole = userRole
        self.userID = userID
        self.endpoint = str(action)

    def endpointGenerator(self):
        if self.userRole == "2":
            return self.endpoint + "/supervisor"
        elif self.userRole == "3":
            return self.endpoint + "/approver"
        else:
            return None

    def FetchPurchaseList(self):
        key = readDBKey()

        #Tiene que cambiar
        url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/requests/"+str(self.endpointGenerator())

        headers = {
            'Authorization': "Basic {0}".format(key),
            'X-ID': "{0}".format(self.userID)
        }


        response = requests.request("GET", url, headers=headers)
        response = json.loads(response.text)

        if response['count'] > 0:
            items = response['items']
            for item in items:
                purchaseid = item['id']
                userid = item['employee']
                description = item['description']
                try:
                    items = json.loads(item['items'])
                except:
                    items = item['items']
                comments = item['comments']
                status = item['status']
                amount = item['amount']
                supervisor = item['supervisor']
                approver = item['approver']
                date = item['request_date']
                purchase = PurchaseRequest(requestid=purchaseid, userid=userid, description=description, items=items,
                                           comments=comments, amount=amount, status=status, supervisor=supervisor,
                                           approver=approver, date=date)
                self.purchases.append(purchase)
