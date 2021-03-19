import re
import sys
from pyparsing import *

ParserElement.enablePackrat()
sys.setrecursionlimit(3000)

class checkExpression:
    def __init__(self, question):
        self.question = question

    def checkCorrectFormat(self):
        variable = oneOf(" A B C D")
        formula = infixNotation(
            variable,[
                ("NOT", 1, opAssoc.RIGHT),
                ("AND", 2, opAssoc.LEFT),
                ("OR", 2, opAssoc.LEFT),
                ("->", 2, opAssoc.LEFT),
                ("<->", 2, opAssoc.LEFT),
            ],
        )
        try:
            res = formula.parseString(self.question, parseAll = True)
            print(res)
            self.res = res.asList().copy()
        except ParseException:
            print("Code not in right format")
            return False
        return True

    def checkNumberOfVariables(self):
        a = 0
        b = 0
        c = 0
        d = 0
        for word in re.split("[() ]", self.question):
            if word == 'A' and a == 0:
                a += 1
                continue
            if word == 'B' and b == 0:
                b += 1
                continue            
            if word == 'C' and c == 0:
                c += 1
                continue            
            if word == 'D' and d == 0:
                d += 1
                continue
        self.variableNum = a + b + c + d
        if self.variableNum < 1 or self.variableNum > 4:
            return False
        return True

    def checkAlphabet(self):
        # acceptable characters = (), A,B,C,D, OR, AND, NOT, -> , <->
        alphabet = ['A', 'B', 'C', 'D', '(', ')', 'OR', 'NOT', 'AND', '->', '<->', ""]
        for c in re.split("[() ]", self.question):
            if c not in alphabet:
                return False
        return True

    def run(self):
        if (self.checkAlphabet() and self.checkNumberOfVariables() and self.checkCorrectFormat()):
            return True
        return False
        

class createExpression:
    def __init__(self, formula):
        self.formula = formula.res     
    def traverse(self, o, tree_types=(list, tuple)):
        if isinstance(o, tree_types):
            for value in o:
                if len(value) == 3 and value[1] == "->":
                    value[1] = "OR"
                    prev = value[0]
                    value[0] = ["NOT", prev]
                if len(value) == 3 and value[1] == "<->":
                    value[1] = "OR"
                    prev1 = value[0]
                    prev2 = value[2]
                    new1 = [["NOT", prev1], "AND", ["NOT", prev2]]
                    new2 = [prev1 ,"AND", prev2]
                    value[0] = new1
                    value[2] = new2
                for subvalue in self.traverse(value, tree_types):
                    yield subvalue
        else:
            yield o
    def run(self):
        try:
            return (list(self.traverse(self.formula)))
        except:
            print("Error")
    

class createTruthTable:
    def __init__(self):
        pass
    def numberOfColumns(self):
        pass
    def numberOfRows(self):
        pass
    def columnHeadings(self):
        pass
    def trueOrFalse(self):
        pass

class ReadFile:
    def __init__(self, filename):
        self.filename = filename

    def numberOfQuestions(self):
        pass
    def addQuestions(self):
        pass



# ((NOT A) OR B) <-> ((B OR C) -> D)

test = checkExpression("((NOT A) OR B) <-> C")
print(test.run())
test2 = createExpression(test)
# test2.convertImplications()
print(test2.run())
print(test2.formula)