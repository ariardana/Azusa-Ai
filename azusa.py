import streamlit as st
from langchain_community.llms import Ollama

# -------------------------
# Konfigurasi Tampilan
# -------------------------
st.set_page_config(page_title="Azusa AI - Chatbot Cerdas", layout="wide")

st.markdown(
    """
    <style>
    .main {background-color: #f5f7fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
    h1 {color: #2c3e50; text-align: center;}
    .stButton>button {background-color: #ff5733; color: white; border-radius: 5px;}
    .stTextInput>div>input {border: 2px solid #ff5733; border-radius: 5px;}
    .chat-bubble {background-color: #ff5733; color: white; padding: 10px; border-radius: 10px; margin-bottom: 10px;}
    .chat-bubble-user {background-color: #ecf0f1; color: black; padding: 10px; border-radius: 10px; margin-bottom: 10px;}
    </style>
    """, unsafe_allow_html=True
)

# -------------------------
# Judul Aplikasi
# -------------------------
st.title("🤖 Azusa AI - Chatbot Cerdas")
st.markdown("Selamat datang di Azusa AI! Tanyakan apa saja, dan AI akan menjawab.")

# -------------------------
# Simpan Riwayat Percakapan
# -------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------
# Koneksi ke Model DeepSeek R1 melalui Ollama
# -------------------------
try:
    llm = Ollama(model="deepseek-r1:1.5b")
except Exception as e:
    st.error(f"Error saat menghubungkan ke model: {e}")
    st.stop()

# -------------------------
# Menampilkan Riwayat Chat
# -------------------------
st.markdown("## **Percakapan dengan Azusa AI**")

for message in st.session_state.chat_history:
    role, text = message
    if role == "user":
        st.markdown(f'<div class="chat-bubble-user">{text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble">{text}</div>', unsafe_allow_html=True)

# -------------------------
# Form Input Chat
# -------------------------
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ketik pertanyaan Anda di sini...", placeholder="Contoh: Apa itu AI?")
    submit_button = st.form_submit_button("Kirim")

if submit_button and user_input:
    with st.spinner("Azusa AI sedang berpikir..."):
        try:
            response = llm.invoke(user_input)
        except Exception as e:
            response = f"Error: {e}"

    # Simpan ke riwayat chat
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("ai", response))

    # Tampilkan jawaban terbaru
    st.markdown(f'<div class="chat-bubble-user">{user_input}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-bubble">{response}</div>', unsafe_allow_html=True)

# -------------------------
# Footer
# -------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center>© 2025 Azusa AI - Dibangun dengan DeepSeek R1</center>", unsafe_allow_html=True)
