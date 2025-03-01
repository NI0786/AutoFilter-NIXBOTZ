import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, APPROVED, APPROVED_TEXT, APPROVED_IMG, CHNL_LNK
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def auto_approve(client, message: ChatJoinRequest):
    if APPROVED == True:
    chat = message.chat 
    user = message.from_user 
    print(f"{user.first_name} Joined") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        buttons = [[ 
            InlineKeyboardButton('◉ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ◉', url=CHNL_LNK)
            
        ]]
        replymarkup = InlineKeyboardMarkup(buttons)
        await client.send_photo(
            message.from_user.id, 
            photo=APPROVED_IMG, 
            caption=ʜᴇʟʟo {user},\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {chat} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ ᴀɴᴅ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {chat},
            reply_markup=markup
        )




# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT
