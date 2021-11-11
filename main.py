import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('TOKEN')

def get_eva_status(user_id):
    status = vk.friends.getOnline()
    print(status)
    if user_id in status:
        return True
    else:
        return False

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
flag = False
longpoll = VkLongPoll(vk_session)
s = 1
# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
#    #Слушаем longpoll, если пришло сообщение то:
#         if event.text == 'Привет' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
#             print(event.text)
#             if event.from_user: #Если написали в ЛС
#                 vk.messages.send(user_id=event.user_id, random_id = randint(366,777) , message='пока')

for event in longpoll.listen():
    if event.type == VkEventType.USER_ONLINE:
        if get_eva_status(480878879) and not flag:
            flag = True
            vk.messages.send(user_id=480878879, random_id=randint(366, 777), message='Доброе утлооооо❤❤❤❤❤, Евочка\nЭто я, пишу чаще чем твой парень\n'
                                                                                     'Сегодня я очень добрый, и с каждым твоим сообщением я отправлю побольше сердечек, напиши несколько раз, поймёшь,'
                                                                                     'я пока пойду отдохну, а ты развлекайся\nС любовью, твой робот🤖💘')
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.user_id == 480878879:
            s += 1
            mes = '❤❤' * s
            vk.messages.send(user_id=480878879, random_id=randint(366, 777), message=mes)
