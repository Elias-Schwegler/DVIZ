import fitz
import sys

pdf_path = sys.argv[1]
output_path = sys.argv[2]

doc = fitz.open(pdf_path)
num_pages = len(doc)

with open(output_path, 'w', encoding='utf-8') as f:
    for i, page in enumerate(doc):
        text = page.get_text()
        f.write(f'=== PAGE {i+1} ===\n')
        f.write(text)
        f.write('\n\n')

doc.close()
print(f'Done. Extracted {num_pages} pages to {output_path}')
