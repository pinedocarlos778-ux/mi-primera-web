import streamlit as str
import datetime
import time

# Configuración de la página al estilo San Valentín / Dedicatoria
str.set_page_config(page_title="Para Alguien Especial", page_icon="❤️", layout="centered")

# Estilos CSS personalizados para cambiar el fondo y las fuentes
str.markdown("""
    <style>
    .stApp {
        background-color: #F5E8DC;
    }
    h1, h2, h3, p {
        color: #5C4033 !important;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    .Contador {
        font-size: 24px;
        font-weight: bold;
        color: #E91E63;
        text-align: center;
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Título principal y mensaje
str.write("# 💖 Para la chica más increible del mundo 'Siomara' 💖")
str.write("""
Si las mariposas pudieran hablar, dirían que eres la más hermosa que, 
asta la primavera necesesita de ti para florecer.
""")

str.markdown("---")

# Fecha de inicio (Cambia esto por tu fecha especial: Año, Mes, Día, Hora, Minuto)
fecha_inicio = datetime.datetime(2025, 2, 14, 0, 0, 0)

# Contenedor para el temporizador en tiempo real
espacio_contador = str.empty()

# EL BOTÓN SE CREA AQUÍ (AFUERA DEL BUCLE) - SOLO UNA VEZ
if str.button("Haz clic para una sorpresa 🎁", key="btn_sorpresa"):
    str.balloons() # Lluvia de globos en la pantalla
    str.success("¡Feliz cumpleaños, Siomara.! 🚀🌌")

# Animación del contador en vivo (Solo actualiza el texto del reloj)
while True:
    ahora = datetime.datetime.now()
    diferencia = ahora - fecha_inicio
    
    dias = diferencia.days
    horas, residuo = divmod(diferencia.seconds, 3600)
    minutos, segundos = divmod(residuo, 60)
    
    # Renderizar solo el contador con diseño HTML
    texto_html = f"""
        <div class="Contador">
            Mi cariño por ti comenzó hace:<br>
            {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos
        </div>
    """
    espacio_contador.markdown(texto_html, unsafe_allow_html=True)
    
    time.sleep(1)