import random
import string
import os

def getWebsiteName():
    accountName = input("\n> Enter website or account name (optional) or 'q/Q' to exit: ")
    return accountName

def generateUsername():
    base = "someUser"
    randomPart = random.randint(0, 9999)
    return base + str(randomPart)


def generatePassword():
    firstSegment = []
    secondSegment = []
    thirdSegment = []
    fourthSegment = []
    for i in range(4):
        firstSegment.append(string.ascii_lowercase[random.randint(0, 25)])
    for i in range(4):
        secondSegment.append(string.ascii_uppercase[random.randint(0, 25)])
    for i in range(4):
        thirdSegment.append(string.digits[random.randint(0, 9)])
    a = "$&()*+,-.:;<=>?@[]^_"
    for i in range(4):
        fourthSegment.append(a[random.randint(0, 19)])
    generatedPass = firstSegment+secondSegment+thirdSegment+fourthSegment
    generatedPass = ''.join(generatedPass)
    return generatedPass

def exportToFile(password ,accName="blank", uname=""):
    result = 0
    currentPath = os.getcwd() + "\\"
    try:
        with open(currentPath+accName+".txt", 'a+') as f:
            f.write("\nUsename: "+ uname + "\n" +"Password: "+ password+"\n")
            result = 1
    except Exception as e:
        print("ExportToFile - ERROR: ", e)
        result = -1 # some error occured
    else:
        f.close()
    return result

def main():
    print("\n\n\t\t*** Quick Password Generator by Ark948 ***")
    print("\nThis tool will quickly generate and export a password entry for you. (as text file)")
    illegalFileNameChars = ['#', '%', '&', '{', '}', '\\', '<', '>', '*', '?', '/', ' ', '$', '!', '\'', "\"", ':', '@', '+', '`', '|', '=']
    illegalCharsStr = ''.join(illegalFileNameChars)
    while (True):
        try:
            try:
                tempAccName = getWebsiteName()
                if (len(tempAccName) == 0):
                    raise Exception
                elif (tempAccName == 'q' or tempAccName == 'Q'):
                    print("\nExiting the program...")
                    break
                elif (tempAccName == ' '):
                    print("\nEmpty space is not allowed.")
                    raise Exception
                elif (tempAccName == '\t'):
                    print("\nTab character is not allowed.")
                    raise Exception
                elif ('\\' in tempAccName):
                    print("\nIllegal character detected.")
                    raise Exception
                else:
                    for i in range(len(illegalCharsStr)):
                        if (illegalCharsStr[i] in tempAccName):
                            tempAccName = tempAccName.replace(illegalCharsStr[i], '-')
                    print("\n Notice: All illegal characters will be replaced with '-' .")
            except Exception as e01:
                print("\n> E01 - A random name will be generated for the file.")
                tempAccName = "blank" + str(random.randint(0, 500))
            try:
                tempUname = generateUsername()
                tempPassword = generatePassword()
                finalResult = []
                finalResult.append(tempAccName)
                finalResult.append(tempUname)
                finalResult.append(tempPassword)
                print("\n", "Entry created: ", "\n")
                print("\t\t", "Account Name/Website: ", finalResult[0], "\n")
                print("\t\t", "Username: ", finalResult[1], "\n")
                print("\t\t", "Password: ", finalResult[2], "\n")
            except Exception as e02:
                print("\n> E02 Error - [Internal Processing Error]")
                break
            try:
                user_answer = input("\n> Export entry to text file? (Y-N): ")
                if (len(user_answer) > 1):
                    raise Exception
                elif (user_answer == 'y' or user_answer == 'Y'):
                    try:
                        exportToFile(tempPassword, tempAccName, tempUname)
                        print("\n Entry successfully created.")
                    except Exception as ExToFi_error:
                        print("\n> Error occured while trying to export text file.")
                elif (user_answer == 'n' or user_answer == 'N'):
                    print("\n Exporting to file cannelled.")
                    continue # skip writing to file, return back to main loop
                elif ('\\' in user_answer):
                    raise Exception
                else:
                    print("\n> Empty input. Writing to file cancelled. Please manually copy your entry.")
                    continue                    
            except Exception as e03:
                print("\n> E03 Error - Incorrect input. Operation cancelled.")
                print("\n Please manually copy your entry.")
                continue # skip this entry
        except Exception as finalError:
            print("\n> Sorry, some unknown error occurred.")


if __name__ == "__main__":
    main()