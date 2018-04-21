import ast

class FinalProject693:

    def __init__(self):
        return

    def getlinesofcode(self, file):

        linesOfCode = 0
        counter = 0
        blockCommentFlag = False

        commentUsrInpt = input("Do you want to exclude comments? (y/n)  ")
        emptyUsrInpt = input("Do you want to exclude empty lines? (y/n)  ")
        importUsrInpt = input("Do you want to exclude import statements? (y/n)  ")
        print("\n")

        python_file = open(file, 'r')
        currentLine = next(python_file)

        while currentLine:
            linesOfCode += 1

            # finding single comments
            if commentUsrInpt == "y" and currentLine.find("#") != -1:
                linesOfCode -= 1

            # finding block comments
            if commentUsrInpt == "y" and currentLine.find('"""') != -1:

                if blockCommentFlag == False:
                    blockCommentFlag = True

                else:
                    blockCommentFlag = False

                if currentLine.find('"""') == 4:
                   blockCommentFlag = False
                   counter += 1

            if blockCommentFlag == True and currentLine != "\n":
                counter += 1

            # finding empty lines
            if emptyUsrInpt == "y":
                if currentLine in ["\n", "\r\n"]:
                    linesOfCode -= 1

            # finding imports
            if importUsrInpt == "y" and currentLine.find("import") != -1 and linesOfCode < 20:
                    linesOfCode -= 1

            currentLine = next(python_file, None)
        linesOfCode = linesOfCode - counter
        print("--Total Number of Lines--\n")
        print(linesOfCode)
        print("\n")

    def lcom4(self, file):

        python_file = open(file, 'r')
        tree = ast.parse(python_file.read())

        print("\n------ LCOM -------\n")

        myDict = {}
        attributeList = []

        # Walks through the tree
        for n in ast.walk(tree):

            # Finds the Classes
            if isinstance(n, ast.ClassDef):
                myDict[n.name] = {}

                # Finds the Defs
                for x in n.body:

                    if isinstance(x, ast.FunctionDef):
                        if x.name != "__init__":
                            myDict[n.name][x.name] = []

                        # Finds the attributes
                        for y in x.body:
                            findAttribute = AttributeFinder()
                            findAttribute.visit(y)
                            temp = findAttribute.getAttribute

                            # No empty attr
                            if temp != "" and x.name != "__init__":
                                myDict[n.name][x.name].append(findAttribute.getAttribute)
        print(myDict)

        # Find LCOM
        lcom = 0
        attributesFound = []

        for x in myDict:
            defNames = myDict.get(x)

            if defNames != {}:

                for y in defNames:
                    values = defNames.get(y)
                    # if
                    attributesFound.append(values)
                    lcom += 1
                    print(attributesFound)
                    # print(values)
            else:
                print(x, " = ", 0)



    def cbo(self, file):

        python_file = open(file, 'r')
        tree = ast.parse(python_file.read())

        print("\n ------CBO------\n")

        classNames = []
        defNames = []

        for n in ast.walk(tree):

            # Finds the Classes
            if isinstance(n, ast.ClassDef):
                classNames.append(n.name)

            # Finds Def
            if isinstance(n, ast.FunctionDef):
                if n.name != "__init__":
                    defNames.append(n.name)

            # Find a Class in the Def
            if isinstance(n, ast.Name):
                print(n.id)

        print(classNames)



    def dit(self, file):

        python_file = open(file, 'r')
        currentLine = next(python_file)

        objectUsrInpt = input("Do you want to include the object? (y/n)   ")

        print("\n-----Depth of Inheritance Tree-----\n")

        # Arrays for counting
        classNames = []
        noDitNames = []

        # Depth Variables
        ditCount = 0

        while currentLine:

            # Remove the Blanks
            removedBlanks = currentLine.strip()

            # Finds the Class
            if removedBlanks.startswith("class"):

                # Gets info inside parenthesis
                location = 0
                for n in removedBlanks:
                    location += 1
                    if n == "(":
                        currentPosition = location
                        if removedBlanks[currentPosition:currentPosition + 1] != ")":
                            # print(removedBlanks)
                            classNames.append(removedBlanks)
                        else:
                            noDitNames.append(removedBlanks[:currentPosition - 1])

                if removedBlanks.find("(") == -1:
                    noDitNames.append(removedBlanks)

            currentLine = next(python_file, None)

        # Find the Depth
        print(classNames)
        for c in classNames:
            ditCount += 1

            # Object Constructor
            if c.find("object") != -1:
                ditCount += 1

                # Removes Object if user does not want
                if objectUsrInpt == "n":
                    ditCount -= 1

            print(c[6:], " ", ditCount)
            ditCount = 0

        # No DIT Functions
        for y in noDitNames:
            print(y[6:], " ", "0")

    def noc(self, file):

        python_file = open(file, 'r')
        currentLine = next(python_file)

        print("\n-----Number of Children-----\n")

        # Arrays for counting
        classNames = []
        parenthesisNames = []
        tempArray = []

        # Class Names
        classCounter = 0
        classFirstPara = 0
        temp = 0

        # Inside parenthesis variables
        testCounter = 0
        firstPara = 0
        lastPara = 0

        while currentLine:

            # Remove the Blanks
            removedBlanks = currentLine.strip()

            # Finds the Class
            if removedBlanks.startswith("class"):

                # Gets class info
                for n in removedBlanks:

                    classCounter += 1

                    if removedBlanks.find("(") == -1:
                        if n == ":":
                            classFirstPara = classCounter - 1

                    if n == "(":
                        classFirstPara = classCounter - 1

                classCounter = 0
                classInfo = removedBlanks[6:classFirstPara]

                if classInfo.strip() != "":
                    classNames.append(classInfo)

                # Gets info inside parenthesis
                for n in removedBlanks:
                    testCounter += 1

                    if n == "(":
                        firstPara = testCounter

                    if n == ")":
                        lastPara = testCounter - 1

                testCounter = 0
                paraInfo = removedBlanks[firstPara:lastPara]
                if paraInfo.strip() != "":
                    parenthesisNames.append(paraInfo)

            currentLine = next(python_file, None)

        # Counts the children
        tempCounter = 0
        for c in parenthesisNames:
            tempCounter += 1
            if parenthesisNames.count(c) > 0 and c != "object":
                name = c
                number = parenthesisNames.count(c)
                tempArray.append(name)
                print(name, " ", number)

        for q in classNames:
            if tempArray.count(q) > 0:
                temp += 1
            else:
                print(q, " 0")

    def wmc(self, file):

        methodCounter = 0
        printCounter = 0

        python_file = open(file, 'r')
        currentLine = next(python_file)

        print("\n")
        constructorUsrInpt = input("Do you want to include the constructor? (y/n)   ")
        print("\n--Weighted Methods per Class--\n")

        while currentLine:

            # Remove the blanks
            removedBlanks = currentLine.strip()

            # Finds the Class
            if removedBlanks.startswith("class"):

                # Gets rid of the __init__
                if constructorUsrInpt == "n":
                    methodCounter -= 1
                if printCounter > 0:
                    print("Number of Methods: ", methodCounter, "\n ----------")

                print(currentLine[6:])
                methodCounter = 0
                printCounter += 1

            # Finds the number of def
            if removedBlanks.startswith("def "):
                methodCounter += 1

            currentLine = next(python_file, None)
        if constructorUsrInpt == "n":
            methodCounter -= 1
        print("Number of Methods: ", methodCounter, "\n ---------- ")

class AttributeFinder(ast.NodeVisitor):

    def __init__(self):
        self.getAttribute = ""

    def visit_Attribute(self, currentNode):
        self.getAttribute = currentNode.attr



f = FinalProject693()

filesList = []
fileToLoad = input("What is the name of the file(s) you would like to use?  Please separate them by a space. ")
filesList.append(fileToLoad.split())

for x in filesList:
    for y in x:
        print("\n--------", y, "--------\n")
        # f.getlinesofcode(y)
        # f.lcom4(y)
        # f.cbo(y)
        f.dit(y)
        # f.noc(y)
        # f.wmc(y)
