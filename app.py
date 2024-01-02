import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from source import generateUsername, generatePassword, exportToFile
import random
import string
import os

accountNameValidated = ''
username = ''
password = ''
finalresult = ''

def accNameInputValidation(user_input):
    print("\ncalled> accNameInputValidation")
    print(f"\n{user_input} - {type(user_input)}")
    illegalFileNameChars = ['#', '%', '&', '{', '}', '\\', '<', '>', '*', '?', '/', ' ', '$', '!', '\'', "\"", ':', '@', '+', '`', '|', '=']
    illegalCharsStr = ''.join(illegalFileNameChars)
    result = 0
    if (type(user_input) != str):
        print(f"\nError in input type")
    elif (len(user_input) <= 0):
        print(f"\nEmpty input")
    else:
        for i in range(len(illegalCharsStr)):
            if (illegalCharsStr[i] in user_input):
                user_input = user_input.replace(illegalCharsStr[i], '-')
        result = 1
    print(f"\n> Validation complete {user_input}")
    return [result, user_input]

def handleAccNameEnter(txt):
    pass

def generateButtonAction():
    resultText['state'] = 'normal'
    print("\ncalled> generateButtonAction")
    accNameTemp = accNameVar.get()
    print(f"\n{accNameTemp} - {type(accNameTemp)}")
    tempResult = accNameInputValidation(accNameTemp)
    print(f"\n{tempResult}")
    if (tempResult[0] == 1):
        account_var.set(tempResult[1])
        username = generateUsername()
        username_var.set(username)
        password = generatePassword()
        password_var.set(password)
        finalresult = f"Account/Website: {tempResult[1]}\nUsername: {username}\nPassword: {password}"
        resultText.insert('1.0', finalresult)
        print(f"\n > {tempResult[1]}")
        resultText['state'] = 'disabled'
    elif (tempResult[0] == 0):
        accountNameValidated = "blank" + str(random.randint(0, 9999))
        account_var.set(accountNameValidated)
        username = generateUsername()
        username_var.set(username)
        password = generatePassword()
        password_var.set(password)
        finalresult = f"Account/Website {accountNameValidated}\nUsername: {username}\nPassword: {password}"
        resultText.insert('1.0', finalresult)
        resultText['state'] = 'disabled'
    else:
        print(f"\nError in generateButtonFunction")


def exportEntryCommand():
    try:
        resultText['state'] = 'normal'
        resulttextcontent = resultText.get("1.0","end-1c")
        if (len(resulttextcontent) <= 0):
            print("EMPTY")
            showerror("Empty entry", "Please generate entry first.")
            resultText['state'] = 'disabled'
            raise Exception
        else:
            print("Exporting...")
            exportToFile(password_var.get(), account_var.get(), username_var.get())
            clear()
    except Exception:
        print("Exception")


def clear():
    resultText['state'] = 'normal'
    accNameTextEntry.delete(0, tk.END)
    resultText.delete('1.0', tk.END)
    account_var.set('')
    username_var.set('')
    password_var.set('')
    resultText['state'] = 'disabled'


root = tk.Tk()
root.title("quickPassGenerator")
root.geometry('400x550+300+100')
root.resizable(False, False)

account_var = tk.StringVar()
username_var = tk.StringVar()
password_var = tk.StringVar()

menuBar = tk.Menu(root)
root.config(menu=menuBar)

file_menu = tk.Menu(menuBar, tearoff=False)
file_menu.add_command(label="Exit", command=root.destroy)

help_menu = tk.Menu(menuBar, tearoff=False)
help_menu.add_command(label="About", command=lambda: showinfo(
    title="About this program.",
    message="This tiny tool quickly generates and exports a random username and password for you. Please only use it for unimportant and non-essential accounts. Developed by Ark948. Entire source code is available on github."
))

menuBar.add_cascade(label="File", menu=file_menu, underline=0)
menuBar.add_cascade(label="Help", menu=help_menu, underline=0)

accNameLabel = ttk.Label(root, text="Account Name/Website:", font=("", 10, "bold"))
accNameLabel.place(x=20, y=18)
accNameLabelInfo01 = ttk.Label(root, text="Example: someWebsite.com", font=("", 8))
accNameLabelInfo01.place(x=20, y=42)
accNameLabelInfo02 = ttk.Label(root, text="(Leave blank to generate randomly)", font=("", 8))
accNameLabelInfo02.place(x=20, y=62)

accNameVar = tk.StringVar()
accNameTextEntry = ttk.Entry(root, width=50, foreground='black', textvariable=accNameVar)
accNameTextEntry.place(x=45, y=92)

generateButton = ttk.Button(root, text="Geneate", width=20, command=generateButtonAction)
generateButton.place(x=135, y=140)

resultLabel = ttk.Label(root, text="Generated result: ", font=("", 10, "bold"))
resultLabel.place(x=20, y=180)

resultText = tk.Text(root, height=7, width=33, font=("Consolas", 12))
resultText.place(x=45, y=220)
resultText['state'] = 'disabled'

exportEntryButton = ttk.Button(root, text="Export (txt)", width=20, command=exportEntryCommand)
exportEntryButton.place(x=45, y=380)

exportEntryInfo = ttk.Label(root, text="(Exported text file will be right next to program file.)")
exportEntryInfo.place(x=45, y=420)

exportResultInfo = ttk.Label(root)

clearEverythingButton = ttk.Button(root, text="Clear", width=20, command=clear)
clearEverythingButton.place(x=220, y=380)

exitButton = ttk.Button(root, text="Exit", width=20, command=root.destroy)
exitButton.place(x=135, y=480)

def main(root):
    root.mainloop()
    

if __name__ == "__main__":
    main(root)