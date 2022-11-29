from selene.support.shared import browser
from selene import by, be, have
import time

"""Самый полезный автотест в мире!"""

def test_mes_user():
    # Открываю браузер и ищу пользователя
    browser.open('http://test.qahunter.ru/')
    browser.element(by.name("search_query")).type('Arsenii').press_enter()
    # Кликаю на карточку пользователя"""
    browser.element('/html/body/main/section[2]/div/div/div/div/a').click()
    # В окне резюме кликаю кнопку 'написать сообщение'
    browser.element('/html/body/main/div/div/div[1]/div/div/a').click()
    # Пишу сообщение пользователю
    browser.element(by.name('subject')).type('йоу')
    browser.element(by.name('body')).type('Я дарю тебе пиццу, бро!')
    browser.element('/html/body/main/div/div/form/input[2]').click()
    # Выполняю вход на пользователя, кому отправили сообщение
    browser.element("/html/body/header/div/nav/ul/li[4]/a").click()
    browser.element(by.name('username')).type("arsen")
    browser.element(by.name('password')).type("456tt456yy")
    browser.element(".btn--lg").click()
    # Открываю влкадку сообщения
    browser.element("/html/body/header/div/nav/ul/li[4]/a").click()
    # Проверка на доставку сообщения
    subject = "йоу"
    # Я устал! Переробовал кучу вариантов, уже слишком поздно, подскажите плиз :)
    if browser.element('.message__subject') == subject:
        print('Все ок, попей воды!')
    else:
        print('Нуб ты, а не тестер! ахах')
    time.sleep(4)