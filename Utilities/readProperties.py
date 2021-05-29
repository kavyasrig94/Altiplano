import configparser


config = configparser.RawConfigParser()
config.read("C:\\Users\\kg\\PycharmProjects\\AltiplanoTesting\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('password')
        return password

    @staticmethod
    def gettitle():
        title = config.get('title')
        return title