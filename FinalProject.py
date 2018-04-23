import ast
import itertools

# SampleIncludingAll1.py

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

        # Find LCOM

        # Find the Def Names
        for x in myDict:
            defNames = myDict.get(x)

            # If the names are not Null
            if defNames != {}:

                # Master List, see if things are connected
                l = []
                for key in defNames:  # same as in defName.keys()
                    l.append([key])  # Adding Method names
                    for var in defNames.get(key):
                        l[-1].append(var)  # Finds the values which are variables and/or the method calls

                # Now attach the lists
                # Had to go through the while twice, because it ended with 2 lists when there were the same elements in both lists
                t = 0
                while t < 2:
                    # Take the first element in the list
                    for onedl in l:
                        # Iterate through that element, for each of the names
                        for e in onedl:
                            # Building a list with a range the size of the Master List, because some elements will be removed later (index error)
                            indecies = list(range(len(l)))
                            # Iterating through the Index list
                            for i in indecies:
                                # Checking to see if not the same
                                if l[i] != onedl:
                                    # If the element exists, combine the lists
                                    if e in l[i]:
                                        l[i] += onedl
                                        indecies.pop(-1)
                                        # If there are two of the same elements in a list, it will try to remove that element twice
                                        try:
                                            l.remove(onedl)
                                        except ValueError:
                                            pass
                    t += 1
                # If there is only one value in the list, if yes empty it
                if len(l[0]) < 2:
                    l = []
                print(x, " = ", len(l))
            else:
                print(x, " = ", 0)

    def cbo(self, file):

        python_file = open(file, 'r')
        tree = ast.parse(python_file.read())

        print("\n ------CBO------\n")

        myDict = {}

        # Walks through the tree
        for n in ast.walk(tree):
            # Finds the Classes
            if isinstance(n, ast.ClassDef):
                myDict[n.name] = {}
                # Finds the Defs
                for classTree in ast.walk(n):
                    if isinstance(classTree, ast.FunctionDef):
                        myDict[n.name][classTree.name] = []

                        # Find the Function calls based on the AST Class which is before the name.id in the AST
                        for call in ast.walk(classTree):
                            if isinstance(call, ast.Call):
                                # If a call is found and it is not self, add it to dictionary
                                for func in ast.walk(call):
                                    try:
                                        if func.id != "self":
                                            myDict[n.name][classTree.name].append(func.id)
                                    except AttributeError:
                                        pass

        # Find CBO
        for comb in list(itertools.combinations(myDict, 2)):
            x = comb[0]
            y = comb[1]
            cbo = list(myDict[x].values()).count([y]) + \
                  list(myDict[y].values()).count([x])
            print(x, ' <-> ', y, ' = ', cbo)
        print("\n")

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

fileToLoad = input("What is the name of the file(s) you would like to use?  Please separate them by a space. ")
filesList = fileToLoad.split()

# For Multiple Files
for y in filesList:
    print("\n--------", y, "--------\n")
    f.getlinesofcode(y)
    f.lcom4(y)
    f.cbo(y)
    f.dit(y)
    f.noc(y)
    f.wmc(y)
