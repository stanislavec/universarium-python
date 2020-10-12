"""
Скрипт запрашивает auth-информацию при исполнении.
Если такой информации нет / сложно подготовить, можно использовать это:
    API-токен бота telegram:: 1328371373:AAGN2Iejq2bDcA8yLOsS2cO1FZiu17_uTig
    Telegram Сhat_id: -446654820.
"""

import vk_api
import telebot

MAX_STRING_LENGTH = 140
SUCCESS_VK_POST = 'Запрос ВК отправлен успешно, код записи: '
COMMON_VK_ERROR = 'Запрос ВК завершился с ошибкой'
SUCCESS_TLG_POST = 'Сообщение в телеграмм-чат отправлено успешно'
COMMON_TLG_ERROR = 'Отправка телеграмм-сообщения завершилась с ошибкой'
STRING_ERROR = 'Превышен максимальный размер сообщения'


def makeAPIRequests():
    # Запрашиваем сообщение пользователя
    message = input("Введите сообщение (не более " + str(MAX_STRING_LENGTH) +
                    " символов): ")

    # Проверяем количество символов в строке

    if len(message) > MAX_STRING_LENGTH:
        raise Exception(STRING_ERROR)

    # Принимаем логин/пароль пользователя ВК
    VKusername = input("Логин ВК: ")
    VKpassword = input("Пароль ВК: ")
    statusVK = None

    # Принимаем токен и чат-id для телеграмм
    TLGtoken = input("Введите API-токен бота telegram: ")
    TLGChatId = input("Введите chat_id, куда направить сообщение: ")
    statusTLG = None

    try:
        # Публикация записи на стену ВК
        vk_session = vk_api.VkApi(VKusername, VKpassword)
        vk_session.auth()
        vk = vk_session.get_api()
        statusVK = vk.wall.post(message=message)

        # Публикация записи в чат телеграмм
        TLGbot = telebot.TeleBot(TLGtoken)
        statusTLG = TLGbot.send_message(TLGChatId, message)

    except Exception as error:
        print('Возникла ошибка: ', error)
    finally:
        if statusVK and statusVK['post_id']:
            print(SUCCESS_VK_POST, statusVK['post_id'])
        else:
            print(COMMON_VK_ERROR)

        if statusTLG:
            print(SUCCESS_TLG_POST)
        else:
            print(COMMON_TLG_ERROR)


makeAPIRequests()
