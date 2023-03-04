import configparser

config = configparser.RawConfigParser()
config.read(".//configurations//config.ini")  # Load the config.ini file


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
