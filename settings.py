from dotenv import load_dotenv
import os
load_dotenv()

#       .env
# BOT_TOKEN="1231312:ABCDEFGKADLKLakdADK"
# NAUBOT
#
DB_CONN_STR = "sqlite:///Data/UsersDB.sqlite3"
BOT_TOKEN = os.getenv("BOT_TOKEN")

