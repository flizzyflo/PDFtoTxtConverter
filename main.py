
from UserInterface.UserInterface import PDF_UserIterface
from Settings.Settings import *

def start_application():

    root = PDF_UserIterface()
    root.title(TITLE)
    root.geometry(GEOMETRY)
    root.config(bg= BACKGROUNDCOLOR)
    root.iconbitmap("pdf_bitmap.ico")


    root.mainloop()


if __name__ == "__main__":
    start_application()