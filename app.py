import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Klinik Cantik Caca | Premium Aesthetics", 
    page_icon="💖", 
    layout="wide"
)

# 2. CSS Kustom - Full Contrast & Premium Styling
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

    /* BOX HASIL (OUTPUT CARD) - Memaksa teks berwarna Pink Tua Pekat */
    .result-box {
        background-color: #FFD1DC; 
        padding: 25px; 
        border-radius: 15px; 
        border: 3px solid #880E4F;
        margin-top: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
    }
    .result-box h3, .result-box p, .result-box li, .result-box b {
        color: #880E4F !important; /* Pink Tua sangat gelap agar terbaca */
    }

    /* FIX TABEL: Background Pink Soft, Teks Pink Tua */
    .stTable { background-color: #FFD1DC !important; border-radius: 15px; overflow: hidden; }
    .stTable td, .stTable th { 
        color: #880E4F !important; 
        font-weight: bold !important; 
        font-size: 16px !important;
        border-bottom: 1px solid #D81B60 !important;
    }

    /* FIX FORM & INPUT: Teks input tidak boleh putih */
    input, select, textarea, [data-baseweb="select"] {
        background-color: #FFF0F5 !important;
        color: #880E4F !important;
    }
    label { color: #FFD1DC !important; font-weight: bold; }

    /* Metrik Dashboard */
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-weight: bold; }
    [data-testid="stMetricLabel"] { color: #FFB6C1 !important; }

    /* Sidebar Customization */
    [data-testid="stSidebar"] { background-color: #FFD1DC; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] h2 { color: #880E4F !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. Data Master: Dokter & Diagnosis
data_klinik = {
    "Spesialis Kulit & Kelamin": {"dokter": "dr. Cindy Permata, Sp.DV", "jadwal": "Senin - Rabu (09:00 - 12:00)"},
    "Laser & Rejuvenation": {"dokter": "dr. Sarah Amelia, Sp.KK", "jadwal": "Kamis - Sabtu (13:00 - 16:00)"},
    "Injeksi Filler & Botox": {"dokter": "dr. Bella Jovita", "jadwal": "Selasa & Jumat (10:00 - 14:00)"},
    "Estetika Medis & Peeling": {"dokter": "dr. Mega Putri", "jadwal": "Senin - Jumat (15:00 - 18:00)"},
    "Anti-Aging Specialist": {"dokter": "dr. Alika Najwa", "jadwal": "Rabu & Sabtu (08:00 - 11:00)"},
    "Acne Care Expert": {"dokter": "dr. Rania Safira", "jadwal": "Setiap Hari (16:00 - 20:00)"},
    "Hydration & Facial Glow": {"dokter": "dr. Tasya Kamila", "jadwal": "Senin - Kamis (11:00 - 15:00)"}
}

diagnosis_db = {
    "Jerawat Bruntusan": {"obat": "Pengobatan BHA 2% & Clay Mask.", "produk": "Caca Glow Purifying Toner & BHA Serum."},
    "Jerawat Batu": {"obat": "Injeksi Intralesi (Dokter) & Benzoyl Peroxide.", "produk": "Caca Intensive Acne Spot & Gentle Cleanser."},
    "Flek Hitam": {"obat": "Laser Q-Switched & Krim Retinoid.", "produk": "Caca Brightening Night Cream & Sunscreen SPF 50."},
    "Bekas Jerawat": {"obat": "Chemical Peeling Medis & Microneedling.", "produk": "Caca Dark Spot Eraser & Serum Niacinamide 10%."},
    "Kulit Kusam": {"obat": "Diamond Glow Facial & Eksfoliasi AHA.", "produk": "Caca Radiance Face Wash & Glass Skin Moisturizer."},
    "Pori-Pori Besar": {"obat": "Treatment Microneedle & Toning Solution.", "produk": "Caca Poreless Serum & Bamboo Charcoal Mask."},
    "Garis Halus": {"obat": "Terapi Botox Injeksi & Filler.", "produk": "Caca Youthful Peptide Cream & Retinol Encapsulated."},
    "Kulit Sangat Kering": {"obat": "Deep Hydration Infusion & Barrier Repair.", "produk": "Caca Barrier Repair Cream & Hyaluronic Acid."},
    "Mata Panda": {"obat": "Under Eye Laser & Pijat Limfatik.", "produk": "Caca Bright Eye Caffeine Serum & Eye Lift Gel."},
    "Berminyak Parah": {"obat": "Double Cleansing & Pengaturan Sebum.", "produk": "Caca Oil-Control Cleanser & Matte Sunscreen."}
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='text-align: center;'>Beauty Suite</h2>", unsafe_allow_html=True)
    menu = st.radio("Main Menu ✨", ["🏠 Dashboard", "🔍 Konsultasi Wajah Otomatis", "📝 Pendaftaran Otomatis", "👩‍⚕️ Tim Dokter", "🏢 Profil Klinik"])

# --- HEADER ---
st.markdown("<h1 class='klinik-title'>KLINIK CANTIK CACA</h1>", unsafe_allow_html=True)
st.markdown("<p class='klinik-slogan'>\"Kecantikanmu adalah keajaiban dunia, rawatlah dengan cinta.\"</p>", unsafe_allow_html=True)

# --- MENU: KONSULTASI WAJAH OTOMATIS ---
if menu == "🔍 Konsultasi Wajah Otomatis":
    st.subheader("Konsultasi Pakar Instan 🧪")
    pilihan = st.selectbox("Pilih Keluhan Wajah Anda Saat Ini:", list(diagnosis_db.keys()))
    
    if st.button("Dapatkan Analisis Sekarang ✨"):
        hasil = diagnosis_db[pilihan]
        st.markdown(f"""
        <div class="result-box">
            <h3>📋 Hasil Konsultasi: {pilihan}</h3>
            <p><b>🏥 Pengobatan Awal:</b> {hasil['obat']}</p>
            <p><b>🛍️ Rekomendasi Produk:</b> {hasil['produk']}</p>
            <hr style="border-color: #880E4F;">
            <p style="font-size: 14px;"><i>Catatan: Hasil ini adalah diagnosis awal. Untuk hasil maksimal, silakan daftar konsultasi langsung.</i></p>
        </div>
        """, unsafe_allow_html=True)

# --- MENU: PENDAFTARAN OTOMATIS ---
elif menu == "📝 Pendaftaran Otomatis":
    st.subheader("Reservasi Jadwal Pasien 🤖")
    with st.form("form_pendaftaran"):
        nama_pasien = st.text_input("Nama Lengkap Pasien")
        layanan_pilihan = st.selectbox("Pilih Layanan / Keluhan Utama:", list(data_klinik.keys()))
        
        if st.form_submit_button("Daftar Sekarang ✨"):
            if nama_pasien:
                info = data_klinik[layanan_pilihan]
                st.balloons()
                st.markdown(f"""
                <div class="result-box">
                    <h3>✅ Reservasi Berhasil!</h3>
                    <p>Halo <b>{nama_pasien}</b>, reservasi Anda telah tercatat dalam sistem kami.</p>
                    <ul>
                        <li><b>Layanan:</b> {layanan_pilihan}</li>
                        <li><b>Dokter Ahli:</b> {info['dokter']}</li>
                        <li><b>Jadwal Praktik:</b> {info['jadwal']}</li>
                    </ul>
                    <p><i>Mohon tunjukkan bukti pendaftaran ini di meja resepsionis saat kedatangan.</i></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Mohon isi nama lengkap Anda.")

# --- MENU: PROFIL KLINIK (SEJARAH PANJANG) ---
elif menu == "🏢 Profil Klinik":
    st.subheader("Sejarah & Visi Klinik Cantik Caca")
    st.markdown("""
    <p style='color: #FFD1DC; text-align: justify; line-height: 1.6;'>
    Didirikan pada awal tahun 2018, Klinik Cantik Caca bermula dari sebuah visi besar <b>Direktur Utama Caca Beautyani, S.ST</b> 
    untuk menghadirkan standar perawatan kulit premium yang personal dan terjangkau bagi semua kalangan. <br><br>
    Berawal dari sebuah praktek mandiri yang berfokus pada kesehatan kulit alami, klinik ini berkembang pesat berkat kepercayaan 
    masyarakat akan hasil yang nyata dan aman. Hingga tahun 2026 ini, kami telah sukses melayani lebih dari <b>15.000 pasien</b> 
    dengan berbagai kasus kulit, mulai dari acne management hingga rejuvenasi anti-aging. <br><br>
    Kami berkomitmen untuk terus mengadopsi teknologi estetika terbaru dari Korea dan Eropa, memastikan setiap pasien mendapatkan 
    perawatan berbasis sains (science-based skin care). Di bawah kepemimpinan Caca, kami tidak hanya memperbaiki penampilan luar, 
    tetapi juga membangun kepercayaan diri melalui kulit yang sehat dari dalam. Kami percaya bahwa setiap wajah adalah kanvas yang unik, 
    dan kami di sini untuk menjaganya tetap bercahaya.
    </p>
    """, unsafe_allow_html=True)
    
    st.write("### 🏗️ Struktur Kepemimpinan & Manajemen")
    df_struktur = pd.DataFrame({
        "Jabatan": ["Direktur Utama", "Manager Operasional", "Kepala Medis", "Humas & Marketing", "Admin Keuangan"],
        "Nama": ["Caca Beautyani, S.ST", "Dewi Sartika, SE", "dr. Cindy Permata, Sp.DV", "Anita Rahayu, S.Ikom", "Sarah Amalia, A.Md"]
    })
    st.table(df_struktur)

# --- MENU LAINNYA ---
elif menu == "🏠 Dashboard":
    st.subheader("Dashboard Klinik Hari Ini 🌸")
    c1, c2, c3 = st.columns(3)
    c1.metric("Antrean", "12 Orang", "↑2")
    c2.metric("Selesai", "28 Orang", "↑5")
    c3.metric("Status", "BUKA")
elif menu == "👩‍⚕️ Tim Dokter":
    st.subheader("7 Tenaga Medis Spesialis")
    df_dokter = pd.DataFrame([{"Dokter": v["dokter"], "Bidang Ahli": k, "Jadwal": v["jadwal"]} for k, v in data_klinik.items()])
    st.table(df_dokter)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #FFB6C1;'>Klinik Cantik Caca | Excellence in Aesthetics & Skin Health © 2026</div>", unsafe_allow_html=True)