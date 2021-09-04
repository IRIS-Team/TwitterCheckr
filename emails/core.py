import requests

def checkEmail(email) -> bool:
    url = f'https://twitter.com/users/email_available?email={email}'
    r = requests.get(url).json()

    if r['taken'] == True:
        return True
    else:
        return False
