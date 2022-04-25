import io,sys
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

inokashira, inokashiraExpress = [], []
exec(input())

inokashiraFiltered = list(filter(lambda x: x not in inokashiraExpress, inokashira))
print(inokashiraFiltered)
