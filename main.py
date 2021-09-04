from api.core import *
from util.colors import colors

def main():
    banner(); target = menu()
    check = checkUsername(target)
    if check == False: exit('Invalid Handle')
    else: print(f'Registed: {colors.returnColor(check)}')
    twitterRequest = scraper(target)

    print(f'''
{colors.returnColor("@")}{target} -> 
    Full  Name.: {colors.returnColor(twitterRequest[0])} 
    Email Hint.: {colors.returnColor(twitterRequest[1])} 
    Phone Hint.: {colors.returnColor(twitterRequest[2])}
''')


if __name__ == "__main__":
	main()
