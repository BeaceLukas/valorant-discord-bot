import pytesseract
from PIL import Image
import io
import re

# Tesseract Pfad (für Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extract_text_from_image(image_bytes):
    image_rgb = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_bw = image_rgb.convert("L").point(lambda x: 0 if x < 160 else 255, '1')

    width, height = image_rgb.size

    # Fester Tagline-Bereich oben rechts (prozentual, auflösungsunabhängig)
    tagline_box = (int(width * 0.70), int(height * 0.02), width - 10, int(height * 0.14))
    tagline_crop = image_rgb.crop(tagline_box)
    tagline_crop_bw = tagline_crop.convert("L").point(lambda x: 0 if x < 160 else 255, '1')
    tagline_text = pytesseract.image_to_string(tagline_crop_bw)

    # Code-Bereich: unten links
    code_box = (0, int(height * 0.80), int(width * 0.5), height)
    code_crop = image_bw.crop(code_box)
    code_text = pytesseract.image_to_string(code_crop)

    combined = tagline_text.strip() + "\n" + code_text.strip()

    # Zusätzlicher Tagline-Check mit Bereinigung
    lines = combined.splitlines()
    cleaned_taglines = []
    for line in lines:
        match = re.search(r"([A-Za-z0-9]{3,16}#[A-Za-z0-9]{2,5})", line)
        if match:
            cleaned_taglines.append(match.group(1))

    print("[OCR DEBUG] Erkannter Text:\n" + combined)
    if cleaned_taglines:
        print(f"[OCR DEBUG] Erkannte Tagline (bereinigt): {cleaned_taglines[0]}")
    else:
        print("[OCR DEBUG] Keine gültige Tagline im Format erkannt.")

    return combined
