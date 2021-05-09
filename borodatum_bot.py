import telebot;
bot = telebot.TeleBot('1877632005:AAHbI0iNt0GgH1W0YYraa-6D_v2yoRuzg78');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    def start(message):
        if message.text == '/мурк':
            bot.send_message(message.from_user.id, "Тест: Кокая вы принцесса");
            bot.send_message(message.from_user.id, 'Выбирите што вом большы нровится:')
            bot.send_message(message.from_user.id, 'Если нровится поховоть нопишыти "поховоть"')
            bot.send_message(message.from_user.id, 'Если нровится поспоть нопишыти "поспоть"')
            bot.send_message(message.from_user.id, 'Если нровится посяпоться нопишыти "посяпоться"')
            bot.send_message(message.from_user.id, 'Если нровится жоп ухвотить нопишыть "ухвотить"')
        else:
            bot.send_message(message.from_user.id, 'Нопишыти /мурк');

bot.polling(none_stop=True, interval=0)
