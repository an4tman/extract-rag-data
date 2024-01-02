import os
import sys
import logging
import click
from extractors.txt_extractor import extract_text_from_txt
from extractors.docx_extractor import extract_text_from_docx
from extractors.pdf_extractor import extract_text_from_pdf
from extractors.html_extractor import extract_text_from_html
from utils import is_human_readable

@click.command()
@click.argument('directory', type=click.Path(exists=True))
def main(directory):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    for root, dirs, files in os.walk(directory):
        for file in files:
            directory = os.path.join(root, file)
            try:
                if directory.endswith('.txt'):
                    text = extract_text_from_txt(directory)
                elif directory.endswith('.docx'):
                    text = extract_text_from_docx(directory)
                elif directory.endswith('.pdf'):
                    text = extract_text_from_pdf(directory)
                elif directory.endswith('.html'):
                    text = extract_text_from_html(directory)
                else:
                    logging.error(f"Unsupported file type: {directory}")
                    continue

                # Check if the text is human-readable before printing
                if is_human_readable(text):
                    print(text)
                else:
                    logging.error(f"Unreadable text in file: {directory}")
            except Exception as e:
                logging.error(f"Error processing file {directory}: {e}", exc_info=True, stack_info=True)
                sys.stderr.write(f"Error processing file {directory}: {e}\n")

if __name__ == '__main__':
    main()
