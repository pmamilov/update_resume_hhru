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
headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

all_resumes = []
resid = 'RESUME_ID'
get_num = 0
upd_url = []
response_n = []
error_code = []
error_value = []

while os.getenv(resid + str(get_num)):
    all_resumes.append(os.getenv(resid + str(get_num)))
    upd_url.append(f'https://api.hh.ru/resumes/{all_resumes[get_num]}/publish/')
    get_num += 1

#print(upd_url)

def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)

for i in range(get_num):
    response_n.append(requests.post(upd_url[i], headers=headers))

    if response_n[i].status_code == 204:
        send_message('Резюме успешно обновлено!')
    else:
        error_code.append(response_n[i].status_code)
        error_value.append(response_n[i].json()['errors'][0]['value'])
        send_message(f'Ошибка {error_code[i]}: {error_value[i]}')







# if __name__ == '__main__':
#     update_resume()
