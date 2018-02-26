# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input().strip())
sum_ = 0
for a0 in xrange(t):
    sum_ += int(raw_input().strip())

sum_ = str(sum_)
print sum_[0:10]
