import argparse
from os import chdir as chdir
from os import getcwd as getcwd
from os import listdir as listdir
from os import mkdir as mkdir
from shutil import move as move
from zipfile import ZipFile as ZipFile

parser = argparse.ArgumentParser()
parser.add_argument("-game", "-g", help="Takes a game as an argument, then the script uses it to decide which action to take. (Which install method to use)", type=str)
args = parser.parse_args()

class stellaris:
    @staticmethod
    def unzipper(version):
        for fileNameEXT in listdir():
            try:
                if fileNameEXT.endswith(".zip"):
                    fileName = fileNameEXT.replace(".zip", "")
                    with ZipFile(fileNameEXT, 'r') as ex:
                        mkdir(fileName)
                        ex.extractall(fileName)
                        stellaris.editor(fileName, version)

            except Exception as ex:
                print(ex)

    @staticmethod
    def editor(fileName, version):
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
    game = args.game
    version = "1.5.0"
    if game.lower() == "stellaris":
        stellaris.unzipper(version)
except Exception as ex:
    print(ex)