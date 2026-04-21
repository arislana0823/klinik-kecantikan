import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURATION HALAMAN ---
st.set_page_config(
    page_title="BeautyCare Dashboard | ✨",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS UNTUK TEMA "CEWEK BANGET" ---
st.markdown("""
<style>
    /* 1. Ganti Font Global */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        color: #4A4A4A; /* Abu-abu Gelap untuk Teks Utama */
    }

    /* 2. Latar Belakang Utama (Putih Bersih dengan Aksen Pink Fade) */
    .stApp {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF0F5 100%);
    }

    /* 3. Kustomisasi Sidebar (Pink Lembut & Elegant) */
    [data-testid="stSidebar"] {
        background-color: #FFC0CB !important; /* Pink Muda */
        background-image: linear-gradient(180deg, #FFC0CB 0%, #FFB6C1 100%);
        border-right: 2px solid #FF69B4; /* Hot Pink Border */
    }
    
    [data-testid="stSidebar"] .css-17eq0hr { /* Sidebar Title */
        color: #8B008B !important; /* Dark Magenta */
        font-weight: 600;
    }

    /* 4. Kustomisasi Tombol Navigasi Sidebar */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        border: 1px solid transparent !important;
        color: #4A4A4A !important;
        border-radius: 20px !important;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] button:hover {
        background-color: #FF69B4 !important; /* Hot Pink hover */
        color: white !important;
        border: 1px solid #FF1493 !important;
    }
    
    [data-testid="stSidebar"] button[aria-selected="true"] {
        background-color: #FF1493 !important; /* Deep Pink Active */
        color: white !important;
        font-weight: 600;
        box-shadow: 0px 4px 10px rgba(255, 20, 147, 0.4);
    }

    /* 5. Kustomisasi Teks Judul & Subjudul */
    h1, h2, h3 {
        color: #D87093 !important; /* Pale Violet Red */
        font-weight: 600;
    }
    
    .stSubheader {
        color: #C71585 !important; /* Medium Violet Red */
    }

    /* 6. Kustomisasi Input & Form */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stDateInput>div>div>input {
        border-radius: 10px !important;
        border: 2px solid #FFB6C1 !important; /* Light Pink Border */
        background-color: white !important;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #FF69B4 !important;
        box-shadow: 0 0 0 0.2rem rgba(255, 105, 180, 0.25);
    }

    /* 7. Kustomisasi Tombol Utama (Aksen Rose Gold) */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #FF69B4, #D87093) !important;
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 25px !important;
        font-weight: 600 !important;
        box-shadow: 0px 4px 15px rgba(216, 112, 147, 0.4);
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:first-child:hover {
        background: linear-gradient(45deg, #D87093, #C71585) !important;
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(216, 112, 147, 0.6);
    }

    /* 8. Kustomisasi Alert/Pesan Sukses */
    .stAlert {
        border-radius: 15px !important;
        background-color: #FFF0F5 !important; /* Lavender Blush */
        color: #C71585 !important;
        border: 1px solid #FFB6C1 !important;
    }
    
    /* 9. Hilangkan Header Streamlit Default */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* 10. Kustomisasi Tabel */
    .stDataFrame {
        border-radius: 10px;
        border: 1px solid #FFB6C1;
    }

</style>
""", unsafe_allow_safe=True)


# --- DATA DUMMY (UNTUK DEMO) ---
# Di dunia nyata, ini akan diambil dari database
@st.cache_data
def load_data():
    return pd.DataFrame({
        'Nama Pasien': ['Crystabela', 'Audrey', 'Salsabila', 'Vania'],
        'Jenis Layanan': ['Facial Glow', 'Acne Treatment', 'Laser Hair Removal', 'Microneedling'],
        'Dokter': ['Dr. Lala', 'Dr. Sasa', 'Dr. Lala', 'Dr. Caca'],
        'Waktu Kunjungan': ['2026-04-20 10:00', '2026-04-20 11:30', '2026-04-21 09:15', '2026-04-21 14:00'],
        'Status': ['Selesai', 'Selesai', 'Menunggu', 'Konfirmasi']
    })

# --- SIDEBAR & NAVIGASI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80) # Logo Dummy Wanita
    st.title("BeautyCare Dashboard")
    st.markdown("---")
    
    menu = st.radio(
        "Main Menu ✨",
        ["💖 Home & Jadwal", "📝 Pendaftaran Pasien", "📅 Layanan & Treatment", "✨ Konsultasi Online"],
        key="nav_menu"
    )
    st.markdown("---")
    st.info("💡 Tip: Gunakan menu 'Konsultasi Online' untuk chat langsung dengan dokter kami.")

# --- KONTEN UTAMA ---
st.title(f"✨ {menu}")

if menu == "💖 Home & Jadwal":
    st.subheader("Overview Jadwal Hari Ini 🌸")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Pasien Hari Ini", "12", "3")
    with col2:
        st.metric("Pasien Selesai", "8", "5")
    with col3:
        st.metric("Treatment Menunggu", "2", "-1")
    with col4:
        st.metric("Konsultasi Online", "4", "2")
    
    st.markdown("---")
    st.subheader("Detail Jadwal")
    df = load_data()
    # Filter hanya untuk hari ini (demo)
    df_today = df[df['Waktu Kunjungan'].str.contains('2026-04-20')]
    st.dataframe(df_today, use_container_width=True)

elif menu == "📝 Pendaftaran Pasien":
    st.subheader("Formulir Pendaftaran Pasien Baru ✍️")
    
    with st.form("form_pendaftaran"):
        st.markdown("**Informasi Pribadi**")
        nama = st.text_input("Nama Lengkap")
        nik = st.text_input("NIK (16 Digit)")
        tgl_lahir = st.date_input("Tanggal Lahir")
        jenis_kelamin = st.radio("Jenis Kelamin", ["Wanita", "Pria"])
        alamat = st.text_area("Alamat Lengkap")
        no_telp = st.text_input("No. WhatsApp (Aktif)")
        
        st.markdown("---")
        st.markdown("**Informasi Kunjungan**")
        layanan = st.selectbox("Jenis Layanan", ["Facial Glow", "Acne Treatment", "Laser Hair Removal", "Microneedling", "Konsultasi Umum"])
        dokter = st.selectbox("Pilih Dokter", ["Dr. Lala", "Dr. Sasa", "Dr. Caca"])
        
        submitted = st.form_submit_button("Simpan Data ✨")
        
        if submitted:
            if nama and no_telp:
                st.success(f"💖 Data pasien **{nama}** berhasil didaftarkan untuk layanan **{layanan}**!")
                st.info("Silakan cetak nomor antrean di resepsionis.")
            else:
                st.error("Silakan isi nama lengkap dan no. WhatsApp terlebih dahulu.")

elif menu == "📅 Layanan & Treatment":
    st.subheader("Daftar Layanan & Treatment Unggulan ✨")
    
    layanan_data = {
        "Facial Glow ✨": ["Pembersihan mendalam, masker vitamin C, dan pijat relaksasi.", "Rp 350.000"],
        "Acne Treatment 💚": ["Terapi laser acne, pengangkatan komedo, dan serum anti-bakteri.", "Rp 500.000"],
        "Laser Hair Removal 💡": ["Penghapusan rambut permanen dengan teknologi laser terbaru.", "Rp 750.000"],
        "Microneedling 💉": ["Merangsang produksi kolagen untuk tekstur kulit lebih halus.", "Rp 600.000"],
        "Anti-Aging Combo 🕰️": ["Facial lifting, serum kolagen, dan terapi sinar LED.", "Rp 1.200.000"]
    }
    
    for nama, detail in layanan_data.items():
        with st.expander(nama):
            st.write(detail[0])
            st.write(f"**Harga:** {detail[1]}")
            st.button(f"Booking {nama}", key=f"booking_{nama}")

elif menu == "✨ Konsultasi Online":
    st.subheader("Live Chat dengan Dokter Kami 🩺")
    st.write("Silakan pilih dokter untuk memulai konsultasi online.")
    
    col1, col2 = st.columns(2)
    with col1:
        dokter_pilih = st.selectbox("Pilih Dokter", ["Dr. Lala", "Dr. Sasa", "Dr. Caca"])
        pesan_user = st.text_area("Tuliskan keluhan atau pertanyaan Anda:")
        submitted = st.button("Mulai Chat ✨")
        if submitted and pesan_user:
            st.info(f"💖 Pesan Anda berhasil dikirim ke {dokter_pilih}. Mohon tunggu balasan beberapa menit.")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150) # Dokter Avatar
        st.markdown(f"**Chatting dengan {dokter_pilih}**")
        st.markdown("...") # Placeholder untuk live chat
        st.text_input("Tulis pesan balasan...", key="chat_input")
        st.button("Kirim 📩")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #D87093;'>BeautyCare Dashboard © 2026 | Dibuat dengan 💖 untuk Klinik Kecantikan</div>", unsafe_allow_safe=True)