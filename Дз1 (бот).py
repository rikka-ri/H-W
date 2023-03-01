#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytelegrambotapi


# In[2]:


import telebot


# In[3]:


from telebot import types


# In[4]:


bot = telebot.TeleBot("6263141789:AAGixUCsZfaIT2CXQfqZ6UOJn9X5hxBtZXQ")


# In[5]:


@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, "Привет, любимый! Мы часто не знаем, что хотим поесть в тот или иной промежуток дня. Я решила упростить эту задачу. Давай посмотрим, как это работает :)", 
       reply_markup=keyboard())


# In[6]:


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    bt1 = types.KeyboardButton("Давай!✌")
    markup.add(bt1)
    return markup


# In[7]:


text1 = "Тогда осталось купить мне цветы и через час все будет готово!:)"
text2 = "Тогда попробуй еще раз, пожалуйста."
text3 = "Отлично! Точно это блюдо на завтрак?"
text4 = "Класс! Точно это блюдо на обед?"
text5 = "Шикарно! Точно это блюдо на ужин?"


# In[8]:


@bot.message_handler(content_types=["text"])
def send_anytext(message):
    chat_id = message.chat.id
    if message.text == "Давай!✌":
          bot.send_message(chat_id, "Выбери прием пищи - завтрак, обед или ужин. Я предложу два варианта. Если тебе понравится этот бот, то сделаю полноценное меню с большим количеством опций :)")
    elif message.text == "Завтрак":
        bot.send_message(message.chat.id, "Сладкий или сытный?")
    elif message.text == "Сладкий":
        bot.send_message(message.chat.id, "Супер! Я предлагаю тебе кашу с ягодами или панкейки с джемом. Что больше хочется?")
    elif message.text == "Каша с ягодами":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/porridge.jpg", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text3
        bot.send_message(message.chat.id, answer)  
    elif message.text == "Да":
        bot.send_message(message.chat.id, text1)
    elif message.text == "Нет":
        bot.send_message(message.chat.id, text2)
    elif message.text == "Панкейки с джемом":   
        photo = open("/Users/rikkari/Desktop/Новая папка 2/pancakes.jpg", "rb")  
        bot.send_animation(message.chat.id, photo)
        answer = text3
        bot.send_message(message.chat.id, answer)  
    elif message.text == "Сытный":
        bot.send_message(message.chat.id, "Я как раз тоже хотела сытный) Я предлагаю тебе английский завтрак или тосты")
    elif message.text == "Английский завтрак": 
        photo = open("/Users/rikkari/Desktop/Новая папка 2/engbreakfast.png", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text3
        bot.send_message(message.chat.id, answer) 
    elif message.text == "Тосты": 
        photo = open("/Users/rikkari/Desktop/Новая папка 2/toasts.png", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text3
        bot.send_message(message.chat.id, answer) 
            
    elif message.text == "Обед":
        bot.send_message(message.chat.id, "Суп или второе?")
    elif message.text == "Суп":
        bot.send_message(message.chat.id, "Супер! Я предлагаю тебе сырный суп или сливочный суп с брокколи. Что хотелось бы сейчас?")
    elif message.text == "Сливочный суп c брокколи":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/soup.JPG", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text4
        bot.send_message(message.chat.id, answer) 
    elif message.text == "Сырный суп":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/cheese_soup.JPG", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text4
        bot.send_message(message.chat.id, answer) 
    elif message.text == "Второе":
        bot.send_message(message.chat.id, "Супер! Я предлагаю тебе гречку с тефтелями или рис с котлетами. Что хотелось бы сейчас?")
    elif message.text == "Гречка с тефтелями":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/grechka.jpeg", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text4
        bot.send_message(message.chat.id, answer) 
    elif message.text == "Рис с котлетами":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/rice.jpeg", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text4
        bot.send_message(message.chat.id, answer) 
        
    elif message.text == "Ужин":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/plane.jpeg", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = "Ты бы хотел рыбу или мясо?"
        bot.send_message(message.chat.id, answer)
    elif message.text == "Рыба":
        bot.send_message(message.chat.id, "Супер! Я предлагаю тебе стейк или запеченую рыбу. Что больше хочется?")
    elif message.text == "Стейк":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/salmon.JPG", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text5
        bot.send_message(message.chat.id, answer) 
    elif message.text == "Запеченая рыба":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/baked_fish.JPG", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text5
        bot.send_message(message.chat.id, answer)   
    elif message.text == "Мясо":
        bot.send_message(message.chat.id, "Курица или говядина?")
    elif message.text == "Курица":
        bot.send_message(message.chat.id, "Супер! Я предлагаю тебе фарфалле в соусе или карри. Что больше хочется?")
    elif message.text == "Фарфалле в соусе":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/farfalle.JPG", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text5
        bot.send_message(message.chat.id, answer) 
    elif message.text == "Карри":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/curry.JPG", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text5
        bot.send_message(message.chat.id, answer)   
    elif message.text == "Говядина":
        bot.send_message(message.chat.id, "Супер! Я предлагаю тебе плов или спагетти болоньезе. Что больше хочется?")
    elif message.text == "Плов":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/pilaff.jpeg", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text5
        bot.send_message(message.chat.id, answer) 
    elif message.text == "Спагетти болоньезе":
        photo = open("/Users/rikkari/Desktop/Новая папка 2/bolognese.JPG", "rb")
        bot.send_animation(message.chat.id, photo)
        answer = text5
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, "Кажется, ты написал слово, которое я пока не знаю. Попробуй написать выражение полностью еще раз, используя именительный падеж.")


# In[ ]:


bot.polling(none_stop=True, interval=0)


# In[ ]:




