import sys


class Node:
    def __init__(self, alpha, leftNode, rightNode):
        self.alpha = alpha
        self.leftNode = leftNode
        self.rightNode = rightNode


def pre(node, res):
    if node:
        res += node.alpha
        res = pre(node.leftNode, res)
        res = pre(node.rightNode, res)
    return res


def inorder(node, res):
    if node:
        res = inorder(node.leftNode, res)
        res += node.alpha
        res = inorder(node.rightNode, res)
    return res


def post(node, res):
    if node:
        res = post(node.leftNode, res)
        res = post(node.rightNode, res)
        res += node.alpha
    return res


N = int(sys.stdin.readline().rstrip())
dic = {}
for i in range(N):
    dic[chr(i + 65)] = Node(chr(i + 65), None, None)
for i in range(N):
    arr = list(sys.stdin.readline().rstrip().split(" "))
    dic.get(arr[0]).leftNode = dic.get(arr[1])
    dic.get(arr[0]).rightNode = dic.get(arr[2])
print(pre(dic['A'], ""))
print(inorder(dic['A'], ""))
print(post(dic['A'], ""))
