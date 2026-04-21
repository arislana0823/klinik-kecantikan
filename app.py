import streamlit as st
import pandas as pd
from datetime import date

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Klinik Cantik Caca | Official Dashboard", 
    page_icon="💖", 
    layout="wide"
)

# 2. CSS Kustom - High Contrast & Full Data Style
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
        margin-bottom: 0px;
    }
    
    /* Slogan Pink Soft */
    .klinik-slogan {
        color: #FFB6C1; 
        text-align: center; 
        font-style: italic; 
        font-size: 22px;
        margin-bottom: 30px;
    }

    /* Memaksa Semua Teks di Background Tua Jadi Pink Soft */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #FFD1DC !important;
    }

    /* Tabel: Background Pink Soft, Teks Pink Tua (Kontras Tinggi) */
    .stTable {
        background-color: #FFD1DC;
        border-radius: 15px;
        padding: 15px;
    }
    .stTable td, .stTable th {
        color: #880E4F !important;
        font-weight: bold;
        font-size: 16px;
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

    /* Gaya Card Metrik */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("Main Menu ✨", ["🏠 Dashboard", "📝 Pendaftaran", "👩‍⚕️ Tim Dokter Ahli", "🔍 Diagnosis Wajah", "🏢 Profil Klinik"])

# --- HEADER UTAMA ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True)

# --- MENU 1: DASHBOARD ---
if menu == "🏠 Dashboard":
    st.subheader("Ringkasan Aktivitas Hari Ini 🌸")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Pasien Hari Ini", "45", "↑12")
    c2.metric("Konsultasi Selesai", "32", "↑8")
    c3.metric("Menunggu", "13", "↓4")
    c4.metric("Treatment Favorit", "Glass Skin Laser")
    
    st.write("### 📅 Antrean Pasien Saat Ini")
    df_antrean = pd.DataFrame({
        "No": [201, 202, 203, 204],
        "Nama": ["Riana", "Santi", "Siska", "Dewi"],
        "Layanan": ["Facial Glow", "Laser Rejuvenation", "Botox Injeksi", "Chemical Peeling"],
        "Dokter": ["dr. Cindy", "dr. Sarah", "dr. Bella", "dr. Mega"]
    })
    st.table(df_antrean)

# --- MENU 2: TIM DOKTER (7 DATA) ---
elif menu == "👩‍⚕️ Tim Dokter Ahli":
    st.subheader("7 Dokter Spesialis & Praktisi Terbaik Kami")
    data_dokter = {
        "Nama Dokter": [
            "dr. Cindy Permata, Sp.DV", "dr. Sarah Amelia, Sp.KK", "dr. Bella Jovita", 
            "dr. Mega Putri", "dr. Alika Najwa", "dr. Rania Safira", "dr. Tasya Kamila"
        ],
        "Keahlian Utama": [
            "Spesialis Kulit & Kelamin", "Laser & Rejuvenation", "Injeksi Filler & Botox", 
            "Estetika Medis & Peeling", "Anti-Aging Specialist", "Acne Care Expert", "Hydration Glow"
        ],
        "Sertifikasi": [
            "Board Certified", "Laser Professional Cert.", "Master of Injectables", 
            "Esthetician Certified", "CIDESO International", "Acne Management", "Diplomate Aesthetic"
        ]
    }
    st.table(pd.DataFrame(data_dokter))

# --- MENU 3: DIAGNOSIS WAJAH (10 DATA) ---
elif menu == "🔍 Diagnosis Wajah":
    st.subheader("Simulasi Diagnosis & Solusi Kulit Wajah")
    masalah = st.selectbox("Pilih Keluhan Wajah Kamu:", [
        "Jerawat Pasir (Bruntusan)", "Jerawat Batu (Kistik)", "Flek Hitam (Melasma)", 
        "Bekas Jerawat Merah (PIE)", "Kulit Kusam & Gelap", "Pori-Pori Besar", 
        "Garis Halus & Kerutan", "Kulit Sangat Kering", "Kantung Mata Gelap", "Wajah Berminyak Parah"
    ])
    
    saran_db = {
        "Jerawat Pasir (Bruntusan)": "Saran: Gunakan Cleanser BHA & Serum Niacinamide.",
        "Jerawat Batu (Kistik)": "Saran: Wajib Konsultasi Dokter (Mungkin butuh Injeksi Acne).",
        "Flek Hitam (Melasma)": "Saran: Gunakan Sunscreen SPF 50 & Treatment Laser.",
        "Bekas Jerawat Merah (PIE)": "Saran: Gunakan Azelaic Acid & Hindari Scrub kasar.",
        "Kulit Kusam & Gelap": "Saran: Rutin Chemical Peeling & Serum Vitamin C.",
        "Pori-Pori Besar": "Saran: Gunakan Retinol malam hari & Clay Mask rutin.",
        "Garis Halus & Kerutan": "Saran: Treatment Botox atau Filler di Klinik.",
        "Kulit Sangat Kering": "Saran: Pakai Moisturizer Tekstur Cream & Hyaluronic Acid.",
        "Kantung Mata Gelap": "Saran: Gunakan Eye Cream Caffeine & Perbaiki pola tidur.",
        "Wajah Berminyak Parah": "Saran: Gunakan Gel Moisturizer & Double Cleansing."
    }
    
    if st.button("Dapatkan Analisis Cepat"):
        st.write(f"### 📋 Hasil Untuk: {masalah}")
        st.info(saran_db[masalah])

# --- MENU 4: PROFIL KLINIK ---
elif menu == "🏢 Profil Klinik":
    st.subheader("Mengenal Klinik Cantik Caca")
    st.write("""
    Didirikan pada tahun 2018 di bawah kepemimpinan **Direktur Utama Caca Beautyani, S.ST**, 
    Klinik Cantik Caca telah melayani lebih dari 10.000 pasien dengan dedikasi tinggi. 
    Kami berfokus pada hasil yang natural dan kesehatan kulit jangka panjang.
    """)
    
    st.write("### 🏗️ Struktur Organisasi Utama")
    data_struktur = {
        "Jabatan": ["Direktur Utama", "Manager Operasional", "Kepala Medis", "Admin Keuangan", "Humas"],
        "Nama": ["Caca Beautyani, S.ST", "Dewi Sartika, SE", "dr. Cindy Permata, Sp.DV", "Sarah Amalia", "Anita Rahayu"],
        "Masa Bakti": ["6 Tahun", "5 Tahun", "6 Tahun", "4 Tahun", "3 Tahun"]
    }
    st.table(pd.DataFrame(data_struktur))

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #FFB6C1;'>Klinik Cantik Caca Dashboard © 2026 | Built with 💖</div>", unsafe_allow_html=True)