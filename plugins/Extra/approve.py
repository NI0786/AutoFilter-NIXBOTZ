import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, APPROVED, APPROVED_TEXT, APPROVED_IMG, CHNL_LNK
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m : Message):
    n = m.chat
    k = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(n.id, k.id)
        await app.send_message(k.id, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @VJ_Botz __**".format(m.from_user.mention, m.chat.title))
        add_user(k.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
