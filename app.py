import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Klinik Cantik Caca | Smart System", 
    page_icon="💖", 
    layout="wide"
)

# 2. CSS Kustom - Fix Kontras & Estetika
st.markdown("""
    <style>
    .stApp { background-color: #D81B60; }
    .klinik-title {
        color: #FFD1DC; text-align: center; font-size: 50px; font-weight: bold;
        text-shadow: 3px 3px #880E4F; font-family: 'Georgia', serif;
    }
    .klinik-slogan { color: #FFB6C1; text-align: center; font-style: italic; font-size: 20px; margin-bottom: 30px; }

    /* FIX TABEL & FORM agar teks terbaca jelas */
    .stTable { background-color: #FFD1DC !important; border-radius: 15px; }
    .stTable td, .stTable th { color: #880E4F !important; font-weight: bold !important; }
    input, select, [data-baseweb="select"] { background-color: #FFF0F5 !important; color: #880E4F !important; }
    label { color: #FFD1DC !important; font-weight: bold; }

    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #FFD1DC; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] h2 { color: #880E4F !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. Data Master Dokter & Keahlian (Mapping Otomatis)
# Data ini digunakan untuk menu Tim Dokter dan logika pendaftaran otomatis
data_klinik = {
    "Spesialis Kulit & Kelamin": {"dokter": "dr. Cindy Permata, Sp.DV", "jadwal": "Senin - Rabu (09:00 - 12:00)"},
    "Laser & Rejuvenation": {"dokter": "dr. Sarah Amelia, Sp.KK", "jadwal": "Kamis - Sabtu (13:00 - 16:00)"},
    "Injeksi Filler & Botox": {"dokter": "dr. Bella Jovita", "jadwal": "Selasa & Jumat (10:00 - 14:00)"},
    "Estetika Medis & Peeling": {"dokter": "dr. Mega Putri", "jadwal": "Senin - Jumat (15:00 - 18:00)"},
    "Anti-Aging Specialist": {"dokter": "dr. Alika Najwa", "jadwal": "Rabu & Sabtu (08:00 - 11:00)"},
    "Acne Care Expert": {"dokter": "dr. Rania Safira", "jadwal": "Setiap Hari (16:00 - 20:00)"},
    "Hydration & Facial Glow": {"dokter": "dr. Tasya Kamila", "jadwal": "Senin - Kamis (11:00 - 15:00)"}
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    menu = st.radio("Main Menu ✨", ["🏠 Dashboard", "📝 Pendaftaran Pintar", "👩‍⚕️ Tim Dokter Ahli", "🔍 Diagnosis Wajah", "🏢 Profil Klinik"])

# --- HEADER ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True)

# --- LOGIKA MENU ---

if menu == "🏠 Dashboard":
    st.subheader("Overview Aktivitas Klinik 🌸")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Pasien Hari Ini", "45", "↑12")
    c2.metric("Selesai", "32", "↑8")
    c3.metric("Menunggu", "13", "↓4")
    c4.metric("Status", "Buka")

elif menu == "📝 Pendaftaran Pintar":
    st.subheader("Pendaftaran Pasien Otomatis 🤖")
    with st.form("form_pendaftaran"):
        nama_pasien = st.text_input("Nama Lengkap Pasien")
        # Pilihan layanan berdasarkan keahlian 7 dokter
        layanan = st.selectbox("Pilih Layanan / Keluhan:", list(data_klinik.keys()))
        
        submit = st.form_submit_button("Daftar Sekarang ✨")
        
        if submit:
            if nama_pasien:
                # Logika Otomatis: Ambil dokter dan jadwal berdasarkan layanan yang dipilih
                dokter_terpilih = data_klinik[layanan]["dokter"]
                jadwal_periksa = data_klinik[layanan]["jadwal"]
                
                st.balloons()
                st.success(f"Pendaftaran Berhasil, {nama_pasien}!")
                st.markdown(f"""
                ### 💌 Kartu Antrean Digital
                * **Layanan:** {layanan}
                * **Dokter Yang Menangani:** {dokter_terpilih}
                * **Jadwal Periksa:** {jadwal_periksa}
                
                *Silakan datang 15 menit sebelum jadwal dimulai.*
                """)
            else:
                st.error("Mohon isi nama pasien terlebih dahulu.")

elif menu == "👩‍⚕️ Tim Dokter Ahli":
    st.subheader("7 Dokter Spesialis & Jadwal Praktik")
    # Mengubah dictionary ke DataFrame untuk tabel
    df_dokter = pd.DataFrame([
        {"Nama Dokter": v["dokter"], "Keahlian": k, "Jadwal Praktik": v["jadwal"]} 
        for k, v in data_klinik.items()
    ])
    st.table(df_dokter)

elif menu == "🔍 Diagnosis Wajah":
    st.subheader("Simulasi Diagnosis 10 Masalah Wajah")
    pilihan = st.selectbox("Pilih Keluhan:", ["Jerawat Bruntusan", "Jerawat Batu", "Flek Hitam", "Bekas Jerawat", "Kulit Kusam", "Pori-Pori Besar", "Garis Halus", "Kulit Kering", "Mata Panda", "Berminyak"])
    if st.button("Analisis"):
        st.info(f"Hasil awal: {pilihan}. Segera daftar di menu pendaftaran untuk penanganan lebih lanjut.")

elif menu == "🏢 Profil Klinik":
    st.subheader("Mengenal Klinik Cantik Caca")
    st.write("Dibawah kepemimpinan **Direktur Utama Caca Beautyani, S.ST** sejak 2018.")
    st.write("### 🏗️ Struktur Organisasi Utama")
    df_struktur = pd.DataFrame({
        "Jabatan": ["Direktur Utama", "Manager Operasional", "Kepala Medis", "Admin", "Humas"],
        "Nama": ["Caca Beautyani, S.ST", "Dewi Sartika, SE", "dr. Cindy Permata, Sp.DV", "Sarah Amalia", "Anita Rahayu"]
    })
    st.table(df_struktur)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #FFB6C1;'>© 2026 Klinik Cantik Caca Dashboard</div>", unsafe_allow_html=True)