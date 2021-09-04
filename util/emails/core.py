import requests, re, base64

def checkEmail(email) -> bool:
    url = f'https://twitter.com/users/email_available?email={email}'
    r = requests.get(url).json()

    if r['taken'] == True:
        return True
    else:
        return False

def getEmailFromPublicKey(public_key):
    return re.findall(r'\s<(.*?)>', str(base64.b64decode(public_key)))