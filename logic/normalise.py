import unicodedata
import string

def normalize(text):
    # Pasamos a minúsculas
    text = text.lower()
    # Separamos los acentos de las letras
    text = unicodedata.normalize("NFD", text)
    # Eliminamos signos de puntuación
    text = "".join(c for c in text if c not in string.punctuation)
    # Eliminamos acentos
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text