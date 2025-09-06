'''Representing graphs'''

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

def part_1_graph():
    """
    Part 1: Represent the graph using a list of sets
    a → b, c
    b → c, d
    c → d, e
    d → e
    e → (none)
    """
    graph = [
        {'b', 'c'},   # neighbors of a
        {'c', 'd'},   # neighbors of b
        {'d', 'e'},   # neighbors of c
        {'e'},        # neighbors of d
        set()         # neighbors of e
    ]
    return graph

def part_2_graph():
    """
    Part 2: Represent the graph using a list of lists
    a → a, b, c, d
    b → c
    c → b, d
    d → c
    """
    graph = [
        ['a', 'b', 'c', 'd'],  # neighbors of a
        ['c'],                 # neighbors of b
        ['b', 'd'],            # neighbors of c
        ['c']                  # neighbors of d
    ]
    return graph

def part_3_graph():
    """
    Part 3: Represent the weighted digraph using a list of dicts
    a → b (1), c (2), e (4)
    b → c (3)
    c → e (4)
    e → a (8)
    """
    graph = [
        {'b': 1, 'c': 2, 'e': 4},  # neighbors of a with weights
        {'c': 3},                  # neighbors of b with weights
        {'e': 4},                  # neighbors of c with weights
        {},                        # neighbors of d
        {'a': 8}                   # neighbors of e with weights
    ]
    return graph

def part_4_graph():
    """
    Part 4: Represent the digraph using a dict of sets
    a → b, c
    b → a, c
    c → a
    """
    graph = {
        'a': {'a', 'b', 'e'},
        'b': {'c'},
        'c': {'e'},
        'e': {'a'}
    }
    return graph

def part_5_graph():
    """
    Part 5: Represent the weighted digraph using a dict of dicts
    a → b (5), e (2)
    b → e (6)
    e → a (3)
    """
    graph = {
        'a': {'b': 5, 'e': 2},
        'b': {'e': 3},
        'e': {'a': 3}
    }
    return graph
