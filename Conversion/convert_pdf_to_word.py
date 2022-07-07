
from Settings.Settings import filepath
from PyPDF2 import PdfFileReader


def convert_pdf_to_word(labelItem: object) -> None:
    """Function to convert a PDF file into a word file. 
    Word file is stored at the same location as the PDF file."""

    global filepath

    pdf_file = PdfFileReader(filepath[0])                       # reads the filepath as string from the list
    total_page_count = pdf_file.getNumPages()                   # stores the total amount of pages within the pdf file
    

    # with open(fr"{new_path}.docx", "w") as new_word_file:
        
    #     for page_number in range(total_page_count):
    #         current_page = pdf_file.getPage(page_number)
    #         current_page_text = current_page.extract_text()
    #         new_word_file.write(current_page_text)

    # labelItem.config(text= "File converted succesfully")        # changes text of label widget to inform the user.
            

    
    


