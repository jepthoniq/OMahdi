from JoKeRUB import l313l
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/TgCatUB/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/TgCatUB/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import glob
import os
import re
from ..core.managers import edit_delete, edit_or_reply
plugin_category = "tools"


#===============================================================


async def reload_codebase():
    
    BRANCH = "HuRe"
    REPO = "jepthon"
    TOKEN = "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"
    if REPO:
        await _catutils.runcmd(f"git clone -b {BRANCH} https://{TOKEN}@github.com/redaiq90/{REPO}.git TempCat")
        file_list = os.listdir("TempCat")
        for file in file_list:
            await _catutils.runcmd(f"rm -rf {file}")
            await _catutils.runcmd(f"mv ./TempCat/{file} ./")
        await _catutils.runcmd("pip3 install --no-cache-dir -r requirements.txt")
        await _catutils.runcmd("rm -rf TempCat")
    if os.path.exists("catub.log"):
        os.remove("catub.log")
    if os.path.exists("badcatext"):
        await _catutils.runcmd("rm -rf badcatext")
    if os.path.exists("xtraplugins"):
        await _catutils.runcmd("rm -rf xtraplugins")
    if os.path.exists("catvc"):
        await _catutils.runcmd("rm -rf catvc")

@l313l.ar_cmd(
    pattern="تحديث",
    command=("تحديث", plugin_category),
    info={
        "header": "To reload your bot in vps/ similar to restart",
        "flags": {
            "re": "restart your bot without deleting junk files",
            "clean": "delete all junk files & restart",
        },
        "usage": [
            "{tr}reload",
            "{tr}cleanload",
        ],
    },
)
async def reload(event):
    "To reload Your bot"
    cat = await edit_or_reply(event, "`Wait 2-3 min, reloading...`")
    await reload_codebase()
    await event.client.reload(cat)
