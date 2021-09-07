from instabot import Bot
import numpy as np
import pandas as pd
from time import sleep


bot = Bot()
#declarando as contas a serem acessadas
ext_users = ['extensaocear']
#lista com ids das contas
ext_ids = []


#fazer login
bot.login(username="cami.oliveiro", password="100000nudes")

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

    #calculando medias
    like_avg = nlikes//(nmce)
    like10_avg = nlikes10 // cont

    comment_avg = ncomments // (nmce)
    comment10_avg = ncomments10 // cont
    #adicionando dados a lista
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
