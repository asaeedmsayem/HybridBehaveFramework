import configparser

config = configparser.RawConfigParser()
config.read(".\\Config\\Config.ini")


class readConfig:
    @staticmethod
    def getURL():
        url = config.get('common-info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        User = config.get('common-info', 'Username')
        return User

    @staticmethod
    def getPassword():
        Pass = config.get('common-info', 'Password')
        return Pass