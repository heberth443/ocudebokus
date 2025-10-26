import streamlit as st

st.set_page_config(page_title="Weduka", layout="wide", page_icon="🎵")

# CSS customizado
st.markdown("""
<style>
/* Fundo preto geral */
body, .css-1d391kg {
    background-color: black !important;
    color: rgb(128,0,32);
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

/* Texto pulsante no topo */
.pulsing-container {
    position: fixed;
    top: 2%;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    z-index: 10;
}

.pulsing-text {
    font-size: 40px;
    color: rgb(128,0,32);
    text-shadow: 0 0 10px rgba(128,0,32,0.8);
    animation: heartbeat 1.2s infinite ease-in-out;
}

.side-img {
    height: 1em;
    width: auto;
}

/* Animação pulsante */
@keyframes heartbeat {
    0%,40%,80%,100% { transform: scale(1); opacity: 1; }
    20% { transform: scale(1.2); opacity: 0.85; }
    60% { transform: scale(1.15); opacity: 0.9; }
}

/* Container iframe centralizado */
#iframe-container {
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Iframe */
#iframe-container iframe {
    width: 100%;
    height: 100%;
    border: none;
}

/* Player fixo canto inferior direito */
.audio-player {
    position: fixed;
    bottom: 15px;
    right: 20px;
    z-index: 20;
    background: rgba(20,20,20,0.7);
    padding: 8px 12px;
    border-radius: 12px;
}
.audio-player audio {
    width: 220px;
    filter: invert(1) hue-rotate(180deg);
}
</style>
""", unsafe_allow_html=True)

# Texto pulsante com imagem
st.markdown("""
<div class="pulsing-container">
    <img class="side-img" src="https://firebasestorage.googleapis.com/v0/b/image-uploader-br.appspot.com/o/images%2F5a6a4271-d957-435f-a8b0-275b564f374c?alt=media&token=ce041d82-a246-4e53-945d-cb7e8d1f02ed" alt="imagem">
    <div class="pulsing-text">O Cu de Bokus</div>
</div>
""", unsafe_allow_html=True)

# Iframe centralizado
st.markdown("""
<div id="iframe-container">
    <iframe src="https://ovogame.gitlab.io/file/"></iframe>
</div>
""", unsafe_allow_html=True)

# Player de música
st.markdown("""
<div class="audio-player">
  <audio controls autoplay loop>
    <source src="https://raw.githubusercontent.com/heberth443/ocudebokus/refs/heads/main/Garrote%20das%20Meninas%20-%20Você%20me%20vira%20a%20cabeça.mp3" type="audio/mpeg">
    Seu navegador não suporta áudio.
  </audio>
</div>
""", unsafe_allow_html=True)
