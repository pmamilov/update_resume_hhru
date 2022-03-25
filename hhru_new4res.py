import os
import requests
import telebot
from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
RESUME_ID1 = os.getenv('RESUME_ID1')
RESUME_ID2 = os.getenv('RESUME_ID2')
RESUME_ID3 = os.getenv('RESUME_ID3')
RESUME_ID4 = os.getenv('RESUME_ID4')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
body = {'grant_type': 'refresh_token', 'refresh_token': REFRESH_TOKEN}
update_url1 = f'https://api.hh.ru/resumes/{RESUME_ID1}/publish/'
update_url2 = f'https://api.hh.ru/resumes/{RESUME_ID2}/publish/'
update_url3 = f'https://api.hh.ru/resumes/{RESUME_ID3}/publish/'
update_url4 = f'https://api.hh.ru/resumes/{RESUME_ID4}/publish/'
refresh_url = f'https://hh.ru/oauth/token/'
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)


def update_resume():
    response1 = requests.post(update_url1, headers=headers)
    response2 = requests.post(update_url2, headers=headers)
    response3 = requests.post(update_url3, headers=headers)
    response4 = requests.post(update_url4, headers=headers)
    if response1.status_code == 204 and response2.status_code == 204 and response3.status_code == 204 and response4.status_code == 204:
        return send_message('Резюме успешно обновлено!')
    error_code1 = response1.status_code
    error_code2 = response2.status_code
    error_code3 = response3.status_code
    error_code4 = response4.status_code
    error_value1 = response1.json()['errors'][0]['value']
    error_value2 = response2.json()['errors'][0]['value']
    error_value3 = response3.json()['errors'][0]['value']
    error_value4 = response4.json()['errors'][0]['value']
    send_message(f'Ошибка {error_code1}: {error_value1}')
    send_message(f'Ошибка {error_code2}: {error_value2}')
    send_message(f'Ошибка {error_code3}: {error_value3}')
    send_message(f'Ошибка {error_code4}: {error_value4}')
    if error_value1 == 'token_expired':
        refresh_token()


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
