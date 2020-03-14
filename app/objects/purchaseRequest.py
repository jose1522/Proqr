#La clase purchaserequest maneja el objeto request
#Tiene un método que es el constructor
#Si algún valor no se agrega el se encarga de ponerlo vacío

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
        self.date = date
