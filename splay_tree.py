class Node:
    def __init__(self, key, data, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def rotate_right(v: Node):
    p = v.parent
    g = p.parent
    if g:
        if p == g.left:
            g.left = v
        else:
            g.right = v
    v.parent = g
    tmp = v.right
    v.right = p
    p.parent = v
    p.left = tmp
    if tmp:
        tmp.parent = p


def rotate_left(v: Node):
    p = v.parent
    g = p.parent
    if g:
        if p == g.left:
            g.left = v
        else:
            g.right = v
    v.parent = g
    tmp = v.left
    v.left = p
    p.parent = v
    p.right = tmp
    if tmp:
        tmp.parent = p


def splay(v: Node):
    while v.parent:
        p = v.parent
        g = p.parent
        if v == p.left:
            if not g:
                rotate_right(v)
            elif p == g.left:
                rotate_right(p)
                rotate_right(v)
            else:
                rotate_right(v)
                rotate_left(v)
        else:
            if not g:
                rotate_left(v)
            elif p == g.right:
                rotate_left(p)
                rotate_left(v)
            else:
                rotate_left(v)
                rotate_right(v)


def find(t: Node, x):
    curr = t
    while curr:
        if curr.key == x:
            splay(curr)
            return curr
        if x < curr.key:
            if not curr.left:
                splay(curr)
                return curr
            curr = curr.left
        else:
            if not curr.right:
                splay(curr)
                return curr
            curr = curr.right


def get_max(t: Node):
    curr = t
    while curr.right:
        curr = curr.right
    return curr


def get_min(t: Node):
    curr = t
    while curr.left:
        curr = curr.left
    return curr


def merge(t1: Node, t2: Node):
    mx = get_max(t1)
    splay(mx)
    mx.right = t2
    t2.parent = mx
    return mx


def split_(t: Node, x):
    v = find(t, x)
    if x < v.key:
        t1 = v.left
        t2 = v
        if t1:
            v.left.parent = None
        if t2:
            v.left = None
        return t1, t2
    t1 = v
    t2 = v.right
    if t2:
        v.right.parent = None
    if t1:
        v.right = None
    return t1, t2


def add(t: Node, data, key):
    t1, t2 = split_(t, key)
    v = Node(key, data, t1, t2)
    if t1:
        t1.parent = v
    if t2:
        t2.parent = v
    return v


def remove_(t: Node, x):
    v = find(t, x)
    return merge(v.left, v.right)

t = Node(10, "10")
a = [5, 11, 22, 48, 2]
for el in a:
    t = add(t, str(el), el)