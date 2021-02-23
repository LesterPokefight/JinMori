# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/JinMoriRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1899160  # integer value, dont use ""
    API_HASH = "fa8e5c9465d3bbda077d762f8957bc4c"
    TOKEN = "1612619358:AAE94Q29CYMxaZjRUJYqaWUaN8FR7dcn4yk"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1235046170  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Pokefight"
    SUPPORT_CHAT = "GodOfHighSchoolSupport"  #Your own group for support, do not add the @
    JOIN_LOGGER = -123456798  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -123456798  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "mHCN8mGwzxPe7VBstcqAo0wkFe6GjmZ~cXf_vzD~W89FNR6_Z9G9hAaPusVwRuoE"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('1235046170')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = '-xyz'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = '-xyz'  # Get your API key from https://timezonedb.com/api
    WALL_API = '-xyz'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = '4e646232f43af2a3b142ff8087eee0eebbd3cb95866b56e89ea2a517e34f97779e1bd42e9e15b6392fb09112dbaf9ce9b96ff65bc2ca4a0826a332eeaa910ada'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
