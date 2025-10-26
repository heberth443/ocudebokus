import streamlit as st

st.set_page_config(page_title="Weduka", layout="wide", page_icon="🎵")

st.markdown("""
<style>
body {
  background-color: black;
  color: rgb(128, 0, 32);
  text-align: center;
  font-family: Arial, sans-serif;
}
.pulsing {
  font-size: 40px;
  animation: heartbeat 1.2s infinite ease-in-out;
}
@keyframes heartbeat {
  0%, 40%, 80%, 100% { transform: scale(1); opacity: 1; }
  20% { transform: scale(1.2); opacity: 0.85; }
  60% { transform: scale(1.15); opacity: 0.9; }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="pulsing">O Cu de Bokus</div>', unsafe_allow_html=True)

st.audio("https://raw.githubusercontent.com/heberth443/ocudebokus/refs/heads/main/Garrote%20das%20Meninas%20-%20Voc%C3%AA%20me%20vira%20a%20cabe%C3%A7a.mp3", autoplay=True)
