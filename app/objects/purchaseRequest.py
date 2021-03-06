#La clase purchaserequest maneja el objeto request
#Tiene un método que es el constructor
#Si algún valor no se agrega el se encarga de ponerlo vacío
#Tiene un método que convierte el timestamp al date

from datetime import datetime


class PurchaseRequest:
#Aqui se define los atributos de los los requests
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

    #Método que permite saber si tienen que mostrarse los botones en el form basado en el role

    def isOpen(self,role):
        if role > self.status or self.status == 1:
            return True
        else:
            return False
