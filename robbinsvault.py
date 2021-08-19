import configparser

config = configparser.ConfigParser()
config.read('config.cfg')
token = config['Telegram']['token']

print(token)