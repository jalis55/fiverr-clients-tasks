import os
import requests, threading, random, time,re

from colorama import Fore
ran = 'qwertyuiopasdfghjklzxcvbnm'
ba = str("".join(random.choice(ran) for i in range(12)))
ra = str("".join(random.choice(ran) for x in range(16)))
device_id = f'{ba}_{ra}'
magenta_color = Fore.LIGHTMAGENTA_EX
reset_color = Fore.RESET
red_color = Fore.LIGHTRED_EX

def registry():
    colour = '\x1b[38;5;56m'
    global proxy_file, username, password, nospam, attempt, email, email_full, email_from_req, domaen_from_req, req_create_email, code, signupcode
    while 1:
        random_proxy = random.choice(proxy_file)
        url_registry = 'https://www.instagram.com/accounts/web_create_ajax/'
        headers_registry = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "ig_did=BDA3E81A-9AF8-4889-9314-28DEA159E082; datr=PRZmYMiyU_a6iPcjKORJVlw6; mid=YHmRqAAEAAGX_OgHP9VjcPwI2kqe; ig_nrcb=1; ds_user_id=47586819033; csrftoken=DVuQnN8UioZHjVj8lyB78CGdbBJAzA3h",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-csrftoken": "DVuQnN8UioZHjVj8lyB78CGdbBJAzA3h",
            "x-ig-app-id": "1217981644879628",
            "x-ig-www-claim": "0",
            "x-instagram-ajax": "fae627f53bc4",
            "x-requested-with": "XMLHttpRequest",
            "referrer": "https://www.instagram.com/accounts/signup/username",
            "referrerPolicy": "strict-origin-when-cross-origin",
        }
        data_registry = {
            'email': email_full,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
            'username': username,
            'first_name': 'by @7e0o',
            'month': '1',
            'day': '1',
            'year': '1990',
            'client_id': device_id,
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': signupcode}
        proxiee = {
            'http': f'http://{random_proxy}',
            'https': f'http://{random_proxy}'
        }
        try:
            req_registry = requests.post(url_registry, headers=headers_registry, data=data_registry,
                                         proxies=proxiee, timeout=3).text
            if ('email_is_taken') in req_registry:
                if nospam == 0:
                    nospam = 1
                    print(
                        f'\n{colour}New Account!{reset_color}\nE-mail{colour}:{reset_color}{email_full}\nUsername{colour}:{username}{reset_color}\nPassword{colour}:{password}{reset_color}')
                    with open('createdaccount.txt', 'a') as done:
                        done.write(
                            f'E-mail : {email_full}\nUsername : {username}\nPassword : {password}\nBy @7e0o tool!\n')
            else:
                if nospam == 0:
                    attempt += 1
                    print(f'\rRegister Attempts: {attempt}', end='')
        except:
            pass

def check_code():
    global proxy_file, username, password, nospam, attempt, email, email_full, email_from_req, domaen_from_req, req_create_email, code, signupcode
    url_check_code = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/'
    headers_check_code = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "ig_did=BDA3E81A-9AF8-4889-9314-28DEA159E082; datr=PRZmYMiyU_a6iPcjKORJVlw6; mid=YHmRqAAEAAGX_OgHP9VjcPwI2kqe; ig_nrcb=1; ds_user_id=47586819033; csrftoken=DVuQnN8UioZHjVj8lyB78CGdbBJAzA3h",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrftoken": "DVuQnN8UioZHjVj8lyB78CGdbBJAzA3h",
        "x-ig-app-id": "1217981644879628",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "fae627f53bc4",
        "x-requested-with": "XMLHttpRequest",
        "referrer": "https://www.instagram.com/accounts/signup/username",
        "referrerPolicy": "strict-origin-when-cross-origin",
    }
    data_check_code = {
        'code': code,
        'device_id': device_id,
        'email': req_create_email
    }
    req_check_code = requests.post(url_check_code, headers=headers_check_code, data=data_check_code)
    if '"status":"ok"' in req_check_code.text:
        signupcode = req_check_code.json()['signup_code']
        for _ in range(30):
            [].append(threading.Thread(target=registry).start())
        for _2 in []:
            _2.join()
        print(f'Your Username Will Be:{magenta_color} {username} {reset_color}')
    else:
        print(req_check_code.text)

