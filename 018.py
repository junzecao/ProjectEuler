# Enter your code here. Read input from STDIN. Print output to STDOUT

class node:
    left = None
    right = None
    def __init__(self,data):
        self.data = data

def read_into_trees(n):
    head_data = int(raw_input().strip())
    head = [node(head_data)]
    head_return = head[0]
    for i in xrange(n-1):
        next_data = map(int,raw_input().strip().split(' '))
        next_node = [node(val) for val in next_data]
        for j in xrange(i+1):
            head[j].left = next_node[j]
            head[j].right = next_node[j+1]
        head = next_node
    return head_return

def find_tree_sum(head):
    if head.left == None:
        return head.data
    left_sum = find_tree_sum(head.left) + head.data
    right_sum = find_tree_sum(head.right) + head.data
    return max(left_sum,right_sum)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    head = read_into_trees(n)
    print find_tree_sum(head)
