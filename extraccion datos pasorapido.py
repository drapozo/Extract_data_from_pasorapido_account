
from helium import *
import pandas as pd
import re
import time
from datetime import datetime

start_firefox('https://pasorapido.gob.do/Account/Login?ReturnUrl=%2Famw', headless=True)

    
lista_de_usuarios = ['User', 'User', 'User', 'User', 'User', 
                     'User', 'User', 'User', 'User', 'User',
                     'User', 'User', 'User', 'User', 'User',
                     'User', 'User', 'User', 'User', 'User',
                     'User', 'User', 'User', 'User', 'User',
                     'User', 'User', 'User', 'User', 'User'
                    ]

balances_del_dia = []

for i in range(0, len(lista_de_usuarios)):
    helium.go_to('https://pasorapido.gob.do/Account/Login?ReturnUrl=%2Famw')
    time.sleep(2.5)
    write(lista_de_usuarios[i], into = 'Nombre de Usuario')
    write(11111 , into = 'Contraseña')
    click('Entrar')
    time.sleep(2.5)
    linea_con_balance = Text("$").value
    balance = str(re.sub('[^0-9.,]', "", linea_con_balance))
    balances_del_dia.append(balance)
    click('salir')

estructura_del_archivo = pd.DataFrame({'Usuario': lista_de_usuarios, 
                                        'Balance' : balances_del_dia})
hoy = datetime.today()
hoy_formato_correcto = hoy.strftime("%d-%m-%Y")
nombre_del_archivo = 'Balances pasorapido del ' + hoy_formato_correcto + ' .csv'

estructura_del_archivo.to_csv(nombre_del_archivo, encoding='utf-8', index = False)
