import configparser
from telegram.ext import Updater

class Initialization:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('configuration/config.cfg')
        self.__token = self.__config['Telegram']['token']

    def create_updater(self):
        self.updater = Updater(token=self.__token, use_context=True)
        return self.updater

    def create_dispatcher(self, updater):
        self.dispatcher = updater.dispatcher
        return self.dispatcher