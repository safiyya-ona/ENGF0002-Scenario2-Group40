import re
import sys
from pyparsing import *
import copy
import math

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
        #evalFormula = self.replaceOperators()
        for i in range(self.numberOfRows()):
            binary  = bin(i)[2:].zfill(self.formula.variableNum)
            values = list(binary)
            evalVariables = {"not" : "~", "and": "&", "or": "|"}
            for j, px in enumerate(self.tableheadings):
                if px == "Result":
                    continue
                evalVariables.update({px.lower(): int(values[j])})
            result = eval(self.formula.convertedString,evalVariables)
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
        
    # def getHeadingsFormula(self):
    #     self.headingsformulalist = []
    #     value = list(self.traverse(self.formula.res))
    #     print(self.headingsformulalist)

    # def traverse(self, o, tree_types=(list, tuple)):
    #     if isinstance(o, tree_types):
    #         for value in o:
    #             if isinstance(value, list):
    #                 self.headingsformulalist.append(" ".join(str(value)))
                
    #             for subvalue in self.traverse(value, tree_types):
    #                 yield subvalue
    #     else:
    #         yield o

    def run(self):
        self.formula = checkExpression(self.origQuestionString)
        if not self.formula.run():
            # exception error in code_body
            print("Wrong format")
            return
        convertFormula = convertImplications(self.formula)
        convertFormula.run()
        self.createTableHeadings()
        table = [self.tableheadings]
        table.extend(self.createRows())
        print(table)
        return table
        

class ReadFile:
    def __init__(self, filename):
        self.filename = filename

    def numberOfQuestions(self):
        pass

    def addQuestions(self):
        pass

# ((NOT A) OR B) <-> ((B OR C) -> D)

truthTable = createTruthTable("((NOT A) OR B) <-> C")
truthTable.run()

# print(bin(1)[2:].zfill(2))

# numRows = 8
# for i in range(numRows):
#     binary  = bin(i)[2:].zfill(2)
#     print(binary)
#string = "a or b"

#print(int(eval(string, {"a": 0, "b" : 1, "not" : "~", "and": "&", "or": "|"})))