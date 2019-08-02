# -*- coding: utf-8 -*-
import config
import telebot
import datetime
import re

bot = telebot.TeleBot(config.token) # берем токен из конфигурации
user0 = config.admin_user #берем список администраторов которым все разрешено
# noinspection PyBroadException
try:
	@bot.message_handler(content_types=['document', 'audio', 'video', 'sticker', 'location', 'contact', 'caption', 'venue', 'photo', 'left_chat_member', 'new_chat_members'])
	def delete_links(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' +str(message.from_user.id) + ' del content_types=[document, audio, video, sticker, location, contact, caption, venue, photo, left_chat_member, new_chat_members] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)

	@bot.message_handler(func=lambda message: message.entities is not None )
	def delete_links(message):
		if (str(message.from_user.id) not in user0):
			if (message.json is not None):
				f = open('log.txt', 'a')
				f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del url, json, text_link, email, code, bot_command ' + '\n')
				f.close()
				bot.delete_message(message.chat.id, message.message_id)
			else:
				for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
				# url - обычная ссылка, text_link - ссылка, скрытая под текстом
				# code -код, bot_command - команды боту
					if entity.type in ["url", "text_link", "email", "code", "bot_command"]:
						bot.delete_message(message.chat.id, message.message_id)
					else:
						return
	@bot.message_handler(content_types=["text"])
	def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
		if (str(message.from_user.id) not in user0):
			if (message.json is not None):
				text_json = str(message.json)
				if re.search(r'inline_keyboard', text_json):
					f = open('log.txt', 'a')
					f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del json, del message with buttons' + '\n')
					f.close()
					bot.delete_message(message.chat.id, message.message_id)
		if (str(message.from_user.id) not in user0):
			if re.search(r'\bзаработку\b', message.text):
				f = open('log.txt', 'a')
				f.write(str(datetime.datetime.now()) + ' user id:' + str(
					message.from_user.id) + ' del text: ' + message.text + '\n')
				f.close()
				bot.delete_message(message.chat.id, message.message_id)
			if re.search(r'\bпервым\b', message.text):
				f = open('log.txt', 'a')
				f.write(str(datetime.datetime.now()) + ' user id:' + str(
					message.from_user.id) + ' del text: ' + message.text + '\n')
				f.close()
				bot.delete_message(message.chat.id, message.message_id)
			if re.search(r'\bkick\b', message.text):
				f = open('log.txt', 'a')
				f.write(str(datetime.datetime.now()) + ' user id:' + str(
					message.from_user.id) + ' del text: ' + message.text + '\n')
				f.close()
				bot.delete_message(message.chat.id, message.message_id)
			if re.search(r'\bзаработок\b', message.text):
				f = open('log.txt', 'a')
				f.write(str(datetime.datetime.now()) + ' user id:' + str(
					message.from_user.id) + ' del text: ' + message.text + '\n')
				f.close()
				bot.delete_message(message.chat.id, message.message_id)
	if __name__ == '__main__':
		bot.polling(none_stop=True)
except:
	f = open('log.txt', 'a')
	f.write(str(datetime.datetime.now()) + ' Error bot' + '\n')
	f.close()
finally:
	if __name__ == '__main__':
		bot.polling(none_stop=True)
