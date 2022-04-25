import io,sys
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

firstLine, secondLine = [], []
exec("firstLine, secondLine = " + input())
ret = []

for station in firstLine:
    ret.append(station)
    if (station in secondLine): # we norikae here
        pos = secondLine.index(station) + 1
        ret.extend(secondLine[pos:])
        print(ret)
        break