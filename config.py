from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5512860435"))

PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/yhyqeu.jpg")
START_IMG = getenv("START_IMG", "https://files.catbox.moe/yhyqeu.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Savage_night_club")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Inflix_Destroyer")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5512860435").split()))


FAILED = "https://files.catbox.moe/yhyqeu.jpg"
