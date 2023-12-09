from KiaraConfig import Config, db_config, os_config
from KiaraUserBot import HEROKU_APP, StartTime
from KiaraUserBot.clients.client_list import (client_id, clients_list,
                                              get_user_id)
from KiaraUserBot.clients.decs import kiara_cmd, kiara_handler
from KiaraUserBot.clients.instaAPI import InstaGram
from KiaraUserBot.clients.logger import LOGGER
from KiaraUserBot.clients.session import (H2, H3, H4, H5, Kiara, KiaraBot,
                                          validate_session)
from KiaraUserBot.DB import gvar_sql
from KiaraUserBot.helpers.anime import *
from KiaraUserBot.helpers.classes import *
from KiaraUserBot.helpers.convert import *
from KiaraUserBot.helpers.exceptions import *
from KiaraUserBot.helpers.formats import *
from KiaraUserBot.helpers.gdriver import *
from KiaraUserBot.helpers.google import *
from KiaraUserBot.helpers.ig_helper import *
from KiaraUserBot.helpers.image import *
from KiaraUserBot.helpers.int_str import *
from KiaraUserBot.helpers.mediatype import *
from KiaraUserBot.helpers.mmf import *
from KiaraUserBot.helpers.movies import *
from KiaraUserBot.helpers.pasters import *
from KiaraUserBot.helpers.pranks import *
from KiaraUserBot.helpers.progress import *
from KiaraUserBot.helpers.runner import *
from KiaraUserBot.helpers.tools import *
from KiaraUserBot.helpers.tweets import *
from KiaraUserBot.helpers.users import *
from KiaraUserBot.helpers.vids import *
from KiaraUserBot.helpers.yt_helper import *
from KiaraUserBot.strings import *
from KiaraUserBot.utils.cmds import *
from KiaraUserBot.utils.decorators import *
from KiaraUserBot.utils.errors import *
from KiaraUserBot.utils.extras import *
from KiaraUserBot.utils.funcs import *
from KiaraUserBot.utils.globals import *
from KiaraUserBot.utils.plug import *
from KiaraUserBot.utils.startup import *
from KiaraUserBot.version import __kiaraver__, __telever__

cjb = "./KiaraConfig/resources/pics/cjb.jpg"
kiara_logo = "./KiaraConfig/resources/pics/kiarabot_logo.jpg"
restlo = "./KiaraConfig/resources/pics/rest.jpeg"
shhh = "./KiaraConfig/resources/pics/chup_madarchod.jpeg"
shuru = "./KiaraConfig/resources/pics/shuru.jpg"
spotify_logo = "./KiaraConfig/resources/pics/spotify.jpg"


kiara_emoji = Config.EMOJI_IN_HELP
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
kiarabot_version = __kiaraver__
telethon_version = __telever__
abuse_m = "Enabled" if str(Config.ABUSE).lower() in enabled_list else "Disabled"
is_sudo = "True" if gvar_sql.gvarstat("SUDO_USERS") else "False"

my_channel = Config.MY_CHANNEL or "Kiara_X_Upadates"
my_group = Config.MY_GROUP or "Kiara_x_Support"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/Kiara_X_Upadates"
grp_link = "https://t.me/Kiara_x_Support"
kiara_channel = f"[†hê Ừʂɛɤẞø†]({chnl_link})"
kiara_grp = f"[Ừʂɛɤẞø† Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {count} : To get group members
  {first} : To use user first name
  {fullname} : To use user full name
  {last} : To use user last name
  {mention} :  To mention the user
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
  {title} : To get chat name in message
  {userid} : To use userid
  {username} : To use user username
"""

# KiaraUserBot
