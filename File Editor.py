doc = []

with open('test.txt') as f:
    for line in f:
        doc.append(line)

with open('test.text', 'w') as f:
    for line in doc:
        f.write(str(line) + '\n')