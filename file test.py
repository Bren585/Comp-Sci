import os

with open("test.txt", "r+") as f:
    line_offset = []
    offset = 0
    for line in f:
        line_offset.append(offset)
        offset += len(line)
    f.seek(0)
    print f.read()
    f.seek(0)
    f.write("Hello World")
    f.seek(0)
    ln = 0
    for line in f:
        if "l" in line:
            for x in range(0,len(line)):
                print line
                print x
                if line[x] == 'l':
                    line = line[0:x] + 'r' + line[x+1:]
            f.write(line)
        ln += 1
