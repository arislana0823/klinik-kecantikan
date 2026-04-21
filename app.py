import streamlit as st
import pandas as pd
import time

# 1. Konfigurasi Halaman (Wajib di Paling Atas)
st.set_page_config(page_title="BeautyCare Pro", page_icon="💖", layout="wide")

# 2. CSS Kustom (Warna-warni & Estetik)
st.markdown("""
    <style>
    /* Background Utama */
    .main { background-color: #FFF5F7; }
    
    /* Judul Utama */
    .title-text {
        color: #D81B60;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
        font-size: 50px;
        text-shadow: 2px 2px #FFB6C1;
    }
    
    /* Box Statistik */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 10px solid #FF69B4;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3409/3409355.png", width=100)
    st.title("Admin Beauty")
    menu = st.radio("Pilih Menu:", ["🏠 Dashboard", "📝 Pendaftaran", "👩‍⚕️ Jadwal Dokter", "💰 Laporan Kasir"])

# --- MENU 1: DASHBOARD ---
if menu == "🏠 Dashboard":
    st.markdown("<h1 class='title-text'>BeautyCare Dashboard</h1>", unsafe_allow_html=True)
    
    # Baris Statistik
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-card'><h3>💖 Pasien Baru</h3><h2>24</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'><h3>✨ Treatment</h3><h2>142</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-card'><h3>💸 Omzet</h3><h2>Rp 45.2M</h2></div>", unsafe_allow_html=True)

    st.write("### Grafik Tren Kunjungan")
    chart_data = pd.DataFrame({'Hari': ['Sen', 'Sel', 'Rab', 'Kam', 'Jum'], 'Pasien': [10, 25, 15, 30, 45]})
    st.line_chart(chart_data.set_index('Hari'))

# --- MENU 2: PENDAFTARAN ---
elif menu == "📝 Pendaftaran":
    st.header("Form Pendaftaran Pasien")
    with st.form("form_regis"):
        nama = st.text_input("Nama Pasien")
        umur = st.slider("Umur", 15, 60, 25)
        keluhan = st.text_area("Keluhan Kulit")
        submit = st.form_submit_button("Simpan Data")
        
        if submit:
            with st.spinner('Mencatat data...'):
                time.sleep(1)
                st.balloons()
                st.success(f"Data {nama} berhasil disimpan ke sistem!")

# --- MENU 3: JADWAL DOKTER ---
elif menu == "👩‍⚕️ Jadwal Dokter":
    st.header("Jadwal Praktek Dokter Spesialis")
    data_dokter = {
        "Nama Dokter": ["dr. Cindy (Skin)", "dr. Sarah (Laser)", "dr. Bella (Filler)"],
        "Jam Praktek": ["08:00 - 12:00", "13:00 - 17:00", "18:00 - 21:00"],
        "Status": ["Tersedia", "Penuh", "Tersedia"]
    }
    st.table(pd.DataFrame(data_dokter))

# --- MENU 4: LAPORAN KASIR ---
elif menu == "💰 Laporan Kasir":
    st.header("Laporan Transaksi Hari Ini")
    df_transaksi = pd.DataFrame({
        "No": [1, 2, 3],
        "Pasien": ["Rina", "Santi", "Dewi"],
        "Layanan": ["Facial", "Peeling", "Botox"],
        "Total": ["500k", "750k", "2.5M"]
    })
    st.dataframe(df_transaksi, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Dibuat dengan ✨ untuk klinik tercinta</p>", unsafe_allow_html=True)