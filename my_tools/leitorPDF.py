from pdfminer.high_level import extract_text, extract_text_to_fp
from unidecode import unidecode
from io import StringIO
import pdfplumber
import PyPDF2
import re


class LeitorPDF:
    def __init__(self):
        pass

    def __show_text(self, document, pages=''):
        text_in_document = []
        pdf_file = open(document, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        if pages == '': 
            pages = pdf_reader.numPages
    
        for i in range(pages):
            page_obj = pdf_reader.getPage(i)
            text_in_document.append(page_obj.extractText())
        return ' '.join(text_in_document)


    def show_all_text(self, document):
        return self.__show_text(document)


    def clean_text(self, text):
        sem_acento = unidecode(text)
        sem_quebra_de_linha = sem_acento.replace('\n','')
        tudo_minusculo = sem_quebra_de_linha.lower()
        unico_espacamento = re.sub(r'\s+', ' ', tudo_minusculo)
        sem_cifrao = re.sub(r'r\$', '', unico_espacamento)
        return sem_cifrao


    def _can_clean_text(self, answer: bool, text: str):
        if answer:
            return self.clean_text(text)
        else:
            return text


    def show_clean_text(self, file):
        text = self.__show_text(file)
        return self.clean_text(text)


    def show_the_page_number(self, n: int, document: str):
        return self.__show_text(document, n)


    def text_pdf_with_table(self, document):
        text_in_pdf = extract_text(document)
        return self.clean_text(text_in_pdf)
    

    def text_pdf_with_table_and_page_number(self, document: str, n: int):
        text_in_pdf: str = extract_text(document, page_numbers=[n])
        return self.clean_text(text_in_pdf)


    def text_pdf_fp(self, document: str, clean_text: bool, n_page: int = None, max_pages: int = 0) -> str:
        output_string = StringIO()
        with open(document, 'rb') as f:
            extract_text_to_fp(f, output_string, maxpages=max_pages, page_numbers=n_page)
        return self._can_clean_text(clean_text, output_string.getvalue())


    def text_with_pdfplumber(self, file: str, clean_text: bool, page_number: int = None) -> str:
        text = ''
        with pdfplumber.open(file) as pdf:
            if page_number == None:
                for page in pdf.pages:
                    text += page.extract_text()
            else:
                page = pdf.pages[page_number]
                text = page.extract_text()
            
        return self._can_clean_text(clean_text, text)