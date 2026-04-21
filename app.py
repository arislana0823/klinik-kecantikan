import streamlit as st
import pandas as pd
import time
from datetime import date

# 1. Konfigurasi Halaman (Estetik & Berwarna)
st.set_page_config(
    page_title="Klinik Cantik Caca | Perawatan Kulit Impian", 
    page_icon="💖", 
    layout="wide",
    initial_sidebar_state="expanded" # Kita pakai sidebar untuk navigasi menu utama
)

# --- FUNGSI LOAD DATA (Placeholder biar gak error) ---
def load_data():
    return pd.DataFrame()

# 2. CSS Kustom "Ultra Soft Pink & User Friendly"
# Kita buat desain yang bersih, kotak-kotak bulat (rounded), dan warna-warni ceria.
st.markdown("""
    <style>
    /* 1. Background Utama - Soft Pink */
    .stApp { background-color: #FFF0F5; }
    
    /* 2. Judul Utama (Estetik) */
    .klinik-title {
        color: #D81B60; 
        font-family: 'Georgia', serif; 
        text-align: center; 
        font-size: 50px; 
        font-weight: bold;
        text-shadow: 2px 2px #FFD1DC;
        margin-top: -20px;
    }
    
    /* 3. Slogan Motivasi (Italic) */
    .klinik-slogan {
        color: #C71585; 
        font-family: 'Times New Roman', serif; 
        text-align: center; 
        font-style: italic; 
        font-size: 20px;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    
    /* 4. Kustomisasi Sidebar (Menu Samping) */
    [data-testid="stSidebar"] {
        background-color: #FFD1DC; /* Pink yang sedikit lebih gelap */
    }
    
    /* 5. Box/Card Estetik (Header Menu) */
    .stHeader {
        background-color: #FFB6C1;
        padding: 10px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-weight: bold;
    }
    
    /* 6. Kustomisasi Tabel */
    .stDataFrame {
        border-radius: 10px;
        border: 1px solid #FFB6C1;
    }
    
    /* 7. Box Menu Utama (Di Sidebar) */
    .sidebar-menu {
        padding: 10px;
        background-color: white;
        border-radius: 10px;
        margin-bottom: 5px;
        border-left: 5px solid #D81B60;
    }

</style>
""", unsafe_allow_html=True) # <--- JANGAN LUPA INI!

# --- SIDEBAR & NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Logo Klinik
    st.markdown("<h2 style='color: #D81B60; text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio(
        "Main Menu ✨",
        ["💖 Home & Jadwal", "📝 Pendaftaran Pasien", "👩‍⚕️ Profil Dokter", "🔍 Diagnosis & Obat", "🏢 Tentang Klinik"],
        key="nav_menu"
    )
    st.markdown("---")
    st.info("💡 Tip: Gunakan menu 'Pendaftaran' untuk pendaftaran pasien baru.")

# --- KONTEN UTAMA ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True) #
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True) #


# --- MENU 1: HOME & JADWAL PASIEN ---
if menu == "💖 Home & Jadwal":
    st.subheader("Overview Jadwal Hari Ini 🌸")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Pasien Hari Ini", "12", "↑3")
    with col2:
        st.metric("Pasien Selesai", "8", "↑5")
    with col3:
        st.metric("Pasien Menunggu", "4", "↓2")
    with col4:
        st.metric("Layanan Populer", "Facial Glow", "Hot!")

    st.markdown("---")
    
    # JADWAL KEDATANGAN PASIEN (Tabel)
    st.write("### 📅 Jadwal Antrean Pasien")
    data_antrean = {
        "No Antrean": [101, 102, 103, 104, 105],
        "Nama Pasien": ["Rina", "Santi", "Siska", "Dewi", "Anita"],
        "Layanan": ["Facial Glow", "Peeling", "Botox", "Facial Glow", "Laser Whitening"],
        "Dokter": ["dr. Cindy", "dr. Sarah", "dr. Bella", "dr. Cindy", "dr. Mega"],
        "Jam Datang": ["08:00", "08:30", "09:00", "09:15", "09:45"],
        "Status": ["Selesai", "Selesai", "Menunggu", "Menunggu", "Menunggu"]
    }
    st.table(pd.DataFrame(data_antrean))
    st.markdown("<p style='text-align: center; color: gray;'>Tip: Gunakan menu 'Pendaftaran' untuk pendaftaran baru.</p>", unsafe_allow_html=True)


