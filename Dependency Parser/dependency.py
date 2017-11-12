def shift(stack, buff,  dgraph):
    # TODO

    stack.append(buff[-1])
    buff.remove(buff[-1])
    
    #raise NotImplementedError

def left_arc(stack, buff, dgraph):
    # TODO

    dgraph.append((stack[-2],stack[-1]))
    stack.remove(stack[-2])
    
    #raise NotImplementedError

def right_arc(stack, buff, dgraph):
    # TODO

    dgraph.append((stack[-1],stack[-2]))
    stack.remove(stack[-1])
    
    #raise NotImplementedError

def oracle_std(stack, buff, dgraph, gold_arcs):
    # TODO

    if len(stack) < 2 and len(buff) > 0:
        return 'shift'

    j = stack[-1]
    i = stack[-2]
    
    if (i,j) in gold_arcs:
        return 'left_arc'
    
    if (j,i) in gold_arcs:

        for (k,l) in gold_arcs:
            if l == j and (k,l) not in dgraph:
                return 'shift'
            
        return 'right_arc'

    if len(buff) > 0:
        return 'shift'
    else:
        return 'invalid'

        
    #raise NotImplementedError()

def make_transitions(buff, oracle, gold_arcs=None):
    stack = []
    dgraph = []
    configurations = []

    
    while (len(buff) > 0 or len(stack) > 1):
        choice = oracle(stack, buff, dgraph, gold_arcs)
        
        # Makes a copy. Else configuration has a reference to buff and stack.
        config_buff = list(buff)
        config_stack = list(stack)
        configurations.append([config_stack,config_buff,choice])
        if choice == 'shift': shift(stack, buff, dgraph)
        elif choice == 'left_arc': left_arc(stack, buff, dgraph)
        elif choice == 'right_arc': right_arc(stack, buff, dgraph)
        else: return None

        
    return dgraph,configurations
