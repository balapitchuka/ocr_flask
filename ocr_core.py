try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

def ocr_core(file_name):
    text = pytesseract.image_to_string(Image.open(file_name))
    return text

print(ocr_core('images/ocr_core_example_1.png'))
