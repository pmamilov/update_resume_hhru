import os
import requests
import telebot
from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')

ALL_RESUMES = []
resid = 'RESUME_ID'
get_num = 1


while os.getenv(resid + str(get_num)):
    ALL_RESUMES.append(os.getenv(resid + str(get_num)))
    get_num += 1

#print(ALL_RESUMES)

upd_url = []
ir = 0

while os.getenv(resid + str(get_num)):
    ALL_RESUMES.append(os.getenv(resid + str(get_num)))
    get_num += 1

for get_num in ALL_RESUMES:
    upd_url.append(f'https://api.hh.ru/resumes/{ALL_RESUMES[ir]}/publish/')
    ir += 1

print(upd_url)


response1 = requests.post(update_url1, headers=headers)
response2 = requests.post(update_url2, headers=headers)
response3 = requests.post(update_url3, headers=headers)
response4 = requests.post(update_url4, headers=headers)






# if __name__ == '__main__':
#     update_resume()
