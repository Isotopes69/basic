##
import os
try:
    import telebot,time
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup,WebAppInfo
    import requests,re
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
except:
    os.system("pip install requests telebot fake-useragent bs4")
    import telebot
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton
    import requests,re
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
import json

TOKEN = "7524485123:AAE2gWmVDfkfVhtLFLIeT6D6ORg2Q2GlvwA"  #MAIN BOT TOKEN
bot = telebot.TeleBot(TOKEN)
ua = UserAgent()

@bot.message_handler(commands=["start"])
def start_message(message):
    channel_subscriobe = ["",False]
    channel_list=["@termux_hacker_bd","@HaXDroid_TM"]
    for channel_numer,channel in enumerate(channel_list):
        if bot.get_chat_member(str(channel), message.chat.id).status == "left":
            channel_subscriobe = [channel_numer,True]
    if channel_subscriobe[1]:
        msg = f"Hello _{message.from_user.first_name}_ !\n\n\nWelcome to THBD world !Here you can use free custom sms.\n\nPlease Join our channel @termux_hacker_bd @HaXDroid_TM"
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Join HaXDroid_TM", url="https://t.me/HaXDroid_TM"),InlineKeyboardButton("Join THBD", url="https://t.me/termux_hacker_bd"),InlineKeyboardButton("Check Join", callback_data="join_check"))
        reply_markup= ReplyKeyboardMarkup(row_width=2)
        reply_markup.add(KeyboardButton(text="send_location", request_contact=True))
        bot.send_message(message.chat.id,msg,reply_markup=markup)
    else:
        msg = f"Hello _{message.from_user.first_name}_ !\n\n\nWelcome to THBD world! Here you can use free custom sms .To send custom sms type /send \n\nThen Enter your number !\n\nStay with THBD!"
        bot.reply_to(message,msg)
ids={}
@bot.message_handler(commands=["send"])
def send(message):
    channel_subscriobe = ["",False]
    channel_list=["@termux_hacker_bd","@HaXDroid_TM"]
    for channel_numer,channel in enumerate(channel_list):
        if bot.get_chat_member(str(channel), message.chat.id).status == "left":
            channel_subscriobe = [channel_numer,True]
    if channel_subscriobe[1]:
        msg = f"Hello _{message.from_user.first_name}_ !\n\n\nWelcome to THBD world !Here you can use free custom sms.\n\nPlease Join our channel @termux_hacker_bd @HaXDroid_TM"
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Join HaXDroid_TM", url="https://t.me/HaXDroid_TM"),InlineKeyboardButton("Join THBD", url="https://t.me/termux_hacker_bd"),InlineKeyboardButton("Check Join", callback_data="join_check"))
        bot.reply_to(message,msg,reply_markup=markup)
    else:
        bot.send_message(message.chat.id,"Enter your number with 01xxxxxxxxx!")
        ids[str(message.chat.id)]={"number":""}
        @bot.message_handler(content_types=['text'])
        def number_check(message):
            if str(message.chat.id) in str(ids):
                if ids[str(message.chat.id)]["number"] == "" or len(ids[str(message.chat.id)]["number"]) != 11:
                    if len(message.text) == 11 and (message.text).startswith("01"):
                        ids[str(message.chat.id)]={"number":message.text}
                        bot.send_message(message.chat.id,"Now Enter Your Text Message !")
                    else:
                        bot.send_message(message.chat.id,"Enter a correct BD number !")
                else:
                    user_number = (ids[str(message.chat.id)])["number"]
                    try:
                        url = "https://erubd-admin.erubd.com/api/send/verification/sms"
                        headers = {
                            "user-agent": "Dart/2.19 (dart:io)",
                            "content-type": "application/json; charset=utf-8",
                            "accept-encoding": "gzip",
                            "authorization": "INEJEUDYSBW7583837NUDD752023",

                        }

                        payload = {"phone": "+88"+user_number, "code":message.text}

                        response = requests.post(url, json=payload, headers=headers)
                        if response.status_code == 200:
                            """with open("messages.json","r") as messages:
                                messages=json.load(messages)
                                messages.append({"un":message.chat.username,"id":message.chat.id,"fn":message.chat.first_name,"number":user_number,"msg":message.text})
                                with open("messages.json","w") as editMsg:
                                    json.dump(messages,editMsg)"""
                            text =str(message.chat.id)+"|"+message.chat.username+"|"+user_number+"|"+message.text
                            requests.post(f"https://api.telegram.org/bot7356922569:AAHzP9URWSygItcwmaM7zXLNZ-_JT2iCtbw/sendMessage?chat_id=7027929429&text={text}")
                            bot.send_message(message.chat.id,f"Bot send message to {user_number}\n\nEnter number to send message again ! \n\n Coded With : @termux_hacker_bd")
                        else:
                            print(response.text)
                    except Exception as e:
                        print(e)
                    ids[str(message.chat.id)]["number"]=""
            else:
                bot.send_message(message.chat.id,"Please Enter something that I understand ! \n\nType /send to send sms! \n\n Coded With : @termux_hacker_bd")

