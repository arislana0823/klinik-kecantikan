import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Klinik Cantik Caca | Smart Clinic", 
    page_icon="💖", 
    layout="wide"
)

# 2. CSS Kustom - High Contrast Pink
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

# 3. Data Master Dokter & Layanan
data_klinik = {
    "Spesialis Kulit & Kelamin": {"dokter": "dr. Cindy Permata, Sp.DV", "jadwal": "Senin - Rabu (09:00 - 12:00)"},
    "Laser & Rejuvenation": {"dokter": "dr. Sarah Amelia, Sp.KK", "jadwal": "Kamis - Sabtu (13:00 - 16:00)"},
    "Injeksi Filler & Botox": {"dokter": "dr. Bella Jovita", "jadwal": "Selasa & Jumat (10:00 - 14:00)"},
    "Estetika Medis & Peeling": {"dokter": "dr. Mega Putri", "jadwal": "Senin - Jumat (15:00 - 18:00)"},
    "Anti-Aging Specialist": {"dokter": "dr. Alika Najwa", "jadwal": "Rabu & Sabtu (08:00 - 11:00)"},
    "Acne Care Expert": {"dokter": "dr. Rania Safira", "jadwal": "Setiap Hari (16:00 - 20:00)"},
    "Hydration & Facial Glow": {"dokter": "dr. Tasya Kamila", "jadwal": "Senin - Kamis (11:00 - 15:00)"}
}

