


rule = {"111": '0', "110": '0', "101": '0', "000": '0',
        "100": '1', "011": '1', "010": '1', "001": '1'}



initial_state = '00000000000000000000100000000000000000000'
def window(iterable):
    for index in range(len(iterable) - 2):
        yield iterable[index:index + 3]
        
def generate_pattern(state):
    for time in range(50):
        print(state)
        patterns = window(state)
        state = ''.join(rule[pat] for pat in patterns)
        state = '0{}0'.format(state)
    print(state)
    
    
generate_pattern(initial_state)

    
    
