from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import ConversationHandler
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
        self.__logout_handler = CommandHandler('logout', self.logout)
        self.__dispatcher.add_handler(self.__logout_handler)
        self.__username = username
        self.__password = password
        self.__username_holder = ""
        self.__password_holder = ""
        self.logged_in = False

        self.USERNAME, self.PASSWORD = range(2)

        self.__login_handler = ConversationHandler(
            entry_points=[CommandHandler('login', self.login)],
            states={
                self.USERNAME: [MessageHandler(Filters.text & ~Filters.command, self.login_check)],
                self.PASSWORD: [MessageHandler(Filters.text & ~Filters.command, self.password_check)]
            },
            fallbacks=[CommandHandler('cancel', self.logout)],
            allow_reentry=True
        )
        self.__dispatcher.add_handler(self.__login_handler)

    def logout(self, update, context):
        if self.logged_in == False:
            pass
        else:
            self.logged_in = False
            update.message.reply_text("Goodbye. Logging out now.")

    def login(self, update, context):
        if self.logged_in == False:
            update.message.reply_text("Please enter your username:")
            return self.USERNAME
        else:
            pass

    def login_check(self, update, context):
        self.__username_holder = update.message.text
        if self.logged_in == False:
            if self.__username_holder == self.__username:
                update.message.reply_text("Please enter your password:")
                return self.PASSWORD
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Incorrect Username, please try again.")
                return self.login(update,context)
        else:
            pass

    def password_check(self, update, context):
        self.__password_holder = update.message.text
        context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
        if self.logged_in == False:
            if self.__password_holder == self.__password:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Logged in to RobbinsVault." + \
                                              "\n\nWelcome " + self.__username)
                self.logged_in = True
                self.start(update,context)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Incorrect password, please try again.")
                return self.login(update,context)
        else:
            pass

    def start(self, update, context):
        if self.logged_in == False:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Welcome to RobbinsVault, " +\
                                     "To login type /login.")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text="Welcome to RobbinsVault, "+\
                                          "please enter a command.\n\n" +\
                                          "/start  - Restart the Bot / Show Help Options\n" +\
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