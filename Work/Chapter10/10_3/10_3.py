name = input("What's your name?")

filename = r'${FileDir}\guest.txt'

with open(filename, 'w') as f:
    f.write(name)
