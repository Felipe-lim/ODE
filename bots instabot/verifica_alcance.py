from instabot import Bot
import time as tm
import random as rd
import shutil


bot = Bot()


#declarando as contas a serem acessadas
ext_users = ['users']
#lista com ids das contas
ext_ids = []
data = ['1', '2', '3']
#fazer login
bot.login(username="fionagatos", password="pitocofiona3")


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
    elif n%25==0:
        tm.sleep(18000)
    elif n%4==0:
        espere(3)
    elif n%6==0:
        #espera muito tempo depois de 80 contas
        tm.sleep(rd.uniform(1500,2000))
    elif n%2 == 0:
        espere(2)
    else:
        espere(1)

n=0
error_counter=0
for x in ext_users:
    #função de espera
    como_esperar(n)

    #preenchendo a lista de ids
    ext_ids.append(bot.get_user_id_from_username(ext_users[n]))

    # pegando o len para parar o código em caso de erro
    aux1=len(followers)
    #preenchendo a lista de seguidores
    followers = bot.get_user_followers(ext_ids[n])
    aux2=len(followers)

    #testando código em caso de erro
    if aux1==aux2:
        error_counter+=1
    else:
        error_counter=0

    if error_counter==2:
        shutil.rmtree('config', ignore_errors=True)
        exit()

    #acrescentando seguidores aos dados
    data = data + followers
    print(data)

    #tirando repetições
    data=set(data)
    data=list(data)
    
    #contando repetições
    counter=len(data)

    print(counter)
    print(ext_users[n])
    n += 1
    








