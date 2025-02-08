#------------------- ᴄʀᴇᴅɪᴛ ------------------------------------

# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT

#---------------------------••••••••••••••-------------------------------

import re
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')


#------------------------- ʙoᴛ ɪɴғoʀᴍᴀᴛɪᴏɴ --------------------------

SESSION = environ.get('SESSION', 'NIXBOTZ')
API_ID = int(environ.get('API_ID', '25061703'))
API_HASH = environ.get('API_HASH', '744a017a9c53f3ab489ea0bfa0ffce3f')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

#--------------------------- ɪᴍᴀɢᴇs ʟɪɴᴋ -----------------------------

# sᴛᴀʀᴛ ɪᴍᴀɢᴇs ʟɪɴᴋ  
PICS = (environ.get('PICS', 'https://envs.sh/fC8.jpg https://envs.sh/fC7.jpg https://envs.sh/fCo.jpg https://envs.sh/fCr.jpg https://envs.sh/fCs.jpg https://envs.sh/fRe.jpg https://envs.sh/fRt.jpg')).split() 

NOR_IMG = environ.get("NOR_IMG", "https://envs.sh/fRe.jpg")

MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/fRb.jpg")
APPROVED_IMG = environ.get("APPROVED_IMG", "https://envs.sh/fRb.jpg")

VERIFY_IMG = environ.get("VERIFY_IMG", "")

SPELL_IMG = environ.get("SPELL_IMG", "https://envs.sh/f1A.jpg")

FORCESUB_IMG = (environ.get('FORCESUB_IMG', 'https://graph.org/file/9649c1dcbae09f2e7700e.jpg'))

REFER_IMG = (environ.get("REFER_IMG", "https://envs.sh/fRn.jpg")).split() 

SUBSCRIPTION_IMG = (environ.get('SUBSCRIPTION_IMG', 'https://envs.sh/fRA.jpg'))
QR_CODE = (environ.get('QR_CODE', 'https://envs.sh/fRg.jpg'))

#------------------ sᴛᴀʀᴛ ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴀcᴛɪoɴs ----------------------

REACTIONS = ["🦋", "🤝", "😇", "🤗", "😍", "😎",  "👍", "🌚", "🎅", "😁", "😐", "🥰", "🤩", "😈", "😱", "🤣", "😘", "👏", "😛", "🎉", "⚡️", "🫡", "🤓", "🏆", "🔥", "🤭", "🆒", "👻"] # ᴅoɴ'ᴛ ᴀᴅᴅ ᴀɴʏ ᴇᴍojɪ ʙᴇcᴀᴜsᴇ ᴛɢ ɴᴏᴛ sᴜᴘᴘoʀᴛ ᴀʟʟ ᴇᴍojɪ

#--------------------------------- ʀᴇғᴇʀᴀʟ sᴇᴛᴛɪɴɢs -------------------------------

REFFER_POINT = int(environ.get('REFERAL_POINT', "100")) # ɴᴜᴍʙᴇʀ ᴏꜰ ʀᴇғᴇʀᴀʟ ᴘoɪɴᴛ

REFERAL_PREMUM_TIME = environ.get('REFERAL_PREMUM_TIME', '2592000') # sᴇᴛ ɪɴ ʀᴇғᴇʀᴀʟ ᴛɪᴍᴇ sᴇcoɴᴅ || ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ sᴇᴛᴇᴅ 1 ᴍoɴᴛʜ ᴘʀᴇᴍɪᴜᴍ.

#-------------------------------- ɪᴅ -----------------------------------

# 📌 ɴoᴛᴇ: ɢɪvᴇ ʙᴇʟow vᴀʀɪᴀʙʟᴇs wʜo cʜᴀɴɴᴇʟs ɪᴅ ᴀᴅᴅ ɪɴ ᴛʜᴇ cʜᴀɴɴᴇʟ, ʙᴏᴛ ᴍᴜsᴛ ᴀᴅᴍɪɴ wɪᴛʜ ꜰᴜʟʟ sᴜᴘᴘoʀᴛ