# --- MENU 2: PENDAFTARAN PASIEN ---
elif menu == "📝 Pendaftaran Pasien":
    st.subheader("Formulir Pendaftaran Pasien Baru ✍️")
    with st.form("form_regis"):
        nama_pasien = st.text_input("Nama Lengkap Pasien")
        umur_pasien = st.slider("Umur (Tahun)", 15, 60, 25)
        tanggal_daftar = st.date_input("Tanggal Pendaftaran", date.today())
        layanan_pilihan = st.selectbox("Pilih Layanan", ["Facial Glow", "Laser Whitening", "Peeling", "Botox", "Consultation Only"])
        pesan_tambahan = st.text_area("Keluhan/Catatan Tambahan")
        submit_pendaftaran = st.form_submit_button("Daftar Sekarang ✨")
        
        if submit_pendaftaran:
            with st.spinner('Menyimpan data...'):
                time.sleep(1)
                st.balloons()
                st.success(f"Selamat! {nama_pasien} telah terdaftar untuk {layanan_pilihan} pada {tanggal_daftar}.")


# --- MENU 3: PROFIL 5 DOKTER & SERTIFIKASI ---
elif menu == "👩‍⚕️ Profil Dokter":
    st.subheader("Tim Dokter Spesialis & Sertifikasi 💖")
    
    # 5 DOKTER CANTIK (Placeholder Data)
    dokter_data = {
        "Nama Dokter": ["dr. Cindy Permata, Sp.DV", "dr. Sarah Amelia, Sp.KK", "dr. Bella Jovita", "dr. Mega Putri", "dr. Alika Najwa"],
        "Keahlian": ["Skin Specialist", "Laser Whitening", "Injeksi & Filler", "Estetika Medis", "Anti-Aging"],
        "Jam Praktek": ["08:00 - 12:00", "13:00 - 17:00", "18:00 - 21:00", "08:00 - 17:00 (Sab)", "08:00 - 12:00 (Sen-Rab)"],
        "Sertifikasi": ["CNA (Cosmetic)", "Dermatologist Certified", "Filler Certified", "Esthetician Certified", "Geriatric Skin Certified"]
    }
    
    # Kita buat 5 Kolom atau 1 Kolom besar (Tabel)
    st.table(pd.DataFrame(dokter_data))
    st.info("💡 Semua dokter kami telah memiliki sertifikasi internasional di bidang estetika.")


