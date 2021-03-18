import re

class checkExpression:
    def __init__(self, question):
        self.question = question

    def checkCorrectFormat(self):
        pass

    def checkNumberOfVariables(self):
        a = 0
        b = 0
        c = 0
        d = 0
        for word in self.question.split():
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
        alphabet = ['A', 'B', 'C', 'D', '(', ')', 'OR', 'NOT', 'AND', '->', '<->']
        for c in self.question.split():
            if c not in alphabet:
                return False
        return True

    def run(self):
        self.checkAlphabet()
        self.checkNumberOfVariables()
        

class createExpression:
    def __init(self):
        pass

    def convertInput(self):
        pass

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

test = checkExpression("")
test.checkNumberOfVariables()
print(test.variableNum)
