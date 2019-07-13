def hello():
    print('Oh! Hello!')

def incorrect():
    print('I\'m sorry, that is the wrong input')

def Dave():
    print('Nah man, Dave\'s not here')

response = input('''Who\'s there?
''')

if response == "Hi, it's me.":
    hello()
else:
    incorrect()

if response == "It's Dave man. I got the stuff.":
    Dave()
