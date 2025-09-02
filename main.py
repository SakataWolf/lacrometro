import streamlit as st
from PIL import Image

# Título da aplicação
st.title("📸 Lacrômetro")

st.write("Envie uma imagem para iniciar a análise.")

# Upload de imagem
uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Abrir e exibir a imagem
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem enviada", use_column_width=True)
    
    # Botão para processar (placeholder por enquanto)
    if st.button("Analisar"):
        st.success("🔍 Análise em desenvolvimento...")