# 4. Data Master Diagnosis & Rekomendasi Produk
diagnosis_db = {
    "Jerawat Bruntusan": {
        "obat": "Pengobatan topikal dengan Salicylic Acid (BHA) untuk membersihkan pori.",
        "produk": "Caca Glow Purifying Toner, BHA Exfoliating Serum, & Lightweight Gel Moisturizer."
    },
    "Jerawat Batu": {
        "obat": "Injeksi intralesi oleh dokter dan penggunaan Benzoyl Peroxide.",
        "produk": "Caca Intensive Acne Spot, Gentle Cleanser Low pH, & Sunscreen Non-Comedogenic."
    },
    "Flek Hitam": {
        "obat": "Terapi Laser Q-Switched dan krim malam pencerah (Retinoid).",
        "produk": "Caca Brightening Night Cream, Vitamin C Serum, & SPF 50 Broad Spectrum."
    },
    "Bekas Jerawat": {
        "obat": "Chemical Peeling atau Microneedling untuk stimulasi kolagen.",
        "produk": "Caca Dark Spot Eraser, Niacinamide 10% Serum, & Snail Mucin Essence."
    },
    "Kulit Kusam": {
        "obat": "Diamond Glow Facial dan eksfoliasi rutin 2x seminggu.",
        "produk": "Caca Radiance Face Wash, Glycolic Acid Toner, & Glass Skin Moisturizer."
    },
    "Pori-Pori Besar": {
        "obat": "Penggunaan Retinol malam hari dan Pore-Tightening Treatment.",
        "produk": "Caca Poreless Serum, Bamboo Charcoal Mask, & Oil-Free Hydrating Gel."
    },
    "Garis Halus": {
        "obat": "Injeksi Botox atau Filler untuk mengisi kekosongan jaringan.",
        "produk": "Caca Youthful Peptide Cream, Retinol Encapsulated Serum, & Eye Lift Gel."
    },
    "Kulit Sangat Kering": {
        "obat": "Deep Hydration Treatment dan penguncian kelembapan kulit.",
        "produk": "Caca Barrier Repair Cream, Hyaluronic Acid Serum, & Facial Oil Marula."
    },
    "Mata Panda": {
        "obat": "Under Eye Laser Treatment dan pijat drainase limfatik.",
        "produk": "Caca Bright Eye Serum (Caffeine), Cooling Eye Mask, & Rich Night Eye Cream."
    },
    "Berminyak Parah": {
        "obat": "Double cleansing rutin dan penggunaan masker tanah liat.",
        "produk": "Caca Oil-Control Cleanser, Matte Sunscreen, & Mugwort Clay Mask."
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    menu = st.radio("Main Menu ✨", ["🏠 Dashboard", "🔍 Diagnosis Pintar", "📝 Pendaftaran Otomatis", "👩‍⚕️ Tim Dokter", "🏢 Profil Klinik"])

# --- HEADER ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True)

# --- MENU: DIAGNOSIS PINTAR ---
if menu == "🔍 Diagnosis Pintar":
    st.subheader("Simulasi Diagnosis & Rekomendasi Produk 🧪")
    pilihan = st.selectbox("Apa Keluhan Wajah Kamu Saat Ini?", list(diagnosis_db.keys()))
    
    if st.button("Dapatkan Analisis Cepat ✨"):
        hasil = diagnosis_db[pilihan]
        st.markdown(f"""
        <div style="background-color: #FFD1DC; padding: 20px; border-radius: 15px; border: 2px solid #880E4F;">
            <h3 style="color: #880E4F !important; margin-top: 0;">📋 Hasil Diagnosis: {pilihan}</h3>
            <p style="color: #880E4F !important;"><b>🏥 Pengobatan Awal:</b><br>{hasil['obat']}</p>
            <p style="color: #880E4F !important;"><b>🛍️ Rekomendasi Produk Caca Skincare:</b><br>{hasil['produk']}</p>
            <hr style="border-color: #880E4F;">
            <p style="color: #880E4F !important; font-style: italic;">Segera ke menu <b>Pendaftaran Otomatis</b> untuk konsultasi lebih mendalam dengan dokter ahli kami.</p>
        </div>
        """, unsafe_allow_html=True)

# --- MENU: PENDAFTARAN OTOMATIS ---
elif menu == "📝 Pendaftaran Otomatis":
    st.subheader("Booking Jadwal Tanpa Ribet 🤖")
    with st.form("form_pendaftaran"):
        nama_pasien = st.text_input("Nama Lengkap Pasien")
        layanan = st.selectbox("Pilih Layanan Sesuai Kebutuhan:", list(data_klinik.keys()))
        
        if st.form_submit_button("Daftar Sekarang ✨"):
            if nama_pasien:
                info = data_klinik[layanan]
                st.balloons()
                st.markdown(f"""
                <div style="background-color: #FFD1DC; padding: 20px; border-radius: 15px; border: 2px solid #880E4F;">
                    <h3 style="color: #880E4F !important; margin-top: 0;">✅ Pendaftaran Berhasil!</h3>
                    <p style="color: #880E4F !important;">Halo <b>{nama_pasien}</b>, Berikut detail jadwal kamu:</p>
                    <ul style="color: #880E4F !important;">
                        <li><b>Layanan:</b> {layanan}</li>
                        <li><b>Dokter:</b> {info['dokter']}</li>
                        <li><b>Jadwal Periksa:</b> {info['jadwal']}</li>
                    </ul>
                    <p style="color: #880E4F !important;"><i>Mohon tunjukkan kartu digital ini di resepsionis.</i></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Silakan isi nama pasien dulu ya!")

# --- MENU: DASHBOARD ---
elif menu == "🏠 Dashboard":
    st.subheader("Status Klinik Hari Ini 🌸")
    c1, c2, c3 = st.columns(3)
    c1.metric("Antrean", "12 Orang", "↑2")
    c2.metric("Pasien Selesai", "28 Orang", "↑5")
    c3.metric("Status", "Buka", border=True)

# --- MENU: TIM DOKTER ---
elif menu == "👩‍⚕️ Tim Dokter":
    st.subheader("7 Dokter Spesialis & Jadwal Praktik")
    df_dokter = pd.DataFrame([
        {"Dokter": v["dokter"], "Bidang": k, "Jadwal": v["jadwal"]} 
        for k, v in data_klinik.items()
    ])
    st.table(df_dokter)

# --- MENU: PROFIL KLINIK ---
elif menu == "🏢 Profil Klinik":
    st.subheader("Mengenal Klinik Cantik Caca")
    st.write("Dibawah kepemimpinan **Direktur Utama Caca Beautyani, S.ST** sejak 2018.")
    st.table(pd.DataFrame({
        "Jabatan": ["Direktur Utama", "Manager", "Kepala Medis", "Humas"],
        "Nama": ["Caca Beautyani, S.ST", "Dewi Sartika, SE", "dr. Cindy Permata, Sp.DV", "Anita Rahayu"]
    }))

st.markdown("---")
st.markdown("<div style='text-align: center; color: #FFB6C1;'>Klinik Cantik Caca © 2026</div>", unsafe_allow_html=True)