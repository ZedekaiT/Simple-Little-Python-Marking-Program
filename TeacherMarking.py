#For Mum 
#Zedekai Thorpe
#z@zedekai.com
from pathlib import Path
#Opens the relative paths
parent = Path(__file__).resolve().parent
markingConfig = str(parent) + "\MarkingConfig.txt"
resultsWrite =  str(parent) + "\YOUR_RESULTS.txt"

#main program loop
while True:
    print("(LEAVE BLANK IF DESIRED)")
    studentName = str(input("Student Name: "))
    print("\n")

    f = open(markingConfig, "r")
    lines = f.readlines()
    lineCount = 0
    chosenOptionsList = []
    script = ""

    for line in lines:
        if "SCRIPT" in line:
            for line in lines[lineCount + 1:]:
                if line.strip(): #If line not empty
                    script = script + line
                else:            #Breaks at an empty line
                    break
        
        if "OPTION" in line:
            print(line)
            currentLoopList = []
            count = 1
            for line in lines[lineCount + 1:]:
                if line.strip():
                    print(str(count) + ".", line) #Prints the counting list numbers (1., 2., 3. ...)
                    currentLoopList.append(line)
                    count +=1
                else:
                    print("\n")
                    break
            
            #Asks for input, checks if valid, appends chosen option
            while True:
                try:
                    chosenOption = int(input("Input Option's Number: "))
                    if chosenOption > count-1:
                        raise ValueError
                    else:
                        chosenOptionsList.append(currentLoopList[chosenOption-1])
                        print("\n")
                        break
                except ValueError:
                    print("Oops! That was not a valid number. Please try again...")

        lineCount += 1
    
    script = script.replace("(studentName)", studentName)

    for i in range(1, len(chosenOptionsList)+1):
        optionString = "(opt" + str(i) + ")"
        script = script.replace(optionString, chosenOptionsList[i-1])
        script = script.replace("\n", "")
    print("\n")
    print("RESULTS:")
    print(script)
    print("\n")
    f.close()
    f = open(resultsWrite, "a+")
    f.write(script)
    f.write("\n \n")
    f.close()

    #Asks whether to run again.
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            print("\n")
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
print("WARNING: This window will now close.\nPlease ensure your results have been saved.")
input("PRESS ENTER TO CLOSE WINDOW")