# ᴀᴅᴍɪɴs ɪᴅ  || ꜰɪʟʟ ᴍᴜʟᴛɪᴘʟᴇꜱ ɪᴅ ʙʏ ɢɪvɪɴɢ oɴᴇ sᴘᴀcᴇ ʙᴇᴛwᴇᴇɴ ᴇᴀc𝙷 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6899946963').split()]

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʏoᴜ ᴜᴘʟoᴀᴅ ʏoᴜʀ ꜰɪʟᴇꜱ ᴛʜᴇɴ, ʙᴏᴛ ᴀᴜᴛoᴍᴀᴛɪcᴀʟʟʏ sᴀvᴇ ɪᴛ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ. ɪᴛ ɪs ᴀʟso ᴋɴowɴ ᴀs ꜰɪʟᴇ cʜᴀɴɴᴇʟ.
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002319064428').split()]

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʙᴏᴛ sᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇs ɪꜰ ɴᴇw ᴜsᴇʀ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴏʀ ʙᴏᴛ sᴇɴᴅ ꜰɪʟᴇꜱ ᴀɴʏ ᴜsᴇʀ.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002377076025'))

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʙᴏᴛ oɴʟʏ sᴇɴᴅ ᴘʀᴇᴍɪᴜᴍ ᴍᴇꜱꜱᴀɢᴇs 
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002377076025')) 

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ wʜᴇʀᴇ ʙᴏᴛ ᴅᴇʟᴇᴛᴇ ɪɴᴅᴇx ꜰɪʟᴇ, ғoʀwᴀʀᴅ wʜo ꜰɪʟᴇ ɪɴ ᴛʜᴇ cʜᴀɴɴᴇʟ ғʀoᴍ ꜰɪʟᴇ cʜᴀɴɴᴇʟ wʜɪcʜ ʏoᴜ wᴀɴᴛ ᴛo ᴅᴇʟᴇᴛᴇ ᴛʜᴇɴ, ʙᴏᴛ ᴀᴜᴛoᴍᴀᴛɪcᴀʟʟʏ ᴅᴇʟᴇᴛᴇ ᴛʜᴀᴛ ꜰɪʟᴇ ғʀoᴍ ᴅᴀᴛᴀʙᴀsᴇ. 
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002264438255').split()]  

# ɢɪvᴇ wʜo ᴜsᴇʀ ɪᴅ wʜɪcʜ ʏoᴜ wᴀɴᴛ sᴇᴀʀᴄʜ ɪɴʟɪɴᴇ 
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '6899946963').split()]

PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '6899946963').split()]

# ɢɪvᴇ ʏoᴜʀ ғoʀcᴇ sᴜʙscʀɪʙᴇ cʜᴀɴɴᴇʟ ɪᴅ ᴇʟsᴇ ʟᴇᴀvᴇ ɪᴛ ʙʟᴀɴᴋ.
auth_channel = environ.get('AUTH_CHANNEL', '-1002386346176')

# ɢɪvᴇ sᴜᴘᴘoʀᴛ cʜᴀɴɴᴇʟ ɪᴅ ʙᴏᴛ ɴᴏᴛ sᴇɴᴅ ꜰɪʟᴇ ʜᴇʀᴇ ʙᴇcᴀᴜsᴇ ᴛʜɪs ɪs sᴜᴘᴘoʀᴛ cʜᴀɴɴᴇʟ.
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002386346176') 

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ ғoʀ ɪꜰ ᴜsᴇʀ ʀᴇQᴜᴇsᴛ ꜰɪʟᴇ wɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ oʀ ʜᴀsʜᴛᴀɢ ʟɪᴋᴇ - /request oʀ #request
reqst_channel = environ.get('REQST_CHANNEL_ID', '-4554257154') 

# ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ɪᴅ ғoʀ /batch ᴄᴏᴍᴍᴀɴᴅ ꜰɪʟᴇ sᴛoʀᴇ
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]

auth_grp = environ.get('AUTH_GROUP')

AUTH_USERS = (auth_users + ADMINS) if auth_users else []
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

#------------------------------ ʟɪɴᴋ --------------------------------

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Ni_Movie_Request_Group') 
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/NIXBOTZ') 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/NIXBOTZ_Support') 

#------------------------- ᴍoɴɢoᴅʙ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ --------------------------------------------

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://bipinmfp07:OmodwqrRcvV6lrV4@cluster0.2t7so.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "NIXDB")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'NIXFILES')

#---------------------------- sʜᴏʀᴛʟɪɴᴋ ---------------------------

SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False)) # sᴇᴛ True ᴏʀ False
SHORTLINK_API = environ.get('SHORTLINK_API', '') 

SHORTLINK_URL = environ.get('SHORTLINK_URL', '')  

