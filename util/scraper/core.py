from util.core import *
from util.duckduckgo import *
from util.emails import *

def verifyScraper():
    results = DuckDuckGo.search(f'intext:"Verifying myself: I am" site:twitter.com verified')

    if len(results) == 0:
        raise Exception('No results found')

    for result in results:
        try:
            emailList = []

            username = result[0].split('https://twitter.com/')[1].split('/')[0]
            keybase  = result[1].split('«Verifying myself: I am ')[1].split('on')[0]

            res = requests.get('https://keybase.io/_/api/1.0/user/lookup.json', params={'username': username})

            if res.status_code != 200:
                return

            profile = res.json()['them']


            public_key = profile.get('public_keys', {}).get('primary', {}).get('bundle', '').split('\n\n')[1].split('-----')[0]
            emails = getEmailFromPublicKey(public_key)

            for email in email:
                if len(email > 20): emailList.append(email)

            print(f'''
Username.....: {colours.main}{username}
Keybase......: {colours.main}{keybase}
Email Address: {colours.main}{email}
''')
        except Exception as e:
            pass