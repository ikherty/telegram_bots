import settings
import telebot
from telebot.types import Message
bot = telebot.TeleBot(settings.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, а ты подписан на хозяйку?) https://www.youtube.com/c/PropWashService")

@bot.message_handler(commands=['help'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton('Сообщение разработчику', url='telegram.me/ValentinaPetrenko')
   )
   bot.send_message(
       message.chat.id,
       'Список команд - /help.\n' +
       'Привет,\n' +
       'Вас приветствует бот Косяк (@kosyk_bot).\n'+
       'На данном этапе могу только быть повторюшей (/repeat)',
       reply_markup=keyboard
   )

@bot.message_handler(commands=['repeat'], func=lambda message: True)
def upper(message: Message):
	bot.reply_to(message, message.text.upper())

bot.polling()
