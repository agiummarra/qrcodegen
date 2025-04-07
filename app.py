import qrcode
import streamlit as st
import os
import io
from datetime import datetime
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import (
    HorizontalGradiantColorMask,
    VerticalGradiantColorMask,
    RadialGradiantColorMask,
    SquareGradiantColorMask,
    SolidFillColorMask
)
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer

# Configurazione della pagina
st.set_page_config(
    page_title="Generatore QR Code",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Stile CSS personalizzato
st.markdown("""
<style>
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: #f8f9fa;
    }
    .stTitle {
        color: #1e3a8a;
        font-weight: 700;
    }
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .download-button {
        text-align: center;
        margin: 1rem 0;
    }
    .color-picker-container {
        display: flex;
        gap: 10px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Directory per salvare i QR code generati
GENERATED_QRCODES_PATH = "generated_qrcodes"
os.makedirs(GENERATED_QRCODES_PATH, exist_ok=True)

# Funzione per convertire colore hex in RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generate_qrcode(url, style_option, color_options, box_size=10, border=4, embed_image=None):
    """Genera un QR code con le opzioni specificate"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Estrazione dei colori dalle opzioni
    back_color = hex_to_rgb(color_options["back_color"])
    color_1 = hex_to_rgb(color_options["color_1"])
    color_2 = hex_to_rgb(color_options["color_2"])
    
    # Seleziona la maschera di colore in base all'opzione
    if style_option == "Colore Unico":
        color_mask = SolidFillColorMask(back_color=back_color, front_color=color_1)
    elif style_option == "Orizzontale":
        color_mask = HorizontalGradiantColorMask(back_color=back_color, left_color=color_1, right_color=color_2)
    elif style_option == "Verticale":
        color_mask = VerticalGradiantColorMask(back_color=back_color, top_color=color_1, bottom_color=color_2)
    elif style_option == "Radiale":
        color_mask = RadialGradiantColorMask(back_color=back_color, center_color=color_1, edge_color=color_2)
    else:  # Quadrato
        color_mask = SquareGradiantColorMask(back_color=back_color, center_color=color_1, edge_color=color_2)
    
    # Crea il QR code con stile arrotondato
    module_drawer = CircleModuleDrawer() if style_option != "Colore Unico" else RoundedModuleDrawer()
    img = qr.make_image(image_factory=StyledPilImage, color_mask=color_mask, module_drawer=module_drawer)
    
    # Se è stata caricata un'immagine da inserire al centro, aggiungiamola
    if embed_image is not None:
        # Apri l'immagine caricata
        logo = Image.open(embed_image)
        
        # Calcola la dimensione per il logo (25% del QR code)
        logo_size = int(img.size[0] * 0.25)
        logo = logo.resize((logo_size, logo_size))
        
        # Calcola la posizione per centrare il logo
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        
        # Crea una copia dell'immagine e incolla il logo
        qr_with_logo = img.copy()
        qr_with_logo.paste(logo, pos, logo.convert('RGBA'))
        img = qr_with_logo
    
    # Salva l'immagine e restituisci il percorso
    current_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    qrcode_path = os.path.join(GENERATED_QRCODES_PATH, f"qrcode_{current_ts}.png")
    img.save(qrcode_path)
    
    return qrcode_path, img

# Header dell'applicazione
st.title("🚀 Generatore di QR Code")
st.markdown("### Crea QR code personalizzati per i tuoi URL")

# Form per l'input
with st.form(key="qrcode_form"):
    url = st.text_input("Inserisci l'URL 👇", placeholder="https://esempio.com")
    
    # Selezione dello stile di QR code
    style_option = st.selectbox(
        "Stile del QR Code",
        options=["Colore Unico", "Orizzontale", "Verticale", "Radiale", "Quadrato"],
        index=0
    )
    
    # Layout in colonne per i parametri
    col1, col2 = st.columns(2)
    
    # Colonna per la selezione dei colori
    with col1:
        st.subheader("Colori")
        back_color = st.color_picker("Colore sfondo", "#FFFFFF")
        
        if style_option == "Colore Unico":
            color_1 = st.color_picker("Colore QR code", "#1E3A8A")
            color_2 = color_1  # Non utilizzato ma inizializzato per uniformità
        else:
            st.write("Colori gradiente:")
            color_1 = st.color_picker("Colore primario", "#1E3A8A")
            color_2 = st.color_picker("Colore secondario", "#4682B4")
    
    # Colonna per altre impostazioni
    with col2:
        st.subheader("Dimensioni e Logo")
        box_size = st.slider("Dimensione", min_value=5, max_value=20, value=10)
        
        # Opzione per caricare un'immagine da inserire al centro del QR code
        uploaded_image = st.file_uploader("Carica logo (opzionale)", type=["png", "jpg", "jpeg"])
        
        # Mostra un'anteprima dell'immagine caricata
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption="Anteprima logo", width=100)
    
    # Pulsante per generare il QR code
    submit_button = st.form_submit_button(label="Genera QR Code")

# Genera QR code quando il form viene inviato
if submit_button:
    if url:
        with st.spinner("Generazione QR Code in corso... ⏳"):
            try:
                # Prepara le opzioni di colore
                color_options = {
                    "back_color": back_color,
                    "color_1": color_1,
                    "color_2": color_2
                }
                
                qrcode_path, qr_img = generate_qrcode(
                    url, 
                    style_option,
                    color_options,
                    box_size=box_size,
                    embed_image=uploaded_image
                )
                
                # Visualizza il QR code
                st.success("QR Code generato con successo! ✅")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("")
                with col2:
                    st.image(qrcode_path, caption=f"QR Code per: {url}", use_container_width=True)
                with col3:
                    st.write("")
                
                # Bottone per scaricare il QR code
                with open(qrcode_path, "rb") as file:
                    img_bytes = file.read()
                
                st.download_button(
                    label="📥 Scarica QR Code",
                    data=img_bytes,
                    file_name=f"qrcode_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                    mime="image/png",
                    key="download_qr"
                )
                
                # Mostra l'URL codificato
                st.info(f"**URL codificato**: {url}")
            
            except Exception as e:
                st.error(f"Si è verificato un errore: {e}")
    else:
        st.warning("⚠️ Per favore, inserisci un URL valido!")

# Footer
st.markdown("---")
st.markdown("### Come funziona?")
st.markdown("""
1. Inserisci l'URL che desideri codificare nel QR code
2. Scegli lo stile (colore unico o gradiente) e personalizza i colori
3. Imposta la dimensione e carica opzionalmente un logo da inserire al centro
4. Clicca 'Genera QR Code'
5. Scarica l'immagine generata
""")

st.markdown("---")
st.markdown("Sviluppato da [Andrea Giummarra](https://github.com/agiummarra) con ❤️ usando Streamlit e qrcode") 