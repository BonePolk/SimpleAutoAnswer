from pyrogram import Client, filters

class AutoAnswerClient(Client):
    def __init__(self, str, app_id, app_hash):
        super().__init__(str, app_id, app_hash)
        
        self.already = {}
        self.enable = False
        
        self.blacklist = [1680780422]
        self.stopfrase = ["ok", "ок", "хорошо", "okey"]
        
app_id = "28091304"
app_hash = "bf3863212c54af7a45f20a5e0f8db84e"

app = AutoAnswerClient("my_account", app_id, app_hash)
    

@app.on_message(filters.private and filters.incoming)
async def mes(client, message):
    
    if not message.chat.type.value == "private":
        return
    
    if message.from_user.is_self:
        
        if "AS" in message.text:
            client.enable = False
            client.already = {}
            await client.send_message(message.chat.id, "Stopped")
        elif "AE" in message.text:
            client.enable = True
            await client.send_message(message.chat.id, "Started")
    
    if message.text.lower in client.stopfrase:
        client.already[message.from_user.id] = 7
        await client.send_message(message.chat.id, "Спасибо что цените мой труд 😍")
          
    
    elif client.enable:
        if message.from_user.id in client.already.keys():
            if client.already[message.from_user.id] == 5:
                await client.send_message(message.chat.id, "Почему ты не ценишь мой труд :(")
            elif client.already[message.from_user.id] == 6:
                await client.send_message(message.chat.id, "Ну всё я обиделся")
            elif client.already[message.from_user.id] < 5:
                await client.send_message(message.chat.id, "Я же написал мой хозяин занят")
            else:
                return
            client.already[message.from_user.id] += 1
        else:
            client.already[message.from_user.id] = 1
            await client.send_message(message.chat.id, "Этот кожанный мешок занят, но автоответчик всегда свободен :)")
            await client.send_message(message.chat.id, "Возможно он вам скоро ответит просто подождите")
            if message.chat.id not in client.blacklist:
                await client.send_message(message.chat.id, "А если он не ответит, напишите ему в 19:00 по мск скорее всего он будет уже более менее свободен")
                await client.send_message(message.chat.id, "Либо вообще пишите @...")
    
    return
    



def main():
    app.run()

if __name__ == "__main__":
    main()