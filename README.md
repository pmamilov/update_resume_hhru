# update_resume_hhru
Скрипт автоматически поднимает резюме на hh.ru и уведомляет об этом в ваш телеграм.  
***
## Использование
#### Клонируйте репозиторий и перейдите в него:
    cd update_resume_hhru
#### Создайте виртуальное окружение, активируйте его и установите зависимости:
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
#### Создайте файл *.env* и добавьте в него свои значения:
    ACCESS_TOKEN = Ваш токен, для доступа к API hh.ru
    REFRESH_TOKEN = Токен для обновления access токена
    RESUME_ID0 = ID вашего резюме (из адресной строки страницы с резюме)
    TELEGRAM_TOKEN = Токен вашего телеграм-бота
    CHAT_ID = ID вашего телеграм аккаунта
    
Если у вас несколько резюме, то добавляйте данные с переменными RESUME_ID1, RESUME_ID2, RESUME_ID3 и т.д.
Как получить токен для API можно почитать [здесь](https://github.com/hhru/api/blob/master/docs/authorization_for_user.md).  
***
#### Теперь нужно запускать скрипт каждые 4 часа, для этого добавьте таск в cron:  
Открываем cron на редактирование:

    crontab -e
И добавляем в конец строку:

    0 */4 * * * update_resume_hhru/venv/bin/python update_resume_hhru/hhru.py
    
    или только в рабочие часы
    
    0 9,13,17 * * * update_resume_hhru/venv/bin/python update_resume_hhru/hhru.py

Готово!

Access token действителен 2 недели и обновить его раньше нельзя.  
По истечении этого срока и получения ошибки, access token будет автоматически  
обновлён с помощью refresh token, и скрипт продолжит работу.  
Так же будет обновлён и refresh token, т.к. его можно использовать только один раз.  
О всех событиях придёт сообщение в телеграм.
