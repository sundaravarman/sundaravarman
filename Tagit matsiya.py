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
def searchcmd(*event):
    y = 0
    if var1.get() == ("on"):
        searchbox = textbox1.get("1.0", "end").strip()
        textbox1.delete("0.0", "end")
        textbox1.insert("0.0", searchbox)
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

                        if bool(saving):
                            editresul.grid(column=0, row=5)
                            result.grid(row=6, columnspan=2)
                            scrollbar.grid(column=3, row=6, rowspan=6, sticky='ns')
                            if var3.get() == 0:
                                string = word
                                new_string = string.split("@@", 1)[1]
                                # result.insert("0.0", new_string)
                                username = getpass.getuser()
                                filename = username + "temp.Tag"

                                # Path instr file
                                cpath = "C:\\SearchTool\\Application\\"
                                path = cpath + filename
                                outFileName = path
                                outFile = open(outFileName, "a")
                                outFile.write(word)
                                outFile.close()

                                y = y + 1
                                print(y)
                                taging = '"' + "tag" + str(y) + '"'
                                print(taging)
                                if taging == '"tag1"':

                                    result.tag_config("tag1", foreground="blue", font="Timezones")
                                    result.tag_bind("tag1", "<Button-1>", lambda e: callback(e, "tag1"))
                                    result.insert(END, new_string, taging)

                                elif taging == '"tag2"':
                                    result.tag_config("tag2", foreground="blue", font="timezones")
                                    result.tag_bind("tag2", "<Button-1>", lambda e: callback(e, "tag2"))
                                    result.insert(END, new_string, "tag2")
                                elif taging == '"tag3"':

                                    result.tag_config("tag3", foreground="blue", font="timezones")
                                    result.tag_bind("tag3", "<Button-1>", lambda e: callback(e, "tag3"))
                                    result.insert(END, new_string, "tag3")
                                elif taging == '"tag4"':
                                    result.tag_config("tag4", foreground="blue", font="timezones")
                                    result.tag_bind("tag4", "<Button-1>", lambda e: callback(e, "tag4"))
                                    result.insert(END, new_string, "tag4")
                                elif taging == '"tag5"':
                                    result.tag_config("tag5", foreground="blue", font="timezones")
                                    result.tag_bind("tag5", "<Button-1>", lambda e: callback(e, "tag5"))
                                    result.insert(END, new_string, "tag5")
                                elif taging == '"tag6"':
                                    result.tag_config("tag6", foreground="blue", font="timezones")
                                    result.tag_bind("tag6", "<Button-1>", lambda e: callback(e, "tag6"))
                                    result.insert(END, new_string, "tag6")
                                elif taging == '"tag7"':
                                    result.tag_config("tag7", foreground="blue", font="timezones")
                                    result.tag_bind("tag7", "<Button-1>", lambda e: callback(e, "tag7"))
                                    result.insert(END, new_string, "tag7")
                                elif taging == '"tag8"':
                                    result.tag_config("tag8", foreground="blue", font="timezones")
                                    result.tag_bind("tag8", "<Button-1>", lambda e: callback(e, "tag8"))
                                    result.insert(END, new_string, "tag8")
                                elif taging == '"tag9"':
                                    result.tag_config("tag9", foreground="blue", font="timezones")
                                    result.tag_bind("tag9", "<Button-1>", lambda e: callback(e, "tag9"))
                                    result.insert(END, new_string, "tag9")
                                elif taging == '"tag10"':
                                    result.tag_config("tag10", foreground="blue", font="timezones")
                                    result.tag_bind("tag10", "<Button-1>", lambda e: callback(e, "tag10"))
                                    result.insert(END, new_string, "tag10")
                                elif taging == '"tag11"':
                                    result.tag_config("tag11", foreground="blue", font="timezones")
                                    result.tag_bind("tag11", "<Button-1>", lambda e: callback(e, "tag11"))
                                    result.insert(END, new_string, "tag11")
                                elif taging == '"tag12"':
                                    result.tag_config("tag12", foreground="blue", font="timezones")
                                    result.tag_bind("tag12", "<Button-1>", lambda e: callback(e, "tag12"))
                                    result.insert(END, new_string, "tag12")
                                elif taging == '"tag13"':
                                    result.tag_config("tag13", foreground="blue", font="timezones")
                                    result.tag_bind("tag13", "<Button-1>", lambda e: callback(e, "tag13"))
                                    result.insert(END, new_string, "tag13")
                                elif taging == '"tag14"':
                                    result.tag_config("tag14", foreground="blue", font="timezones")
                                    result.tag_bind("tag14", "<Button-1>", lambda e: callback(e, "tag14"))
                                    result.insert(END, new_string, "tag14")
                                elif taging == '"tag15"':
                                    result.tag_config("tag15", foreground="blue", font="timezones")
                                    result.tag_bind("tag15", "<Button-1>", lambda e: callback(e, "tag15"))
                                    result.insert(END, new_string, "tag15")
                                elif taging == '"tag16"':
                                    result.tag_config("tag16", foreground="blue", font="timezones")
                                    result.tag_bind("tag16", "<Button-1>", lambda e: callback(e, "tag16"))
                                    result.insert(END, new_string, "tag16")
                                elif taging == '"tag17"':
                                    result.tag_config("tag17", foreground="blue", font="timezones")
                                    result.tag_bind("tag17", "<Button-1>", lambda e: callback(e, "tag17"))
                                    result.insert(END, new_string, "tag17")
                                elif taging == '"tag18"':
                                    result.tag_config("tag18", foreground="blue", font="timezones")
                                    result.tag_bind("tag18", "<Button-1>", lambda e: callback(e, "tag18"))
                                    result.insert(END, new_string, "tag18")
                                elif taging == '"tag19"':
                                    result.tag_config("tag19", foreground="blue", font="timezones")
                                    result.tag_bind("tag19", "<Button-1>", lambda e: callback(e, "tag19"))
                                    result.insert(END, new_string, "tag19")
                                elif taging == '"tag20"':
                                    result.tag_config("tag20", foreground="blue", font="timezones")
                                    result.tag_bind("tag20", "<Button-1>", lambda e: callback(e, "tag20"))
                                    result.insert(END, new_string, "tag20")
                                elif taging == '"tag21"':
                                    result.tag_config("tag21", foreground="blue", font="timezones")
                                    result.tag_bind("tag21", "<Button-1>", lambda e: callback(e, "tag21"))
                                    result.insert(END, new_string, "tag21")
                                elif taging == '"tag22"':
                                    result.tag_config("tag22", foreground="blue", font="timezones")
                                    result.tag_bind("tag22", "<Button-1>", lambda e: callback(e, "tag22"))
                                    result.insert(END, new_string, "tag22")
                                elif taging == '"tag23"':
                                    result.tag_config("tag23", foreground="blue", font="timezones")
                                    result.tag_bind("tag23", "<Button-1>", lambda e: callback(e, "tag23"))
                                    result.insert(END, new_string, "tag23")
                                elif taging == '"tag24"':
                                    result.tag_config("tag24", foreground="blue", font="timezones")
                                    result.tag_bind("tag24", "<Button-1>", lambda e: callback(e, "tag24"))
                                    result.insert(END, new_string, "tag24")
                                elif taging == '"tag25"':
                                    result.tag_config("tag25", foreground="blue", font="timezones")
                                    result.tag_bind("tag25", "<Button-1>", lambda e: callback(e, "tag25"))
                                    result.insert(END, new_string, "tag25")
                                elif taging == '"tag26"':
                                    result.tag_config("tag26", foreground="blue", font="timezones")
                                    result.tag_bind("tag26", "<Button-1>", lambda e: callback(e, "tag26"))
                                    result.insert(END, new_string, "tag26")
                                elif taging == '"tag27"':
                                    result.tag_config("tag27", foreground="blue", font="timezones")
                                    result.tag_bind("tag27", "<Button-1>", lambda e: callback(e, "tag27"))
                                    result.insert(END, new_string, "tag27")
                                elif taging == '"tag28"':
                                    result.tag_config("tag28", foreground="blue", font="timezones")
                                    result.tag_bind("tag28", "<Button-1>", lambda e: callback(e, "tag28"))
                                    result.insert(END, new_string, "tag28")
                                elif taging == '"tag29"':
                                    result.tag_config("tag29", foreground="blue", font="timezones")
                                    result.tag_bind("tag29", "<Button-1>", lambda e: callback(e, "tag29"))
                                    result.insert(END, new_string, "tag29")
                                elif taging == '"tag30"':
                                    result.tag_config("tag30", foreground="blue", font="timezones")
                                    result.tag_bind("tag30", "<Button-1>", lambda e: callback(e, "tag30"))
                                    result.insert(END, new_string, "tag30")
                                elif taging == '"tag31"':
                                    break


                            else:
                                return word



        else:
            result.delete("0.0", "end")
            result.grid_forget()
            scrollbar.grid_forget()
            editresul.grid_forget()

    else:
        searchbox = textbox1.get("1.0", "end").strip()
        if bool(searchbox) == 1:
            searchbox = textbox1.get("1.0", "end").strip()
            textbox1.delete("0.0", "end")
            textbox1.insert("0.0", searchbox)
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
                            scrollbar.grid(column=3, row=6, rowspan=6, sticky='ns')
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
            scrollbar.grid_forget()
            editresul.grid_forget()


