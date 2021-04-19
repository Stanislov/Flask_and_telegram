from aiogram.types import ReplyKeyboardMarkup, \
                        KeyboardButton

# Одна кнопка
btnHello = KeyboardButton("Привет 👋")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnHello)

# Много кнопок
button1 = KeyboardButton("🔔")
button2 = KeyboardButton("2")
button3 = KeyboardButton("3")

markup1 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)
markup2 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3)
markup3 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3) \
                                                .add(KeyboardButton("Средняя кнопка! 👋"))

greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(markup3)

markup3.row(KeyboardButton("4"), KeyboardButton("5"))
markup3.insert(KeyboardButton("6"))
markup3.add(KeyboardButton("Новая строка"))

# Кнопки отправки контакта и геолокации
markup_requests = ReplyKeyboardMarkup(resize_keyboard=True) \
  .add(KeyboardButton('Отправить свой контакт', request_contact=True)).add(KeyboardButton('Отправить свою геолокацию', request_location=True))