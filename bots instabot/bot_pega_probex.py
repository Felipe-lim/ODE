from instabot import Bot
bot = Bot()
import shutil



#fazer login
#bot.login(username="auroragatabranca@gmail.com", password="pitocofiona")
bot.login(username="fionagatos", password="pitocofiona3")

print("ok")

#coletando as contas que postaram com as tags
userids=bot.get_hashtag_users("probex2021")

print("ok")


#transformando as ids em username
name = []
n4 =0
for x in userids:
    name.append(bot.get_username_from_user_id(x))
    n4+=1

shutil.rmtree('config', ignore_errors=True)

print("ok")

#limpando as repetições
tname = set(name)
print("ok")
name_list = list(tname)
print("ok")
print(name_list)