def callback(event, tag):
    value = (event.widget.get('%s.first' % tag, '%s.last' % tag))
    vale = value.strip()
    valesplit = value.split
    print(valesplit)
    pattern = ".templ"
    pattern1 = ".input"

    if bool(re.search(pattern, vale)) == True:
        template = vale
        vale = ('"{}"'.format(vale))
        print(vale)
        file1 = open("MyFile.txt", "w")
        file1.write(vale)
        file1.close()
        labeltemplate.grid(column=1, row=4)
    elif bool(re.search(pattern1, vale)) == True:
        vale=('"{}"'.format(vale))
        input = vale
        print("input")
        with open("MyFile.txt", "r") as refi:
            template = refi.readlines()
            listToStr = ' '.join([str(elem) for elem in template])
            print(listToStr)
            outputname = listToStr.replace(".templ", ".output")
            outputnamewithcolen = ('"{}"'.format(outputname))
        runcommand = 'python "C:\\pysearchtool\\arg_substitute.py" -t ' + listToStr + " " + "-v" + " " + input + " " + "-o" + " "+ outputnamewithcolen
        print(runcommand)
        path = "C:\\pysearchtool\\"
        filename = "runme_dir.bat"
        runpath = path + filename
        file = open(runpath, "w")
        file.write(runcommand)
        file.close()
        labelinput.grid(column=1,row=5)
        runbutton.grid(column=0, row=5)
    else:

        os.startfile(vale)
        labeltemplate.grid_forget()
        labelinput.grid_forget()
        runbutton.grid_forget()
        return vale
