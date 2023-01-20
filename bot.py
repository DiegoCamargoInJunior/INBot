import telebot
from random import randint

CHAVE_API = '5908875346:AAGeVy54Tdycvt7Rn9ljx46U5dnpKiiFiIs'

bot = telebot.TeleBot(CHAVE_API)

def uivo():
  uivo = 'A'
  for n in range(randint(0, 3)):
    uivo = f'{uivo}a'
  for n in range(randint(0, 6)):
    uivo = f'{uivo}u'
  for n in range(randint(0, 3)):
    uivo = f'{uivo}!'
  return uivo

@bot.message_handler(commands=["oque_um_lobo_faz?"])
def responder(mensagem):
  bot.reply_to(mensagem, "A gente uiva")
  for n in range(randint(1, 4)):
    bot.reply_to(mensagem, uivo())
    print(mensagem.chat.id)
  bot.send_sticker(chat_id=mensagem.chat.id, sticker='CAACAgEAAxkBAAN5Y8ohJQ-uLKuvjOSXg-jLXA6lOgUAAn4EAAITIFFGyA5aKc3Au7wtBA')


bot.polling()