def get_code():
    global proxy_file, username, password, nospam, attempt, email, email_full, email_from_req, domaen_from_req, req_create_email, code
    headers_get_code = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
        "cookie": f"PHPSESSID={req_create_email.cookies['PHPSESSID']}; tmail-emails=a%3A1%3A%7Bi%3A0%3Bs%3A17%3A%22{email_from_req}%40{domaen_from_req}%22%3B%7D",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "referrer": "https://besttemporaryemail.com/",
        "referrerPolicy": "strict-origin-when-cross-origin"}
    url_save_email = 'https://besttemporaryemail.com/actions.php?action=saveEMails'
    req_save_email = requests.get(url_save_email, headers=headers_get_code)
    numb_req = 0
    num_stop = 0
    while True:
        req_get_code = requests.get('https://besttemporaryemail.com/mail.php?unseen=1',
                                    headers=headers_get_code).text
        if req_get_code != '':
            try:
                subject = req_get_code.split('subject">')[1]
                code = subject.split(' is your Instagram code')[0]
                code.strip()
                color = '\u001b[36m'
                print(f'\nSYour Code is {color}: {reset_color}{code}{reset_color}')
                if num_stop == 0:
                    num_stop = 1
                check_code()
            except:
                pass
        else:
            if num_stop == 0:
                numb_req += 1
                print(f'\r[{numb_req}] Attempt(s)', end='')
                time.sleep(0.2)

def send_code_to_email():
    global proxy_file, username, password, nospam, attempt, email, email_full, email_from_req, domaen_from_req, req_create_email
    headers_send_code_to_email = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "ig_did=BDA3E81A-9AF8-4889-9314-28DEA159E082; datr=PRZmYMiyU_a6iPcjKORJVlw6; mid=YHmRqAAEAAGX_OgHP9VjcPwI2kqe; ig_nrcb=1; ds_user_id=47586819033; csrftoken=DVuQnN8UioZHjVj8lyB78CGdbBJAzA3h",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrftoken": "DVuQnN8UioZHjVj8lyB78CGdbBJAzA3h",
        "x-ig-app-id": "1217981644879628",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "fae627f53bc4",
        "x-requested-with": "XMLHttpRequest",
        "referrer": "https://www.instagram.com/accounts/signup/username",
        "referrerPolicy": "strict-origin-when-cross-origin",
    }
    url_send_code_to_email = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
    data_send_code_to_email = {
        'device_id': device_id,
        'email': email_full
    }
    req_send_code_to_email = requests.post(url_send_code_to_email, headers=headers_send_code_to_email,
                                           data=data_send_code_to_email).text
    if '"email_sent":true' in req_send_code_to_email:
        print(f'Sent Code To{red_color}: {reset_color}{email_full}')
        get_code()
    else:
        input(f'{req_send_code_to_email}\n{red_color}Press Enter To Exit {reset_color}')
        exit(0)

def create_email():
    global proxy_file, email, password, username, nospam, attempt, email_full, email_from_req, domaen_from_req, req_create_email
    headers_create_email = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "referrer": "https://besttemporaryemail.com/",
        "referrerPolicy": "strict-origin-when-cross-origin"}
    url_create_email = f'https://besttemporaryemail.com/user.php?user={email}%40goodbayjo.ml'
    req_create_email = requests.get(url_create_email, headers=headers_create_email)
    email_full = req_create_email.text
    print(req_create_email)
    email_split = re.search(r'(.+)@(.+)', str(req_create_email))
    if email_split:
        email_part=list(email_split.groups())
        try:
            email_from_req =email_part[0]
            domaen_from_req = email_part[1]
        except:
            print("Email is not valid")
    send_code_to_email()

def random_email_and_password_username():
    global email, password, username, nospam, attempt, proxy_file
    nospam = 0
    attempt = 0
    for email in range(1):
        email = ''
        for item in range(8):
            email += random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')
    for username in range(1):
        username = ''
        for item in range(8):
            username += random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')
    for password in range(1):
        password = ''
        for item in range(8):
            password += random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')
    create_email()

def get_proxy():
    global proxy_file
    try:
        proxy_file = open('proxies.txt').read().splitlines()
        random_email_and_password_username()
    except FileNotFoundError:
        print(f'{Fore.LIGHTGREEN_EX}\ncreate a file named proxies.txt and Paste The proxies!{reset_color}')

if __name__ == '__main__':
    os.system('cls')
    os.system(f'cls & mode 85,20 & title [Moat Instagram Account Creator] - Configuration')
    print(requests.get('http://artii.herokuapp.com/make?text=igc').text)
    print(f'{magenta_color}registry loading{reset_color}')
    get_proxy()
    time.sleep(5)