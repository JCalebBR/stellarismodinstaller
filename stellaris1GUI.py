from os         import chdir    as chdir
from os         import getcwd   as getcwd
from os         import listdir  as listdir
from os         import mkdir    as mkdir
from shutil     import move     as move
from sys        import exit     as sysexit
from tkinter    import *
from zipfile    import ZipFile  as ZipFile


class mainCode:
    pyPath = getcwd()

    def unzipper(self, version):
        for l in listdir():
            if l.endswith(".zip") and l != "base_library.zip":
                nl = l.replace(".zip", "")
                with ZipFile(l, 'r') as ex:
                    mkdir(nl)
                    ex.extractall(nl)
                    mainCode.editor(nl, version)
            else:
                pass

    def editor(self, nl, version):
        chdir(nl)
        with open("descriptor.mod", "w") as fm:
            fm.write("name="+"\""+nl+"\"")
            fm.write("\npath="+"\""+"mod/"+nl+"\"")
            fm.write("\nsupported_version="+"\""+version+"\"")
        nnl = nl+".mod"
        move("descriptor.mod", nnl)
        move(nnl, mainCode.pyPath)
        chdir(mainCode.pyPath)


class mainWindow:                                                       # Class that will be responsible for GUI
    def __init__(self, toplevel):                                       # Initialization function, inits all other widgets/functions
        self.frm = Frame(toplevel)                                      # Initializes a frame
        self.frm2= Frame(toplevel)                                      # Initializes another frame
        self.frm.pack()                                                 # Packs the frame
        mainWindow.initWidgets(self)                                    # Calls initWidgets function
    
    def initWidgets(self, parent=__init__):                             # Responsible for initializing all other widgets
        def initLabels(self, parent=None):                              # Responsible for initializing all Labels
            self.label1 = Label(self.frm, text="Welcome to Stellaris (multiple) Mod Installer")
            self.label2 = Label(self.frm, text="This installer will automatically unzip all zips to their respective folders,")
            self.label3 = Label(self.frm, text="edit \"archive=\"MODNAME.mod\" into \"path=\"MODNAME.mod\" and descriptor.mod into MODNAME.mod")
            self.label4 = Label(self.frm, text="then move it outside their own folders to root mod folder.")
            self.label5 = Label(self.frm, text="\nPS: Please use _ (underscore) instead of spacebar on zip filenames, just to be safe!!!")
            self.label6 = Label(self.frm, text="\n\nProceed to installation process? (Y/N)")
            chc = ""
            self.entry1 = Entry(self.frm, width="3", textvariable=chc)
            def clique1(self, chc):
                if chc == "Y" or chc == "y":
                    pass
                elif chc == "N" or chc == "n":
                    root.destroy()
            
            self.entry1.focus_force()
            self.label1.pack()
            self.label2.pack()
            self.label3.pack()
            self.label4.pack()
            self.label5.pack()
            self.label6.pack()
            self.entry1.pack()

            return chc

        def initButtons(self, parent=None):                             # Responsible for initializing all buttons
            self.button1 = Button(self.frm, text="OK!")
            self.button1.bind("<Button-1>", self.clique1)
            self.button1.pack()

        #def initB(self, parent=__init__):

        #def initC(self, parent=__init__):
        initLabels(self)
        initButtons(self)
root=Tk()
mainWindow(root)
root.title("Stellaris Mod Installer")
root.mainloop()
