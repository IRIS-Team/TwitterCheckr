from api import checker, menu, twitterAPI

def main():
    menu.banner(); target = menu.menu()
    check = twitterAPI.checkUsername(target)
    if check == False: exit('Invalid Handle')
    else: print(f'Registed: {menu.returnColor(check)}')

    twitterRequest = twitterAPI.execute(target)

    print(f'''
{menu.returnColor("@")}{target} -> 
    Full  Name.: {menu.returnColor(twitterRequest[0])} 
    Email Hint.: {menu.returnColor(twitterRequest[1])} 
    Phone Hint.: {menu.returnColor(twitterRequest[2])}
''')


if __name__ == "__main__":
	main()
