# Enter your code here. Read input from STDIN. Print output to STDOUT

number_history = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}

def number_less_than_thousand(n):
    hundred = n//100
    if hundred != 0:
        print number_history[hundred], "Hundred",
    n -= hundred*100
    if n == 0:
        return
    ten = n//10
    if ten == 0 or ten == 1:
        print number_history[n],
        return
    print number_history[ten*10],
    n -= ten*10
    if n != 0:
        print number_history[n],
        
def number_to_words(n):
    if n == 10**12:
        print "One Trillion"
        return
    billion = n//10**9
    if billion != 0:
        number_less_than_thousand(billion)
        print "Billion",
    n -= billion*10**9
    million = n//10**6
    if million != 0:
        number_less_than_thousand(million)
        print "Million",
    n -= million*10**6
    thousand = n//10**3
    if thousand != 0:
        number_less_than_thousand(thousand)
        print "Thousand",
    n -= thousand*10**3
    if n != 0:
        number_less_than_thousand(n)
    print ""

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    number_to_words(n)
