
from tkinter import filedialog
from Settings.Settings import filepath


def select_file_path(labelItem: object) -> None:
    """Function to select the path where a PDF file is stored."""

    global filepath
    filepath.clear() #clears global path variable to ensure only the actual path is stored in the list.

    tempFile = filedialog.askopenfile().name
    pdfTypeCheck = tempFile.split(".")

    # checks if pdf file is read in
    if ("pdf" in pdfTypeCheck) or ("PDF" in pdfTypeCheck):
        filepath.append(tempFile) # appends filepath to the global filepath variable

        labelItem.config(text= "File selected succesfully", relief= "groove", borderwidth= 1) # changes text of label widget to inform the user.

    else:
        raise IOError("Wrong file type. No PDF-File selected. Please select a new file.")
   
