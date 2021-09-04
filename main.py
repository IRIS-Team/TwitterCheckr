from api.core import *

def main():
    banner(); target = menu()
    check = checkUsername(target)
    if check == False: exit('Invalid Handle')
    else: print(f'Registed: {returnColor(check)}')
    twitterRequest = scraper(target)

    print(f'''
{returnColor("@")}{target} -> 
    Full  Name.: {returnColor(twitterRequest[0])} 
    Email Hint.: {returnColor(twitterRequest[1])} 
    Phone Hint.: {returnColor(twitterRequest[2])}
''')


if __name__ == "__main__":
	main()
