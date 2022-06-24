from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '5090431490:AAHx73qxmnQacQC_5ovF23AyDcSgu8riaeM'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "👋Assalomu alaykum, Xush kelibsiz! \nBiror bir matn kriting:")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Bu bot 📝matnlarni kirildan♻️lotinga va lotindan♻️kirilga o'tkazishingiz uchun yordam beradi✅ \n📜Botdan foydalanish uchun 📝matningizni yuboring❗️")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg= message.text
    # qisqaroq varyanti
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()



# Bu ma'lumotlar ham ishlaydi faqat uzun bolganligi uchun biz qisqaroq korinishidan foydalandik

 # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
	

# matn = input('Matn kiriting:')

# if matn.isascii():
#     print(to_cyrillic(matn))

# else:
#     print(to_latin(matn))