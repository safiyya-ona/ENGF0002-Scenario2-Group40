import re
import sys
from pyparsing import *
import copy
import math
import random

ParserElement.enablePackrat()
sys.setrecursionlimit(3000)

class checkExpression:
    def __init__(self, question):
        self.question = question
        self.hasImplication = False
        self.convertedRes = []
        self.res = []
        self.convertedString = ""
        
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
            self.res = res.asList().copy()
        except ParseException:
            print("Code not in right format")
            return False
        return True

    def checkNumberOfVariables(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        for word in re.split("[() ]", self.question):
            if word == 'A' and self.a == 0:
                self.a += 1
                continue
            if word == 'B' and self.b == 0:
                self.b += 1
                continue            
            if word == 'C' and self.c == 0:
                self.c += 1
                continue            
            if word == 'D' and self.d == 0:
                self.d += 1
                continue
        self.variableNum = sum([self.a, self.b, self.c, self.d])
        if self.variableNum < 1 or self.variableNum > 4:
            return False
        return True

    def checkAlphabet(self):
        # acceptable characters = (), A,B,C,D, OR, AND, NOT, -> , <->
        alphabet = ['A', 'B', 'C', 'D', '(', ')', 'OR', 'NOT', 'AND', '->', '<->', ""]
        for c in re.split("[() ]", self.question):
            if c not in alphabet:
                return False
            if c == '->' or c == '<->':
                self.hasImplication = True
        return True

    def run(self):
        if (self.checkAlphabet() and self.checkNumberOfVariables() and self.checkCorrectFormat()):
            return True
        return False
        

# makes the stuff we need to evaluate by
class convertImplications:
    def __init__(self, formula):
        self.formula = copy.deepcopy(formula)
        self.originalFormula = formula


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
        
        if not self.formula.hasImplication:
            self.originalFormula.convertedString = self.originalFormula.question.lower()
            return
    
        list_values = list(self.traverse(self.formula.res))
        self.originalFormula.convertedString = " ".join(list_values).lower()
        self.originalFormula.convertedRes = self.formula.res

        # print("Original result after : ", self.originalFormula.res)
        # print("Original converted result after : ", self.originalFormula.convertedRes)
        
        return 
    

class createTruthTable:
    def __init__(self, question):
        self.tableheadings = []
        self.origQuestionString = question
        self.headingsformulalist = []
        self.rows = []

    def numberOfColumns(self):
        return self.formula.variableNum + 1
        
    def createTableHeadings(self):
        if self.formula.a != 0:
            self.tableheadings.append("A")
        if self.formula.b != 0:
            self.tableheadings.append("B")
        if self.formula.c != 0:
            self.tableheadings.append("C")
        if self.formula.d != 0:
            self.tableheadings.append("D")
        self.tableheadings.append("Result")
        # self.traverse(self.formula.res)
    
    def numberOfRows(self):
        return 2 ** self.formula.variableNum

    def createRows(self):
        rows  = []
        for i in range(self.numberOfRows()):
            binary  = bin(i)[2:].zfill(self.formula.variableNum)
            values = list(binary)
            evalVariables = {"not" : "~", "and": "&", "or": "|"}
            for j, px in enumerate(self.tableheadings):
                if px == "Result":
                    continue
                evalVariables.update({px.lower(): int(values[j])})

            try:
                result = eval(self.formula.convertedString,evalVariables)
            except SyntaxError:
                raise QuestionWrongFormat
                pass
            values.append(int(result))
            rows.append(values)
        return rows
        
    def trueOrFalse(self):
        pass

    def replaceOperators(self):
        replaceAnds = self.formula.convertedString.replace("AND", "&")
        replaceOrs = replaceAnds.replace("OR", "|")
        replaceNots = replaceOrs.replace("NOT", "~")
        return replaceNots
        

    def run(self):
        self.formula = checkExpression(self.origQuestionString)
        if not self.formula.run():
            # exception error in code_body
            print("Wrong format")
            raise QuestionWrongFormat
            pass
        convertFormula = convertImplications(self.formula)
        convertFormula.run()
        self.createTableHeadings()
        table = [self.tableheadings]
        table.extend(self.createRows())
        # print(table)
        return table

class TruthTableErrors(Exception):
    """ Errors for truth table generator """
    pass


class QuestionWrongFormat(TruthTableErrors):
    """ Raised when question has wrong format """
    pass

class WrongFileFormat(TruthTableErrors):
    """Raised when file format is wrong"""
    """ Attributes 
        message - Wrong question on line: 
        linenumber - where the wrong message is
    
    """
    def __init__(self, linenumber, message= "Wrong question format for Question {}"):
        self.linenumber = linenumber + 1
        self.message  = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.linenumber)
    pass

        

class CheckFile:
    def __init__(self, filename):
        self.filename = filename
        self.generatedTables = dict()

    def checkQuestionFormats(self):
        # reads number of questions
        inputFile = open(self.filename, "r")
        line1 = inputFile.readline().strip().split(" ")
        numQuestions = int(line1[0])
        #reads each question and checks
        for i in range(numQuestions):
            line = inputFile.readline().strip()
            newQuestion = checkExpression(line)
            if not newQuestion.run():
                raise WrongFileFormat(i)

    def generateTruthTables(self):
        # reads number of questions
        inputFile = open(self.filename, "r")
        line1 = inputFile.readline().strip().split(" ")
        numQuestions = int(line1[0])
        #reads each question and generates table
        for i in range(numQuestions):
            line = inputFile.readline().strip()
            newTable = createTruthTable(line)
            table = newTable.run()
        
            self.generatedTables.update({i + 1: table})      
        return self.generatedTables

    def run(self):
        self.checkQuestionFormats()
        self.generateTruthTables()


class GenerateQuestions:
    def __init__(self, filename):
        self.filename = filename
        self.questionDatabase = list()
        self.numQuestions = 0

    def addQuestions(self):
        # reads number of questions
        inputFile = open(self.filename, "r")
        line1 = inputFile.readline().strip().split(" ")
        self.numQuestions = int(line1[0])
        #reads each question and adds to list
        for i in range(self.numQuestions):
            line = inputFile.readline().strip()
            self.questionDatabase.append(line)

    def getQuestion(self):
        number = random.randint(0, self.numQuestions-1)
        return self.questionDatabase[number]

    def run(self):
        self.addQuestions()
        self.getQuestion()

# ((NOT A) OR B) <-> ((B OR C) -> D)


if __name__ == "__main__":
    truthTable = createTruthTable("((NOT A) OR B) <-> C")
    truthTable.run()
    read  = CheckFile("test.txt")
    print(read.run())
