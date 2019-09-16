# -*- coding: utf-8 -*-
import config
import telebot
import datetime
# import re
# from telebot import types

bot = telebot.TeleBot(config.token) # берем токен из конфигурации
user0 = config.admin_user #берем список администраторов которым все разрешено


try:
	@bot.message_handler(content_types=['document'])
	def delete_links_document(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[document] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['audio'])
	def delete_links_audio(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[audio] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['video'])
	def delete_links_video(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' +str(message.from_user.id) + ' del message content_types=[video] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['sticker'])
	def delete_links_sticker(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message  content_types=[sticker] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['location'])
	def delete_links_location(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' +str(message.from_user.id) + ' del message content_types=[location] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['contact'])
	def delete_links_contact(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[contact] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['caption'])
	def delete_links_caption(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[caption] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['venue'])
	def delete_links_venue(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[venue] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['photo'])
	def delete_links_photo(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[photo] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['left_chat_member'])
	def delete_links_left_chat_member(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[left_chat_member] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)
	@bot.message_handler(content_types=['new_chat_members'])
	def delete_links_new_chat_members(message):
		if (str(message.from_user.id) not in user0):
			f = open('log.txt', 'a')
			f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message content_types=[new_chat_members] ' + '\n')
			f.close()
			bot.delete_message(message.chat.id, message.message_id)

	@bot.message_handler(func=lambda message: message.entities is not None )
	def delete_links(message):
		if (str(message.from_user.id) not in user0):
			j = 0
			for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
				j = j + 1
				if (j == 1):
					if (entity.type in ["url"]):
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'url'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if (entity.type in ["text_link"]):
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'text_link'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if (entity.type in ["pre"]):
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'pre'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if entity.type in ["hashtag"]:
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'hashtag'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if entity.type in ["email"]:
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'email'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if entity.type in ["code"]:
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'code'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if entity.type in ["bot_command"]:
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'bot_command'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if entity.type in ["bold"]:
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'bold'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if entity.type in ["mention"]:
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'mention'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
					if (entity.type in ["italic"]):
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message type == 'italic'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)

	@bot.message_handler(content_types=["text"])
	def repeat_all_messages(message):
		if (str(message.from_user.id) not in user0):
			if message.forward_from_chat :
				f = open('log.txt', 'a')
				f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + ' del message with buttons ' + '\n')
				f.close()
				bot.delete_message(message.chat.id, message.message_id)
			else:
				for e in message.json:
					if e in 'reply_markup':
						f = open('log.txt', 'a')
						f.write(str(datetime.datetime.now()) + ' user id:' + str(message.from_user.id) + " del message json, del message 'reply_markup'" + '\n')
						f.close()
						bot.delete_message(message.chat.id, message.message_id)
	if __name__ == '__main__':
		bot.polling(none_stop=True)
except Exception as e:
	f = open('log.txt', 'a')
	f.write(str(datetime.datetime.now()) + ' Error bot:' + e + '| Error bot argument: ' + e.args +'\n')
	f.close()
finally:
	if __name__ == '__main__':
		bot.polling(none_stop=True)
