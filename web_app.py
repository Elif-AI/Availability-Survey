
import streamlit as st
from data_handler import secimi_kaydet, oy_say

st.set_page_config(page_title="Haftanın Günü Anketi", page_icon="📊")
st.title("📊 Haftanın En Sevilen Günü")

gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

secilen = st.multiselect("En sevdiğiniz gün/günleri seçin:", gunler)

if st.button("Seçimi Kaydet"):
    if secilen:
        secimi_kaydet(secilen)
        st.success("Seçiminiz kaydedildi!")
    else:
        st.warning("Lütfen en az bir gün seçin.")

sayim = oy_say()
if sayim:
    st.subheader("Anket Sonucu")
    en_populer = sayim.most_common(1)[0]
    st.write(f"*En çok seçilen gün:* {en_populer[0]} ({en_populer[1]} oy)")
    st.bar_chart({g: sayim.get(g, 0) for g in gunler})
