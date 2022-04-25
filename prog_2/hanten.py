import io,sys
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

i, j, risto = 0, 0, []
exec("i, j, risto = " + input())
if (0 <= i <= j < len(risto)):
    ret = risto[j::-1] + risto[j + 1:]
    print(ret)
else:
    print(f"Invalid input for indices -> i,j={i},{j}")
