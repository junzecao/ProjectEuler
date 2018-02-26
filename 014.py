# Enter your code here. Read input from STDIN. Print output to STDOUT

length_history = [0] * 5000001
number_stack = []
length_stack = []

def populate_length(n):
    if n == 1:
        return 0
    if n < 5000001 and length_history[n] != 0:
        return length_history[n]
    if n%2 == 0:
        length = populate_length(n//2) + 1
    else:
        length = populate_length(3*n+1) + 1
    if n < 5000001:
        length_history[n] = length
    return length
    
def populate_length_history():
    for i in xrange(5000000,0,-1):
        length = populate_length(i)
        while len(length_stack) != 0 and length > length_stack[-1]:
            number_stack.pop()
            length_stack.pop()
        number_stack.append(i)
        length_stack.append(length)

def collatz_sequence(n):
    for i in number_stack:
        if i<=n:
            return i

populate_length_history()
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print collatz_sequence(n)
