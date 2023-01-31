# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b>♕︎ ᴘᴇʀɪɴᴛᴀʜ ᴜɴᴛᴜᴋ ᴘᴇɴɢɢᴜɴᴀ ʙᴏᴛ ɪɴɪ
 ➪ /start - Mulai Bot
 ➪ /about - Tentang Bot ini
 ➪ /help - Bantuan Perintah Bot ini
 ➪ /ping - Untuk mengecek bot hidup
 ➪ /uptime - Untuk melihat status bot 
 
 ♕︎ ᴘᴇʀɪɴᴛᴀʜ ᴜɴᴛᴜᴋ ᴘᴇᴍɪʟɪᴋ ʙᴏᴛ ɪɴɪ
 ➪ /logs - Untuk melihat logs bot
 ➪ /setvar - Untuk mengatur var dengan command dibot
 ➪ /delvar - Untuk menghapus var dengan command dibot
 ➪ /getvar - Untuk melihat salah satu var dengan command dibot
 ➪ /users - Untuk melihat statistik pengguna bot
 ➪ /batch - Untuk membuat link lebih dari satu file
 ➪ /speedtest - Untuk Mengetes kecepatan server bot
 ➪ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

♔︎ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :  </b><a href='https://t.me/TeknoProject'>@TeknoProject</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʙᴀɴᴛᴜᴀɴ", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ :

@{} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴜɴᴛᴜᴋ ᴍᴇɴʏɪᴍᴘᴀɴ ᴘᴏsᴛɪɴɢᴀɴ ᴀᴛᴀᴜ ғɪʟᴇ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴅɪᴀᴋsᴇs ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴋʜᴜsᴜs.

 • ᴘᴇᴍʙᴜᴀᴛ ʙᴏᴛ : @{}
 • ғʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • ʀᴇᴘᴏ : <a href='https://github.com'>Tekno Project V2</a>

𖠌 ᴘᴇᴍɪʟɪᴋ ʀᴇᴘᴏ : @Rzrgnshn
"""
