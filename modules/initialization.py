from tinydb import TinyDB, Query
import configparser
from telegram.ext import Updater
from getpass import getpass

class Initialization:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('configuration/config.ini')
        self.__token = self.__config['Telegram']['token']
        self.__db = TinyDB('configuration/db.json')
        self.__username = ""
        self.__password = ""

    def initial_db_create(self):
        if self.__config['TinyDB']['setup'] == 'True':
            return self.get_login_information()
        else:
            print('Please enter a username: ')
            username = input('username ==> ')
            print('Please enter your password: ')
            password = getpass('password ==> ')
            self.__config.set('TinyDB','setup','True')
            with open('configuration/config.ini', 'w') as configuration:
                self.__config.write(configuration)
            self.__db.insert({'username':username,'password':password})
            return self.get_login_information()


    def get_login_information(self):
        self.__user_information = self.__db.all()
        self.__username = self.__user_information[0]['username']
        self.__password = self.__user_information[0]['password']
        return self.__username, self.__password
    
    def create_updater(self):
        self.updater = Updater(token=self.__token, use_context=True)
        return self.updater

    def create_dispatcher(self, updater):
        self.dispatcher = updater.dispatcher
        return self.dispatcher