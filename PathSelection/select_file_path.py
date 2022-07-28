
from tkinter import filedialog


def select_file_path(labelItem: object) -> str:
    """Function to select the path where a PDF file is stored."""

    tempFile = filedialog.askopenfile().name
    pdfTypeCheck = tempFile.split(".")

    # checks if a pdf file is read in
    if ("pdf" in pdfTypeCheck) or ("PDF" in pdfTypeCheck):

        labelItem.config(text= "File selected succesfully", relief= "groove", borderwidth= 1) # changes text of label widget to inform the user.
        
        # returns the filepath 
        return tempFile                                                             

    else:
        raise IOError("Wrong file type. No PDF-File selected. Please select a new file.")
   
