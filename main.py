# This program is gonna sort files on your desktop and put them in a folder :
# document/picture/software etc...
import os
from os import listdir
from os.path import isfile, join

# PATH to Desktop location
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

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

print("Here are the kind of file that can be sorted: ")
for type in choice[0]:
    print("- " + type)
argument = input("If you want more details about a type, type it\'s name else type 0: ")
if "0" in argument:
    result = 0
else:
    result = "string"

while(isinstance(result, str)):
    result = switcher.get(argument, "Invalid choice")
    if isinstance(result, str):
        print( result)
        argument = input('\n' + "which type do you wanna display (0 if nothing) ? ")
        if "0" in argument:
            result = -1
    else:
        print("\nhere are all the extention of this category: ")
        print(choice[1][result])
        input("\nPress Enter to continue...")


# Find all files on the desktop and put them in an array
for f in listdir(desktop):
    if isfile(join(desktop, f)):
        allFiles.append(f)

print("file found: " + str(len(allFiles)))

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
print("Here are the type of file that are going to be sort from what we found on your desktop")
# Choice of which type of file we want to sort
for x in range(len(choice[1])):
    if len(choice[1][x]) >1:
        userchoice.append(x)
        print(str(x) + ")" + choice[0][x])
argument = print("enter the number to see what files will be sorted for a category: ")
#TODO details

for y in range(len(userchoice)):
    try:
        path = desktop+"\\"+choice[0][userchoice[y]]
        os.mkdir(path)
        for file in range(len(choice[1][userchoice[y]])-1):
            try:
                os.rename(desktop+"\\"+choice[1][userchoice[y]][file+1], path+"\\"+choice[1][userchoice[y]][file+1])
            except OSError:
                print("Changing location of %s failed"% choice[1][userchoice[y]][file+1])
            else:
                print("Succussfully changed location of %s" % choice[1][userchoice[y]][file+1])
    except OSError:
        print ("Creation of the directory %s failed" % path )
    else:
        print ("Successfully created the directory %s" % path)

# TODO type the name to see more details for a type of file
# TODO Type number to ignore that kinda file

# Récupérer tout les types de fichier, voir quel dossier créer, demander le nom
# demander quel type trier, montrer les formats, si y en a qu'on veut pas avec on tape leur numéro séparés par un espace.
