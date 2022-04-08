import os
import requests
import telebot
from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
all_resumes = []
resid = 'RESUME_ID'
get_num = 0
upd_url = []
response_n = []
error_code = []
error_value = []
mes_sbor_er = []

while os.getenv(resid + str(get_num)):
    all_resumes.append(os.getenv(resid + str(get_num)))
    upd_url.append(f'https://api.hh.ru/resumes/{all_resumes[get_num]}/publish/')
    get_num += 1

headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
body = {'grant_type': 'refresh_token', 'refresh_token': REFRESH_TOKEN}
refresh_url = f'https://hh.ru/oauth/token/'
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)


def update_resume():
    for i in range(get_num):
        response_n.append(requests.post(upd_url[i], headers=headers))

        if response_n[i].status_code == 204:
            mes_sbor = (f'Резюме успешно обновлено! {get_num} резюме.')
        else:
            error_code.append(response_n[i].status_code)
            error_value.append(response_n[i].json()['errors'][0]['value'])
            mes_sbor_er.append(f'Ошибка {error_code[i]}: {error_value[i]}\n')
            mes_sbor = mes_sbor_er
            #send_message(f'Ошибка {error_code[i]}: {error_value[i]}')
            if error_value[i] == 'token_expired':
                send_message(''.join('Отправлен запрос на обновление токена'))
                refresh_token()
                mes_sbor = ''
                break
    if mes_sbor != ''
        send_message(''.join(mes_sbor))


def refresh_token():
    response = requests.post(refresh_url, headers=headers, data=body)
    if response.status_code == 200:
        new_access_token = response.json()['access_token']
        new_refresh_token = response.json()['refresh_token']
        write_to_env(new_access_token, new_refresh_token)
        return send_message('Токен успешно обновлён!')
    error_code = response.status_code
    error = response.json()['error']
    error_description = response.json()['error_description']
    return send_message(f'Ошибка {error_code}. {error}: {error_description}')


def write_to_env(at, rt):
    set_key(dotenv_file, 'ACCESS_TOKEN', at)
    set_key(dotenv_file, 'REFRESH_TOKEN', rt)


if __name__ == '__main__':
    update_resume()
