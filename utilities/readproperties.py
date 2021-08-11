import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class Readconfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPasswrd():
        password = config.get('common info', 'password')
        return password