import numpy as np
from PIL import Image

def process_image(image: Image.Image):
    """
    Função placeholder para processar a imagem.
    Retorna um dicionário com características básicas.
    """
    # Redimensionar para padrão
    image = image.resize((256, 256))

    # Extração de cores predominantes (exemplo simples)
    colors = np.array(image).mean(axis=(0,1))

    # Proporções dummy
    proportions = {
        "corpo": 0.5,  # placeholder
        "rosto": 0.5   # placeholder
    }

    features = {
        "colors": colors,
        "proportions": proportions
    }
    return features
