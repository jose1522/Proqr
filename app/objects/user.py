#La clase user maneja el objeto user
#Tiene un método que es el constructor
#Si algún valor no se agrega el se encarga de ponerlo vacío

class User:
#Aqui se define los atributos de los users, constructor
    def __init__(self, userid="", firstname="", lastname="", email="", password="", role="", supervisor="", status=""):
        self.userId = userid
        self.firstName = firstname
        self.lastName = lastname
        self.email = email
        self.password = password
        self.role = role
        self.supervisor = supervisor
        self.status = status
        self.userLink = "/user/{0}".format(self.userId)

