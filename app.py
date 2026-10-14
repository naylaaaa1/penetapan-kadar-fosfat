import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(
    page_title="Kalkulator Fosfat - Spektrofotometer Digital",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Penetapan Kadar Fosfat Metode Asam Askorbat")
st.markdown("Aplikasi web interaktif untuk perhitungan kurva kalibrasi dan analisis kadar fosfat menggunakan **Spektrofotometer UV-Vis**.")

# Sidebar Navigasi
menu = st.sidebar.selectbox("Pilih Menu", ["Kalkulator Analisis", "Panduan & Deploy ke GitHub"])

if menu == "Kalkulator Analisis":
    st.header("1. Data Kurva Kalibrasi (Deret Standar)")
    st.markdown("Masukkan atau sesuaikan konsentrasi larutan standar fosfat (mg/L atau ppm) beserta nilai absorbansinya ($A$).")
    
    # Data default deret standar
    data_default = pd.DataFrame({
        "Konsentrasi (mg/L)": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        "Absorbansi": [0.000, 0.122, 0.245, 0.370, 0.495, 0.620]
    })
    
    # Tabel interaktif untuk edit data standar
    df_standar = st.data_editor(data_default, num_rows="dynamic", use_container_width=True)
    
    # --- PERBAIKAN: Konversi ke numerik & drop baris kosong/invalid untuk mencegah error ---
    df_standar["Konsentrasi (mg/L)"] = pd.to_numeric(df_standar["Konsentrasi (mg/L)"], errors='coerce')
    df_standar["Absorbansi"] = pd.to_numeric(df_standar["Absorbansi"], errors='coerce')
    df_clean = df_standar.dropna()
    
    x = df_clean["Konsentrasi (mg/L)"]
    y = df_clean["Absorbansi"]
    
    if len(x) >= 2 and x.var() > 0:
        # Perhitungan Regresi Linear (y = ax + b)
        slope, intercept = np.polyfit(x, y, 1)
        
        # Mencegah NaN pada koefisien korelasi
        corr_matrix = np.corrcoef(x, y)
        r_sq = corr_matrix[0, 1]**2 if not np.isnan(corr_matrix[0, 1]) else 0.0
        
        st.success(f"**Persamaan Garis Regresi:** $y = {slope:.4f}x + {intercept:.4f}$")
        st.info(f"**Koefisien Korelasi ($R^2$):** `{r_sq:.4f}`")
        
        # Visualisasi Kurva Kalibrasi
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(x, y, color='#1f5fbf', s=50, label='Data Standar')
        ax.plot(x, slope * x + intercept, color='#b42318', linestyle='--', label=f'y = {slope:.4f}x + {intercept:.4f}')
        ax.set_xlabel('Konsentrasi Fosfat (mg/L)')
        ax.set_ylabel('Absorbansi')
        ax.set_title('Kurva Kalibrasi Penetapan Fosfat')
        ax.legend()
        ax.grid(True, linestyle=':', alpha=0.7)
        st.pyplot(fig)
        
        st.markdown("---")
        st.header("2. Perhitungan Kadar Sampel")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            abs_sampel = st.number_input("Absorbansi Sampel ($A_s$)", value=0.310, format="%.4f")
        with col2:
            fp = st.number_input("Faktor Pengenceran (FP)", value=10.0, min_value=1.0)
        with col3:
            vol_ml = st.number_input("Volume Sampel (mL)", value=50.0, min_value=1.0)
            
        if st.button("Hitung Kadar Fosfat", type="primary"):
            if slope != 0:
                # Menghitung konsentrasi dari kurva kalibrasi: x = (y - b) / a
                konsentrasi_kurva = (abs_sampel - intercept) / slope
                kadar_akhir = konsentrasi_kurva * fp
                
                st.metric(label="Konsentrasi dalam Kurva ($x$)", value=f"{konsentrasi_kurva:.4f} mg/L")
                st.metric(label="Kadar Fosfat Akhir ($C \\times FP$)", value=f"{kadar_akhir:.4f} mg/L")
            else:
                st.error("Slope tidak boleh bernilai nol.")
    else:
        st.warning("⚠️ Harap masukkan minimal **2 titik data numerik yang valid** pada tabel di atas untuk membentuk kurva kalibrasi.")

elif menu == "Panduan & Deploy ke GitHub":
    st.header("📂 Cara Menjalankan & Deploy ke GitHub / Streamlit Cloud")
    st.markdown("""
    Ikuti langkah-langkah ringkas berikut untuk mengunggah aplikasi ini ke **GitHub** agar dapat diakses secara online:

    ### 1. Persiapan File Proyek
    Buat folder baru di komputer Anda, lalu sediakan dua file utama:
    * `app.py` (simpan kode program Streamlit di atas ke dalam file ini).
    * `requirements.txt` (berisi pustaka yang diperlukan).

    ### 2. Isi File `requirements.txt`
    Buat file teks bernama `requirements.txt` dan isi dengan baris berikut:
    ```text
    streamlit
    pandas
    numpy
    matplotlib
    ```

    ### 3. Unggah ke Repository GitHub
    1. Buat repository baru di akun [GitHub](https://github.com/new).
    2. Unggah (`upload`) kedua file (`app.py` dan `requirements.txt`) ke dalam repository tersebut.
    3. Klik **Commit changes**.

    ### 4. Deploy di Streamlit Community Cloud
    1. Buka laman [share.streamlit.io](https://share.streamlit.io/).
    2. Masuk menggunakan akun GitHub Anda.
    3. Klik tombol **New app**.
    4. Pilih repository GitHub, branch utama (`main`/`master`), serta jalur file `app.py`.
    5. Klik **Deploy!** Aplikasi web Anda kini siap digunakan secara online. 🚀
    """)
