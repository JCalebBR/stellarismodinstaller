from os import chdir as chdir
from os import listdir as listdir
from os import mkdir as mkdir
from os import getcwd as getcwd
from shutil import move as move
from sys import exit as sysexit
from zipfile import ZipFile as ZipFile

pyPath = getcwd()
def start():                                            # Just a welcoming-message function
    print("\nWelcome to Stellaris (multiple) Mod Installer")
    print("by JCaleb")
    print("This installer will automatically unzip all zips to their respective folders,")
    print("edit \"archive=\"MODNAME.mod\" into \"path=\"MODNAME.mod\" and descriptor.mod into MODNAME.mod")
    print("then move it outside their own folders to root mod folder.")
    print("\nPS: Please use _ (underscore) instead of spacebar on zip filenames, just to be safe!!!")

    chc = input("\nProceed? (Y/N): ")                   # Asks if the user wants to proceed or exit

    if chc == "Y" or chc == "y":                        # If user input is equal to either Y or y (case-sensitive) proceeds normally
        pass
    elif chc == "N" or chc == "n":                      # Else if user input is equal to either N or n (case-sensitive) exit the script
        sysexit()
    else:                                               # If neither cases above were used, it means something is wrong, so calls startError function
        startError()
    
    version = input("What is the current version of the game?\nExample: 1.5.1: ")
    unzipper(version)

def startError():                                       # Is called when start() founds an error
    print("\nThat is not a valid option!, TRY AGAIN!")
    chc = input("\nProceed? (Y/N): ")                   # Asks if the user wants to proceed or exit again

    if chc == "Y" or chc == "y":                        # If user input is equal to either Y or y (case-sensitive) proceeds normally
        pass
    elif chc == "N" or chc == "n":                      # Else if user input is equal to either N or n (case-sensitive) exit the script
        sysexit()
    else:                                               # If neither cases above were used, it means something is wrong, so calls startError function
        startError()

def unzipper(version):
    for l in listdir():
        if l.endswith(".zip"):
            if l != "base_library.zip":
                nl = l.replace(".zip", "")
                with ZipFile(l, 'r') as ex:
                    mkdir(nl)
                    ex.extractall(nl)
                    editor(nl, version)
            else:
                pass

def editor(nl, version):
    chdir(nl)
    with open("descriptor.mod", "w") as fm:
        fm.write("name="+"\""+nl+"\"")
        fm.write("\npath="+"\""+"mod/"+nl+"\"")
        fm.write("\nsupported_version="+"\""+version+"\"")
    nnl = nl+".mod"
    move("descriptor.mod", nnl)
    move(nnl, pyPath)
    chdir(pyPath)

start()
