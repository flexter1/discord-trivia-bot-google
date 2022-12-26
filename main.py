import requests
from bs4 import BeautifulSoup
import lxml
from loguru import logger
from googletrans import Translator
import json

with open('config.json','r') as file:
    json_file = json.load(file)
    DISCORD_TOKEN = json_file['discord_token']
    CHAT_ID = json_file['chat_id']
    AUTHOR_NAME = json_file['author_name']
    LAST_AUTHOR_MESSAGE = json_file['last_author_message']

def get_answer(question):
    cookies = {
        'SEARCH_SAMESITE': 'CgQI9ZYB',
        'SID': 'Rgiymzph0gLL72BUn-QN3wIVXiXVpMlPnIPLv73zeZfNcvYvXtrUOLJEgtRX4YyEretV6w.',
        '__Secure-1PSID': 'Rgiymzph0gLL72BUn-QN3wIVXiXVpMlPnIPLv73zeZfNcvYvCblA8lMXfhVLtHROO-cf3g.',
        '__Secure-3PSID': 'Rgiymzph0gLL72BUn-QN3wIVXiXVpMlPnIPLv73zeZfNcvYvJFxOSeowdWwpJnOmN_2yMA.',
        'HSID': 'AMZQbShuBUtix2ikq',
        'SSID': 'ANnX8coFmL8Q2Q8zH',
        'APISID': 'sDqHO6aNQpXsl_5T/Ah1woEootQiBYoa0s',
        'SAPISID': 'kNnEroZcSRPaC074/AmraYZmzSFWBOgGFD',
        '__Secure-1PAPISID': 'kNnEroZcSRPaC074/AmraYZmzSFWBOgGFD',
        '__Secure-3PAPISID': 'kNnEroZcSRPaC074/AmraYZmzSFWBOgGFD',
        '__Secure-ENID': '9.SE=NzPPRmmwH16K9a86hOVwlvOYU7MQRAxuPeZvAJKuRhgxZVvfYOjIILmK8PsUBBPKfgyCRAdLdY9nXQcSYo-iO6Od_3199Ti5-4i0_cCDvX_BH5tkJXA2cRrQjR1ifsRE_Zw4I3UGslw8RBk791OcP78kUb7D1JR_WVySbu_Oz-2mOztF-Y4FZPP8P8r6oorhG47OLyFvohROe4NyRleTAKeIyZhx39lW2nAxgtbW4zS3RKo',
        'OTZ': '6820572_32_32__32_',
        'AEC': 'AakniGMv626Ctf2f1xW08gJP4vRUhfvjOwVVcspvPGrF-hEKaeD3qcjQdA',
        'NID': '511=X_4vX2IiYxSQXkhL66YfWMnLZwcuj55mEIUREyQUD9nxUpFlVyF4bS1hNR6G1cut7ydEbmxQgMuNBe8tO1BM-IgMIap-2SS6JnZPaZnR0ckFvzGuJGcr5q2A5fmV3cLqvMNulW5rH8Bm15TWA1b6Nkz_ALiqyyZlkRXqT1WKTvXtwQnYJ3eeTNsZzHbDI4kC-MHUeRjrdIfziJrbfhcktqkfwLdD9edZUfzl5MfDzMDJx9K-JB9HBx6SwgY8Zkydh1PfqgdKcM6acE8FZE4abDO3aRs-VuCBy-oHWcRPlgwloJDVZojfII4HtKIT1PqyJ13okmNkHUbXJqJMDtjBtgvN9Ug2Pc8c54ObjiiwgFk3-vVsRyxNmJjwRqY7PgEbH98CUQRU9N8IDKUxIVZf4OPHqwNOHUW1aHvJMWrLJw1-cVBkX1ynfF98emm9LVmqE3B9gWWRMmG1QVWQtaRkJMmPBn0C2rwac17psiVG1bjEXmSWTdwQsTmkqPC7JFHetXcQaLiKr069yGDEpAY',
        'DV': 'Yw5GdPo5b3lbsO9g7sjbrke68GM2U1jjuvLUHP2UhQAAAFDnUmPnDIwfmgAAAGC9VCFbQNaLUwAAAIQQ4-QFXGMHFQAAAA',
        '1P_JAR': '2022-12-21-06',
        'SIDCC': 'AIKkIs1l7IB6N5K6bgFSQ81mzHO-ojZoliJ8MSoFAhDovxSK97WmmZDgkPMJG8wikufE8A1zhNw',
        '__Secure-1PSIDCC': 'AIKkIs389P4zcURYP44t5UfljxFW2UmKrmHhfJfyi2uyiBDMTwzE-bW577LnCFwoLGgjpFcBj70',
        '__Secure-3PSIDCC': 'AIKkIs2EAPlC3w5x8CjhZTAPCLqTiBXOWFOf251hkzh5FvsXNVDvJPxH9Vj-NZxSM_FPNZglG5U',
    }

    headers = {
        'authority': 'www.google.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-full-version': '"96.0.4664.93"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '"5.4.0"',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-bitness': '"64"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-client-data': 'CK21yQEIl7bJAQimtskBCKmdygEIvpHLAQiWocsBCMuJzAEYq6nKAQ==',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = {
        'q': question,
        'oq': question,
        'aqs': 'chrome..69i57.2846j1j7',
        'sourceid': 'chrome',
        'ie': 'UTF-8',
    }


    html = requests.get('https://www.google.com/search', headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(html.text, 'lxml')


    translator = Translator()
    try:
        answer = translator.translate(soup.find('a', class_='FLP8od').text).text
    except AttributeError:
        try:
            answer = translator.translate(soup.find('div',class_='Z0LcW t2b5Cf CfV8xf').text).text
        except AttributeError:
            try:
                answer = translator.translate(soup.find('div', class_='wx62f PZPZlf x7XAkb').text).text
            except AttributeError:
                try:
                    answer = translator.translate(soup.find('div', {'class': 'LGOjhe'}).text).text
                except AttributeError:
                    try:
                        #calculator
                        answer = soup.find('div', class_='z7BZJb XSNERd').text.strip()
                    except Exception:
                        answer = False
                        logger.error('Couldn\'t find the answer for question... Sorry')
    return answer



def message_parser(CHAT_ID, AUTHOR_NAME,LAST_AUTHOR_MESSAGE):
    headers = {
        'authorization': DISCORD_TOKEN,
            }

    params = {
        'limit': '50',
    }

    response = requests.get(
        f'https://discord.com/api/v9/channels/{CHAT_ID}/messages',
        params=params,
        headers=headers,
    )
    for message in range(len(response.json())):
        author = response.json()[message]['author']['username']
        content = response.json()[message]['content']
        if author.find(AUTHOR_NAME)!=-1 and content.find(LAST_AUTHOR_MESSAGE)==-1:
            return content
        else:
            logger.info('There are no new messages from author...')
            return LAST_AUTHOR_MESSAGE

def send_answer(CHAT_ID, question):
    answer = get_answer(question)

    headers = {
        'authorization': DISCORD_TOKEN,
    }

    json_data = {
        'content': answer,
        'tts': False,
    }

    response = requests.post(
        f'https://discord.com/api/v9/channels/{CHAT_ID}/messages',
        headers=headers,
        json=json_data,)
    if response.status_code==200:
        logger.success(f'Successfully sent the answer\nQuestion: {question}\nAnswer: {answer}')


def main(CHAT_ID, AUTHOR_NAME, LAST_AUTHOR_MESSAGE):
    while True:
        content = message_parser(CHAT_ID, AUTHOR_NAME, LAST_AUTHOR_MESSAGE)
        if content.find(LAST_AUTHOR_MESSAGE)==-1:


            send_answer(CHAT_ID, content)
            LAST_AUTHOR_MESSAGE = content


if __name__ == '__main__':
    main(CHAT_ID=CHAT_ID, AUTHOR_NAME=AUTHOR_NAME, LAST_AUTHOR_MESSAGE=LAST_AUTHOR_MESSAGE)
