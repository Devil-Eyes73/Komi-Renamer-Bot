
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import jishubotz
from config import Config, Txt  
  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await jishubotz.add_user(client, message)                
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton('• ᴜᴘᴅᴀᴛᴇs', url='https://t.me/+ASSnqJ3Nz3cwNWY9'),
        InlineKeyboardButton('sᴜᴩᴩᴏʀᴛ •', url='https://t.me/+FGM0HOnjDC45ZDk1')],
        [InlineKeyboardButton('• ᴀʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('ʜᴇʟᴘ •', callback_data='help')],
        [InlineKeyboardButton("🍁 ᴍᴀsᴛᴇʀ 🍁", url='https://t.me/Devil_Eyes_Xe')]
    ])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('• ᴜᴘᴅᴀᴛᴇs', url='https://t.me/+ASSnqJ3Nz3cwNWY9'),
                InlineKeyboardButton('sᴜᴩᴩᴏʀᴛ •', url='https://t.me/+FGM0HOnjDC45ZDk1')],
                [InlineKeyboardButton('• ᴀʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('ʜᴇʟᴘ • ', callback_data='help')],
                [InlineKeyboardButton("🍁 ᴍᴀsᴛᴇʀ 🍁", url='https://t.me/Devil_Eyes_Xe')]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʙᴏᴛ •", url="https://t.me/Zoro_Xe_Bot")],
                [InlineKeyboardButton("✘ Cʟᴏsᴇ", callback_data = "close"),
                InlineKeyboardButton("《 Bᴀᴄᴋ", callback_data = "start")]
            ])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ᴍᴏʀᴇ ʙᴏᴛs •", url="https://t.me/+ASSnqJ3Nz3cwNWY9")],
                [InlineKeyboardButton("✘ Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("《 Bᴀᴄᴋ", callback_data = "start")]
            ])            
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()





@Client.on_message(filters.private & filters.command(["donate", "d"]))
async def donate(client, message):
	text = Txt.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("🦋 ᴀᴅᴍɪɴ",url = "https://t.me/Devil_Eyes_Xe"), 
        			InlineKeyboardButton("✘ ᴄʟᴏsᴇ",callback_data = "close") ]])
	await message.reply_text(text = text,reply_markup = keybord)



# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