def run():
    runtool = ("C:\\pysearchtool\\runme_dir.bat")
    os.startfile(runtool)
    labeltemplate.grid_forget()
    labelinput.grid_forget()
    runbutton.grid_forget()
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
                scrollbar.grid_forget()
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
                scrollbar.grid_forget()
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
        scrollbar.grid_forget()
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
            result.delete("0.0", "end")
            username = getpass.getuser()
            filename = username + "temp.Tag"
            # Path instr file
            cpath = "C:\\SearchTool\\Application\\"
            path = cpath + filename
            outFileName = path
            with open(outFileName, "r") as refi:
                resultline = refi.readlines()
                for x in resultline:
                    result.insert("0.0", x)

        else:
            saveedit.grid(column=1, row=5)
    else:
        saveedit.grid_forget()
        saveedittool.grid_forget()
        result.delete("0.0", "end")
        result.grid_forget()
        scrollbar.grid_forget()


# GUI section
# Heading label
label1hed = ttk.Label(window, text="Enter your TAG ")
label1hed.grid(column=0, row=1)
# template selected label
labeltemplate = ttk.Label(window,text="Template selected")
# Input selection label
labelinput= ttk.Label(window,text="Input selected")
# search button
sbutton = ttk.Button(window, text="Search", command=searchcmd)
sbutton.grid(column=0, row=2)

# Tag search
textbox1 = tk.Text(window, height=1, width=40, font="Timezones")
textbox1.grid(column=1, row=2)
textbox1.focus_set()

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
scrollbar = Scrollbar(window)
result = tk.Text(window, height=10, width=50, font="Timezones", wrap=WORD, yscrollcommand=scrollbar.set)
scrollbar.config(command=result.yview)
# Addtoolbutton
Addtoolbutton = ttk.Button(window, text="Add", command=application)

# edit button
edditbutton = ttk.Button(window, text="Edit")

# saveedit  button
saveedit = ttk.Button(window, text="Save", command=editresult)

# save edit applicartion
saveedittool = ttk.Button(window, text="savetool", command=editApplication)

# Enter button bind
window.bind('<Return>', searchcmd)
# Runbutton
runbutton = ttk.Button(window,text="Run",command=run)





window.mainloop()
