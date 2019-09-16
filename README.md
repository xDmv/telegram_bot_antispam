<h2><b>Bot Telegram antispam<b></h2>
<br> Author: Makushin Dmitriy
<br> Author-email: avtospam2@gmail.com
<br> License: MIT
<br>
<br>Instrution (En):
<br>Bot written in Python 3.5
<br>Use librery pyTelegramBotAPI
https://github.com/eternnoir/pyTelegramBotAPI

<br># install librery:
<br>$ pip3 install pytelegrambotapi

<br># run the bot from the directory with the command:
<br>$ python3 bot.py

<br># When adding a bot to a group, you need to make it an "administrator" and allow it to send and edit messages.

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

<br># устанавливаем библиотеку для phyton:
<br>$ pip3 install pytelegrambotapi

<br># запуск бота из папки командой:
<br>$ python3 bot.py

<br># при добавлении бота в группу необходимо сделать его "администратором" и разрешить ему отпровлять и редактировать сообщения.

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

Relice 1.0.1
- add function delete message with bottons and  message with json

Relice 1.0.2
- up all function
- add function delete message with all bottons type 

Relice 1.0.3
- add new function for message.entities