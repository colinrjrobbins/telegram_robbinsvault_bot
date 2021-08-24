from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import socket

## TODO ##
# command to check running docker systems and return in a list

# command to reset docker systems

# command to watchdog files and send notifications when files are added or removed

# class to allow for login

class Commands:
    def __init__(self, dispatcher, username, password):
        self.__dispatcher = dispatcher
        self.__start_handler = CommandHandler('start', self.start)
        self.__dispatcher.add_handler(self.__start_handler)
        self.__ip_address_handler = CommandHandler('ipadd', self.getip)
        self.__dispatcher.add_handler(self.__ip_address_handler)
        self.__echo_handler = MessageHandler(Filters.text & (~Filters.command), self.echo)
        self.__dispatcher.add_handler(self.__echo_handler)
        self.__username = username
        self.__password = password
        self.logged_in = False

    def login_check(self, update, context):
        if self.logged_in == False:
            if update.message.text == self.__username:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Password:")
                self.__password_handler = MessageHandler(Filters.text & (~Filters.command), self.password_check)
                self.__dispatcher.add_handler(self.__password_handler)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Incorrect Username, please try again.")
        else:
            pass

    def password_check(self, update, context):
        if self.logged_in == False:
            if update.message.text == self.__password:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Logged in to RobbinsVault." + \
                                              "\n\nWelcome " + self.__username)
                self.logged_in = True
                self.start(update,context)
        else:
            pass

    def start(self, update, context):
        if self.logged_in == False:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Welcome to RobbinsVault, " +\
                                     "You will now be prompted to log in.\n\n" +\
                                     "Please enter your Username")
            self.__username_handler = MessageHandler(Filters.text & (~Filters.command), self.login_check)
            self.__dispatcher.add_handler(self.__username_handler)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text="Welcome to RobbinsVault, "+\
                                          "please enter a command.\n\n" +\
                                          "/start      Restart the Bot / Show Help Options\n" +\
                                          "/ipadd     Get the system IP Address\n"+\
                                          "\nAnything else entered will be echoed.")

    def echo(self, update,context):
        if self.logged_in == False:
            pass
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text=update.message.text)

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

