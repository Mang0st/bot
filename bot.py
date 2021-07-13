import telebot
import conf
import sqlite3
bot = telebot.TeleBot(conf.TOKEN)
conn = sqlite3.connect('bazabaza.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
  cursor.execute('INSERT INTO bazabaza (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
  conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
  keyboard = telebot.types.ReplyKeyboardMarkup(True)
  keyboard.row('Подписаться')
  keyboard.row('Отписаться')
  bot.send_message(message.chat.id, 'Добро пожаловать, хочешь подписаться на рассылку ?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'подписаться':
        bot.send_message(message.chat.id, 'Ты успешно подписан')

        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_surname = message.from_user.last_name
        username = message.from_user.username
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_surname, username=username)
    else:
        bot.send_message(message.chat.id, 'Пользуйся кнопками)')

bot.polling(none_stop=True)