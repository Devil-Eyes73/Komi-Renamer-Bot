import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = int(os.environ.get("ADMIN", ""))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>ʜᴇʟʟᴏ</b> {} 👋 

<b>➻ ᴛʜɪs ɪs ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀғᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏʏ.</b>

<b>➻ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏғ ʏᴏᴜʀ ғɪʟᴇs.</b>

<b>➻ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ғɪʟᴇ ᴀɴᴅ ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ.</b>

<b>➻ ᴛʜɪs ʙᴏᴛ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛs ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.</b>

<b>ʙᴏᴛ ɪs ᴍᴀᴅᴇ ʙʏ :</b> @ZPro_Bots"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>๏ ᴍʏ ɴᴀᴍᴇ</b> : {}
├<b>๏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</b> : <a href=https://t.me/ZPro_Bots>ᴢᴘʀᴏ ʙᴏᴛs</a> 
├<b>๏ sᴜᴘᴘᴏʀᴛ</b> : <a href=https://t.me/+FGM0HOnjDC45ZDk1>sᴜᴘᴘᴏʀᴛ</a>
├<b>๏ ʟɪʙʀᴀʀʏ</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>๏ ʟᴀɴɢᴜᴀɢᴇ</b> : <a href=https://www.python.org>Python 3</a>
├<b>๏ ᴀɴɪᴍᴇ</b> : <a href=https://t.me/anime_infinitely>ᴀɴɪᴍᴇ ɪɴғɪɴɪᴛᴇʟʏ</a>
├<b>๏ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ</b> : <a href=https://t.me/+6I-gRwgRShUzNWVl>ᴏᴛᴀᴋᴜ ᴢᴏɴᴇ</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b>ʜᴏᴡ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</b>
  
➪ /start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ sᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
➪ /del_thumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
➪ /view_thumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

📑 <b>ʜᴏᴡ ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ</b>

➪ /set_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
➪ /see_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
➪ /del_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
➪ Exᴀᴍᴘʟᴇ - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>ʜᴏᴡ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴀ ғɪʟᴇ</u></b>

<b>➪ sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ᴛʏᴘᴇ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴀɴᴅ sᴇʟᴇᴄᴛ ᴛʜᴇ ғᴏʀᴍᴀᴛ [ ᴅᴏᴄᴜᴍᴇɴᴛ, ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ ].</b>           

<b>ᴀɴʏ ᴏᴛʜᴇʀ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ :-</b> <a href=https://t.me/ZPro_Bots><b>ᴍᴀsᴛᴇʀ</b></a>
"""

    PROGRESS_BAR = """\n
 <b>‣ Sɪᴢᴇ :</b> {1} | {2}
️ <b>‣ Dᴏɴᴇ :</b> {0}%
 <b>‣ Sᴘᴇᴇᴅ :</b> {3}/s
️ <b>‣ Eᴛᴀ :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>

<b>ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 𝟸𝟶 ʀs ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.</b>

<b>🛍 ᴜᴘɪ ɪᴅ:</b> `anime-legend@axl`
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
