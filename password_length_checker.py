# Password length checker
user_name = input('Enter a user name - ')
password = input('Enter your password -')
hide = '*'* len(password)
print(f'{user_name},your Password,{hide}, is {len(password)} characters long')
