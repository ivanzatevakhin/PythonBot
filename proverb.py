import random
from bs4 import BeautifulSoup
import requests
import csv


def proverb():  # Возвращает случайную строку из proverb.txt
    with open('proverb.txt', 'r', encoding='UTF-8') as f:
        d = f.read().split('\n')
        one_prover = random.choice(d)
    return one_prover


def wordsss():
    wrds = '/wether '
    w = wrds.split()
    slovo = w[1]
    sl = slovo[0].upper()
    sdd = sl[0] + slovo[1::]

    print(sdd)


wordsss()


def wether(city):  # Возвращает прогноз погоды
    url = city_geo(city)
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")  # Парсить полученную страницу
    temperatura = bs.find('div', 'temp fact__temp fact__temp_size_s')  # Ищет класс затем значение
    temp2 = bs.find('div', 'link__feelings fact__feelings')
    oblachnost = temp2.find('div', 'link__condition day-anchor i-bem')
    pogoda = 'На вашей местности температура равна ' + temperatura.text + '.' + ' ' + oblachnost.text
    return pogoda


def city_geo(city):     # Географические координаты по названию города и возвращает ссылку
    with open('city.csv', encoding='UTF=8') as f:       # Читаем ксв файл
        reader = csv.DictReader(f)
        for row in reader:
            if row['city'] == city:
                return "https://yandex.com.am/weather/?lat=" + row['geo_lat'] + "&lon=" + row['geo_lon']
