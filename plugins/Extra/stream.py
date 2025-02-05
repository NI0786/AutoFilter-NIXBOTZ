# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT

from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from info import STREAM_MODE, URL, LOG_CHANNEL
from urllib.parse import quote_plus
from NIXBOTZ.util.file_properties import get_name, get_hash, get_media_file_size
from NIXBOTZ.util.human_readable import humanbytes
import humanize
import random

@Client.on_message(filters.private & filters.command("stream"))
async def stream_start(client, message):
    if STREAM_MODE == False:
        return 
    msg = await client.ask(message.chat.id, "**Now send me your file/video to get stream and download link**")
    if not msg.media in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT]:
        return await message.reply("**Please send me supported media.**")
    if msg.media in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT]:
        file = getattr(msg, msg.media.value)
        filename = file.file_name
        filesize = humanize.naturalsize(file.file_size) 
        fileid = file.file_id
        user_id = message.from_user.id
        username =  message.from_user.mention 

        log_msg = await client.send_cached_media(
            chat_id=LOG_CHANNEL,
            file_id=fileid,
        )
        fileName = {quote_plus(get_name(log_msg))}
        stream = f"{URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        download = f"{URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
 
        await log_msg.reply_text(
            text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n•• ᴜꜱᴇʀɴᴀᴍᴇ : {username} \n\n•• ғɪʟᴇ ɴᴀᴍᴇ : {fileName}",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🚀 ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ", url=download),  
                    InlineKeyboardButton('wᴀᴛᴄʜ ᴏɴʟɪɴᴇ 👩🏻‍💻', url=stream)  
                ]]
            )
        )
        x=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("🚀 ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ", url=download),  
                InlineKeyboardButton('wᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🧿', url=stream)
            ]] 
        )
        msg_text = """<b><i><u>yᴏᴜʀ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ !</u></i></b>\n\n<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>\n\n<b> 🖥 ᴡᴀᴛᴄʜ  :</b> <i>{}</i>\n\n<b>🚸 Nᴏᴛᴇ : ʟɪɴᴋ ᴡᴏɴ'ᴛ ᴇxᴘɪʀᴇ ᴛɪʟʟ ɪ ᴅᴇʟᴇᴛᴇ</b>"""

        await message.reply_text(text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(msg)), download, stream), quote=True, disable_web_page_preview=True, reply_markup=x)


# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT
#------------------------ 👻👻👻👻👻👻👻 -------------------------