import PyPDF2

def find_string_page_number(pdf_file, search_string):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        if search_string in text:
            return str(page_num + 1)
    return "None"

def find_and_return_page_number(pdf_file, search_string):
    page_number = find_string_page_number(pdf_file, search_string)
    return page_number
