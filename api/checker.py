import mechanize, requests, os, sys, time, threading
from mechanize import Browser

def breach(user):
    results = []
    
    res = requests.get(
        'https://api.weleakinfo.to/api',
        params={
            'type': 'email',
            'value': user,
            'key': 'KEY'
        }
    )

    json_data = res.json()

    for r in json_data['result']:
        sources = ', '.join(r['sources']) if len(r['sources']) > 0 else 'Unknown Source'
        results.append([r['line'].split(':')[1], sources])
    