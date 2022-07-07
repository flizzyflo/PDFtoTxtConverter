
from Settings.Settings import filepath
import PyPDF2


def convert_pdf_to_word(labelItem: object) -> None:
    """Function to convert a PDF file into a word file. 
    Word file is stored at the same location as the PDF file."""

    global filepath



    labelItem.config(text= "File converted succesfully")  # changes text of label widget to inform the user.

   