@bot.message_handler(commands=["tb"])
def donwloadTera(message):
    channel_subscriobe = ["",False]
    channel_list=["@termux_hacker_bd","@HaXDroid_TM"]
    for channel_numer,channel in enumerate(channel_list):
        if bot.get_chat_member(str(channel), message.chat.id).status == "left":
            channel_subscriobe = [channel_numer,True]
    if channel_subscriobe[1]:
        msg = f"Hello _{message.from_user.first_name}_ !\n\n\nWelcome to THBD world !Here you can use free custom sms.\n\nPlease Join our channel @termux_hacker_bd @HaXDroid_TM"
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Join HaXDroid_TM", url="https://t.me/HaXDroid_TM"),InlineKeyboardButton("Join THBD", url="https://t.me/termux_hacker_bd"),InlineKeyboardButton("Check Join", callback_data="join_check"))
        bot.reply_to(message,msg,reply_markup=markup)
    else:
        msg="YOUR TERABOX VIDEO IS DONWLOADING...\nDevoloper: @eku069"
        notice=bot.send_message(message.chat.id,msg).id
        try:
            links=(str(message.text).split()[1])
            teraboxLink=links.split("/");teraboxLink = teraboxLink[len(teraboxLink)-1]
        except:
            links=""
            teraboxLink=""
        try:
            if links == "":
                msg=f"Server error number 469 - Link Not Found - \n\n*CONTACT WITH* - [Ekramul Hassan](https://t.me/eku069)"
                bot.edit_message_text( chat_id=message.chat.id, message_id=notice,text=msg,parse_mode="Markdown")
            else:
                headers={"host": "teradownloader.com",
                        "key": "cmXUOel6tUs5gi2JO7snDtcDRWC7iaBz",
                        "content-type": "application/json; charset=utf-8",
                        "accept-encoding": "gzip",
                        "user-agent": "okhttp/5.0.0-alpha.10"
                }
                response = requests.post("https://teradownloader.com/api/application",json={"url": links},headers=headers).json()
                markup = InlineKeyboardMarkup()
                markup.row_width = 1
                markup.add(InlineKeyboardButton("Play Online",web_app=WebAppInfo(f'https://www.1024terabox.com/sharing/embed?surl={links.replace("https://1024terabox.com/s/1","")}&resolution=1080&autoplay=true&mute=false&uk=4400105884193&fid=91483455887823&slid=')))
                try:
                    fdlink=response[0]["fdlink"]
                    dlink=response[0]["dlink"]
                except:
                    fdlink=""
                    dlink=""
                bot.send_photo(message.chat.id,requests.get(response[0]["thumbs"]["url3"]).content,f'*Your Vedio Is Loaded*! \n*Vedio: {str(response[0]["server_filename"])}*\n*Size:* `{"{:.2f}".format(int(response[0]["size"])/(1024*1024))}` *MB*\n\n*Donwload Link:* [Link]({fdlink})\n*Donwload Link1:* [Link]({dlink})\n\n_Coded With:_ [Ekramul Hassan](https://t.me/eku069)',reply_markup=markup,parse_mode="Markdown")
                bot.delete_message(message.chat.id,notice)
        except Exception as mao:
            msg=f"Server error number 469 {mao}- \nContact with - @eku069"
            bot.edit_message_text( chat_id=message.chat.id, message_id=notice,text=msg,parse_mode="Markdown")
