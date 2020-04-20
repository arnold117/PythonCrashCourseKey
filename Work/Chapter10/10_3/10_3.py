name = input("What's your name?")

filename = r'${FileDir}\guest.txt'

with open(filename, 'W') as f:
    f.write(name)
