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

# 2. CSS Kustom "Ultra Soft Pink & Kontras Tinggi"
st.markdown("""
    <style>
    /* Background Utama */
    .stApp { background-color: #FFF0F5; }
    
    /* Judul Utama */
    .klinik-title {
        color: #D81B60; 
        font-family: 'Georgia', serif; 
        text-align: center; 
        font-size: 50px; 
        font-weight: bold;
        text-shadow: 2px 2px #FFD1DC;
    }
    
    /* Slogan Motivasi (Warna Pink Tua) */
    .klinik-slogan {
        color: #C71585; 
        font-family: 'Times New Roman', serif; 
        text-align: center; 
        font-style: italic; 
        font-size: 22px;
        margin-bottom: 25px;
    }

    /* Memperbaiki Warna Font Metrik (Angka Statistik) agar Pink Tua */
    [data-testid="stMetricValue"] {
        color: #C71585 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #D81B60 !important;
    }

    /* Memperbaiki Warna Font Tabel agar Pink Tua */
    .stTable td, .stTable th {
        color: #C71585 !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFD1DC;
    }
    
    /* Warna teks umum di sidebar */
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] .stRadio label {
        color: #880E4F !important;
        font-weight: bold;
    }

    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='color: #D81B60; text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio(
        "Main Menu ✨",
        ["💖 Home & Jadwal", "📝 Pendaftaran Pasien", "👩‍⚕️ Profil Dokter", "🔍 Diagnosis & Obat", "🏢 Tentang Klinik"],
        key="nav_menu"
    )
    st.markdown("---")
    st.info("💡 Gunakan menu di atas untuk navigasi.")

# --- KONTEN UTAMA ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True)


# --- MENU 1: HOME & JADWAL ---
if menu == "💖 Home & Jadwal":
    st.subheader("Overview Jadwal Hari Ini 🌸")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Pasien", "12", "↑3")
    with col2:
        st.metric("Pasien Selesai", "8", "↑5")
    with col3:
        st.metric("Pasien Menunggu", "4", "↓2")
    with col4:
        st.metric("Layanan Populer", "Facial Glow")

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
        nama_pasien = st.text_input("Nama Lengkap Pasien")
        umur_pasien = st.slider("Umur", 15, 60, 25)
        layanan_pilihan = st.selectbox("Pilih Layanan", ["Facial Glow", "Laser Whitening", "Peeling", "Botox"])
        submit_pendaftaran = st.form_submit_button("Daftar Sekarang ✨")
        
        if submit_pendaftaran:
            st.balloons()
            st.success(f"Berhasil! {nama_pasien} telah terdaftar.")


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
    kondisi = st.selectbox("Pilih Masalah Kulit:", ["Jerawat Ringan", "Flek Hitam", "Kulit Kering"])
    if st.button("Diagnosis!"):
        if kondisi == "Jerawat Ringan":
            st.write("**Diagnosis:** Papula Ringan")
            st.markdown("<p style='color: #D81B60;'><b>Rekomendasi:</b> Acne Spot Gel & Cleanser.</p>", unsafe_allow_html=True)
        elif kondisi == "Flek Hitam":
            st.write("**Diagnosis:** Hiperpigmentasi")
            st.markdown("<p style='color: #D81B60;'><b>Rekomendasi:</b> Sunscreen SPF 50+ & Vit C.</p>", unsafe_allow_html=True)
        elif kondisi == "Kulit Kering":
            st.write("**Diagnosis:** Dehidrasi Kulit")
            st.markdown("<p style='color: #D81B60;'><b>Rekomendasi:</b> Hyaluronic Acid & Moisturizer.</p>", unsafe_allow_html=True)


# --- MENU 5: TENTANG KLINIK ---
elif menu == "🏢 Tentang Klinik":
    st.subheader("Profil & Struktur Organisasi 🏢")
    st.write("Klinik Cantik Caca hadir untuk mewujudkan impian kulit sehatmu.")
    
    st.write("### 🏗️ Struktur Organisasi")
    data_struktur = {
        "Jabatan": ["Direktur Utama", "Manager", "Humas", "Admin Keuangan", "PJ Medis"],
        "Nama": ["Caca Beautyani", "Dewi Sartika", "Anita Rahayu", "Sarah Amalia", "dr. Cindy Permata"]
    }
    st.table(pd.DataFrame(data_struktur))

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #D87093;'>Klinik Cantik Caca Dashboard © 2026 | Dibuat dengan 💖</div>", unsafe_allow_html=True)