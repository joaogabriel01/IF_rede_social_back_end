class SendEmailDto:
    def __init__(self,mail=""):
        self.__mail = mail

    def getMail(self):
        return self.__mail
    
    def setMail(self,mail):
        self.__mail = mail