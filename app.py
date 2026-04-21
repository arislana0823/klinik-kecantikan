import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="BeautyCare Dashboard", page_icon="✨", layout="wide")

# CSS Kustom untuk Tema Pink/Cewek
st.markdown("""
    <style>
    .main { background-color: #FFF0F5; }
    h1 { color: #D87093; text-align: center; font-family: 'Trebuchet MS'; }
    .stButton>button { 
        background-color: #FFB6C1; color: white; border-radius: 20px; 
        border: none; padding: 10px 24px; font-weight: bold;
    }
    .stButton>button:hover { background-color: #FF69B4; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ BeautyCare Clinic Dashboard ✨")

# Sidebar
st.sidebar.header("Menu Navigasi")
menu = st.sidebar.selectbox("Pilih Menu", ["Home", "Pendaftaran Pasien", "Data Layanan"])

if menu == "Home":
    st.subheader("Selamat Datang, Cantik!")
    st.write("Kelola data klinik kecantikanmu dengan mudah dan elegan di sini.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Pasien", "150", "+5")
    col2.metric("Layanan Populer", "Facial Glow", "Hot")
    col3.metric("Pendapatan", "Rp 25M", "+12%")

elif menu == "Pendaftaran Pasien":
    st.subheader("Formulir Pendaftaran Baru")
    with st.form("form_pasien"):
        nama = st.text_input("Nama Lengkap")
        layanan = st.selectbox("Pilih Layanan", ["Facial Glow", "Laser Whitening", "Peeling", "Botox"])
        tanggal = st.date_input("Rencana Kunjungan")
        submit = st.form_submit_button("Daftar Sekarang")
        
        if submit:
            st.success(f"Berhasil! {nama} telah terdaftar untuk {layanan} pada {tanggal}")

elif menu == "Data Layanan":
    st.subheader("Daftar Harga & Layanan")
    data = {
        "Nama Layanan": ["Facial Glow", "Laser Whitening", "Peeling", "Botox"],
        "Harga (IDR)": ["350.000", "1.200.000", "500.000", "2.500.000"],
        "Durasi": ["60 Menit", "45 Menit", "30 Menit", "20 Menit"]
    }
    st.table(pd.DataFrame(data))

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #D87093;'>BeautyCare Dashboard © 2026 | Dibuat dengan 💖</div>", unsafe_allow_html=True)