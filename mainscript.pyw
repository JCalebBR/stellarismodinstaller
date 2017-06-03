import argparse
from os import chdir as chdir
from os import getcwd as getcwd
from os import listdir as listdir
from os import mkdir as mkdir
from shutil import move as move
from zipfile import ZipFile as ZipFile

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help="sub-command help")
subparsers.add_argument("-install", "-i", help="Checks if you are installing, 1 = Yes.", type=int)
subparsers.add_argument("-remove", "-r", help="Checks if you are removing, 1 = Yes.", type=int)
subparsers.add_argument("-game", "-g", help="Which game you are planning to install mods to", type=str)

args = parser.parse_args()

class Stellaris:
    """
    Class used to group all functions used to install Stellaris' mods.

    Functions:
    \r\tunzipper(version)
    \r\teditor(fileName, version)
    """
    @staticmethod
    def unzipper(version):
        """
        Function used to unzip files and store them in their own folder.

        How it works:
        \r\t1. For each file when listing the content of a directory, do:
        \r\t2. Try: if file ends with .zip (is a zip file), takes file's name and gets rid off its extension (.zip)
        \r\t3. Opens up ZipFile from zipfile module, "instances" it as ex
        \r\t4. Makes a new directory with file's name (no ext.)
        \r\t5. Extracts zip to new directory
        \r\t6. Calls editor function
        \r\t7. When editor is done, it goes over all steps again, until no new file can be found.
        """
        for fileNameExt in listdir():
            try:
                if fileNameExt.endswith(".zip"):
                    fileName = fileNameExt.replace(".zip", "")
                    with ZipFile(fileNameExt, 'r') as ex:
                        mkdir(fileName)
                        ex.extractall(fileName)
                        Stellaris.editor(fileName, version)

            except Exception as ex:
                print(ex)

    @staticmethod
    def editor(fileName, version):
        """
        Function used to create an edit a .mod file.

        How it works:
        \r\t1. Gets current path
        \r\t2. Change working directory to previously created directory (read unzipper doc)
        \r\t3. Creates a new file called descriptor.mod, starts descEdit as an instance of open
        \r\t4. Writes in the first line: name="fileName"
        \r\t5. Writes in the second line: path="mod/fileName"
        \r\t6. Writes in the third line: supported_version="version"
        \r\t7. Renames descriptor.mod to fileName.mod
        \r\t8. Moves it outside the working directory
        \r\t9. Changes back to default directory
        """
        pyPath = getcwd()
        chdir(fileName)
        with open("descriptor.mod", "w") as descEdit:
            descEdit.write("name=" + "\"" + fileName + "\"")
            descEdit.write("\npath=" + "\"" + "mod/" + fileName + "\"")
            descEdit.write("\nsupported_version=" + "\"" + version + "\"")
        desc = fileName + ".mod"
        move("descriptor.mod", desc)
        move(desc, pyPath)
        chdir(pyPath)

try:
    install = args.install
    game = args.game
    version = "1.5.0"
    if install == 1 and game.lower() == "stellaris":
        Stellaris.unzipper(version)
    else:
        ex = Exception
        print(ex)
except Exception as ex:
    print(ex)