
from tkinter import Tk, Label
from Buttons.Button import OwnButton
from Settings.Settings import *
from Conversion.convert_pdf_to_word import convert_pdf_to_word
from PathSelection.PathSelection import select_file_path


class PDF_UserIterface(Tk):
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.readFileButton = OwnButton(master = self, text= "Select PDF File", command = lambda: select_file_path(self.label), bg= BUTTONCOLOR)
        self.readFileButton.place(x= 10, y= 15)

        self.convertFileButton = OwnButton(master = self, text = "Convert PDF to Word", command = lambda: convert_pdf_to_word(self.label), bg= BUTTONCOLOR)
        self.convertFileButton.place(x= 115, y= 15)

        self.quitButton = OwnButton(master= self, text= "Quit", command= lambda: exit(), bg= BUTTONCOLOR)
        self.quitButton.place(x= 255, y= 15)

        self.label = Label(master= self, text= "", font=("calibri", 14, "bold"), bg= BACKGROUNDCOLOR)
        self.label.place(x= 50, y= 55)