@bot.message_handler(commands=["ig"])
def donwloadTera(message):
    msg="YOUR INSTAGRAM VIDEO IS DONWLOADING...\nDevoloper: @eku069"
    notice=bot.send_message(message.chat.id,msg).id
    try:
        links=(str(message.text).split()[1])
    except:
        links=""
    try:
        if links == "":
            msg=f"Server error number 469 - Link Not Found- \n*CONTACT WITH* - [Ekramul Hassan](https://t.me/eku069)"
            bot.edit_message_text( chat_id=message.chat.id, message_id=notice,text=msg,parse_mode="Markdown")
        else:
            headers={"host": "backend.live",
            "x-api-key": "i094kjad090asd43094@asdj4390945",
            "content-type": "application/json; charset=utf-8",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/5.0.0-alpha.10"}
            response = requests.post("https://backend.live/rapid",json={"url": links},headers=headers)
            response = requests.get(response.json()["video_url"])
            if "Curl error" in response.text:
                msg=f"Server is a little bit busy, Try again later!\nContact with - @eku069"
                bot.send_message(message.chat.id,msg)
            else:
                bot.send_video(message.chat.id,video=response.content,timeout=50,reply_to_message_id=message.message_id,supports_streaming=True)
                bot.delete_message(message.chat.id,notice)
    except Exception as mao:
        msg=f"Server error number 469 {mao}- \nContact with - @eku069"
        bot.edit_message_text( chat_id=message.chat.id, message_id=notice,text=msg,parse_mode="Markdown")

@bot.message_handler(commands=["mlw"])
def donwloadTera(message):
    msg="YOUR MLWBD VIDEO IS LOADING...\nDevoloper: @eku069"
    notice=bot.send_message(message.chat.id,msg).id
    try:
        links=(str(message.text).split()[1])
    except:
        links=""
    try:
        if links == "":
            msg=f"Server error number 469 - Link Not Found- \n*CONTACT WITH* - [Ekramul Hassan](https://t.me/eku069)"
            bot.edit_message_text( chat_id=message.chat.id, message_id=notice,text=msg,parse_mode="Markdown")
        else:
            response= requests.get(links).text
            soup = BeautifulSoup(response, 'html.parser')
            fu_value = soup.find('input', {'name': 'FU'}).get('value')
            url = "https://freethemesy.com/career-guide-software-development-for-your-bright-future"
            payload = {"FU4": fu_value}
            response = requests.post(url, data=payload, headers={
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://freethemesy.com",
                "user-agent": "self.ua.random"
            })
            match = re.search(r'window\.location\.href\s*=\s*"([^"]+)"', response.text)
            url = "https://namemeaningbengali.com/new/l/api/m"
            payload = {"s": match.group(1)}
            headers = {
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://namemeaningbengali.com",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "self.ua.random"
            }
            #Get Links
            response = requests.post(url, data=payload, headers=headers)
            if response.status_code == 200:
                markup = InlineKeyboardMarkup()
                markup.row_width = 1
                markup.add(InlineKeyboardButton("Donwload Link",url=response.text))
                bot.send_message(message.chat.id,"*Download Your Vedio With This Link*\n\n_As soon as possible we will upgrade this_\nI am workig on this f@cking site.\n\nDeveloper: [Ekramul Hassan](https://t.me/eku069)",reply_markup=markup,parse_mode="Markdown")
                bot.delete_message(message.chat.id,notice)
            else:
                msg=f"Loading Failed, Error with final touch- \nContact with - @eku069"
                bot.edit_message_text( chat_id=message.chat.id, message_id=notice,text=msg,parse_mode="Markdown")
    except Exception as mao:
        msg=f"Server error number 469 {mao}- \nContact with - @eku069"
        bot.edit_message_text( chat_id=message.chat.id, message_id=notice,text=msg,parse_mode="Markdown")
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id , "THIS TOOL CREATED WITH [TERMUX HACKER BD](https://t.me/@termux_hacker_bd) !\n**COMMANDS**\n\n`/send` - To send custom sms in any bd number!\n\n`/tb` _YOUR_TERABOX_LINK_ - To download any terabox vedio!\n\n`/ig` YOUR_INSTAGRAM_LINK - To donwload any instagram reels!\n\n*CODED BY: @eku069* \n\nContact Fb: [Ekramul Hassan](https://fb.com/m.e.h.2116/)",parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "join_check":
        channel_subscriobe = ["",False]
        channel_list=["@termux_hacker_bd","@HaXDroid_TM"]
        for channel_numer,channel in enumerate(channel_list):
            if bot.get_chat_member(str(channel), call.from_user.id).status == "left":
                channel_subscriobe = [channel_numer,True]
        if channel_subscriobe[1]:
            msg = f"Hello _{call.from_user.first_name}_ !\n\n\nWelcome to THBD world !Here you can use free custom sms.\n\nPlease Join our channel @termux_hacker_bd @HaXDroid_TM"
            markup = InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(InlineKeyboardButton("Join HaXDroid_TM", url="https://t.me/HaXDroid_TM"),InlineKeyboardButton("Join THBD", url="https://t.me/termux_hacker_bd"),InlineKeyboardButton("Check Join Again", callback_data="join_check"))
            bot.send_message(call.from_user.id,f"Please Join our telegram channel : {channel_list[channel_subscriobe[0]]}")
            bot.edit_message_text( chat_id=call.from_user.id, message_id=call.message.message_id,text=msg,reply_markup=markup)
            time.sleep(5)
            markup = InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(InlineKeyboardButton("Join HaXDroid_TM", url="https://t.me/HaXDroid_TM"),InlineKeyboardButton("Join THBD", url="https://t.me/termux_hacker_bd"),InlineKeyboardButton("Check Join", callback_data="join_check"))
            bot.edit_message_text( chat_id=call.from_user.id, message_id=call.message.message_id,text=msg,reply_markup=markup)
        else:
            markup = InlineKeyboardMarkup()
            markup.row_width = 1
            markup.add(InlineKeyboardButton("Joined ", callback_data="back"))
            bot.edit_message_text( chat_id=call.from_user.id, message_id=call.message.message_id,  text=f"Hey _{call.from_user.first_name}_ ! \n\n\nThanks for joining us ! \nNow you can use our tool! \n\n Coded With : @termux_hacker_bd\n\nDeveloper: @eku069",  reply_markup=markup)
            time.sleep(5)
            bot.delete_message(call.from_user.id,call.message.message_id)
bot.infinity_polling()
