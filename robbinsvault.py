import logging
from modules.initialization import Initialization
from modules.login import Login

initial = Initialization()
updater = initial.create_updater()
dispatcher = initial.create_dispatcher(updater)
username, password = initial.initial_db_create()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

login = Login(dispatcher, username, password)

updater.start_polling()

updater.idle()