#(©)CodeXBotz
#Recoded By @i_killed_my_clan



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7432362257:AAGzW19vj3ZycautMo1Z2gkEmr8WEC3MjGA")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20718334"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002177334941"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "949657126"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://spyderman11220:hLJuIvmc4txZbUtn@cluster0.esc85vg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "spyderman11220")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001948532295"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001622914589"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002237171878"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/a319f6b9ce3b993c6e22f.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/0338e5f9959b111abc01b.jpg")

HELP_TXT = "https://t.me/Movie_Loverzz"
ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n⌬ ᴏᴡɴᴇʀ : <a href=https://t.me/mladmin>LOKI</a>\n⌬ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/MOVIE_LOVERZZ'>ᴏɴɢᴏɪɴɢ sᴏᴄɪᴇᴛʏ</a>\n⌬ ᴄʜᴀᴛ ᴢᴏɴᴇ : <a href='https://t.me/+xD8sN57OJ6JiYWZl'>ᴄʜᴀᴛ ᴢᴏɴᴇ</a>\n࿂ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href='https://t.me/MLADMIN'>❰⏤͟͞ MOONK NIGHT-//-❱</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href=https://t.me/movie_loverzz>Movie Loverzz</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5585016974").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!\n\nమీరు ఈ క్రింద ఉన్న 3 ఛానల్స్ లో జాయిన్ అవ్వాలి.. Join అయిన తర్వాత ' try Again ' Click చేస్తే File వస్తుంది 😊")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - <a href=https://t.me/Movie_loverzz>Movie Loverzz</a>"

ADMINS.append(OWNER_ID)
ADMINS.append(5585016974)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
