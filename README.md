Bot Telegram antispam

<br> Author: Makushen Dmitriy
<br> Author-email: avtospam2@gmail.com
<br> License: MIT
<br>
<br>Instrution (En):
<br>Bot written in Python 3.5
<br>Use librery pyTelegramBotAPI
https://github.com/eternnoir/pyTelegramBotAPI

<br># install librery:
$ pip3 install pytelegrambotapi

<br># run the bot from the directory with the command:
$ python3 bot.py

Capability my bot:
    <br>Delete all message that have:
    <br>- url;
    <br>- email;
    <br>- code lang;
    <br>- system message add or del user in group;
    <br>- command bot;
    <br>- add video or audio file;
    <br>- stiker;
    <br>- venue message;
    <br>- picture or photo file.
    <br>Bot actions apply to all but the list of users who are allowed.
    <br>The list of users who are allowed to do everything is specified in the config.py file in the admin_user array.
    

<br># Инструкция (Ru):
<br>Бот написан на Python 3.5
<br>использовал библиотеку: pyTelegramBotAPI
https://github.com/eternnoir/pyTelegramBotAPI

# устанавливаем библиотеку для phyton:
$ pip3 install pytelegrambotapi

# запуск бота из католога командой:
$ python3 bot.py

Возможности бота:
<br>Удаляет все сообщения в которых есть:
<br>- ссылки в любом виде;
<br>- емайл;
<br>- код (но туту есть нюансы не все режит);
<br>- контакт другого пользователя;
<br>- системное сообщение об вступлении или удалении пользователя в группу;
<br>- команды для бота;
<br>- прикрепленое видео или аудио файл;
<br>- параметры локации;
<br>- стикер (смайлы пропускает);
<br>- голосовое сообщение;
<br>- картинка в любом виде (прикреплена как файл или фото без разницы).
<br>Действия бота распространяются на всех кроме списка пользователей которым это разрешено.
<br>Список пользоватлей, которым разрешается все делать указывается в файле config.py в массиве admin_user.

<br>Если хотите его разместить на свой сервер то ознакомтесь с этой статьей:
https://groosha.gitbooks.io/telegram-bot-lessons/content/ini_and_pyz.html