import io,sys
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

local, express = [], []
exec("local, express = " + input())
ret = []
current = 0
for sta in local:
    if sta in express:
        ret.append(current)
        current = 0
    else:
        current += 1
if(ret[0] == 0):
    ret.pop(0)
print(ret)