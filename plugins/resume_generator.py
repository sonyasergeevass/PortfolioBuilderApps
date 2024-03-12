__plugin_name__ = "Resume Generator"
__version__ = "1.0"
__author__ = "Sonya Sergeeva BPI21-01"

from xhtml2pdf import pisa
import requests
def generate_resume_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

    return not pisa_status.err

