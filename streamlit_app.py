import streamlit as st
from PIL import Image

# Pengaturan dasar
st.set_page_config(page_title="Portofolio Saya", page_icon=":briefcase:", layout="centered")

# Header
st.title("Halo, Saya Rahmat Ivaldy 👋")
st.write("Selamat datang di portofolio saya! Di sini Anda bisa mengetahui lebih banyak tentang saya, keahlian saya, dan proyek-proyek yang sudah saya kerjakan.")

# Sidebar - Navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih halaman:", ["Tentang Saya", "Keahlian", "Proyek", "Kontak", "Kode Sumber"])

# Halaman "Tentang Saya"
if page == "Tentang Saya":
    st.header("Tentang Saya")
    st.image("images/foto gw tuh.jpg", width=200)  # Ganti dengan foto profil Anda
    st.write("""
    Saya adalah seorang [profesi Anda], berfokus pada [bidang yang ditekuni]. 
    Saya memiliki pengalaman dalam [deskripsi singkat pengalaman atau latar belakang Anda].
    """)

# Halaman "Keahlian"
elif page == "Keahlian":
    st.header("Keahlian")
    st.write("""
    - **Bahasa Pemrograman**: Python, JavaScript, HTML, CSS
    - **Framework**: Streamlit, Flask, Django
    - **Tools**: Git, Docker, SQL
    - **Lainnya**: Machine Learning, Data Analysis, UX/UI Design
    """)

# Halaman "Proyek"
elif page == "Proyek":
    st.header("Proyek")
    st.write("Berikut beberapa proyek yang pernah saya kerjakan:")
    # Proyek 1
    st.subheader("Proyek 1: Nama Proyek")
    st.write("Deskripsi singkat proyek dan teknologi yang digunakan.")
    st.image("images/proyek1.jpg", width=300)  # Ganti dengan gambar proyek
    # Proyek 2
    st.subheader("Proyek 2: Nama Proyek")
    st.write("Deskripsi singkat proyek dan teknologi yang digunakan.")
    st.image("images/proyek2.jpg", width=300)  # Ganti dengan gambar proyek

# Halaman "Kontak"
elif page == "Kontak":
    st.header("Kontak")
    st.write("Anda dapat menghubungi saya melalui:")
    st.write("- Email: [rahmativaldy11@gmail.com](mailto:rahmativaldy11@gmail.com)")
    st.write("- LinkedIn: [linkedin.com/in/username](https://linkedin.com/in/username)")
    st.write("- GitHub: [github.com/username](https://github.com/username)")

# Halaman "Kode Sumber"
elif page == "Kode Sumber":
    st.header("Kode Sumber")
    st.write("Anda dapat melihat kode sumber dari website ini di repositori berikut:")
    st.write("- GitHub: [github.com/username/portfolio](https://github.com/username/portfolio)")

