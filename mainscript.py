"""
argparse module
"""
from argparse import ArgumentParser as ArgumentParser
from os import chdir as chdir
from os import getcwd as getcwd
from os import listdir as listdir
from os import mkdir as mkdir
from os import path as path
from os import remove as Remove
from shutil import move as move
from shutil import rmtree as rmtree
from sys import argv as argv
from zipfile import ZipFile as ZipFile

PARSER = ArgumentParser()
PARSER.add_argument(
    "-install", "-i", help="Checks if you are installing, 1 = Yes.", type=int)
PARSER.add_argument(
    "-uninstall", "-u", help="Checks if you are uninstalling, 1 = Yes.", type=int)
PARSER.add_argument(
    "-game", "-g", help="Which game you are planning to install mods to.", type=str)

ARGS = PARSER.parse_args()

class InvalidArgumentError(Exception):
    """
    Custom exception
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class Stellaris:
    """
    Class used to group all functions used to install Stellaris' mods.

    Functions:
    \r\tunzipper()
    \r\teditor(file_name)
    """
    @staticmethod
    def install():
        """
        Simply runs unzipper function. Used only to clarify code
        """
        Stellaris.unzipper()

    @staticmethod
    def uninstall():
        """
        Simply runs delete function. Used only to clarify code
        """
        Stellaris.delete()

    @staticmethod
    def unzipper():
        """
        Function used to unzip files and store them in their own folder.

        How it works:
        \r\t1. For each file when listing the content of a directory, do:
        \r\t2. Try: if file ends with .zip (is a zip file), proceed
        \r\t3. Takes file's name and gets rid off its extension (.zip)
        \r\t4. Opens up ZipFile from zipfile module, "instances" it as ex
        \r\t5. Makes a new directory with file's name (no ext.)
        \r\t6. Extracts zip to new directory
        \r\t7. Calls editor function
        \r\t8. When editor is done, it goes over all steps again, until no new file can be found.
        """
        success = 0
        error = 0
        for file_name_ext in listdir():
            if file_name_ext.endswith(".zip"):
                file_name = file_name_ext.replace(".zip", "")
                with ZipFile(file_name_ext, 'r') as exe:
                    mkdir(file_name)
                    exe.extractall(file_name)
                    success += 1
                    Stellaris.editor(file_name)
            else:
                error += 1
                print(
                    "Error! File {0} isn't a zip".format(file_name_ext))

        if success != 0 and error == 0:
            # If any number of files were successfully extracted
            # and no non-zip were found, print msg:
            print("Extracted {0} files".format(success))
        elif success != 0 and error != 0:
            # If any number of files were succesfully extracted
            # and there was at least one non-zip, print msg:
            print(
                "Extracted {0} files, but found {1} non-zip files".format(
                    success, error))
        else:
            # If no files were deleted and no error found,
            # print msg
            print("Extracted 0 files, because none [eligible] were found.")

    @staticmethod
    def editor(file_name):
        """
        Function used to create an edit a .mod file.

        How it works:
        \r\t1. Gets current path
        \r\t2. Change working directory to previously created directory (read unzipper doc)
        \r\t3. Creates a new file called descriptor.mod, starts mod as an instance of open
        \r\t4. Writes in the first line: name="file_name"
        \r\t5. Writes in the second line: path="mod/file_name"
        \r\t6. Writes in the third line: supported_version="version"
        \r\t7. Renames descriptor.mod to file_name.mod
        \r\t8. Moves it outside the working directory
        \r\t9. Changes back to default directory
        """
        py_path = getcwd()
        version = "1.*.*"
        chdir(file_name)
        with open("descriptor.mod", "w") as mod:
            mod.write("name=" + "\"" + file_name + "\"")
            mod.write("\npath=" + "\"" + "mod/" + file_name + "\"")
            mod.write("\nsupported_version=" + "\"" + version + "\"")
        desc = file_name + ".mod"
        move("descriptor.mod", desc)
        move(desc, py_path)
        chdir(py_path)

    @staticmethod
    def delete():
        """
        Function used to delete files and folders

        How it works:
        \r\t1. Creates a tuple of ignored files
        \r\t2. Creates a tuple of allowed files
        """
        ignore = (
            ".git", ".gitignore", ".vscode", "LICENSE", "license",
            ".py", ".pyw", ".exe")
        allowed = (".zip", ".mod")
        success = 0
        error = 0
        for data in listdir():
            if data not in ignore:
                if path.isdir(data):
                    rmtree(data)
                    success += 1
                elif path.isfile(data) and data.endswith(tuple(allowed)):
                    Remove(data)
                    success += 1
                elif data == argv[0]:
                    pass
                else:
                    error += 1
                    print(
                        "Error! File {0} not allowed to be deleted.".format(data))

        if success != 0 and error == 0:
            # If any number of files were successfully deleted
            # and no errors were found, print msg:
            print("Deleted {0} files and/or folders!".format(success))
        elif success != 0 and error != 0:
            # If any number of files were succesfully deleted
            # and there was at least one error, print msg:
            print(
                "Deleted {0} files and/or folders!, but there were {1} errors!".format(
                    success, error))
        else:
            # If no files were deleted and no error found,
            # print msg
            print("Deleted 0 files and/or folders!, because none [eligible] were found.")

try:
    INSTALL = ARGS.install
    REMOVE = ARGS.uninstall
    GAME = ARGS.game

    GAMES = ("stellaris")

    if INSTALL == 1 and GAME.lower() == "stellaris":
        Stellaris.install()
    elif REMOVE == 1 and GAME.lower() == "stellaris":
        Stellaris.uninstall()
    elif (INSTALL == 1 or REMOVE == 1) and GAME.lower() not in GAMES:
        print("\"{0}\" isn't a supported game!".format(GAME))
    else:
        raise InvalidArgumentError(
            "mainscript.py: error: no arguments. use -h for help")
except InvalidArgumentError as ex:
    print(ex)
