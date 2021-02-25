from dotenv import load_dotenv
import os
load_dotenv()

#       .env
BOT_TOKEN="1231312:ABCDEFGKADLKLakdADK"
#
#

BOT_TOKEN = os.getenv("BOT_TOKEN")
print(BOT_TOKEN)

