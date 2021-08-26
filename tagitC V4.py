import tkinter as tk
from tkinter import ttk
from tkinter import *
import re
import os
import os.path
import getpass


window = ttk
window = tk.Tk()
window.title("TAG 'IT'")
window.iconbitmap("C:\pysearchtool\Tagit_tagicon.ico")
window.minsize(400, 100)


# search module
def searchcmd():
    if var1.get() == ("on"):
        searchbox = textbox1.get("1.0", "end").strip()
        if bool(searchbox) == 1:
            searchbox = textbox1.get("1.0", "end").strip()
            if bool(searchbox) == 1:
                username = getpass.getuser()
                filename = username + ".Tag"
                # Path instr file
                cpath = "C:\\SearchTool\\Application\\"
                path = cpath + filename
                searchbox = textbox1.get("1.0", "end").strip()
                splsearcbox = searchbox.split()
                file = open(path, "r")
                if var3.get() == 0:
                    result.delete("0.0", "end")
                    username = getpass.getuser()
                    filename = username + "temp.Tag"
                    # Path instr file
                    cpath = "C:\\SearchTool\\Application\\"
                    path = cpath + filename
                    outFileName = path
                    outFile = open(outFileName, "w")
                    outFile.write("")
                    outFile.close()
                for word in file:

                    for x in splsearcbox:
                        pattern = x
                        if bool(re.search(pattern, word)) == True:
                            saving = word

                        else:
                            saving = ""
                            break
                    # opeaning resultbox and print result

                    else:

                        if bool(saving) == True:
                            editresul.grid(column=0, row=5)
                            result.grid(row=6, columnspan=2)
                            if var3.get() == 0:
                                result.insert("0.0", word)
                                username = getpass.getuser()
                                filename = username + "temp.Tag"
                                # Path instr file
                                cpath = "C:\\SearchTool\\Application\\"
                                path = cpath + filename
                                outFileName = path
                                outFile = open(outFileName, "a")
                                outFile.write(word)
                                outFile.close()
                            else:
                                return word



        else:
            result.delete("0.0", "end")
            result.grid_forget()
            editresul.grid_forget()

    else:
        searchbox = textbox1.get("1.0", "end").strip()
        if bool(searchbox) == 1:
            searchbox = textbox1.get("1.0", "end").strip()
            if bool(searchbox) == 1:
                username = getpass.getuser()
                filename = username + ".Tag"
                # Path instr file
                cpath = "C:\\SearchTool\\Documents\\"
                path = cpath + filename
                searchbox = textbox1.get("1.0", "end").strip()
                splsearcbox = searchbox.split()
                file = open(path, "r")
                if var3.get() == 0:
                    result.delete("0.0", "end")
                    username = getpass.getuser()
                    filename = username + "temp.Tag"
                    # Path instr file
                    cpath = "C:\\SearchTool\\Documents\\"
                    path = cpath + filename
                    outFileName = path
                    outFile = open(outFileName, "w")
                    outFile.write("")
                    outFile.close()
                for word in file:

                    for x in splsearcbox:
                        pattern = x
                        if bool(re.search(pattern, word)) == True:
                            saving = word

                        else:
                            saving = ""
                            break
                    # opeaning resultbox and print result

                    else:

                        if bool(saving) == True:
                            editresul.grid(column=0, row=5)
                            result.grid(row=6, columnspan=2)
                            if var3.get() == 0:
                                result.insert("0.0", word)
                                username = getpass.getuser()
                                filename = username + "temp.Tag"
                                # Path instr file
                                cpath = "C:\\SearchTool\\Documents\\"
                                path = cpath + filename
                                outFileName = path
                                outFile = open(outFileName, "a")
                                outFile.write(word)
                                outFile.close()
                            else:
                                return word



        else:
            result.delete("0.0", "end")
            result.grid_forget()
            editresul.grid_forget()


def editresult():
    word = searchcmd()
    edittext = result.get("1.0", "end").strip()
    string = word
    editedtext = string.replace(word, edittext)
    print("Edited text is ", editedtext)

    username = getpass.getuser()
    filename = username + "temp.Tag"
    # Path instr file
    cpath = "C:\\SearchTool\\Documents\\"
    path = cpath + filename
    outFileName = path
    with open(outFileName, "r") as refi:
        resultline = refi.readlines()
        print(resultline)

    # calling reult from above function

    # geting the edited text from thew edited text box.

    # replasing the old tag that have been edited
    username = getpass.getuser()

    filename = username + ".Tag"
    # Path
    cpath = "C:\\SearchTool\\Documents\\"
    instrpath = cpath + filename
    with open(instrpath, "r") as f:
        lines = f.readlines()
        for x in resultline:
            lines.remove(x)
        f.close()
        with  open(instrpath, "w") as new_f:  # append mode
            for line in lines:
                new_f.write(line)
            new_f.close()
            string1 = editedtext + "\n"
            # opening a text file
            file1 = open(instrpath, "r")

            # read file content
            readfile = file1.read()

            # checking condition for string found or not
            if string1 in readfile:
                print('String', string1, 'Found In File')
                new_f.close()
                result.delete("0.0", "end")
            else:
                with open(instrpath, "a") as new_g:
                    new_g.write(editedtext)
                    new_g.write("\n")
                    new_g.close()
                result.delete("0.0", "end")
                result.grid_forget()
                saveedit.grid_forget()


