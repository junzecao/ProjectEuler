# Enter your code here. Read input from STDIN. Print output to STDOUT

history = [[1]*501 for i in xrange(501)]
def populate_history():
    for i in xrange(1,501):
        for j in xrange(1,i):
            history[i][j] = (history[i-1][j] + history[i][j-1]) % 1000000007
        history[i][i] = (history[i][i-1] * 2) % 1000000007

populate_history()
t = int(raw_input().strip())
for a0 in xrange(t):
    [m,n] = map(int,raw_input().strip().split(' '))
    print history[max(m,n)][min(m,n)]
