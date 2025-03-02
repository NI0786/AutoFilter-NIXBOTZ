from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Script import script

CMD = ["/", "."]

@Client.on_message(filters.command("country", CMD))
async def country_info(bot, update):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""𝖢𝗈𝗎𝗇𝗍𝗋𝗒 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
ɴᴀᴍᴇ : {country.name()}
ɴᴀᴛɪvᴇ ɴᴀᴍᴇ : {country.native_name()}
cᴀᴘɪᴛᴀʟ : {country.capital()}
ᴘᴏᴘᴜʟᴀᴛɪᴏɴ : <code>{country.population()}</code>
ʀᴇɢɪᴏɴ : {country.region()}
sᴜʙ ʀᴇɢɪᴏɴ : {country.subregion()}
ᴛoᴘ ʟᴇvᴇʟ ᴅoᴍᴀɪɴs : {country.tld()}
cᴀʟʟɪɴɢ coᴅᴇs : {country.calling_codes()}
cᴜʀʀᴇɴᴄɪᴇs : {country.currencies()}
ʀᴇsɪᴅᴇɴcᴇ : {country.demonym()}
ᴛɪᴍᴇ zoɴᴇ : <code>{country.timezones()}</code>
"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    buttons=[[
      InlineKeyboardButton("ᴡɪᴋɪᴘᴇᴅɪᴀ", url=f"{country.wiki()}"),
      InlineKeyboardButton("ɢᴏᴏɢʟᴇ ✦", url=f"https://www.google.com/search?q={country_name}")
    ],[
       InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close_data')
    ]]
    try:
        await update.reply_photo(
            photo="https://telegra.ph/file/834750cfadc32b359b40c.jpg",
            caption=info,
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
        

# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT
#------------------------ 👻👻👻👻👻👻👻 -------------------------
