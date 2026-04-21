import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="GlowUp Beauty Clinic", page_icon="✨", layout="wide")

# --- CUSTOM CSS (Biar Tampilan "Cewe Banget") ---
st.markdown("""
    <style>
    /* Warna Background Utama */
    .stApp {
        background-color: #FFF0F5;
    }
    /* Warna Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFC0CB !important;
    }
    /* Warna Teks Judul */
    h1, h2, h3 {
        color: #D87093 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Gaya Tombol */
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 15px;
        border: none;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #DB7093;
        color: white;
        transform: scale(1.05);
    }
    /* Card untuk Produk */
    .product-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR MENU ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🌸 GlowUp</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your Beauty Journey Starts Here</p>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("Navigasi", ["Beranda", "Pendaftaran Pasien", "Konsultasi Dokter AI", "Katalog Skincare"])

# --- HALAMAN 1: BERANDA ---
if menu == "Beranda":
    st.title("✨ Selamat Datang di GlowUp Clinic")
    st.subheader("Wujudkan Kulit Impianmu Bersama Kami")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&q=80&w=1000", use_container_width=True)
    with col2:
        st.write("""
        **Promo Bulan Ini:**
        * 💖 Diskon 20% Facial Treatment
        * 💖 Buy 1 Get 1 Serum Brightening
        * 💖 Gratis Konsultasi untuk Member Gold
        """)
        if st.button("Ambil Promo Sekarang"):
            st.balloons()

# --- HALAMAN 2: PENDAFTARAN PASIEN ---
elif menu == "Pendaftaran Pasien":
    st.title("📋 Pendaftaran Member Baru")
    with st.container():
        col_a, col_b = st.columns(2)
        with col_a:
            nama = st.text_input("Nama Lengkap")
            tgl_lahir = st.date_input("Tanggal Lahir")
        with col_b:
            wa = st.text_input("Nomor WhatsApp (Aktif)")
            member_type = st.selectbox("Pilih Paket Member", ["Basic", "Silver", "Gold (Best Seller)"])
        
        alamat = st.text_area("Alamat Lengkap")
        
        if st.button("Simpan Data Member"):
            if nama and wa:
                st.success(f"Selamat Kak {nama}! Data Anda berhasil tersimpan sebagai Member {member_type}.")
                st.snow()
            else:
                st.error("Mohon isi nama dan nomor WhatsApp ya Kak!")

# --- HALAMAN 3: KONSULTASI & DIAGNOSA ---
elif menu == "Konsultasi Dokter AI":
    st.title("🔍 Analisis Kondisi Kulit")
    st.write("Isi keluhan Kakak di bawah ini untuk saran perawatan:")
    
    jenis_kulit = st.selectbox("Jenis Kulit Kamu:", ["Pilih", "Berminyak", "Kering", "Sensitif", "Kombinasi"])
    keluhan = st.multiselect("Masalah Kulit:", ["Jerawat", "Kusam", "Flek Hitam", "Pori-pori Besar", "Kemerahan"])
    
    if st.button("Lihat Hasil Diagnosa"):
        if jenis_kulit == "Pilih" or not keluhan:
            st.warning("Silakan pilih jenis kulit dan keluhan dulu ya.")
        else:
            st.divider()
            st.subheader("💡 Rekomendasi Untukmu:")
            
            if "Jerawat" in keluhan:
                st.error("**Diagnosa:** Acne-Prone Skin Condition")
                st.info("**Saran Perawatan:** Acne Facial + Blue Light Therapy")
                st.success("**Produk:** Acne Clarifying Night Cream")
            elif "Kusam" in keluhan:
                st.warning("**Diagnosa:** Dull Skin / Kurang Hidrasi")
                st.info("**Saran Perawatan:** Microdermabrasion + Vitamin C Injection")
                st.success("**Produk:** Brightening Booster Serum")
            else:
                st.success("**Diagnosa:** Kulit butuh maintenance rutin")
                st.info("**Saran Perawatan:** Silk Peel Facial")

# --- HALAMAN 4: KATALOG PRODUK ---
elif menu == "Katalog Skincare":
    st.title("🛍️ Shopping Lab")
    st.write("Produk terbaik untuk kecantikanmu:")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3163/3163211.png", width=120)
        st.write("**Glow Serum**")
        st.write("Rp 145.000")
        st.button("Tambah ke Keranjang", key="p1")
        
    with c2:
        st.image("https://cdn-icons-png.flaticon.com/512/3163/3163195.png", width=120)
        st.write("**Sunscreen SPF 50**")
        st.write("Rp 89.000")
        st.button("Tambah ke Keranjang", key="p2")
        
    with c3:
        st.image("https://cdn-icons-png.flaticon.com/512/3163/3163201.png", width=120)
        st.write("**Cleansing Milk**")
        st.write("Rp 65.000")
        st.button("Tambah ke Keranjang", key="p3")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 GlowUp Clinic - Dibuat dengan Cinta</p>", unsafe_allow_html=True
            
            # update baru