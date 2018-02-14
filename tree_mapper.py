def tree_mapper():
    f = open('config.txt','r+')
    depth = {}
    for line in f:
        parent, children = read_node(line)
        print(str(parent) + ':' + str(children))
        if children:
            depth[parent] = max(depth.get(child,1) for child in children) + 1


def read_node(line):
    parent, children = line.split(":")
    return parent, children.split()

tree_mapper()
