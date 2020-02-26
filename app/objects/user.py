class User:

    def __init__(self, userid="", firstname="", lastname="", email="", password="", role="", supervisor=""):
        self.userId = userid
        self.firstName = firstname
        self.lastName = lastname
        self.email = email
        self.password = password
        self.role = role
        self.supervisor = supervisor
        self.userLink = "/user/{0}".format(self.userId)
