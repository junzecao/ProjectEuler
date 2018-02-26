# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sum(int(i) for i in str(1 << n))
