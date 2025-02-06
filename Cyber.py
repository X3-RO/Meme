import os, sys, re, requests, bs4, time, random, json, string,uuid
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
os.system('xdg-open https://t.me/+cd2wzNiC2XQ2NGZl')        
ugen=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ UA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
for x in range(5000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='K)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) obsidian/1.6.3 Chrome/120.0.6099.291 Electron/28.3.3 Safari/537.36"
    return xx    




          
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LINEX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sys.stdout.write('\x1b]2;CYBER WORLD\x07')
def clear():os.system('clear');print(logo)
def linex():print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOUR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";blue="\033[38;5;6m"
BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
logo=(f"""
{green}

 ▗▄▄▖▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖ 
▐▌    ▝▚▞▘ ▐▌ ▐▌▐▌   ▐▌ ▐▌
▐▌     ▐▌  ▐▛▀▚▖▐▛▀▀▘▐▛▀▚▖
▝▚▄▄▖  ▐▌  ▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌
                          
                          
                          
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ """)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ NAME ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
boy = ["Abdullah Hossain","Arif Rahman","Asif Ahmed","Bashir Chowdhury","Binod Sarker","Rafiq Miah","Mohammad Khan","Mahmud Ali","Mahin Islam","Masud Hossain","Mustafa Uddin","Mohiuddin Bhuiyan","Noor Khan","Nasir Ahmed","Nurul Haque","Rajib Siddique","Rezaul Islam","Riyad Rahman","Sabbir Mia","Sadik Chowdhury","Samsuddin Mollah","Selim Sarker","Shahid Hossain","Shafik Ahmed","Shams Uddin","Shahin Alam","Tanveer Khan","Touhid Hossain","Iqbal Rahman","Jafar Mia","Jewel Siddique","Ziaur Islam"]
girl = ["Ayesha Sultana","Momena Begum","Rokeya Sultana","Fatema Anwar","Sultana Kamal","Jahanara Alam","Ruma Akter","Farzana Yasmin","Salma Begum","Nusrat Jahan","Shaheen Akter","Sabrina Sultana","Purnima Roy","Shirin Akter","Jannatul Ferdous","Mousumi Parveen","Rina Begum","Laila Islam","Rubina Sultana","Nigar Sultana","Shamima Nasrin","Dilruba Sultana","Khatun Begum","Fariha Rahman","Kazi Rupa","Mariam Begum","Selina Akter","Nabila Rahman","Sadia Islam","Rumana Akter","Sumi Akter","Hena Sultana"]
ok = []
cp = []
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MENU ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def manu():
    os.system('clear')
    pp()
    print (logo)
    print (f'{A}[{R}1{A}] {G}AUTO CREATE ')
    print (f'{A}[{R}2{A}] {G}ANY PROBLEM CONTACT ME TELEGRAM ')
    print (f'{A}[{R}3{A}] {G}ANY PROBLEM CONTACT ME WHATS APP ')
    print (f'{A}[{R}4{A}] {G}JOIN WHATS APP GROUP  ')
    linex()
    sel = input(f'{A}[{R}={A}] {G}INPUT {R}>>{A} ')
    if sel in['1', '01']:
        create().start()
    elif sel in ['2', '02']:
        os.system('xdg-open https://t.me/+8801616305316')
        manu()
    elif sel in ['3', '03']:
    	os.system('xdg-open https://wa.me/+8801608478782');manu() 	      	
    elif sel in ['4', '04']:
    	os.system('xdg-open https://chat.whatsapp.com/LQSpgMVHogKIEdj4Oeg6Sb');manu() 	      	
    else:
        print (f'{A}[{R}={A}] {G}SELECT VALID OPTION')
        time.sleep(3)
        menu()
class create:
    
    def __init__(self):
        self.loop = 0
        self.gender = []
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ SEIF ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#        
    def start(self):
        os.system('clear')
        print (logo)
        print (f'{A}[{R}+{A}] {G}BOYS NAME IDS')
        print (f'{A}[{R}+{A}] {G}GIRLS NAME IDS')
        linex()
        gen = input(f'{A}[{R}+{A}] {G}INPUT {R}>>{A}')
        linex()
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ EXAMPLE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
        os.system('clear')
        print (logo)
        print(f'{A}[{R}+{A}] {G}EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999');linex()
        lim = int(input(f'{A}[{R}+{A}] {G}INPUT {R}>>{A}  '))
        os.system('clear')
        print (logo)
        agent = random.choice(ugen)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FULL METHOD ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#        
        headers = {
            'authority': 'p.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',}
        headers1 = {
            'authority': 'p.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,}
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r\r{G}[CYBER-AUTO] {A}{self.loop}|{G}{len(ok)}')
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://p.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",})
                gett = self.ses.post('https://p.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://p.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print (f'{B}[XIVE-CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print(f'\r{G}[CYBER-OK] '+cok['c_user']+' | '+passw+'')
                                    print(f'\r{G}[COOKIE]{BU} '+coki)
                                    linex()
                                    open("/sdcard/CYBER-AUTO-COOKIE.txt","a").write(cok['c_user']+"|"+passw+"|"+coki+"\n")
                                    open('/sdcard/CYBER-AUTO-UID.txt','a').write(cok['c_user']+'|'+passw+'\n')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                pass
            except Exception as e:
                pass               
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ CRACKED ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#                
        print ('')
        linex()
        print (f'{A}[{R}+{A}] {G}TOTAL OK ID {R}:{G} '+str(len(ok)))
        print (f'{A}[{R}+{A}] {G}TOTAL CP ID {R}: '+str(len(cp)))
        linex()
        
        
        
def pp():
    try:
            ky = open('/sdcard/Android/.nonmedia.js','r').read()
    except(FileNotFoundError):
            op = uuid.uuid1().hex.upper()
            open('/sdcard/Android/.nonmedia.js','w').write(op)
            pp()
    except(KeyError,OSError,IOError):
            linex()
            os.system('termux-setup-storage')
            print(' [×] allow storage permission ')
            pp()
    if len(ky) > 32:
            os.system('rm -rf /sdcard/Android/.nonmedia.js')
            pp()
    if len(ky) <32:
            os.system('rm -rf /sdcard/Android/.nonmedia.js')
            pp()
    else:
            pass
    clear()
    print(' [•] wait checking approval...!')
    try:
            #li = ['h','t','t','p','s',':','/','/','s','h','a','i','k','h','k','e','y','.','b','l','o','g','s','p','o','t','.','c','o','m','/','2','0','2','4','/','0','2','/','s','h','a','i','k','h','.','h','t','m','l','?','m','=','1']
            #li = ''.join(li)
            system = requests.get("https://github.com/X3-RO/Meme/blob/main/key.txt").text 
            #ck = requests.get(f'{li}').text
            if ky in system:
                linex()
                print(' [√] your key approved...!')
                time.sleep(2)
                pass
            else:
                linex()
                print(' [×] your key not approved...!')
                time.sleep(2)
                clear()
                print(f' \033[1;31mYour Key : {str(ky)} ')
                linex()
                #print('\033[1;37m [\033[1;32m1\033[1;37m]\033[1;32m 10$ \033[1;37mApproval For 1 month')
            #    print(' \033[1;37m[\033[1;32m2\033[1;37m]\033[1;32m 7$ \033[1;37mApproval For 15 days')
            #    print(' \033[1;37m[\033[1;32m3\033[1;37m]\033[1;32m 4$ \033[1;37m Approval For 7 days')
                lol=input(' \033[1;31mNOTE \033[1;92m➤\033[1;37m IF YOU BUY THEN PRESS ENTER :')
                xx='➤➤Selected=='
                os.system('xdg-open https://wa.me/+8801608478782?text='+str(ky)+lol)
                pp()
    except requests.exceptions.ConnectionError:
        exit(f' [!] Your Internet Connection Lol...!')
    except Exception as e:print(e)
       
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ EXIT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#        
manu()
