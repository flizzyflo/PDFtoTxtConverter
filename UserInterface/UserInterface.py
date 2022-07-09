
from tkinter import Tk, Label
from Buttons.Button import OwnButton
from Settings.Settings import *
from Conversion.convert_pdf_to_word import convert_pdf_to_word as convertFile
from PathSelection.select_file_path import select_file_path as getfilepath


class PDF_UserIterface(Tk):
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.readFileButton = OwnButton(master = self, text= "Select PDF File", command = lambda: self.select_file_path(), bg= BUTTONCOLOR)
        self.readFileButton.place(x= 10, y= 15)

        self.convertFileButton = OwnButton(master = self, text = "Convert PDF to Word", command = lambda: self.convert_pdf_to_word(), bg= BUTTONCOLOR)
        self.convertFileButton.place(x= 115, y= 15)

        self.quitButton = OwnButton(master= self, text= "Quit", command= lambda: exit(), bg= BUTTONCOLOR)
        self.quitButton.place(x= 255, y= 15)

        self.label = Label(master= self, text= "", font=("calibri", 14, "bold"), bg= BACKGROUNDCOLOR)
        self.label.place(x= 50, y= 55)

        self.filepath = None

        print(self.convertFileButton, self.quitButton, self.readFileButton)

    def convert_pdf_to_word(self):
        """Converts the file to the word format."""

        print(self.filepath)
        convertFile(self.label)

    def select_file_path(self) -> str:
        """Grabs the path of the pdf file passed in via file selector."""

        if self.filepath != None: # if self.path already stores a path to avoid mixing up paths.
            self.filepath = None

        else:
            self.filepath = getfilepath(self.label)

