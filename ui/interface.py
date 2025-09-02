import streamlit as st
from processing.image_processor import process_image
from classification.classifier import classify_character
from visualization.radar_chart import create_radar_chart
from suggestions.improve import suggest_improvements
from PIL import Image

def run_ui():
    st.title("Lacrometro")
    st.write("Analise sua personagem: Woke / Sexualizado / Fofo")

    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png, webp"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Personagem enviada", use_column_width=True)

        # Botão para processar (placeholder por enquanto)
    if st.button("Analisar"):
        st.success("🔍 Análise em desenvolvimento...")

        # Processamento da imagem
        features = process_image(image)

        # Classificação
        category, scores = classify_character(features)
        st.write(f"Categoria principal: **{category}**")

        # Gráfico
        create_radar_chart(scores)
        st.pyplot()  # Exibe o gráfico gerado

        # Sugestões
        suggestions = suggest_improvements(features)
        st.write("Ideias de melhoria:")
        for s in suggestions:
            st.write(f"- {s}")
