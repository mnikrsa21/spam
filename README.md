# Panduan install
```bash
apt update -y && apt upgrade -y
```
```bash
apt install python2 -y
```
```bash
apt install pip2 -y
```
```bash
pip2 install -r requirements.txt
```
if pip2 is can't install ( on ubuntu, etc ) you can install with using
```bash
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
```
```bash
python2 get-pip.py
```
python2 -m install pip
# Setting config
- Open file mail.py
- Ganti value dari variabel :
  ```python
  - smtp = "ganti_dengan_server_mail"
  - port = ganti_dengan_port_server
  - fromaddr = "ganti_dengan_username_atau_addres_akun"
  - passwd = "ganti_dengan_password_akun"
   ```
# Jumlah input
- 1-11 send 1-11 message
- unli send unlimited message
# Run script
- python2 mail.py

```txt
This tool for educational purpose only!
```
