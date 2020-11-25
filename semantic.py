import re

import requests

MODEL = 'ruscorpora_upos_cbow_300_20_2019'
FORMAT = 'csv'
WORD = 'шаурма'
print('Заданное слово', WORD)


def api_neighbor(m, w, f):
    neighbors = {}
    url = '/'.join(['http://rusvectores.org', m, w, 'api', f]) + '/'
    r = requests.get(url=url, stream=True)
    for line in r.text.split('\n'):
        try:  # первые две строки в файле -- служебные, их мы пропустим
            word, sim = re.split(r'\s+', line)  # разбиваем строку по одному или более пробелам
            neighbors[word] = sim
        except:
            continue
    return neighbors


def get_related_words(word):
    words_clear = re.findall(r'\w+', word)[0]
    print(type(words_clear))
    words = list(api_neighbor(MODEL, word, FORMAT).keys())
    for item in words:
        words_clear += ' ' + (re.sub(r'_\w+', '', item))
    return words_clear


print('Близкие слова:', get_related_words(WORD))
