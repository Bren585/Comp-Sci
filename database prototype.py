d = []

with open('test.txt') as f:
    for line in f:
        d.append(line)

l = 0
for line in d:
    i = 0
    for x in line:
        if x == 't' or x == 'e':
            d[l] = d[l][:i] + '*' + d[l][i+1:]
        i+=1
    l+=1

for x in d:
    print x