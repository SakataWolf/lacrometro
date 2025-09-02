import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(scores):
    """
    Cria um radar chart (hexagonal) baseado nas pontuações.
    """
    labels = list(scores.keys())
    values = list(scores.values())

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]  # fecha o círculo
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_ylim(0, 1)
    plt.title("Perfil da Personagem")
    return fig
