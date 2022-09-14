from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import ConversationHandler
import socket

## TODO ##
# command to check running docker systems and return in a list

# command to reset docker systems

# command to watchdog files and send notifications when files are added or removed

# command to add custom users, on boot add their own passwords (have moderators and users)

# class to allow for login

class Commands:
    def __init__(self, dispatcher):
        self.__dispatcher = dispatcher
        self.__info_handler = CommandHandler('info', self.info)
        self.__dispatcher.add_handler(self.__info_handler)
        self.__ip_address_handler = CommandHandler('ipadd', self.getip)
        self.__dispatcher.add_handler(self.__ip_address_handler)
        self.__docker_handler = CommandHandler('docker', self.getdocker)
        self.__dispatcher.add_handler(self.__docker_handler)
        self.__logout_handler = CommandHandler('logout', self.kill)
        self.__dispatcher.add_handler(self.__logout_handler)
        self.username = ""
        self.logged_in = False


    def kill(self, update, context):
        self.logged_in = False
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Goodbye " + self.username)
        del self

    def info(self, update, context):
        if self.logged_in == False:
            pass
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text="Welcome to RobbinsVault, "+\
                                          "please enter a command.\n\n" +\
                                          "/info  - Show Help Options\n" +\
                                          "/docker - Show Docker Containers\n" +\
                                          "/ipadd  - Get the system IP Address\n"+\
                                          "/logout - Logout of the system.")

    def getip(self, update,context):
        if self.logged_in == False:
            pass
        else:                
            st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:       
                st.connect(('10.255.255.255', 1))
                IP = st.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                st.close()
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text=IP)

    def getdocker(self,update,context):
        pass