TUTORIAL = environ.get('TUTORIAL', 'https://t.me/')  # ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ʟɪɴᴋ wʜᴇʀᴇ ʏoᴜ ᴜᴘʟoᴀᴅ oᴘᴇɴɪɴɢ sʜᴏʀᴛʟɪɴᴋ wᴇʙsɪᴛᴇ

#------------------------------- vᴇʀɪғʏ ---------------------------

VERIFY = bool(environ.get('VERIFY', False)) # sᴇᴛ vᴇʀɪғɪcᴀᴛɪoɴ True ᴏʀ False

VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '') 
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')

HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/') # ɢɪvᴇ wʜo cʜᴀɴɴᴇʟ ʟɪɴᴋ wʜᴇʀᴇ ʏoᴜ ᴜᴘʟoᴀᴅ ʜow ᴛo vᴇʀɪғʏ vɪᴅᴇo. 

#------------------------------ sᴇcoɴᴅ vᴇʀɪғʏ ----------------------

SND_VERIFY = bool(environ.get('SND_VERIFY', False)) # sᴇᴛ True ᴏʀ False

SND_VERIFY_SHORTLINK_URL = environ.get('SND_VERIFY_SHORTLINK_URL', '') 
SND_VERIFY_SHORTLINK_API = environ.get('SND_VERIFY_SHORTLINK_API', '') 

#------------------------------ ᴛʜɪʀᴅ vᴇʀɪғʏ --------------------------

THRD_VERIFY = bool(environ.get('THRD_VERIFY', False)) # sᴇᴛ True ᴏʀ False

THRD_VERIFY_SHORTLINK_URL = environ.get('THRD_VERIFY_SHORTLINK_URL', '') 
THRD_VERIFY_SHORTLINK_API = environ.get('THRD_VERIFY_SHORTLINK_API', '') 

#--------------------------------- oᴛʜᴇʀ ------------------------------

MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = bool(environ.get('MAX_BTN', True))
PORT = environ.get("PORT", "8080")
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', '…👻')
P_TTI_SHOW_OFF = bool(environ.get('P_TTI_SHOW_OFF', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False)) # "True" ɪꜰ ʏoᴜ want ɴo ʏoᴜ ʀᴇsᴜʟᴛs ᴍᴇꜱꜱᴀɢᴇs ɪɴ ʟoɢ cʜᴀɴɴᴇʟ ᴇʟsᴇ "False"

BUTTON = bool(environ.get('BUTTON', True))
IMDB = bool(environ.get('IMDB', False))
CACHE_TIME = int(environ.get('CACHE_TIME', 1200))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
WELCOME_TEXT = environ.get("WELCOME_TEXT", f"{script.WELCOME_TXT}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION",  False))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', True))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', "True", True))

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", "", "bengali", ""]

YEARS = ["1980" , "1981" , "1982" , "1983" , "1984" , "1985" , "1986" , "1987" , "1988" , "1989" , "1990" , "1991" , "1992" , "1993" , "1994" , "1995" , "1996" , "1997" , "1998" , "1999" , "2000" , "2001" , "2002" , "2003" , "2004" , "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015" , "2016" , "2017" , "2018" , "2019" , "2020" , "2021" , "2022" , "2023" , "2024" , "2025"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

#---------------------- ᴏɴʟɪɴᴇ sᴛʀᴇᴀᴍ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ----------------------

STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # sᴇᴛ True ᴏʀ False
                                  
MULTI_CLIENT = False                        
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 ᴍɪɴᴜᴛᴇs
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")  

#-------------------------- ᴀᴜᴛo ᴀᴘᴘʀᴏᴠᴇ ------------------------------

APPROVED = is_enabled(environ.get("APPROVED", False)) # sᴇᴛ True ᴏʀ False

# ɢɪvᴇ wʜo cʜᴀᴛ ɪᴅ wʜᴇʀᴇ ʏoᴜ wᴀɴᴛ ʙᴏᴛ ᴀᴜᴛoᴍᴀᴛɪcᴀʟʟʏ ᴀᴜᴛo ᴀᴘᴘʀᴏᴠᴇᴅ ᴜsᴇʀs.
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
APPROVED_TEXT = environ.get("APPROVED_TEXT", f"<b>ʜᴇʟʟo {mention},\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ. ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {title}</b>""")

#------------------------------ ᴄʀᴇᴅɪᴛ -------------------------------

# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT

#---------------------------••••••••••••••-------------------------------
