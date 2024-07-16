from flask import Flask, request, render_template, send_file
import csv
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            xml_filepath = convert_csv_to_xml(filepath)
            return send_file(xml_filepath, as_attachment=True)
    return render_template('index.html')

def convert_csv_to_xml(csv_filepath):
    root = ET.Element('root')

    with open(csv_filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            item = ET.SubElement(root, 'item')
            for key, val in row.items():
                element = ET.SubElement(item, key)
                element.text = val

    tree = ET.ElementTree(root)
    xml_filepath = csv_filepath.rsplit('.', 1)[0] + '.xml'
    tree.write(xml_filepath)
    return xml_filepath

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)