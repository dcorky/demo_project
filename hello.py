def hello():
    print('Oh! Hello!')

def incorrect():
    print('I\'m sorry, that is the wrong input')

response = input('''Who\'s there?
''')

if response == "Hi, it's me.":
    hello()
else:
    incorrect()
