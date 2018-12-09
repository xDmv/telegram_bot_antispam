# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token) # берем токен из конфигурации
user0 = config.admin_user #берем список администраторов которым все разрешено

@bot.message_handler(content_types=['document', 'audio', 'video', 'sticker', 'location', 'contact', 'caption', 'venue', 'photo', 'left_chat_member'])
def delete_links(message):
	if (str(message.from_user.id) not in user0):
		if (str(message.from_user.id) not in user0):
			bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: message.entities is not None )
def delete_links(message):
	if (str(message.from_user.id) not in user0):
		for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
		# url - обычная ссылка, text_link - ссылка, скрытая под текстом
		# code -код, bot_command - команды боту
			if entity.type in ["url", "text_link", "email", "code", "bot_command"]:
				bot.delete_message(message.chat.id, message.message_id)
			else:
				return

@bot.message_handler(content_types=['new_chat_members'])
def dell_system_message(message):
	if (str(message.from_user.id) not in user0):
		if (str(message.from_user.id) not in user0):
			bot.delete_message(message.chat.id, message.message_id)

if __name__ == '__main__':
	bot.polling(none_stop=True)
