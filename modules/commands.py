from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import socket

## TODO ##
# command to check running docker systems and return in a list

# command to reset docker systems

# command to watchdog files and send notifications when files are added or removed

# 

class Commands:
    def __init__(self, dispatcher):
        self.__dispatcher = dispatcher
        self.__start_handler = CommandHandler('start', self.start)
        self.__dispatcher.add_handler(self.__start_handler)
        self.__ip_address_handler = CommandHandler('ipadd', self.getip)
        self.__dispatcher.add_handler(self.__ip_address_handler)
        self.__echo_handler = MessageHandler(Filters.text & (~Filters.command), self.echo)
        self.__dispatcher.add_handler(self.__echo_handler)

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to RobbinsVault, please enter a command.")

    def echo(self, update,context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def getip(self, update,context):
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:       
            st.connect(('10.255.255.255', 1))
            IP = st.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            st.close()
        context.bot.send_message(chat_id=update.effective_chat.id, text=IP)
        