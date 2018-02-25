def tree_mapper():

    mapper = []
    f = open('config.txt','r+')
    c = f
    depth = {}
    dictionary = {}
    copy = False
    check = False

    for line in f:
        if line.strip() == '@':
            copy = not copy

        elif copy:
            parent, children = read_node(line)
            dictionary[parent] = children
            if children:
                depth[parent] = max(depth.get(child,1) for child in children) + 1
    return ( dictionary )



def read_node(line):
    parent, children = line.split(":")
    return parent, children.split()
