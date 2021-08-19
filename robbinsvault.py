import logging
from modules.initialization import Initialization
from modules.commands import Commands

initial = Initialization()
updater = initial.create_updater()
dispatcher = initial.create_dispatcher(updater)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

command = Commands(dispatcher)

while True:
    updater.start_polling()
