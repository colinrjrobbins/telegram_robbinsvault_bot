from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import ConversationHandler
from modules.commands import Commands
import socket

class Login:
    def __init__(self, dispatcher, username, password):
        self.__dispatcher = dispatcher
        self.__username = username
        self.__password = password
        self.__username_holder = ""
        self.__password_holder = ""
        self.logged_in = False
        self.USERNAME, self.PASSWORD = range(2)

        self.__start_handler = CommandHandler('start', self.start)
        self.__dispatcher.add_handler(self.__start_handler)

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

    def login(self, update, context):
        update.message.reply_text("Please enter your username:")
        return self.USERNAME

    def logout(self, update, context):
        del self.commands
        self.logged_in = False
        update.message.reply_text("Goodbye. Logging out now.")

    def login_check(self, update, context):
        self.__username_holder = update.message.text

        if self.__username_holder == self.__username:
            update.message.reply_text("Please enter your password:")
            return self.PASSWORD
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Incorrect Username, please try again.")
            return self.login(update,context)

    def password_check(self, update, context):
        self.__password_holder = update.message.text
        context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
        
        if self.__password_holder == self.__password:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Logged in to RobbinsVault." + \
                                              "\n\nWelcome " + self.__username)
            self.logged_in = True
            self.commands = Commands(self.__dispatcher)
            self.commands.username = self.__username_holder
            self.commands.logged_in = True
            self.commands.info(update,context)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                        text="Incorrect password, please try again.")
            return self.login(update,context)

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Welcome to RobbinsVault. " +\
                                      "To login type /login.")