import os

with open("test.txt", "r+") as f:
    f.truncate(0)
    f.write("Hello World")
    f.seek(0)
    line_offset = []
    offset = 0
    lines = 0
    for line in f:
        line_offset.append(offset)
        offset += len(line)
        lines += 1
    print lines
    f.seek(0)
    ln = 0
    for line in f:
        if "l" in line and ln < lines:
            print ln
            for x in range(0,len(line)):
                print line
                print x
                if line[x] == 'l':
                    line = line[0:x] + 'r' + line[x+1:]
            f.seek(line_offset[ln])
            print
            print line
        ln += 1
