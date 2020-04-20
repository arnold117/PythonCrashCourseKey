filename = r'${FileDir}\learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with c.
    line = line.rstrip()
    print(line.replace('Python', 'C'))

"""
* for-loop can also be:
* for line in lines:
*     print(line.rstrip().replace('Python', 'C'))
"""
