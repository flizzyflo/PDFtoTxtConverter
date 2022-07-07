
from Conversion.convert_pdf_to_word import convert_pdf_to_word
from PathSelection.PathSelection import select_file_path
from Buttons.Button import OwnButton
from UserInterface.UserInterface import PDF_UserIterface
from Settings.Settings import *
from tkinter import *


def start_application():

    root = PDF_UserIterface()
    root.title(TITLE)
    root.geometry(GEOMETRY)
    root.config(bg= BACKGROUNDCOLOR)

    root.mainloop()


if __name__ == "__main__":
    start_application()