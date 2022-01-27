# Code by Tryo ( It's me X )
#!chaset utf-8
import smtplib
import os
import time
import linecache
import argparse
from colorama import Fore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


hijau = Fore.GREEN
biru = Fore.BLUE
kuning = Fore.YELLOW
merah = Fore.RED
putih = Fore.WHITE

logo = """
		{}_  _{}    ____    ____ ___  ____ _  _
                {} \/ {}    | __ __ [__  |__] |__| |\/|
                {}_/\_{}    |__]    ___] |    |  | |  |
	"""

os.system('clear')
print(logo).format(merah, biru, merah, biru, merah, biru)
print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
print('')

# GANTI DENGAN AKUN MU! / REPLACE THIS TO YOUR ACCOUNT
smtp = "smtp.gmail.com"     # GANTI DENGAN SERVER MU
port = 587     # GANTI DENGAN PORT SERVER ( TANPA TANDA PETIK )
fromaddr = "lanla1632@gmail.com"     # GANTI DENGAN ADDRES/USERNAME AKUN
paswd = "Trio1632"     # GANTI DENGAN PASSWORD AKUN MU

toaddr = raw_input(biru+"Masukan Email Penerima : "+putih)
subj = raw_input(biru+"Masukan Subject : "+putih)
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subj

body = raw_input(biru+"Masukan Pesan : "+putih)
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(fromaddr, paswd)
text = msg.as_string()
send = server.sendmail(fromaddr, toaddr, text)
lagi = raw_input(biru+'Masukan Jumlah : '+putih)
if lagi == "1":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "2":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "3":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "4":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "5":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "6":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "7":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "8":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "9":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "10":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
    print(merah+'Selesai!'+putih)
elif lagi == "unli":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(merah+'Alert! this unlimited send message!')
    time.sleep(1)
    print(biru+"If you want to stop, click "+merah+"CTRL+Z")
    time.sleep(2)
    print(biru+'Mengirim'+merah+' ....')
    while (1 + 2 == 3):
        server.sendmail(fromaddr, toaddr, text)
        print(hijau+"[+]"+biru+'Berhasil mengirim pesan ke '+merah+toaddr)
elif lagi == "11":
    os.system('clear')
    print(logo).format(merah, biru, merah, biru, merah, biru)
    print(merah+'[-] '+biru+'Tools  : '+hijau+'Gmail Spammer')
    print(merah+'[-] '+biru+'GitHub : '+hijau+'github.com/mnikrsa21')
    print(merah+'[-] '+biru+'Lang   : '+hijau+'Python2')
    print('')
    print(biru+'Mengirim'+merah+' ....')
    for i in range(11):
        exec 'send'
        print(hijau+'Berhasil mengirim '+lagi+' pesan ke '+merah+toaddr)
else:
    print('Maksimal 11!, jika ingin unlimited ketikan unli')
    time.sleep(2)
    os.system('python2 mail.py')