def editApplication():
    word = searchcmd()
    edittext = result.get("1.0", "end").strip()
    string = word
    editedtext = string.replace(word, edittext)
    print("Edited text is ", editedtext)

    username = getpass.getuser()
    filename = username + "temp.Tag"
    # Path instr file
    cpath = "C:\\SearchTool\\Application\\"
    path = cpath + filename
    outFileName = path
    with open(outFileName, "r") as refi:
        resultline = refi.readlines()
        print(resultline)

    # calling reult from above function

    # geting the edited text from thew edited text box.

    # replasing the old tag that have been edited
    username = getpass.getuser()

    filename = username + ".Tag"
    # Path
    cpath = "C:\\SearchTool\\Application\\"
    instrpath = cpath + filename
    with open(instrpath, "r") as f:
        lines = f.readlines()
        for x in resultline:
            lines.remove(x)
        f.close()
        with  open(instrpath, "w") as new_f:  # append mode
            for line in lines:
                new_f.write(line)
            new_f.close()
            string1 = editedtext + "\n"
            # opening a text file
            file1 = open(instrpath, "r")

            # read file content
            readfile = file1.read()

            # checking condition for string found or not
            if string1 in readfile:
                print('String', string1, 'Found In File')
                new_f.close()
                result.delete("0.0", "end")
            else:
                with open(instrpath, "a") as new_g:
                    new_g.write(editedtext)
                    new_g.write("\n")
                    new_g.close()
                result.delete("0.0", "end")
                result.grid_forget()
                saveedit.grid_forget()


def showwidget():
    if var.get() == ("on"):
        textbox2.grid(column=1, row=3)
        Addbutton.grid(column=0, row=5)
        textout = textbox2.get("1.0", "end")
        exicute.grid_forget()
        print(textout)


    elif var.get() == ("off"):
        textbox2.grid_forget()
        Addbutton.grid_forget()
        result.grid_forget()
        exicute.grid(column=0, row=4)


def exewidget():
    if var1.get() == ("on"):

        Add.grid_forget()
        Addtool.grid(column=0, row=3)
    elif var1.get() == ("off"):
        Addtool.grid_forget()
        Add.grid(column=0, row=3)


def Addtoolswidgetshow():
    if var2.get() == ("on"):
        textbox2.grid(column=1, row=3)
        exicute.grid_forget()
        Addtoolbutton.grid(column=0, row=4)
    elif var2.get() == ("off"):
        textbox2.grid_forget()
        Addtoolbutton.grid_forget()
        exicute.grid(column=0, row=4)


# add modulle
def fileexist():
    # check for pathexist
    path: str = 'C:\SearchTool\Documents'
    # Check whether the
    # specified path is an
    # existing directory or not
    isdir = os.path.isdir(path)
    print("path found", isdir)
    if bool(isdir) == 0:
        # findsearchtool folder avail
        path: str = 'C:\SearchTool'
        isdir = os.path.isdir(path)
        print("searchtool available")
        if bool(isdir) == 1:
            directory2 = "Documents"
            parent_dir2 = "C:\\SearchTool\\"
            pathdir2 = os.path.join(parent_dir2, directory2)
            os.mkdir(pathdir2)
        else:
            # Directory check
            parent_dir = "C:\\"
            directory = "SearchTool"
            pathdir = os.path.join(parent_dir, directory)
            os.mkdir(pathdir)
            # make Documents directory
            directory2 = "Documents"
            parent_dir2 = "C:\\SearchTool\\"
            pathdir2 = os.path.join(parent_dir2, directory2)
            os.mkdir(pathdir2)
            print("no directory found")
            # make Application directory
            directory3 = "Application"
            parent_dir3 = "C:\\SearchTool\\"
            pathdir3 = os.path.join(parent_dir3, directory3)
            os.mkdir(pathdir3)

    # to create file
    username = getpass.getuser()
    filename = username + ".Tag"
    # Path instr file
    cpath = "C:\\SearchTool\\Documents\\"
    path = cpath + filename
    # Check whether the
    # specified path is an
    # existing directory or not
    isFile = os.path.isfile(path)
    print("File found", isFile)
    if bool(isFile) == 0:
        outFileName = path
        outFile = open(outFileName, "a")
        outFile.close()
        print("filecreated")
    # add tag to search
    # check for string exist
    addbox = textbox2.get("1.0", "end").strip()
    searchbox = textbox1.get("1.0", "end").strip()
    instr = (searchbox + "@@" + addbox)
    username = getpass.getuser()
    filename = username + ".Tag"
    # Path
    cpath = "C:\\SearchTool\\Documents\\"
    instrpath = cpath + filename

    string1 = instr
    # opening a text file
    file1 = open(instrpath, "r")

    # read file content
    readfile = file1.read()

    # checking condition for string found or not
    if string1 in readfile:
        print('String', string1, 'Found In File')
    else:
        file1 = open(instrpath, "a")  # append mode
        file1.write(instr)
        file1.write("\n")
        file1.close()
        textbox2.delete("1.0", "end")
        textbox1.delete("1.0", "end")
        print('search', string1, 'added')


