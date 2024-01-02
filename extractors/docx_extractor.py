import docx

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
    return text