# --- MENU 4: DIAGNOSIS & OBAT ---
elif menu == "🔍 Diagnosis & Obat":
    st.subheader("Simulasi Diagnosis Awal & Rekomendasi 🧪")
    st.markdown("<p style='color: gray; font-style: italic;'>Tip: Ini adalah diagnosis awal otomatis, silakan konsultasi ke dokter untuk diagnosis lengkap.</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 3])
    with col1:
        st.write("### Pilih Kondisi Kulit")
        kondisi = st.selectbox("Jenis Masalah Kulit:", ["Jerawat Ringan", "Jerawat Parah", "Flek Hitam (Melasma)", "Kerutan Halus", "Kulit Kering"])
        pilih_diagnosis = st.button(" Diagnosis Sekarang!")
        
    if pilih_diagnosis:
        with col2:
            st.write("### 📋 Hasil Diagnosis Awal")
            if kondisi == "Jerawat Ringan":
                st.write("**Diagnosis:** Jerawat hormon biasa atau papula ringan.")
                st.write("**Saran:** Jaga kebersihan wajah, gunakan cleanser yang tepat.")
                st.markdown("<p style='color: #D81B60;'><b>Rekomendasi Obat:</b> Cleansing Gel, Acne Spot Gel, Moisturizer.</p>", unsafe_allow_html=True)
            elif kondisi == "Jerawat Parah":
                st.write("**Diagnosis:** Acne Vulgaris tingkat lanjut.")
                st.write("**Saran:** Wajib konsultasi ke dr. Cindy untuk resep obat."),
                st.markdown("<p style='color: #D81B60;'><b>Rekomendasi Obat:</b> Salep antibiotik, Oral medication (butuh resep).</p>", unsafe_allow_html=True)
            elif kondisi == "Flek Hitam (Melasma)":
                st.write("**Diagnosis:** Hiperpigmentasi kronis.")
                st.write("**Saran:** Laser Whitening oleh dr. Sarah sangat dianjurkan.")
                st.markdown("<p style='color: #D81B60;'><b>Rekomendasi Obat:</b> Sunscreen SPF 50+, Vitamin C Serum.</p>", unsafe_allow_html=True)
            elif kondisi == "Kerutan Halus":
                st.write("**Diagnosis:** Tanda penuaan dini.")
                st.write("**Saran:** Botox Injeksi oleh dr. Bella untuk hasil instan.")
                st.markdown("<p style='color: #D81B60;'><b>Rekomendasi Obat:</b> Retinol Serum, Collagen Supplements.</p>", unsafe_allow_html=True)
            elif kondisi == "Kulit Kering":
                st.write("**Diagnosis:** Kulit mengalami dehidrasi kronis.")
                st.write("**Saran:** Facial Glow secara rutin untuk menghidrasi kulit.")
                st.markdown("<p style='color: #D81B60;'><b>Rekomendasi Obat:</b> Cleanser tanpa sabun, Hyaluronic Acid Cream.</p>", unsafe_allow_html=True)
            st.markdown("<p style='color: gray; font-style: italic; font-size: 12px;'>Rekomendasi obat di atas bukan resep medis final.</p>", unsafe_allow_html=True)


# --- MENU 5: TENTANG KLINIK ---
elif menu == "🏢 Tentang Klinik":
    st.subheader("Profil Klinik Cantik Caca 🏢")
    
    col_kiri, col_kanan = st.columns([1, 2])
    with col_kiri:
        st.image("https://cdn-icons-png.flaticon.com/512/3241/3241517.png", width=150)
    with col_kanan:
        st.write("Klinik Cantik Caca adalah tempat perawatan kulit terpadu yang memadukan keahlian dermatologi dengan teknologi estetika modern. Kami hadir untuk mewujudkan impianmu memiliki kulit yang sehat, cerah, dan tampak lebih muda. Kenyamanan pasien dan hasil yang natural adalah prioritas utama kami.")

    st.markdown("---")
    
    # STRUKTUR ORGANISASI (Tabel)
    st.write("### 🏗️ Struktur Organisasi Klinik")
    data_struktur = {
        "Jabatan": ["Direktur Utama", "Manager Operasional", "Humas", "Admin Keuangan", "Penanggung Jawab Medis"],
        "Nama": ["Caca Beautyani, S.ST", "Dewi Sartika, SE", "Anita Rahayu, S.Ikom", "Sarah Amalia, A.Md.Ak", "dr. Cindy Permata, Sp.DV"],
        "Divisi": ["Manajemen", "Operasional", "Marketing", "Finance", "Medis"]
    }
    st.table(pd.DataFrame(data_struktur))
    st.info("💡 Semua staf medis kami telah memiliki sertifikasi internasional di bidang estetika.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #D87093;'>Klinik Cantik Caca Dashboard © 2026 | Dibuat dengan 💖 untuk Klinik Kecantikan</div>", unsafe_allow_html=True) #