# to make application folder
def application():
    # check for pathexist
    path: str = 'C:\SearchTool\Application'
    # Check whether the
    # specified path is an
    # existing directory or not
    isdir = os.path.isdir(path)
    print("path found", isdir)
    if bool(isdir) == 0:
        # findsearchtool folder avail
        path: str = 'C:\SearchTool'
        isdir = os.path.isdir(path)
        print("searchtool available")
        if bool(isdir) == 1:
            directory2 = "Application"
            parent_dir2 = "C:\\SearchTool\\"
            pathdir2 = os.path.join(parent_dir2, directory2)
            os.mkdir(pathdir2)
        else:
            # Directory check
            parent_dir = "C:\\"
            directory = "SearchTool"
            pathdir = os.path.join(parent_dir, directory)
            os.mkdir(pathdir)

            # make Application directory
            directory3 = "Application"
            parent_dir3 = "C:\\SearchTool\\"
            pathdir3 = os.path.join(parent_dir3, directory3)
            os.mkdir(pathdir3)

    # to create Application file
    username = getpass.getuser()
    filename = username + ".Tag"
    # Path instr file
    cpath = "C:\\SearchTool\\Application\\"
    path = cpath + filename
    # Check whether the
    # specified path is an
    # existing directory or not
    isFile = os.path.isfile(path)
    print("File found", isFile)
    if bool(isFile) == 0:
        outFileName = path
        outFile = open(outFileName, "a")
        outFile.close()
        print("filecreated")
    # add tag to search
    # check for string exist
    addbox = textbox2.get("1.0", "end").strip()
    searchbox = textbox1.get("1.0", "end").strip()
    instr = (searchbox + "@@" + addbox)
    username = getpass.getuser()
    filename = username + ".Tag"
    # Path
    cpath = "C:\\SearchTool\\Application\\"
    instrpath = cpath + filename

    string1 = instr
    # opening a text file
    file1 = open(instrpath, "r")

    # read file content
    readfile = file1.read()

    # checking condition for string found or not
    if string1 in readfile:
        print('String', string1, 'Found In File')
    else:
        file1 = open(instrpath, "a")  # append mode
        file1.write(instr)
        file1.write("\n")
        file1.close()
        textbox2.delete("1.0", "end")
        textbox1.delete("1.0", "end")
        print('search', string1, 'added')


def saveedited():
    if var3.get() == 1:
        if var1.get() == "on":
            saveedittool.grid(column=1, row=5)
        else:
            saveedit.grid(column=1, row=5)
    else:
        saveedit.grid_forget()
        saveedittool.grid_forget()
        result.delete("0.0", "end")
        result.grid_forget()


# GUI section
# Heading label
label1hed = ttk.Label(window, text="Enter your TAG ")
label1hed.grid(column=0, row=1)

# search button
sbutton = ttk.Button(window, text="Search", command=searchcmd)
sbutton.grid(column=0, row=2)

# Tag search
textbox1 = tk.Text(window, height=1, width=40, font="Timezones")
textbox1.grid(column=1, row=2)

# Add Tag
var: tk.StringVar = tk.StringVar()
Add = ttk.Checkbutton(window, text="AddTag", variable=var, onvalue="on", offvalue="off", command=showwidget)
Add.grid(column=0, row=3)

# exicute
var1: tk.StringVar = tk.StringVar()
exicute = ttk.Checkbutton(window, text="Execute", variable=var1, onvalue="on", offvalue="off", command=exewidget)
exicute.grid(column=0, row=4)

# Add tool
var2: tk.StringVar = tk.StringVar()
Addtool = ttk.Checkbutton(window, text="AddTool", variable=var2, onvalue="on", offvalue="off",
                          command=Addtoolswidgetshow)
# editwidget
var3: tk.StringVar = tk.IntVar()
editresul = ttk.Checkbutton(window, text="  Edit    ", variable=var3, onvalue=1, offvalue=0,
                            command=saveedited)

# Add textbox
textbox2 = tk.Text(window, height=1, width=40, font="timezones")
textbox2.grid(column=1, row=3)
textbox2.grid_forget()

# saveTagButton
Addbutton = ttk.Button(window, text="ADD", command=fileexist)
Addbutton.grid_forget()

# show results
result = tk.Text(window, height=10, width=50, font="Timezones", wrap=WORD)

# Addtoolbutton
Addtoolbutton = ttk.Button(window, text="Add", command=application)

# edit button
edditbutton = ttk.Button(window, text="Edit")

# saveedit  button
saveedit = ttk.Button(window, text="Save", command=editresult)

# save edit applicartion
saveedittool = ttk.Button(window, text="savetool", command=editApplication)

window.mainloop()
