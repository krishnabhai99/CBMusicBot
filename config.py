import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQHJLOcALoMyfdaV_exwACrwEgzn5bBaS-IPJUuUPJ9hI05rpK2jUcRd69vbOCT1GCEWf_5YVEWOCJBjn6CaV8LNl_3j3dvyyPyu6qb64_io8sdlHO6CNVBQk6v58Rz424n8ktXznwIuGCIhVB95O5vMx66C-u8AymxsJr-yGYLorT6s2wVTwxskkIAGxx721Vp2N_1heS8bIgQZewDArI-IePnSv4GWiZFPRqZNS5wbJYE8nTFcHaJKxHDidvOgZNsDHm039qkLyitAPCqNO6HlRKhKfz2sbzRnJtqRQIthyMnIIiZppp2ddrPaXRrzwmxYCNBJNP3E5xUjd_p0JScxOJZJIAAAAAFsEZ8KAA")
BOT_TOKEN = getenv("7959845792:AAG5xEToJNEt3ufVPR_oRxev7NsRl8WSFqg")
BOT_NAME = getenv("BOT_NAME", "「⋆ 𝐍azuna ✘ ᴍᴜsɪᴄ ◉」♪")
BG_IMAGE = getenv("BG_IMAGE", "https://graph.org/file/f5853d2ebb78c3788c6e1-6dd6a6eeda52c6378d.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://graph.org/file/2b679a159d9d8795759af-e60b2920c692bacf73.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("29961447"))
API_HASH = getenv("be2e07ad90b5c8b5d368cb4efd302568")
BOT_USERNAME = getenv("BOT_USERNAME", "@nazuna_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SaitamaHelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Animes_India_bots_support_group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Animes_India_bot")
OWNER_NAME = getenv("OWNER_NAME", "krishna") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("5446367898")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-4718320272")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("5446367898").split()))
LANG = getenv("LANG", "id")
