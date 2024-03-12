from bs4 import BeautifulSoup
form_class = "modal-content"
login_page = open("./temp/SITV - Login.html")
soup = BeautifulSoup(login_page, 'html.parser')
# Find the form by class name
form = soup.find('form')
# print(form.text) 
input_names = [a.get('name') for a in form.find_all('input')]
print(input_names)
key_username = input_names[0]
key_password = input_names[1]
key_captcha = input_names[2]