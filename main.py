import re

class createExpression:
    def __init__(self, question):
        self.question = question
        self.valid = True

    def checkCorrectFormat(self):
    
    def checkNumberOfVariables(self):
        counter = 0

    def checkAlphabet(self):
        # acceptable characters = (), A,B,C,D, OR, AND, NOT, -> , <->
        alphabet = ['A', 'B', 'C', 'D', '(', ')', 'OR', 'NOT', 'AND', '->', '<->']
        for c in self.question:
            if c not in alphabet:
                self.valid = False
                break
        #acceptedFormat = re.compile("(variable operator)")

    def convertInput(self):


class createTruthTable:
    def __init__(self):

    def numberOfColumns(self):
    
    def numberOfRows(self):

    def columnHeadings(self):

    def trueOrFalse(self):


class ReadFile:
    def __init__(self, filename):
        self.filename = filename

    def numberOfQuestions(self):

    def addQuestions(self):