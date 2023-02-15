
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6114061883:AAFF1NObBKGrkYRjinuyPjW4tVJJ21BbGjc")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "5973272980"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "0a56df2f25eefcace1c2e8948106dd66")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BVtsOGQBu3ghcwIbSSJarDNkKykV95-IUb6wYGC7ZeWbUoEgAeiG9oSejtvo2dqpzzSyFmHZAyEAZ3MaJaWgR9Nf_n9pfHoJQaxg5NtmQVuJLVGEKsU1r0JoYmvgKE3CFp_1rGuWyPGYtDs95X_NSKmwacEgOEPL9oDKpEmtuDTLcOdALGCkrAu_xYy07K85PSKdgJPobM2GGQUZVmPpj_vfYLOoy8iocqi7xaXgnfV1N1KXrJ3uOTHKvR4I-QR8kNcB_wtA9zUJcgaNfA7rO7vd5cvvF6Ie4Eld5vmJv72MiqA27y7-FY0TNuUnODV2C4mUXi8Aa2U1FUREuTGHZiFOP9E7AmE=")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001746191897")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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
