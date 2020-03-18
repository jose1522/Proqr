#La clase purchaserequest maneja el objeto request
#Tiene un método que es el constructor
#Si algún valor no se agrega el se encarga de ponerlo vacío
from datetime import datetime


class PurchaseRequest:
#Aqui se define los atributos de los users
    def __init__(self, userid="", requestid="",description="", items="", comments="", amount="", status="", supervisor="", approver="", date=""):
        self.userid = userid
        self.requestid = requestid
        self.description = description
        self.items = items
        self.comments = comments
        self.amount = amount
        self.status = status
        self.supervisor = supervisor
        self.approver = approver
        self.date = self.timestampToDate(date)
        self.purchaseLink = "/purchase/{0}".format(self.requestid)


    def timestampToDate(self, input):
        try:
            ts = datetime.strptime(input, "%Y-%m-%dT%H:%M:%SZ")
            return datetime.date(ts)
        except:
            return  None

