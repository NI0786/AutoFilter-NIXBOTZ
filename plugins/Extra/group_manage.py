# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT

from pyrogram import Client, filters, enums 
from plugins.helper.admin_check import admin_check, admin_fliter  
from plugins.helper.extract import extract_time, extract_user                               
from pyrogram.types import Message, ChatPermissions
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT_ID, LOG CHANNEL
import asyncio
from utils import temp 
from time import time, sleep
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid                              

REPORT_MSG = """ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs"""

REPORT_TXT = """@admin, @admins, /report. ғᴏʀ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs (ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ)"""

CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
INPUT_REQUIRED = "❗ Arguments Required ❗   

KICKED = """Successfully Kicked {} Members According To The Arguments Provided."""
      
START_KICK = """⛹🏻 Removing Inactive Members This May Take A While..."""
      
ADMIN_REQUIRED = """❗<b>I will not go where I am not made Admin Bii..Add Me Again with all admin rights.</b>"""
      
DKICK = """Kicked {} Deleted Accounts Successfully."""
      
FETCHING_INFO = """<b>Let's get rid of everything now...</b>"""
      
STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>"""     
    
                          
@Client.on_message(filters.command("ban"))
async def ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return 
    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.ban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))                    
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(f"Someone else is dusting off..! \n{user_first_name} \nIs forbidden.")                              
        else:
            await message.reply_text(f"Someone else is dusting off..! \n<a href='tg://user?id={user_id}'>{user_first_name}</a> Is forbidden")                      
            

@Client.on_message(filters.command("tban"))
async def temp_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    if not len(message.command) > 1:
        return
    user_id, user_first_name = extract_user(message)
    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        return await message.reply_text(text=f"Invalid time type specified. \nExpected m, h, or d, Got it: {message.command[1][-1]}")   
    try:
        await message.chat.ban_member(user_id=user_id, until_date=until_date_val)            
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(f"Someone else is dusting off..!\n{user_first_name}\nbanned for {message.command[1]}!")
        else:
            await message.reply_text(f"Someone else is dusting off..!\n<a href='tg://user?id={user_id}'>Lavane</a>\n banned for {message.command[1]}!")


@Client.on_message(filters.command(["unban", "unmute"]))
async def un_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Okay, changed ... now "
                f"{user_first_name} To "
                " You can join the group!"
            )
        else:
            await message.reply_text(
                "Okay, changed ... now "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> To "
                " You can join the group!"
            )
          

@Client.on_message(filters.private & filters.command("admin"))
async def forward_message_to_group(client, message):
 try:
    text = message.text.split(" ", 1)[1] 
    user_id = message.from_user.id
    name = message.from_user.mention
    await message.forward(LOG_CHANNEL)
    await client.send_message(LOG_CHANNEL, text=f"ᴀ ɴᴇᴡ ᴍᴇssᴀɢᴇ ғʀᴏᴍ {name}\n\nᴜꜱᴇʀ-ɪᴅ= <code>{user_id}</code>")
    await client.send_message(LOG_CHANNEL, text=f"ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ᴛᴏ ʀᴇᴘʟʏ ᴛʜᴇɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ\n\n<code>!ans {user_id} ur_messaage</code>")
    success_message = await message.reply_text("Mᴇssᴀɢᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴs. ᴡᴀɪᴛ ғᴏʀ ᴛʜᴇ ʀᴇᴘʟʏ.")

 except Exception as e:
    await message.reply_text(f"error{e}")

@Client.on_message(filters.command("ans", "!") & filters.user(ADMINS) & filters.chat(int(SUPPORT_CHAT_ID)))
async def reply_to_forwarded_message(client, message:Message):
 try: 
    mrtg = message.text.split(" ", 2)
    user_id = int(mrtg[1])
    reply_text = mrtg[2]
    await client.send_message(user_id, text=f"Rᴇᴘʟʏ ғʀᴏᴍ ᴍʏ ᴀᴅᴍɪɴ")
    await client.send_message(user_id, text=f"<code>{reply_text}</code>")
    await message.reply_text(f"ᴍᴇssᴀɢᴇ sᴇɴᴛ sᴜᴄᴇssғᴜʟʟʏ ᴛᴏ <a href='tg://user?id={user_id}'><b>ᴜsᴇʀ</b></a>")
 except Exception as e:
    await message.reply_text(f"error{e}") 
    
    
@Client.on_message(filters.incoming & ~filters.private & filters.command('inkick'))
def inkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == ("creator"):
    if len(message.command) > 1:
      input_str = message.command
      sent_message = message.reply_text(START_KICK)
      sleep(20)
      sent_message.delete()
      message.delete()
      count = 0
      for member in client.iter_chat_members(message.chat.id):
        if member.user.status in input_str and not member.status in ('administrator', 'creator'):
          try:
            client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
            count += 1
            sleep(1)
          except (ChatAdminRequired, UserAdminInvalid):
            sent_message.edit(ADMIN_REQUIRED)
            client.leave_chat(message.chat.id)
            break
          except FloodWait as e:
            sleep(e.x)
      try:
        sent_message.edit(KICKED.format(count))
      except ChatWriteForbidden:
        pass
    else:
      message.reply_text(INPUT_REQUIRED)
  else:
    sent_message = message.reply_text(CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()
    message.delete()

@Client.on_message(filters.incoming & ~filters.private & filters.command('dkick'))
def dkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == ("creator"):
    sent_message = message.reply_text(START_KICK)
    sleep(20)
    sent_message.delete()
    message.delete()
    count = 0
    for member in client.iter_chat_members(message.chat.id):
      if member.user.is_deleted and not member.status in ('administrator', 'creator'):
        try:
          client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
          count += 1
          sleep(1)
        except (ChatAdminRequired, UserAdminInvalid):
          sent_message.edit(ADMIN_REQUIRED)
          client.leave_chat(message.chat.id)
          break
        except FloodWait as e:
          sleep(e.x)
    try:
      sent_message.edit(DKICK.format(count))
    except ChatWriteForbidden:
      pass
  else:
    sent_message = message.reply_text(CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()
    message.delete()

@Client.on_message(filters.incoming & ~filters.private & filters.command('instatus'))
def instatus(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status in ('administrator', 'creator', 'ADMINS'):
    sent_message = message.reply_text(FETCHING_INFO)
    recently = 0
    within_week = 0
    within_month = 0
    long_time_ago = 0
    deleted_acc = 0
    uncached = 0
    bot = 0
    for member in client.iter_chat_members(message.chat.id):
      user = member.user
      if user.is_deleted:
        deleted_acc += 1
      elif user.is_bot:
        bot += 1
      elif user.status == "recently":
        recently += 1
      elif user.status == "within_week":
        within_week += 1
      elif user.status == "within_month":
        within_month += 1
      elif user.status == "long_time_ago":
        long_time_ago += 1
      else:
        uncached += 1
    sent_message.edit(STATUS.format(message.chat.title, recently, within_week, within_month, long_time_ago, deleted_acc, bot, uncached))
    
    
    
@Client.on_message(filters.command("mute"))
async def mute_user(bot, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(
            )
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "👍🏻 "
                f"{user_first_name}"
                " Lavender's mouth is shut! 🤐"
            )
            await bot.send_message(LOG_CHANNEL, text=f"**MUTE**\n\n**USER**: <a href='tg://user?id={user_id}'>{user_first_name}</a> \n\n**USER ID**:`{user_id}`\n\n**PERMISSIONS: MUTED**\n\nin **CHAT NAME**: {message.chat.title}\n**CHAT ID** `{message.chat.id}`\n\n\n**POWERD BY:** {temp.B_LINK}")
        else:
            await message.reply_text(
                "👍🏻 "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " The mouth is closed! 🤐"
            )
            await bot.send_message(LOG_CHANNEL, text=f"**MUTE**\n\n**USER**: <a href='tg://user?id={user_id}'>{user_first_name}</a>\n\n**USER ID**:`{user_id}`\n\n**PERMISSIONS: MUTED**\n\nin **CHAT NAME**: {message.chat.title}\n**CHAT ID** `{message.chat.id}`\n\n\n**POWERD BY:** {temp.B_LINK}")
        

@Client.on_message(filters.command("purge") & (filters.group | filters.channel))                   
async def purge(client, message):
    if message.chat.type not in ((enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL)):
        return
    is_admin = await admin_check(message)
    if not is_admin:
        return

    status_message = await message.reply_text("...", quote=True)
    await message.delete()
    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(message.reply_to_message.id, message.id):
            message_ids.append(a_s_message_id)
            if len(message_ids) == "100":
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=message_ids,
                    revoke=True
                )
                count_del_etion_s += len(message_ids)
                message_ids = []
        if len(message_ids) > 0:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message_ids,
                revoke=True
            )
            count_del_etion_s += len(message_ids)
    await status_message.edit_text(f"deleted {count_del_etion_s} messages")
    await asyncio.sleep(5)
    await status_message.delete()
    
    
@Client.on_message(filters.command("tmute"))
async def temp_mute_user(bot, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalid time type specified. "
                "Expected m, h, or d, Got it: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(
            ),
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Be quiet for a while! 😠"
                f"{user_first_name}"
                f" muted for {message.command[1]}!"
            )
            await bot.send_message(LOG_CHANNEL, text=f"**MUTE**\n\n**USER**: <a href='tg://user?id={user_id}'>{user_first_name}</a>\n\n**USER ID**:`{user_id}`\n\n**PERMISSIONS: MUTED**\n\nin **CHAT NAME**: {message.chat.title}\n**CHAT ID** `{message.chat.id}`\n\n\n**POWERD BY:** {temp.B_LINK}")
        else:
            await message.reply_text(
                "Be quiet for a while! 😠"
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " Mouth "
                f" muted for {message.command[1]}!"
            )
            await bot.send_message(LOG_CHANNEL, text=f"**MUTE**\n\n**USER**: <a href='tg://user?id={user_id}'>{user_first_name}</a>\n\n**USER ID**:`{user_id}`\n\n**PERMISSIONS: MUTED**\n\nin **CHAT NAME**: {message.chat.title}\n**CHAT ID** `{message.chat.id}`\n\n\n**POWERD BY:** {temp.B_LINK}")
        

@Client.on_message(filters.command("pin") & admin_fliter)
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(filters.command("unpin") & admin_fliter)             
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
      
      
      
      

# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT
