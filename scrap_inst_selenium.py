from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time as tm
import random as rd
import numpy as np
import pandas as pd
from datetime import datetime


#specify the path to chromedriver.exe 
driver = webdriver.Chrome('C:/Users/Felilpe Lima/Documents/chromedriver.exe')

#funcao de espera
def espere(m):
    #m deve levar valor de 1 a 3
    if m == 0:
        tm.sleep(rd.uniform(0,1))
    if m == 1:
        tm.sleep(rd.uniform(1,6))
    elif m == 2:
        tm.sleep(rd.uniform(8, 16))
    elif m == 3:
        tm.sleep(rd.uniform(30,120))
#função de como esperar

def como_esperar(n):
    #fazendo o programa de espera em tempos aleatorios
    if n==0:
        espere(0)
    elif n%22==0:
        espere(3)
    elif n%80==0:
        #espera muito tempo depois de 80 contas
        tm.sleep(rd.uniform(3600,3000))
    elif n%2 == 0:
        espere(2)
    else:
        espere(1)
#função login
def login(account_now):
    
    #open the webpage
    driver.get("https://www.instagram.com/accounts/login/")
    
    #target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    
    my_username = ["username"]
    my_password = ["senha"]

    print('fazendo o login como',my_username[account_now])

    #enter username and password
    username.clear()
    username.send_keys(my_username[account_now])
    password.clear()
    password.send_keys(my_password[account_now])
    
    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    tm.sleep(5)
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()
    alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()

#encontrar a data por motivo de analise de progresso
date=datetime.now()
StrDate=str(date.day) + '_' + str(date.month) + '_' + str(date.year)


#login
my_account_now=-1
#login(my_account_now)

#loading accounts
accounts_to_scrap = ['accounts']
false_accounts=[]
accounts_scrap_done = []
data=[]
number_reapeted_errors = 0
n=0

espere(2)

while n < len(accounts_to_scrap):

    account = accounts_to_scrap[n]

    #guardando contas já feitas
    accounts_scrap_done.append(account)

    link = 'http://www.instagram.com/' + account
    espere(1)

    #open the webpages
    driver.get(link)

    #espere
    como_esperar(n)

    #data = pub + seguidores + seguidos
    #procurando os elementos na pagina
    new_data=driver.find_elements_by_class_name("g47SY")

    #salvando o len dos dados antes da adicao de novos dados para anular erros
    qt1= len(data)

    #substituindo os elementos no destino
    for y in new_data:
        data.append(y.text)
    
    #salvando o len dos dados depois da adicao de novos dados para anular erros
    qt2= len(data)

    #comparando os lens antes e depois, caso o len seja o mesmo, novos dados não foram adicionados, então ele deve salvar todas as contas que funcionaram e as que não
    if qt1==qt2:
        false_accounts.append(account)

        #contando as contas que tiveram erro, pois caso aconteca muitas vezes, o instagram bloqueou a pesquisa
        number_reapeted_errors+=1

        #printando contas com erro
        print('contas  que nao deram certo:', false_accounts)

        #acrescentando ODE nas contas que deram erro
        i=0
        while i<3:
            data.append('ODE')
            i+=1
        
        

        #se ocorrerem 3 erros seguidos, outra conta deve fazer login
        if number_reapeted_errors==3:
            driver.close()

            driver = webdriver.Chrome('C:/Users/Felilpe Lima/Documents/chromedriver.exe')

            #faz novo login
            my_account_now+=1
            login(my_account_now)

            #Indica as contas que faltam fazer o scrap
            n-=3

            #remove os erros da lista de contas analisadas
            p=0
            while p<3:
                accounts_scrap_done.pop(-1)
                false_accounts.pop(-1)
                p+=1

            #remove dos dados os erros das contas
            q=0
            while q <9:
                data.pop(-1)
                q+=1


    else:
        number_reapeted_errors=0

    #fazendo tabela de seguidores e seguidos
    columns = ['Pubs  ','seguidores  ','seguindo']

    data_for_table = np.array(data).reshape(len(accounts_scrap_done), 3 )

    pd.set_option("display.max_rows",999)
    main_table = pd.DataFrame(data=data_for_table, index=accounts_scrap_done,columns=columns)

    print('\n\n', main_table)
        
    
    print('\n', data, '\n', n)
    


    n+=1

#exportando os dados até o excell
with pd.ExcelWriter("C:/Users/Felilpe Lima/Documents/Data Ode.xlsx", mode="a", engine="openpyxl") as writer:
    main_table.to_excel(writer, sheet_name=StrDate)


driver.close()
