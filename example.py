import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(src_file, dst_file,  from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(src_file, encoding='utf-8') as f:
        src_text = f.read()


    params = {
        'key': API_KEY,
        'text': src_text,
        'lang': f'{from_lang}-{to_lang}'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    trans_text = ''.join(json_['text'])

    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(trans_text)

    return trans_text


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    print(translate_it(src_file='ES.txt', dst_file='ES_tr.txt', from_lang='es'))
    print("*" * 10)
    print(translate_it(src_file='DE.txt', dst_file='DE_tr.txt', from_lang='de'))
    print("*" * 10)
    print(translate_it(src_file='FR.txt', dst_file='FR_tr.txt', from_lang='fr'))


# *Задача №2
# Нет возможности выполнить задание, т.к. не использую аккаунт Яндекс