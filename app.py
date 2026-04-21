import streamlit as st
import pandas as pd
import time
from datetime import date

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Klinik Cantik Caca | High Contrast", 
    page_icon="💖", 
    layout="wide"
)

# 2. CSS Kustom - Perbaikan Kontras Warna
st.markdown("""
    <style>
    /* Background Utama Pink Tua */
    .stApp { background-color: #D81B60; }
    
    /* Judul Utama Pink Soft */
    .klinik-title {
        color: #FFD1DC; 
        font-family: 'Georgia', serif; 
        text-align: center; 
        font-size: 55px; 
        font-weight: bold;
        text-shadow: 3px 3px #880E4F;
    }
    
    /* Slogan Pink Soft */
    .klinik-slogan {
        color: #FFB6C1; 
        text-align: center; 
        font-style: italic; 
        font-size: 24px;
        margin-bottom: 30px;
    }

    /* Memaksa Semua Teks di Background Tua Jadi Pink Soft */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #FFD1DC !important;
    }

    /* Angka Metrik Jadi Putih agar Sangat Jelas */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: bold;
    }
    [data-testid="stMetricLabel"] {
        color: #FFB6C1 !important;
    }

    /* Tabel: Background Pink Soft, Teks Pink Tua (Kontras Tinggi) */
    .stTable {
        background-color: #FFD1DC;
        border-radius: 15px;
        padding: 10px;
    }
    .stTable td, .stTable th {
        color: #880E4F !important;
        font-weight: bold;
        border-bottom: 1px solid #D81B60 !important;
    }
    
    /* Sidebar: Background Pink Soft, Teks Pink Tua */
    [data-testid="stSidebar"] {
        background-color: #FFD1DC;
    }
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h2 {
        color: #880E4F !important;
        font-weight: bold;
    }

    /* Form Input agar kontras */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #FFF0F5 !important;
        color: #880E4F !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("Main Menu ✨", ["🏠 Dashboard", "📝 Pendaftaran", "👩‍⚕️ Profil Dokter", "🔍 Diagnosis", "🏢 Tentang Klinik"])

# --- HEADER UTAMA ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True)

# --- ISI MENU ---
if menu == "🏠 Dashboard":
    st.subheader("Overview Jadwal Hari Ini 🌸")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Pasien", "12", "↑3")
    with col2: st.metric("Pasien Selesai", "8", "↑5")
    with col3: st.metric("Pasien Menunggu", "4", "↓2")
    with col4: st.metric("Layanan Populer", "Facial Glow")

    st.write("### 📅 Jadwal Antrean")
    df = pd.DataFrame({
        "No": [101, 102, 103, 104],
        "Nama Pasien": ["Rina", "Santi", "Siska", "Dewi"],
        "Layanan": ["Facial Glow", "Peeling", "Botox", "Laser"],
        "Status": ["Selesai", "Selesai", "Menunggu", "Menunggu"]
    })
    st.table(df)

elif menu == "📝 Pendaftaran":
    st.subheader("Pendaftaran Pasien Baru")
    with st.form("form_reg"):
        st.text_input("Nama Lengkap")
        st.selectbox("Pilih Layanan", ["Facial Glow", "Laser", "Peeling", "Botox"])
        if st.form_submit_button("Daftar Sekarang ✨"):
            st.balloons()
            st.success("Data berhasil masuk ke sistem!")

elif menu == "👩‍⚕️ Profil Dokter":
    st.subheader("Dokter Spesialis & Sertifikasi")
    dokter = pd.DataFrame({
        "Nama Dokter": ["dr. Cindy Permata", "dr. Sarah Amelia", "dr. Bella Jovita", "dr. Mega Putri", "dr. Alika Najwa"],
        "Sertifikasi": ["Sp.DV (Skin)", "Laser Certified", "Filler Expert", "Esthetician", "Anti-Aging Cert."]
    })
    st.table(dokter)

elif menu == "🔍 Diagnosis":
    st.subheader("Simulasi Diagnosis & Rekomendasi Obat")
    masalah = st.selectbox("Pilih Masalah Kulit:", ["Jerawat Ringan", "Flek Hitam", "Kulit Kering"])
    if st.button("Lihat Saran"):
        st.write(f"Diagnosis: Kondisi {masalah} terdeteksi.")
        st.info("Saran Obat: Gunakan Moisturizer dan Sunscreen rutin. Silakan temui dr. Cindy.")

elif menu == "🏢 Tentang Klinik":
    st.subheader("Struktur Organisasi Klinik")
    struktur = pd.DataFrame({
        "Jabatan": ["Direktur Utama", "Manager", "Humas"],
        "Nama": ["Caca Beautyani", "Dewi Sartika", "Anita Rahayu"]
    })
    st.table(struktur)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #FFB6C1;'>Klinik Cantik Caca © 2026 | Perawatan Kulit Impian</div>", unsafe_allow_html=True)