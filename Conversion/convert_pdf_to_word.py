import PyPDF2
import os


def convert_pdf_to_txt(pdf_filepath: str) -> None:
    """Function to convert a PDF file into a word file. 
    Word file is stored at the same location as the PDF file."""
    
    # take path of the pdf file and split the file name away
    # take folder path for saving the transformed file there
    splitted_path = os.path.split(pdf_filepath)

    # set current os working dir to the folder where the pdf is stored
    os.chdir(splitted_path[0])
    
    # read in pdf file as file in binary read mode
    with open(file= os.path.join(os.curdir, splitted_path[1]), mode= "rb") as file:

        # create pdf reader object to interact with pdf file
        reader = PyPDF2.PdfFileReader(file)

        # grab total amount of pages of the pdf file
        total_pages = reader.numPages

        # iterate over the whole document pages
        for page_number in range(0, total_pages):
            current_page = reader.getPage(page_number)
            page_content = current_page.extractText()

            # write the information into the newly created txt file or append to existing file.
            with open(file= os.path.join(os.curdir, "transformed_file.txt"), mode= "ab") as text_file:
                text_file.write(bytes(page_content, "utf-8"))
                text_file.write(bytes("\n\n", "utf-8"))
              
