

def gothrough(newlist):
    for operand in newlist:
        if isinstance(operand, list):
            for suboperand in operand:
                 gothrough(suboperand)
        print(operand)
        continue



newlist = [[[['NOT', [['NOT', 'A'], 'OR', 'B']], 'AND', ['NOT', 'C']], 'OR', [[['NOT', 'A'], 'OR', 'B'], 'AND', 'C']]]

gothrough(newlist)