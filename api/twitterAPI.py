import cfscrape, requests, json
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context
from fake_headers import Headers
from colorama import Fore, Style
from urllib3.util.ssl_ import create_urllib3_context
from api.colors import colors

def brutedomain(email, chars):
    guesses = []

    domain_file = open('files/emails.txt', 'r').readlines()

    provider = email.split('@')[1]
    for domain in domain_file:
        domain = domain.rstrip()
        if provider[0] == domain[0]:
            if len(provider.split('.')[0]) == len(domain.split('.')[0]):
                guesses.append(email.split('@')[0]+"@"+domain)
                print(f'Possible Domain - {email.split("@")[0]}@{domain}')

    return guesses[-1]


def checkemail(email) -> bool:
    url = f'https://twitter.com/users/email_available?email={email}'
    r = requests.get(url).text
    if 'Available' in r:
        return True
    else:
        return False

def execute(target: str):
        url = "https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + target + "%22%2C%22withHighlightedLabel%22%3Atrue%7D"
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,bn;q=0.8",
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            "content-type": "application/json",
            "dnt": "1",
            'origin': 'https://twitter.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en'
            }
        resp  = json.loads(requests.get(url, headers=headers).text)
        try:
            if resp["data"]["user"]["id"] in resp:
                pass
        except:
            try:
                err = resp["errors"][0]["message"]
                if "Not found" == err:
                    print(f'{colors.error}•{colors.text} Username Not Found On Twitter')
                else:
                    print(err)
            except:
                print(f'{colors.error}•{colors.text} Username Not Found On Twitter')
                
        bio = resp["data"]["user"]["legacy"]["description"]
        followers = resp["data"]["user"]["legacy"]["followers_count"]
        location = resp["data"]["user"]["legacy"]["location"]
        name = resp["data"]["user"]["legacy"]["name"]
        Id = resp["data"]["user"]["id"]
        created = resp["data"]["user"]["legacy"]["created_at"]

        if location == '':
            location = 'Unknown'
        if bio == '':
            bio = 'Unknown'
            
        class CustomAdapter(HTTPAdapter):
            def init_poolmanager(self, *args, **kwargs):
                ctx = create_urllib3_context()
                super(CustomAdapter, self).init_poolmanager(
                    *args, ssl_context=ctx, **kwargs
                )
        try:
            url = 'https://twitter.com/account/begin_password_reset'
            header = Headers(browser='chrome', os='win', headers=True)
            scraper = cfscrape.create_scraper()

            scraper.mount('https://', CustomAdapter())
            req = scraper.get(url, headers=header.generate())
            soup = bs(req.text, 'html.parser')
            authenticity_token = soup.input.get('value')
            data = {'authenticity_token': authenticity_token, 'account_identifier': target}
            cookies = req.cookies
            response = scraper.post(url, cookies=cookies, data=data, headers=header.generate())
            soup2 = bs(response.text, 'html.parser')

            try:
                if (
                    soup2.find('div', attrs={'class': 'is-errored'}).text
                    == 'Please try again later.'
                ):
                    exit(f'{colors.error}Rate Limit{colors.text}')
            except:
                pass

            try:
                info = soup2.find('ul', attrs={'class': 'Form-radioList'}).findAll('strong')
            except:
                exit(f'{colors.error}Rate Limit{colors.text}')

            try:
                phone = int(info[0].text)
                email = str(info[1].text)
            except:
                email = str(info[0].text)
                phone = 'None'

        except Exception as e:
            exit(f'{colors.error}{e}{colors.text}')

        email = brutedomain(email, None)
        return [name, email, phone]

def checkUsername(username):
    url = f"https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22{username}%22%2C%22withHighlightedLabel%22%3Atrue%7D"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,bn;q=0.8",
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        "content-type": "application/json",
        "dnt": "1",
        'origin': 'https://twitter.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
    }
    resp  = json.loads(requests.get(url, headers=headers).text)
    try:
        return resp["data"]["user"]["legacy"]["created_at"]
    except:
        try:
            if "Not found" == resp["errors"][0]["message"]:
                return False
            else:
                return False
        except:
            return False
