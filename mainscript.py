from argparse import ArgumentParser as ArgumentParser
from os import chdir as chdir
from os import getcwd as getcwd
from os import listdir as listdir
from os import mkdir as mkdir
from os import remove as Remove
from shutil import move as move
from shutil import rmtree as rmtree
from zipfile import ZipFile as ZipFile

PARSER = ArgumentParser()
PARSER.add_argument(
    "-install", "-i", help="Checks if you are installing, 1 = Yes.", type=int)
PARSER.add_argument("-uninstall", "-u",
                    help="Checks if you are uninstalling, 1 = Yes.", type=int)
PARSER.add_argument(
    "-game", "-g", help="Which game you are planning to install mods to.", type=str)

ARGS = PARSER.parse_args()


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
        for file_name_ext in listdir():
            if file_name_ext.endswith(".zip"):
                file_name = file_name_ext.replace(".zip", "")
                with ZipFile(file_name_ext, 'r') as exe:
                    mkdir(file_name)
                    exe.extractall(file_name)
                    Stellaris.editor(file_name)
            else:
                print("Error!, unzipper()")

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
        \r\t1. For each folder found when listing directory, runs if/elif/else
        \r\t2. If folder doesn't end with ".zip" or any other extension, proceed to remove folder
        \r\t3. If it does end with ".zip", proceed to remove folder (as in a file)
        \r\t4. Else, raise ValueError (used for now)
        """
        ignore = {".git", ".gitignore", ".vscode", "LICENSE", "license", ".py", ".pyw", ".exe"}
        for folder in listdir():
            if folder not in ignore:
                if not folder.endswith(".zip") and not folder.endswith(".*"):
                    rmtree(folder)
                elif folder.endswith(".zip"):
                    Remove(folder)
                else:
                    print("Error!, delete()")
            else:
                print("Error!, no elligible files")


try:
    INSTALL = ARGS.install
    REMOVE = ARGS.uninstall
    GAME = ARGS.game

    if INSTALL == 1 and GAME.lower() == "stellaris":
        Stellaris.install()
    elif REMOVE == 1 and GAME.lower() == "stellaris":
        Stellaris.uninstall()
    else:
        raise ValueError
except ValueError as ex:
    print(ex)