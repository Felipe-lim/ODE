from instabot import Bot
import numpy as np
import pandas as pd

bot = Bot()



#fazer login
bot.login(username="extensao@cear.ufpb.br", password="ode2020")

#definindo as tags
tags = ["extensaoufpb", "proexufpb", "ufpb","probex2021", "editaisdaextensao"]

#coletando as contas que postaram com as tags
userids = []
n1 = 0
for x in tags:
    userids.append(bot.get_hashtag_users(tags[n1]))
    n1 += 1



#separando somente as contas que postaram com as 5 tags
tuser = []
n=0
for x in userids:
    for y in userids[n]:
        n2 = 0
        n3 = 0
        while n2 <= 5:
            # ao menos 3 das tags por pub ja servem
            if n3 == 3:
                tuser.append(y)
                n2=5
                break
            elif n2==5:
                break
            elif y in userids[n2]:
                n3+=1
            n2+=1
    n+=1



#transformando as ids em username
name = []
n4 =0
for x in tuser:
    name.append(bot.get_username_from_user_id(tuser[n4]))
    n4+=1

#limpando as repetições
tname = set(name)
name_list = list(tname)

print(name_list)

#declarando as contas a serem acessadas
ext_users = name_list

#lista com ids das contas
ext_ids = []


#preenchendo a lista de ids
n=0
for x in ext_users:
    ext_ids.append(bot.get_user_id_from_username(ext_users[n]))
    n += 1

#tabela com seguidores e seguidos
followship = [ 'seguidos','seguidores']
gdata = []  #gdata = general data

#carregando os seguidos,seguidores, média likes ult 10, média geral likes, quantidade geral likes
#mesmo de like serve para comentarios, total de publicações
n=0


for x in ext_ids:


    nfollowing = bot.get_user_following(ext_ids[n])
    nfollower = bot.get_user_followers(ext_ids[n])

    #carrega lista de publicacao para cada perfil de extensao
    extmedia = bot.get_total_user_medias(ext_ids[n])
    #numero de midias de cada extensao
    nmce = len(extmedia)
    
    #pegando dados de cada pub
    cont=0
    n2 = 0
    nlikes = 0
    nlikes10 = 0
    ncomments = 0
    ncomments10 = 0
    for x in extmedia: 
        #likes
        likes = bot.get_media_likers(extmedia[n2])
        print('\n likes', '\n', extmedia[n2], likes,'\n')
        nlikes += len(likes)
        #comenarios
        comments = bot.get_media_commenters(extmedia[n2])
        print('\n comentarios', '\n', extmedia[n2], comments,'\n')
        ncomments += len(comments)

        #media dos 10 ultimos
        if n2 < 10:
            nlikes10 += len(likes)
            ncomments10 += len(comments)
            cont +=1
        n2 +=1

    like_avg = nlikes//(nmce)
    like10_avg = nlikes10 // cont

    comment_avg = ncomments // (nmce)
    comment10_avg = ncomments10 // cont

    gdata.append(len(nfollowing))
    gdata.append(len(nfollower))
    gdata.append(nmce)

    gdata.append(like10_avg)
    gdata.append(like_avg)
    gdata.append(nlikes)

    gdata.append(comment10_avg)
    gdata.append(comment_avg)
    gdata.append(ncomments)

    n += 1



#fazendo tabela de seguidores e seguidos
data = np.array(gdata).reshape(len(ext_ids), 9 )
columns = ['seguindo', 'seguidores', 'np', 'ml10', 'mlg', 'nl', 'mc10', 'mcg', 'nc']

#np == numero publicacoes
#ml10 == media de like das 10 ultimas pubs
#mlg == media de likes geral
#nl == numero de likes
# mc10 == media de comentario das 10 ultimas pubs
# mcg == media de comentarios geral
# nc == numero de comentarios 


main_table = pd.DataFrame(data=data, index=ext_users,columns=columns)

print('\n\n', main_table)

