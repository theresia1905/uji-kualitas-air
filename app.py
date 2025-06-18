import streamlit as st

st.title("Klasifikasi Kualitas Air Berdasarkan Permenkes")

ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
suhu = st.number_input("Suhu (°C)", min_value=0.0, max_value=100.0, step=0.1)
salinity = st.number_input("Salinity (mg/L)", min_value=0.0, step=1.0)
tds = st.number_input("TDS (mg/L)", min_value=0.0, step=1.0)

if st.button("Klasifikasi"):
    if 6.5 <= ph <= 8.5 and tds <= 500 and salinity <= 500 and 25 <= suhu <= 30:
        hasil = "✅ Memenuhi syarat air minum (baik)"
    elif 6.0 <= ph < 6.5 or 8.5 < ph <= 9 or 500 < tds <= 1000 or 500 < salinity <= 1000:
        hasil = "⚠️ Perlu perhatian (sedang)"
    else:
        hasil = "❌ Tidak memenuhi syarat (buruk)"

    st.success(f"Hasil Klasifikasi: {hasil}")
