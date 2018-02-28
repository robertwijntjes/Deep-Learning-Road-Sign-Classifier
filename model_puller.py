def model_puller():

    mapper = []
    f = open('config.txt','r+')
    depth = {}
    dictionary = {}
    copy = False
    check = False

    for x in f:
        if x.strip() == '?':
            check = not check
        elif check:
            mapper.append(x.strip())
    return ( mapper )
    # Parses by ? using the config file
