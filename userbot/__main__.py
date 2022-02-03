
""" Userbot start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import BOT_TOKEN, BOT_USERNAME, BOT_VER, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import DEVS, LOGS, bot, branch
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, checking, startupmessage, create_supergroup

try:
    bot.start()
    user = bot.get_me()
    roseblacklist = requests.get(
        "https://raw.githubusercontent.com/SendiAp/Reforestation/master/roseblacklist.json"
    ).json()
    if user.id in blacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @pikyus1"
        )
        sys.exit(1)
    if 1307579425 not in DEVS:
        LOGS.warning(
            f"EOL\nRose-UserBot v{BOT_VER}, Copyright © 2021-2022 RoseUserbot• <https://github.com/SendiAp>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/Rose-Userbot"
)

LOGS.info(f"Rose-Userbot ⚙️ V{BOT_VER} [🌹 BERHASIL DIAKTIFKAN! 🌹]")


async def rose_userbot_on():
    try:
        await startupmessage()
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(rose_userbot_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(create_supergroup()) 
    bot.loop.run_until_complete(autobot())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
