# This program is gonna sort files on your desktop and put them in a folder :
# document/picture/software etc...
import os
import re
from os import listdir
from os.path import isfile, join

try:
    # PATH to Desktop location
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
except OSError: #If path to desktop isn't found
    print("Path wasn't found on your pc")
    desktop = input("paste the path to your desktop directory, example: F:\\Users\\username\\Desktop: \n")

# All type of files
audio = [[".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".wav", ".wma", ".wpl", ".ogg"]]
compressed = [[".7z", ".arj", ".pkg", ".rar", ".tar.gz", ".z", ".zip"]]
documents = [[".xml", ".key", ".odp", ".pps", ".ppt", ".pptx", ".xlsx", ".xlsm", ".xls", ".ods",
             ".doc", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd"]]
shortcut = [[".lnk"]]
video = [[".mp4", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mpg", ".rm", ".swf", ".wmv", ".3gp", ".3g2"]]
programming = [[".js", ".html", ".css", ".c", ".cpp", ".class", ".cs", ".h", ".java",
               ".pl", ".sh", ".swift", ".vb", ".php", ".py", ".cfg", ".dll", ".bat", ".apk",  ".sql"]]
pictures = [[".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff", ]]
executable = [[".exe"]]
other = [[".bin", ".iso", ".csv", ".dat", ".dbf", ".db", ".log", ".mdb", ".sav", ".tar"]]

# To display
choice = [["audio", "compressed", "documents", "shortcut", "video", "programming", "pictures", "executable", "other"],
          [audio, compressed, documents, shortcut, video, programming, pictures, executable, other]]

allFiles = [] # All file names found on the user's desktop

# return the index of the type of file the user want more details about
switcher = {
    "audio": 0,
    "compressed": 1,
    "documents": 2,
    "shortcut": 3,
    "video": 4,
    "programming": 5,
    "pictures": 6,
    "executable": 7,
    "other": 8
}

result=  ""
while(1):
    os.system('CLS')
    print("Here are the kind of file that can be sorted: ")
    for type in choice[0]:
        print("------ " + type)
    print('\n')
    argument = input("If you want more details about a type, type it\'s name else press enter: ")
    if len(argument) == 0 :
        break
    else:
        result = "string"

    while(1):
        result = switcher.get(argument, "Invalid choice")
        if isinstance(result, str):
            print( result)
            argument = input('\n' + "which type do you wanna display ? press enter to continue: ")
            if len(argument) == 0:
                break
        else:
            print("\nhere are all the extention of this category: ")
            print(choice[1][result])
            input("\nPress Enter to continue...")



# Find all files on the desktop and put them in an array
for f in listdir(desktop):
    if isfile(join(desktop, f)) and "desktop.ini" not in f :
        allFiles.append(f)

print("\nfile found on your desktop: " + str(len(allFiles)))
if len(allFiles) < 1:
    print("there's no file that can be sorted on your desktop the program will close...")
    input("\nPress Enter to continue...\n")
    os._exit(0)
input("\nPress Enter to continue...\n")
Nocategory = []


for file in allFiles:   # get each file
    found = False
    #Put each file in it's corresponding type
    for type in range(len(choice[1])): # number of types from choice
        for extention in choice[1][type][0]: # get all type of extention
            if extention in file: # check if it correspond to any extention we have
                choice[1][type].append(file)
                found = True
    if found == False:
        Nocategory.append(file) # If the file extention wasn't find

userchoice = []
for x in range(len(choice[1])):
    if len(choice[1][x]) >1:
        userchoice.append(str(x))

while(1):
    os.system('CLS')
    print("Here are the type of file that are going to be sorted from what we found on your desktop: ")
    # Choice of which type of file we want to sort
    for x in range(len(choice[1])):
        if len(choice[1][x]) >1:
            print("------ " + choice[0][x])
    print("\n")

    print(" - If you want to see all files that will be sorted type all")
    print(" - Else if you want to see which files will be sorted in a category, type it's name")
    print(" - If you don't want to sort a category type \"ignore category_name\"") # TODO do the ignore
    print(" - Else press enter")
    argument = input("-> ")
    if "all" in argument:
        print("\n------ ", end ="")
        print(*allFiles, sep=", \n------ ")
    elif len(argument) == 0:
        break
    elif "ignore" in argument:
        toIgnore = argument.split(" ")[1]
        result = switcher.get(toIgnore, "Invalid choice")
        if isinstance(result, str):
            print(result)
        else:
            temp = choice[1][result][0]
            choice[1][result] = []
            choice[1][result].append(temp) #We only keep the extensions and delete files to sort
            userchoice.remove(str(result)) # Remove the index in choice of the folder to create
    else:
        result = switcher.get(argument, "Invalid choice")
        if isinstance(result, str):
            print(result)
        else:
            while(1):
                print("\nFiles: ")
                for x in range(len(userchoice)):
                    if str(result) == userchoice[x]:
                        for y in range(len(choice[1][result])-1):
                            print(str(y+1)+" ------ " + choice[1][result][y+1])

                noSort = input("if you don\'t want a file to be sorted type it\'s number else press enter: ")
                if(len(noSort) == 0):
                    break
                else:
                    try:
                        choice[1][result].pop(int(noSort))
                        if(len(choice[1][result]) < 2):
                            userchoice.remove(str(result)) # Remove the index in choice of the folder to create
                    except IndexError:
                        print("This file doesn't exist")
                    except ValueError:
                        print("Wrong input")

    input("\nPress Enter to continue...\n")


for y in range(len(userchoice)):
    print('\n')
    try:
        path = desktop+"\\"+choice[0][int(userchoice[y])]
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path +
        "\n(it may be because the folder already exists, if so the file will still be sorted)")
    else:
        print ("Successfully created the directory %s" % path)
    print('\n')
    for file in range(len(choice[1][int(userchoice[y])])-1):
        try:
            os.rename(desktop+"\\"+choice[1][int(userchoice[y])][file+1], path+"\\"+choice[1][int(userchoice[y])][file+1])
        except OSError:
            print("Changing location of %s failed"% choice[1][int(userchoice[y])][file+1])
        else:
            print("Successfully changed location of %s" % choice[1][int(userchoice[y])][file+1])

# Print files that didn't fit any category of there's any
if(len(Nocategory) > 0):
    print("these file didn't have any category found")
for notfound in Nocategory:
    print(" ---- " + notfound)
