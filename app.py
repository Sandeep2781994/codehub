# app.py

from flask import Flask, render_template, request, send_file
from pdf_tools import merge_pdf, convert_to_text, extract_pages, rotate_pdf

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    if 'files[]' not in request.files:
        return "No files uploaded"
    files = request.files.getlist('files[]')
    merged_pdf = merge_pdf(files)
    return send_file(merged_pdf, as_attachment=True, mimetype='application/pdf', download_name='merged.pdf')






@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file:
        text = convert_to_text(file)
        return render_template('result.html', text=text)








@app.route('/extract', methods=['POST'])
def extract():
    file = request.files['file']
    start_page = int(request.form['start_page'])
    end_page = int(request.form['end_page'])
    extracted_pdf = extract_pages(file, start_page, end_page)
    return send_file(extracted_pdf, as_attachment=True, mimetype='application/pdf', download_name='extracted.pdf')

@app.route('/rotate', methods=['POST'])
def rotate():
    file = request.files['file']
    rotation_angle = int(request.form['rotation_angle'])
    rotated_pdf = rotate_pdf(file, rotation_angle)
    return send_file(rotated_pdf, as_attachment=True, mimetype='application/pdf', download_name='rotated.pdf')

if __name__ == '__main__':
    app.run(debug=True)
