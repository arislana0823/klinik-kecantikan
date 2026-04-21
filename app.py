import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Klinik Cantik Caca | Official Dashboard", 
    page_icon="💖", 
    layout="wide"
)

# 2. CSS Kustom untuk Fix Warna Font & Kontras
st.markdown("""
    <style>
    /* Background Utama Pink Tua */
    .stApp { background-color: #D81B60; }
    
    /* Judul & Slogan */
    .klinik-title {
        color: #FFD1DC; text-align: center; font-size: 55px; font-weight: bold;
        text-shadow: 3px 3px #880E4F; font-family: 'Georgia', serif;
    }
    .klinik-slogan { color: #FFB6C1; text-align: center; font-style: italic; font-size: 22px; margin-bottom: 30px; }

    /* FIX TABEL: Memaksa tulisan berwarna Pink Tua agar terlihat jelas */
    .stTable { background-color: #FFD1DC !important; border-radius: 15px; padding: 10px; }
    .stTable td, .stTable th { 
        color: #880E4F !important; 
        font-weight: bold !important; 
        font-size: 16px !important;
        border-bottom: 1px solid #D81B60 !important;
    }

    /* FIX FORM & INPUT: Memaksa teks input tidak berwarna putih */
    input, select, textarea, [data-baseweb="select"] {
        background-color: #FFF0F5 !important;
        color: #880E4F !important;
    }
    label { color: #FFD1DC !important; font-weight: bold; }

    /* Metrik (Angka Dashboard) */
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-weight: bold; }
    [data-testid="stMetricLabel"] { color: #FFB6C1 !important; }

    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #FFD1DC; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] label {
        color: #880E4F !important; font-weight: bold;
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

# --- LOGIKA MENU ---

if menu == "🏠 Dashboard":
    st.subheader("Overview Aktivitas Klinik 🌸")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Pasien", "45", "↑12")
    c2.metric("Selesai", "32", "↑8")
    c3.metric("Menunggu", "13", "↓4")
    c4.metric("Treatment Terlaris", "Glass Skin")

elif menu == "📝 Pendaftaran":
    st.subheader("Form Pendaftaran Pasien Baru ✍️")
    with st.form("form_pendaftaran"):
        st.text_input("Nama Lengkap")
        st.selectbox("Pilih Layanan", ["Facial Glow", "Laser Rejuvenation", "Botox Injeksi", "Chemical Peeling"])
        st.selectbox("Pilih Dokter", ["dr. Cindy Permata", "dr. Sarah Amelia", "dr. Bella Jovita", "dr. Mega Putri"])
        if st.form_submit_button("Daftar Sekarang ✨"):
            st.balloons()
            st.success("Pasien berhasil didaftarkan ke sistem!")

elif menu == "👩‍⚕️ Tim Dokter Ahli":
    st.subheader("7 Dokter Spesialis & Praktisi Terbaik")
    df_dokter = pd.DataFrame({
        "Nama Dokter": ["dr. Cindy Permata, Sp.DV", "dr. Sarah Amelia, Sp.KK", "dr. Bella Jovita", "dr. Mega Putri", "dr. Alika Najwa", "dr. Rania Safira", "dr. Tasya Kamila"],
        "Keahlian": ["Spesialis Kulit", "Laser Specialist", "Injeksi & Botox", "Estetika Medis", "Anti-Aging", "Acne Care", "Glow Expert"],
        "Sertifikasi": ["Board Certified", "Laser Cert.", "Master Injector", "Diplomate Esthetic", "CIDESO", "Acne Expert", "Hydra Cert."]
    })
    st.table(df_dokter)

elif menu == "🔍 Diagnosis Wajah":
    st.subheader("Simulasi Diagnosis 10 Masalah Wajah")
    pilihan = st.selectbox("Apa Keluhan Wajah Kamu?", [
        "Jerawat Bruntusan", "Jerawat Batu", "Flek Hitam", "Bekas Jerawat", 
        "Kulit Kusam", "Pori-Pori Besar", "Garis Halus", "Kulit Kering", 
        "Mata Panda", "Berminyak Parah"
    ])
    
    diag_data = {
        "Jerawat Bruntusan": "Saran: Lakukan Facial Glow & gunakan serum BHA.",
        "Jerawat Batu": "Saran: Konsultasi dr. Rania untuk injeksi acne.",
        "Flek Hitam": "Saran: Treatment Laser Rejuvenation rutin.",
        "Bekas Jerawat": "Saran: Serum Niacinamide & Chemical Peeling.",
        "Kulit Kusam": "Saran: Diamond Glow treatment & Vitamin C.",
        "Pori-Pori Besar": "Saran: Penggunaan Retinol & clay mask rutin.",
        "Garis Halus": "Saran: Injeksi Botox oleh dr. Bella Jovita.",
        "Kulit Kering": "Saran: Hyaluronic Acid & Facial Hydration.",
        "Mata Panda": "Saran: Eye treatment & perbaiki pola tidur.",
        "Berminyak Parah": "Saran: Gunakan gel moisturizer & double cleansing."
    }
    
    if st.button("Lihat Hasil Diagnosis"):
        st.info(f"Diagnosis Awal: {pilihan}. \n\n {diag_data[pilihan]}")

elif menu == "🏢 Profil Klinik":
    st.subheader("Mengenal Klinik Cantik Caca")
    st.write("""
    Didirikan pada tahun 2018 di bawah kepemimpinan **Direktur Utama Caca Beautyani, S.ST**. 
    Klinik ini berfokus pada kesehatan kulit jangka panjang dengan teknologi medis terbaru.
    """)
    st.write("### 🏗️ Struktur Organisasi Utama")
    df_struktur = pd.DataFrame({
        "Jabatan": ["Direktur Utama", "Manager Operasional", "Kepala Medis", "Admin Keuangan", "Humas"],
        "Nama": ["Caca Beautyani, S.ST", "Dewi Sartika, SE", "dr. Cindy Permata, Sp.DV", "Sarah Amalia", "Anita Rahayu"]
    })
    st.table(df_struktur)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #FFB6C1;'>© 2026 Klinik Cantik Caca Dashboard | Dibuat dengan 💖</div>", unsafe_allow_html=True)