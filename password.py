import pyperclip

PASSWORDS = {'email1': 'Password',
             'email2': 'Password'}


while True:
       print('Enter account name you want Password for: (blank to quit)')
       for i in PASSWORDS.keys():
       	print(i)
       account = input()
       if account == '':
           break



if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
