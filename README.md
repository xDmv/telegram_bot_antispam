Bot Telegram antispam

\n Author: Makushen Dmitriy
\n Author-email: avtospam2@gmail.com
\n License: MIT

Instrution (En):
Bot written in Python 3.5
Use librery pyTelegramBotAPI
https://github.com/eternnoir/pyTelegramBotAPI

#install librery:
$ pip3 install pytelegrambotapi

# run the bot from the directory with the command:
$ python3 bot.py

Capability my bot:
    Delete all message that have:
    - url;
    - email;
    - code lang;
    - system message add or del user in group;
    - command bot;
    - add video or audio file;
    - stiker;
    - venue message;
    - picture or photo file.
    Bot actions apply to all but the list of users who are allowed.
    The list of users who are allowed to do everything is specified in the config.py file in the admin_user array.
    

Инструкция (Ru):
Бот написан на Python 3.5
использовал библиотеку: pyTelegramBotAPI
https://github.com/eternnoir/pyTelegramBotAPI

# устанавливаем библиотеку для phyton:
$ pip3 install pytelegrambotapi

# запуск бота из католога командой:
$ python3 bot.py

Возможности бота:
    Удаляет все сообщения в которых есть:
    - ссылки в любом виде;
    - емайл;
    - код (но туту есть нюансы не все режит);
    - контакт другого пользователя;
    - системное сообщение об вступлении или удалении пользователя в группу;
    - команды для бота;
    - прикрепленое видео или аудио файл;
    - параметры локации;
    - стикер (смайлы пропускает);
    - голосовое сообщение;
    - картинка в любом виде (прикреплена как файл или фото без разницы).
    Действия бота распространяются на всех кроме списка пользователей которым это разрешено.
    Список пользоватлей, которым разрешается все делать указывается в файле config.py в массиве admin_user.


Если хотите его разместить на свой сервер то ознакомтесь с этой статьей:
https://groosha.gitbooks.io/telegram-bot-lessons/content/ini_and_pyz.html