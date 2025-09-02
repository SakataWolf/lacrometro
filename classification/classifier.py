def classify_character(features):
    """
    Função placeholder para classificar personagem.
    Retorna categoria principal e pontuações para radar chart.
    """
    # Pontuações dummy
    scores = {
        "Sexualizado": 0.4,
        "Woke": 0.3,
        "Fofo": 0.7,
        "Estilo": 0.6,
        "Originalidade": 0.5,
        "Complexidade": 0.5
    }

    # Categoria principal
    category = max(scores, key=scores.get)
    return category, scores
