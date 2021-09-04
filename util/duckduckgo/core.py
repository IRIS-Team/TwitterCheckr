import requests
import bs4

class DuckDuckGo:
    @staticmethod
    def search(search_query: str) -> list[tuple[str, str]]:
        """ DuckDuckGo search """
        def __search(q: str) -> "requests.models.Response":
            return requests.post(
                'https://lite.duckduckgo.com/lite/',
                headers={
                    'accept': '*/*',
                    'origin': 'https://lite.duckduckgo.com',
                    'referer': 'https://lite.duckduckgo.com/',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36'
                },
                data={
                    'q': q,     # search query
                    'kl': None, # search language (None/wt-wt = global)
                    'dt': None  # search time
                }
            )

        res = __search(search_query)

        if res.status_code == 403:
            __search('cute cat')
            return DuckDuckGo.search(search_query)

        if res.status_code != 200:
            raise Exception(res.text)

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        return [
            (x['href'], x.text)
            for x in soup.find_all('a', {'rel': 'nofollow'})
        ]
