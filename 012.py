# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math


hash_history = {1:{},2:{2:1},3:{3:1},4:{2:2},5:{5:1},6:{2:1,3:1},10:{2:1,5:1},15:{3:1,5:1}}
prime = [2,3,5]
number_history = [2,3]
divisor_history = [2,4]

def merge(d1,d2):
    d3 = dict(d1)
    for i,j in d2.items():
        if d1.has_key(i):
            d3[i] += j
        else:
            d3[i] = j
    return d3

def factor_i_plus_1(n):
    sqrt_ = math.sqrt(n)
    for i in prime:
        if not n%i:
            return i
    prime.append(n)
    return n

def add_i_plus_1(n):
    divisor = factor_i_plus_1(n)
    hash_history[n] = merge(hash_history[n//divisor],{divisor:1})

def find_num_divisor(n):
    num_divisor = 1
    for i in n.values():
        num_divisor *= (i+1)
    return num_divisor

def find_1000_divisors():
    i = 6
    while(True):
        triangular_number = i*(i+1)//2
        if not hash_history.has_key(i+1):
            add_i_plus_1(i+1)
        if not hash_history.has_key(triangular_number):
            hash_history[triangular_number] = merge(hash_history[i],hash_history[i+1])
            hash_history[triangular_number][2] -= 1
        num_divisor = find_num_divisor(hash_history[triangular_number])
        if num_divisor > divisor_history[-1]:
            number_history.append(i)
            divisor_history.append(num_divisor)
            if num_divisor > 1000:
                return
        i += 1

def triangular_number(n):
    for i in xrange(len(divisor_history)):
        if divisor_history[i] > n:
            return (number_history[i] * (number_history[i]+1)) // 2

t = int(raw_input().strip())
find_1000_divisors()
for a0 in xrange(t):
    n = int(raw_input().strip())
    print triangular_number(n)
