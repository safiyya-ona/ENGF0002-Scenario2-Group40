from truthTableGenerator import createTruthTable

newTable = createTruthTable("A AND NOT B")
result = newTable.run()
print(result)