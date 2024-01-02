from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    return soup.get_text()