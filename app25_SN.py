import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import csv
from datetime import datetime



# Configuración de la página
st.set_page_config(page_title="Clasificador de Fauna Venezolana", page_icon="🐾", layout="wide")

# Función para registrar el feedback junto con la ubicación
def log_feedback(species, confidence, feedback, location):
    filename = "feedback_log.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([now, species, confidence, feedback, location])

# Intentar obtener la ubicación del usuario mediante JavaScript
try:
    from streamlit_javascript import st_javascript
    user_location = st_javascript(
        "navigator.geolocation.getCurrentPosition((loc) => { return {lat: loc.coords.latitude, lon: loc.coords.longitude}; });"
    )
    st.info(f"Ubicación obtenida: {user_location}")
except ImportError:
    user_location = None
    st.warning("No se pudo obtener la ubicación automáticamente. Para ello, instala el paquete 'streamlit_javascript'.")

if not user_location:
    user_input = st.text_input("Ingresa tu ubicación (latitud, longitud):", "")
    if user_input:
        user_location = user_input

# Cargar el modelo
model_path = "/content/drive/MyDrive/Modelos/clasificador_sierra_nevada_v1.h5"
try:
    model = tf.keras.models.load_model(model_path)
except OSError as e:
    st.error(f"No se pudo cargar el modelo: {e}")

