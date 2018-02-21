def tree_mapper():

    mapper = []
    f = open('config.txt','r+')
    depth = {}
    dictionary = {}
    for line in f:
        parent, children = read_node(line)
        dictionary[parent] = children
        if children:
            depth[parent] = max(depth.get(child,1) for child in children) + 1
    return ( dictionary )



def read_node(line):
    parent, children = line.split(":")
    return parent, children.split()
