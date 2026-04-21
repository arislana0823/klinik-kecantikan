import streamlit as st
import pandas as pd
import time
from datetime import date

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Klinik Cantik Caca | Perawatan Kulit Impian", 
    page_icon="💖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Kustom "Pink Contrast Mode"
st.markdown("""
    <style>
    /* Background Utama Jadi Pink Tua */
    .stApp { background-color: #D81B60; }
    
    /* Judul Utama Jadi Pink Soft */
    .klinik-title {
        color: #FFD1DC; 
        font-family: 'Georgia', serif; 
        text-align: center; 
        font-size: 55px; 
        font-weight: bold;
        text-shadow: 2px 2px #880E4F;
    }
    
    /* Slogan Jadi Pink Soft */
    .klinik-slogan {
        color: #FFB6C1; 
        font-family: 'Times New Roman', serif; 
        text-align: center; 
        font-style: italic; 
        font-size: 24px;
        margin-bottom: 25px;
    }

    /* Teks Umum di Background Tua Jadi Pink Soft */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #FFD1DC !important;
    }

    /* Font Metrik (Angka) Jadi Pink Soft */
    [data-testid="stMetricValue"] {
        color: #FFD1DC !important;
    }
    [data-testid="stMetricLabel"] {
        color: #FFB6C1 !important;
    }

    /* Tabel: Background tetap soft, Teks di dalamnya jadi Pink Tua */
    .stTable {
        background-color: #FFD1DC;
        border-radius: 10px;
        overflow: hidden;
    }
    .stTable td, .stTable th {
        color: #880E4F !important;
    }
    
    /* Sidebar: Background Tetap Pink Soft, Font Jadi Pink Tua */
    [data-testid="stSidebar"] {
        background-color: #FFD1DC;
    }
    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] h2 {
        color: #880E4F !important;
        font-weight: bold;
    }

    /* Input & Selectbox agar kontras */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #FFD1DC !important;
        color: #880E4F !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio(
        "Main Menu ✨",
        ["💖 Home & Jadwal", "📝 Pendaftaran Pasien", "👩‍⚕️ Profil Dokter", "🔍 Diagnosis & Obat", "🏢 Tentang Klinik"],
        key="nav_menu"
    )
    st.markdown("---")

# --- KONTEN UTAMA ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True)

# --- MENU 1: HOME & JADWAL ---
if menu == "💖 Home & Jadwal":
    st.subheader("Overview Jadwal Hari Ini 🌸")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Pasien", "12", "↑3")
    with col2: st.metric("Pasien Selesai", "8", "↑5")
    with col3: st.metric("Pasien Menunggu", "4", "↓2")
    with col4: st.metric("Layanan Populer", "Facial Glow")

    st.write("### 📅 Jadwal Antrean Pasien")
    data_antrean = {
        "No Antrean": [101, 102, 103, 104, 105],
        "Nama Pasien": ["Rina", "Santi", "Siska", "Dewi", "Anita"],
        "Layanan": ["Facial Glow", "Peeling", "Botox", "Facial Glow", "Laser"],
        "Jam Datang": ["08:00", "08:30", "09:00", "09:15", "09:45"],
        "Status": ["Selesai", "Selesai", "Menunggu", "Menunggu", "Menunggu"]
    }
    st.table(pd.DataFrame(data_antrean))

# --- MENU 2: PENDAFTARAN ---
elif menu == "📝 Pendaftaran Pasien":
    st.subheader("Formulir Pendaftaran ✍️")
    with st.form("form_regis"):
        nama = st.text_input("Nama Lengkap")
        umur = st.slider("Umur", 15, 60, 25)
        layanan = st.selectbox("Layanan", ["Facial Glow", "Laser Whitening", "Peeling", "Botox"])
        if st.form_submit_button("Daftar Sekarang ✨"):
            st.balloons()
            st.success(f"Berhasil! {nama} sudah masuk sistem.")

# --- MENU 3: PROFIL DOKTER ---
elif menu == "👩‍⚕️ Profil Dokter":
    st.subheader("Tim Dokter Spesialis 💖")
    dokter_data = {
        "Nama Dokter": ["dr. Cindy Permata, Sp.DV", "dr. Sarah Amelia, Sp.KK", "dr. Bella Jovita", "dr. Mega Putri", "dr. Alika Najwa"],
        "Keahlian": ["Skin Specialist", "Laser Specialist", "Injeksi & Filler", "Estetika Medis", "Anti-Aging"],
        "Sertifikasi": ["CNA Cosmetic", "Dermatologist", "Filler Certified", "Esthetician", "Anti-Aging Cert."]
    }
    st.table(pd.DataFrame(dokter_data))

# --- MENU 4: DIAGNOSIS & OBAT ---
elif menu == "🔍 Diagnosis & Obat":
    st.subheader("Diagnosis Awal & Rekomendasi 🧪")
    kondisi = st.selectbox("Masalah Kulit:", ["Jerawat Ringan", "Flek Hitam", "Kulit Kering"])
    if st.button(" Diagnosis Sekarang"):
        st.write(f"Diagnosis awal untuk **{kondisi}** sedang diproses...")
        st.info("Rekomendasi: Gunakan serum rutin dan konsultasi ke dokter terkait.")

# --- MENU 5: TENTANG KLINIK ---
elif menu == "🏢 Tentang Klinik":
    st.subheader("Profil & Struktur Organisasi 🏢")
    st.write("Klinik Cantik Caca: Mewujudkan kecantikan natural dengan cinta.")
    st.table(pd.DataFrame({
        "Jabatan": ["Direktur", "Manager", "Humas"],
        "Nama": ["Caca Beautyani", "Dewi Sartika", "Anita Rahayu"]
    }))

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #FFB6C1;'>Klinik Cantik Caca Dashboard © 2026</div>", unsafe_allow_html=True)