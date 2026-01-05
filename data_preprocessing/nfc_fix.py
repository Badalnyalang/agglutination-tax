import unicodedata

def fix_tsmb_normalization(text):
    # Converts Decomposed (NFD) to Composed (NFC)
    return unicodedata.normalize('NFC', text)

# Example usage for your Mizo corpus
# with open('mizo_raw.txt', 'r') as f:
#     clean_text = fix_tsmb_normalization(f.read())
