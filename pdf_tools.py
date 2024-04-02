# pdf_tools.py

from PyPDF2 import PdfReader, PdfWriter
import io

import os
import pytesseract
from pdf2image import convert_from_path
from tempfile import NamedTemporaryFile


def merge_pdf(files):
    merged_pdf = PdfWriter()
    for file in files:
        pdf = PdfReader(file)
        for page in pdf.pages:
            merged_pdf.add_page(page)
    output = io.BytesIO()
    merged_pdf.write(output)
    output.seek(0)
    return output




def convert_to_text(file):
    # Save the uploaded PDF file to a temporary location
    with NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
        temp_pdf_path = temp_pdf.name
        file.save(temp_pdf_path)

        # Convert PDF pages to images
        images = convert_from_path(temp_pdf_path)

    # Perform OCR on each image and extract text
    extracted_text = []
    for img in images:
        text = pytesseract.image_to_string(img)
        extracted_text.append(text)

    # Combine extracted text from all pages
    combined_text = '\n'.join(extracted_text)

    # Delete the temporary PDF file
    os.remove(temp_pdf_path)

    return combined_text






def extract_pages(file, start_page, end_page):
    input_pdf = PdfReader(file)
    extracted_pdf = PdfWriter()
    for i in range(start_page - 1, end_page):
        extracted_pdf.add_page(input_pdf.pages[i])
    output = io.BytesIO()
    extracted_pdf.write(output)
    output.seek(0)
    return output

def rotate_pdf(file, rotation_angle):
    input_pdf = PdfReader(file)
    output_pdf = PdfWriter()
    for page in input_pdf.pages:
        page.rotate(rotation_angle)
        output_pdf.add_page(page)
    output = io.BytesIO()
    output_pdf.write(output)
    output.seek(0)
    return output
