from pyrogram import Client, filters
import asyncio
from random import randint


BLACKLIST = []
MIN_DELAY = 1
MAX_DELAY = 20
DELAY_DIV = 100

class AutoAnswerClient(Client):
    def __init__(self, str, app_id, app_hash):
        super().__init__(str, app_id, app_hash)
        
        self.already = {}
        self.enable = False
        
        self.blacklist = BLACKLIST
        self.stopfrase = ["окей", "хорошо", "okey", "понятно", "ценю", "пон", "ок", "ok"]
        
        self.notread = []
        
        
app_id = ""
app_hash = ""

try:
    app = AutoAnswerClient("my_account", app_id, app_hash)
except:
    quit("Should be app_id and app_hash")
        

@app.on_message(filters.private)
async def mes(client, message):
    
    if message.outgoing:
        await handle_outgo(client, message)
        return
        
    if message.chat.id in client.blacklist:
         return
    
    if message.from_user.is_self:
        
        if "AS" in message.text:
            client.enable = False
            client.already = {}
            client.blacklist = BLACKLIST
            await client.send_message(message.chat.id, "Stopped")
        elif "AE" in message.text:
            client.enable = True
            await client.send_message(message.chat.id, "Started")
        elif "AR" in message.text:
            
            for cid in client.notread:
                
                await client.read_chat_history(cid)
                
            client.notread = []
                
            await client.send_message(message.chat.id, "I am read all garbage")
        
        return
    
    
    if not message.chat.type.value == "private":
        return
    elif not client.enable:
        return
    else:
        await asyncio.sleep(randint(MIN_DELAY, MAX_DELAY)/DELAY_DIV)
    
    if message.from_user.id in client.already.keys():
        if message.text.lower() in client.stopfrase and not client.already[message.from_user.id] > 4:
            client.already[message.from_user.id] = 5
            await client.send_message(message.chat.id, "Спасибо что цените мой труд 😍")
        elif client.already[message.from_user.id] == 3:
            await client.send_message(message.chat.id, "Почему ты не ценишь мой труд :(")
        elif client.already[message.from_user.id] == 4:
            await client.send_message(message.chat.id, "Ну всё я обиделся")
        elif client.already[message.from_user.id] < 3:
            await client.send_message(message.chat.id, "Я же написал мой хозяин занят")
        else:
            return
        client.already[message.from_user.id] += 1
        await asyncio.sleep(randint(MIN_DELAY, MAX_DELAY)/DELAY_DIV)
    else:
        client.already[message.from_user.id] = 1
        await client.send_message(message.chat.id, "Этот кожанный мешок занят, но автоответчик всегда свободен :)")
        await asyncio.sleep(randint(MIN_DELAY, MAX_DELAY)/DELAY_DIV)
        await client.send_message(message.chat.id, "Возможно он вам скоро ответит просто подождите")
        await asyncio.sleep(randint(MIN_DELAY, MAX_DELAY)/DELAY_DIV)
        await client.send_message(message.chat.id, "А если он не ответит, напишите ему в 19:00 по мск скорее всего он будет уже более менее свободен")
        await asyncio.sleep(randint(MIN_DELAY, MAX_DELAY)/DELAY_DIV)
        await client.send_message(message.chat.id, "Либо вообще пишите @...")
        await asyncio.sleep(randint(MIN_DELAY, MAX_DELAY)/DELAY_DIV)
        client.notread.append(message.chat.id)
    
    return
    
async def handle_outgo(client, message):
    if message.chat.id not in client.blacklist:
        client.blacklist.append(message.chat.id)
    
        await message.reply_text("он здесь мой хозяин здесь!", reply_to_message_id=message.id)


def main():
    print("started")
    app.run()

if __name__ == "__main__":
    main()