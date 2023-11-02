import streamlit as st
import math

def hesapla_ev_sayisi_ve_kira_geliri(aylik_birikim, yas, ev_fiyati, kira_gelir, kredi_suresi, pesinat_orani):
  emeklilik_yasi = 65
  toplam_ev_sayisi = 0
  kalan_ev_fiyati = ev_fiyati
  baslangic_birikimi = 0

  while yas < emeklilik_yasi:
    pesinat = kalan_ev_fiyati * pesinat_orani / 100
    kalan_ev_fiyati -= pesinat
    aylik_harcamalar = kalan_ev_fiyati / (kredi_suresi * 12)
    yillik_harcamalar = aylik_harcamalar * 12

    if aylik_birikim >= pesinat + aylik_harcamalar:
      toplam_ev_sayisi += 1
      baslangic_birikimi += aylik_birikim - (pesinat + aylik_harcamalar)
      kalan_ev_fiyati = 0

    yas += 1

  toplam_kira_geliri = float(toplam_ev_sayisi) * 12 * kira_gelir

  return toplam_ev_sayisi, toplam_kira_geliri

def main():
  st.title("Konut Birikim Hesaplayıcı")
  st.write("Bu hesaplayıcı, konut birikimi yaparak emlak yatırımı yapan Hakan'ın sonuçlarını hesaplar.")
  st.write("Lütfen aşağıdaki bilgileri doldurun.")

  aylik_birikim = st.number_input("Aylık birikim miktarı (TL):", min_value=0, step=1)
  yas = st.number_input("Yaşınız:", min_value=0, step=1)
  ev_fiyati = st.number_input("Almak istediğiniz dairenin fiyatı (TL):", min_value=0, step=1)
  kira_gelir = st.number_input("Daire kira getirisi (TL/ay):", min_value=0, step=1)
  kredi_suresi = st.number_input("Kredi Süresi (yıl):", min_value=0, step=1)
  pesinat_orani = st.number_input("Peşinat Oranı (%):", min_value=0, max_value=100, step=1)

  if st.button("Hesapla"):
    toplam_ev_sayisi, toplam_kira_geliri = hesapla_ev_sayisi_ve_kira_geliri(aylik_birikim, yas, ev_fiyati, kira_gelir, kredi_suresi, pesinat_orani)
    st.write(f"Hakan'ın 65 yaşına geldiğinde sahip olduğu ev sayısı: {toplam_ev_sayisi} adet")
    st.write(f"Hakan'ın 65 yaşına geldiğinde elde ettiği toplam kira geliri: {toplam_kira_geliri:.2f} ₺")

if __name__ == "__main__":
  main()
