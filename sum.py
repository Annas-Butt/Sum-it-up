import re

hand=open('actual.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    number=re.findall('[0-9]+',line)
    for num in number:
        num=num.rstrip()
        pieces=num.split(',')
        for piece in pieces:
            rawno=int(piece)
            numlist.append(rawno)
print(sum(numlist))
