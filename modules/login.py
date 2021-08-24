from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import socket

class Login:
    def __init__(self, dispatcher):
        self.__dispatcher = dispatcher