from pyrogram import Client, filters

app_id = "28091304"
app_hash = "bf3863212c54af7a45f20a5e0f8db84e"

app = Client("my_account", app_id, app_hash)

enable = False

allready = []

@app.on_message(filters.private and filters.incoming)
async def mes(client, message):
    global enable, already
    
    if message.from_user.is_self:
        
        if "AS" in message.text:
            enable = False
            already = []
            await app.send_message(message.chat.id, "Stopped")
        elif "AE" in message.text:
            enable = True
            await app.send_message(message.chat.id, "Started")
    
    elif enable and message.chat.type.value == "private":
        if message.from_user.id in already:
            await app.send_message(message.chat.id, "Я же написал мой хозяин занят")
        else:
            already.append(message.from_user.id)
            await app.send_message(message.chat.id, "Я занят")
            await app.send_message(message.chat.id, "Возможно я вам скоро отвечу")
            await app.send_message(message.chat.id, "А если не отвечу напишите мне в 19:00 по мск")
            await app.send_message(message.chat.id, "Либо вообще напишите @...")
    
    return
    

app.run()