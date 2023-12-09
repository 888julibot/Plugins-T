import importlib
import logging
import os
import sys
from pathlib import Path

from KiaraConfig import Config
from telethon.tl.types import InputMessagesFilterDocument
from KiaraUserBot.clients.client_list import client_id
from KiaraUserBot.clients.decs import kiara_cmd
from KiaraUserBot.clients.logger import LOGGER as LOGS
from KiaraUserBot.clients.session import H2, H3, H4, H5, Kiara, KiaraBot
from KiaraUserBot.utils.cmds import CmdHelp
from KiaraUserBot.utils.decorators import admin_cmd, command, sudo_cmd
from KiaraUserBot.utils.extras import delete_kiara, edit_or_reply
from KiaraUserBot.utils.globals import LOAD_PLUG


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import KiaraUserBot.utils

        path = Path(f"KiaraUserBot/plugins/{shortname}.py")
        name = "KiaraUserBot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("KiaraBot - Successfully imported " + shortname)
    else:
        import KiaraUserBot.utils

        path = Path(f"KiaraUserBot/plugins/{shortname}.py")
        name = "KiaraUserBot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Kiara
        mod.H1 = Kiara
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Kiara = Kiara
        mod.KiaraBot = KiaraBot
        mod.tbot = KiaraBot
        mod.tgbot = Kiara.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        mod.Config = Config
        mod.borg = Kiara
        mod.kiarabot = Kiara
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_kiara = delete_kiara
        mod.eod = delete_kiara
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.kiara_cmd = kiara_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot.utils"] = KiaraUserBot
        sys.modules["userbot"] = KiaraUserBot
        sys.modules["userbot.events"] = KiaraUserBot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["KiaraUserBot.plugins." + shortname] = mod
        LOGS.info("⚡ Ừʂɛɤẞø† ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Kiara.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"KiaraUserBot.plugins.{shortname}"

            for i in reversed(range(len(Kiara._event_builders))):
                ev, cb = Kiara._event_builders[i]
                if cb.__module__ == name:
                    del Kiara._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel != 0:
        LOGS.info("⚡ Ừʂɛɤẞø† ⚡ - PLUGIN CHANNEL DETECTED.")
        LOGS.info("⚡ Ừʂɛɤẞø† ⚡ - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"KiaraUserBot/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "KiaraUserBot/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# kiarabot