def preprocess_image(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Lista de especies (más estilizada)
class_names = [
    'Chiguire',                # 0
    'Coati Andino',            # 1
    'Condor',                  # 2
    'Conejo del paramo',       # 3
    'Jaguar',                  # 4
    'Jicotea',                 # 5
    'La curraca',              # 6
    'La lapa',                 # 7
    'Leopardo andino',         # 8
    'Mono araña',             # 9
    'Mono nocturno',           # 10
    'Oso andino',              # 11
    'Oso hormiguero gigante',  # 12
    'Pato de torrente',        # 13
    'Paují de yelmo',         # 14
    'Pava andina',             # 15
    'Puma',                    # 16
    'Tonina',                  # 17
    'Tortuga carey',           # 18
    'Venado andino',           # 19
]

# Descripciones con secciones (usando HTML para formateo)
species_info = {
    "Chiguire": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> El chiguire, conocido como capibara, habita en áreas cercanas a ríos, lagunas y humedales en regiones tropicales, con alta humedad y temperaturas cálidas.</p>
        <p><b>Características y Comportamiento:</b> Es un animal sociable que se desplaza en grupos y muestra gran adaptabilidad a ambientes acuáticos.</p>
        <p><b>Interacción y Conservación:</b> Se recomienda observarlo a distancia, no alimentarlo y dejar intacto su entorno para favorecer su supervivencia.</p>
    </div>
    """,
    "Coati Andino": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Habita bosques y zonas montañosas de los Andes, donde el clima puede variar entre templado y frío dependiendo de la altitud.</p>
        <p><b>Características y Comportamiento:</b> Es un animal curioso, diurno y ágil, con un gran sentido de exploración.</p>
        <p><b>Interacción y Conservación:</b> Es importante mantener la distancia, evitar ofrecer alimentos y observarlo en su ambiente natural.</p>
    </div>
    """,
    "Condor": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se encuentra en áreas de gran altitud con clima frío y ventoso, ideal para aprovechar las corrientes térmicas.</p>
        <p><b>Características y Comportamiento:</b> Es una de las aves voladoras más imponentes, con una envergadura notable y vuelo majestuoso.</p>
        <p><b>Interacción y Conservación:</b> Se recomienda el uso de binoculares y mantener una observación pasiva para no interferir en sus rutas.</p>
    </div>
    """,
    "Conejo del paramo": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Vive en el páramo, un ecosistema de alta montaña con climas fríos y cambios bruscos entre el día y la noche.</p>
        <p><b>Características y Comportamiento:</b> Es pequeño, ágil y se camufla perfectamente en su entorno agreste.</p>
        <p><b>Interacción y Conservación:</b> Observarlo en silencio y sin perturbar su hábitat es clave para su preservación.</p>
    </div>
    """,
    "Jaguar": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se desplaza por bosques tropicales y zonas ribereñas, en ambientes cálidos y húmedos.</p>
        <p><b>Características y Comportamiento:</b> Es un felino poderoso, sigiloso y fundamental en el equilibrio ecológico.</p>
        <p><b>Interacción y Conservación:</b> La observación remota es la mejor práctica para evitar invadir su territorio y contribuir a su conservación.</p>
    </div>
    """,
    "Jicotea": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se asocia a ambientes acuáticos, como ríos y lagunas en regiones tropicales con alta humedad.</p>
        <p><b>Características y Comportamiento:</b> Su vida se desarrolla en el agua y es muy sensible a cambios en la calidad del entorno.</p>
        <p><b>Interacción y Conservación:</b> Evitar la contaminación y no perturbar las aguas donde habita es esencial para su bienestar.</p>
    </div>
    """,
    "La curraca": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Habita bosques y áreas abiertas, generalmente en climas templados a subtropicales.</p>
        <p><b>Características y Comportamiento:</b> Destaca por su plumaje vistoso y vivacidad, siendo una ave muy activa y comunicativa.</p>
        <p><b>Interacción y Conservación:</b> Es preferible observarla sin ruidos fuertes para no alterar su comportamiento natural.</p>
    </div>
    """,
    "La lapa": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se encuentra en zonas rocosas o costeras, con climas que varían de templados a tropicales.</p>
        <p><b>Características y Comportamiento:</b> Con movimientos lentos y un comportamiento sereno, es ideal para la observación cercana.</p>
        <p><b>Interacción y Conservación:</b> Respetar su espacio y evitar interferir en su rutina son acciones fundamentales.</p>
    </div>
    """,
    "Leopardo andino": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se cree que habita en áreas montañosas de los Andes, con climas fríos y ventosos.</p>
        <p><b>Características y Comportamiento:</b> Es un depredador solitario y sigiloso, raramente observado por el hombre.</p>
        <p><b>Interacción y Conservación:</b> Se recomienda la observación a distancia para no alterar su comportamiento.</p>
    </div>
    """,
    "Mono araña": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Vive en densos bosques tropicales, en ambientes cálidos y con alta humedad.</p>
        <p><b>Características y Comportamiento:</b> Es ágil, social y se desplaza con facilidad por las copas de los árboles.</p>
        <p><b>Interacción y Conservación:</b> Observarlo sin interferir en su vida social y sin ofrecerle alimentos es lo ideal.</p>
    </div>
    """,
    "Mono nocturno": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Habita selvas y bosques que se refrescan durante la noche, combinando climas cálidos diurnos y frescos nocturnos.</p>
        <p><b>Características y Comportamiento:</b> Posee adaptaciones especiales para ver en condiciones de poca luz y es muy discreto.</p>
        <p><b>Interacción y Conservación:</b> Es fundamental observarlo en silencio y con iluminación tenue para no alterar su ciclo.</p>
    </div>
    """,
    "Oso andino": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se encuentra en bosques y páramos de alta montaña, con climas fríos y alta humedad.</p>
        <p><b>Características y Comportamiento:</b> Es un animal solitario y cauteloso, adaptado a condiciones extremas.</p>
        <p><b>Interacción y Conservación:</b> Mantener una distancia segura y evitar ruidos o perturbaciones es esencial para su conservación.</p>
    </div>
    """,
    "Oso hormiguero gigante": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se encuentra en áreas tropicales y subtropicales con vegetación densa y climas cálidos.</p>
        <p><b>Características y Comportamiento:</b> Se alimenta principalmente de hormigas y termitas, mostrando un comportamiento tranquilo.</p>
        <p><b>Interacción y Conservación:</b> No intervenir en su búsqueda de alimento y preservar su hábitat es vital.</p>
    </div>
    """,
    "Pato de torrente": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Habita ríos de montaña en ambientes de alta altitud, con clima frío, húmedo y corrientes rápidas.</p>
        <p><b>Características y Comportamiento:</b> Es ágil y se adapta a las aguas turbulentas gracias a sus habilidades natatorias.</p>
        <p><b>Interacción y Conservación:</b> Se debe observar sin perturbar, especialmente durante períodos de migración o reproducción.</p>
    </div>
    """,
    "Paují de yelmo": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se encuentra en bosques montañosos y páramos, en zonas de climas templados a fríos.</p>
        <p><b>Características y Comportamiento:</b> Es un ave de belleza singular, con un comportamiento reservado y elegante.</p>
        <p><b>Interacción y Conservación:</b> Observarla desde la distancia y evitar ruidos es fundamental para no alterar su ciclo natural.</p>
    </div>
    """,
    "Pava andina": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Vive en bosques y páramos andinos, donde las condiciones son frías y variables.</p>
        <p><b>Características y Comportamiento:</b> Desempeña un papel importante en la dispersión de semillas y se destaca por su elegancia en vuelo.</p>
        <p><b>Interacción y Conservación:</b> Es ideal observarla sin interferir en sus actividades para contribuir a su preservación.</p>
    </div>
    """,
    "Puma": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se extiende por amplios territorios que abarcan desde bosques tropicales hasta montañas frías.</p>
        <p><b>Características y Comportamiento:</b> Es un gran felino solitario, con habilidades excepcionales de caza y rol crucial en el equilibrio ecológico.</p>
        <p><b>Interacción y Conservación:</b> La observación a distancia y el respeto por su entorno son fundamentales para su supervivencia.</p>
    </div>
    """,
    "Tonina": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Habita ríos y lagunas en regiones tropicales, donde la calidad del agua es esencial.</p>
        <p><b>Características y Comportamiento:</b> Este delfín de agua dulce es juguetón, ágil y muy sociable.</p>
        <p><b>Interacción y Conservación:</b> Se recomienda observarlo desde la orilla o en excursiones autorizadas, evitando la contaminación de su hábitat.</p>
    </div>
    """,
    "Tortuga carey": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Habita arrecifes y costas tropicales, donde las aguas cálidas y claras son vitales para sus migraciones.</p>
        <p><b>Características y Comportamiento:</b> Aunque de movimientos lentos, sigue rutas migratorias definidas y depende de zonas de anidación específicas.</p>
        <p><b>Interacción y Conservación:</b> Es esencial respetar las áreas de anidación, evitar la contaminación marina y observarla sin perturbar sus hábitos.</p>
    </div>
    """,
    "Venado andino": """
    <div style="text-align: justify;">
        <p><b>Hábitat y Clima:</b> Se encuentra en regiones montañosas de los Andes, con clima frío y condiciones extremas en altitud.</p>
        <p><b>Características y Comportamiento:</b> Ágil y discreto, está perfectamente adaptado a terrenos escarpados y busca alimento con cautela.</p>
        <p><b>Interacción y Conservación:</b> Mantener la distancia y preservar su entorno natural es esencial para su conservación.</p>
    </div>
    """
}

# Encabezado con colores venezolanos y crédito de Byte Warrios
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #002B7F, #FCD116, #E40303); padding: 20px; border-radius: 10px;">
        <h1 style="text-align: center;">Clasificador de Fauna Venezolana en Peligro</h1>
        <p style="text-align: center; font-size: 18px;">Identifica especies endémicas y en peligro en Venezuela</p>
        <p style="text-align: center; font-size: 16px;"><i>Desarrollado por Byte Warrios</i></p>
    </div>
    """, unsafe_allow_html=True
)

# Sección de animación (Lottie)
st.markdown(
    '<div style="text-align: center;">'
    '<lottie-player src="https://assets3.lottiefiles.com/packages/lf20_6hsvu07x.json" background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></lottie-player>'
    '</div>', unsafe_allow_html=True
)

# Sección informativa de especies con lista en dos columnas
st.markdown("<h3 style='text-align: center;'>Especies disponibles</h3>", unsafe_allow_html=True)
cols = st.columns(2)
for i, species in enumerate(class_names):
    cols[i % 2].markdown(f"<div style='padding: 5px;'><b>{i+1}. {species}</b></div>", unsafe_allow_html=True)

# Subir imagen desde la cámara o archivo
st.markdown("<h3 style='text-align: center;'>📸 Captura o sube una imagen para analizar</h3>", unsafe_allow_html=True)
image_from_camera = st.camera_input("Captura una imagen")
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

if image_from_camera is not None:
    image = Image.open(image_from_camera)
elif uploaded_file is not None:
    image = Image.open(uploaded_file)
else:
    image = None

if image is not None:
    st.markdown("<h4 style='text-align: center;'>Imagen cargada:</h4>", unsafe_allow_html=True)
    st.image(image, caption="Vista previa", use_container_width=True)
    
    # Preprocesar y predecir
    image_processed = preprocess_image(image)
    predictions = model.predict(image_processed)
    max_probability = np.max(predictions)
    predicted_index = np.argmax(predictions)
    
    if max_probability < 0.70:
        st.markdown("<h2 style='color: red; text-align: center;'>⚠️ Animal no registrado</h2>", unsafe_allow_html=True)
    else:
        predicted_species = class_names[predicted_index]
        st.markdown(
            f"<h2 style='color: #38abe0; text-align: center;'>✅ Categoría predicha: {predicted_species}</h2>",
            unsafe_allow_html=True
        )
        # Mostrar la descripción formateada
        st.markdown(species_info[predicted_species], unsafe_allow_html=True)
        
        # Sección de feedback y registro de imagen (si es correcta)
        st.markdown(
            """
            <div style="background-color: transparent; padding: 15px; border-radius: 10px; margin-top: 20px; text-align: center;">
                <h4>¿Es correcta la clasificación?</h4>
            </div>
            """, unsafe_allow_html=True
        )
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Correcta"):
                # Guardar la imagen en la carpeta correspondiente
                folder_base = "imagenes clasificadas correctamente"
                folder_category = os.path.join(folder_base, predicted_species)
                if not os.path.exists(folder_category):
                    os.makedirs(folder_category)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{predicted_species}_{timestamp}.jpg"
                image.save(os.path.join(folder_category, filename))
                log_feedback(predicted_species, f"{max_probability:.2f}", "correcta", user_location)
                st.success("¡Gracias por tu feedback! Imagen guardada correctamente.")
        with col2:
            if st.button("❌ Incorrecta"):
                log_feedback(predicted_species, f"{max_probability:.2f}", "incorrecta", user_location)
                st.error("¡Gracias por tu feedback!")

# Pie de página con créditos finales
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <hr>
    <p style="text-align: center; font-size: 14px;">
    Proyecto desarrollado por <b>Byte Warrios</b> utilizando <b>TensorFlow</b> y <b>Streamlit</b> – Especial para la fauna venezolana.
    </p>
    """, unsafe_allow_html=True
)
st.markdown(
    """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.6/lottie.min.js"></script>
    """, unsafe_allow_html=True
)
