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

print(ALL_RESUMES)



while os.getenv(resid + str(get_num)):
    ALL_RESUMES.append(os.getenv(resid + str(get_num)))
    get_num += 1

update_url1 = f'https://api.hh.ru/resumes/{ALL_RESUMES[0]}/publish/'
update_url2 = f'https://api.hh.ru/resumes/{ALL_RESUMES[1]}/publish/'
update_url3 = f'https://api.hh.ru/resumes/{ALL_RESUMES[2]}/publish/'
update_url4 = f'https://api.hh.ru/resumes/{ALL_RESUMES[3]}/publish/'





# if __name__ == '__main__':
#     update_resume()
