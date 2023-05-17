import os
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

def extract_text_from_pdf(pdf_path):
    laparams = LAParams()
    return extract_text(pdf_path, codec='utf-8', laparams=laparams)

# Eingabeaufforderung für den Benutzer, um den Pfad zur PDF-Datei zu erhalten
pdf_name = input("Bitte geben Sie den Pfad zur PDF-Datei ein: ")
pdf_path = os.path.join('/Users/tom.backert/Desktop/', pdf_name)

# Extrahieren des Basisnamens und Erstellen des Ausgabepfad
base_name = os.path.basename(pdf_path)  # Basisname (z. B., 'my_file.pdf')
name_without_extension = os.path.splitext(base_name)[0]  # Name ohne Erweiterung (z. B., 'my_file')
output_path = os.path.join('/Users/tom.backert/Desktop/', f'{name_without_extension}_output.txt')

# Verwendung der Funktion
text = extract_text_from_pdf(pdf_path)

# Schreiben des Textes in eine Textdatei
with open(output_path, 'w') as f:
    f.write(text)