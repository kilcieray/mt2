import streamlit as st
import requests
import time
import random

GOMULU_TOKEN = "8750355385:AAHtl4gTVEmRoho3N3pw5oQiYL8FRXPtCd0"
GOMULU_CHAT_ID = "2078050611"

EFSUN_DICT = {
    1: "Max. HP +", 2: "Max. SP +", 3: "Canlılık +", 4: "Zeka +", 5: "Güç +", 6: "Çeviklik +", 7: "Saldırı Hızı +%", 8: "Hareket Hızı %", 9: "Büyü Hızı +%", 10: "HP Üretimi +%", 11: "SP Üretimi +%", 12: "Zehirleme şansı %", 13: "Bayılma şansı: %", 14: "Yavaşlama şansı: %", 15: "Kritik Vuruş Şansı: +%", 16: "Delici Vuruş için şansı %", 17: "Yarı insanlara karşı güçlü +%", 18: "Hayvanlara karşı güçlü +%", 19: "Orklara karşı güçlü +%", 20: "Mistiklere karşı güçlü +%", 21: "Ölümsüzlere karşı güçlü +%", 22: "Şeytanlara karşı güçlü +%", 23: "% hasar, HP ile absorbe edilir", 24: "% hasar, SP ile absorbe edilir", 25: "SP çalma şansı %", 26: "Vuruş yapıldığında Sp geri kazanım şansı %", 27: "Yakın dövüş saldırıları bloklama şansı: %", 28: "% Okları savuşturma şansı", 29: "Kılıç Savunması %", 30: "Çift-El Savunma %", 31: "Bıçak Savunması %", 32: "Çan Savunması %", 33: "Yelpaze Savunması %", 34: "Ok savunması %", 35: "Ateş direnci %", 36: "Şimşek Direnci %", 37: "Büyüye karşı dayanıklılık %", 38: "Rüzgar Dayanıklılığı %", 39: "Yakın dövüş vuruşlarını yansıtma şansı: %", 40: "Lanet Yansıtılması: %", 41: "Zehre karşı koyma %", 42: "SP yenileme şansı %", 43: "EXP Bonus şansı %", 44: "İki kat Yang düşme şansı %", 45: "İki Kat eşya düşme şansı %", 46: "İksir etkisi % yükseldi", 47: "HP yenileme şansı %", 48: "Sersemlik karşısında bağışıklık", 49: "Yavaşlama karşısında bağışıklık", 50: "Yere düşme karşısında bağışıklık", 51: "Beceriler", 52: "Menzil +m", 53: "Saldırı Değeri +", 54: "Savunma +", 55: "Büyülü Saldırı Değeri +", 56: "Büyü Savunması +", 58: "Max. Dayanıklılık +", 59: "Savasçılara karşı güçlü +%", 60: "Ninjalara karşı güçlü +%", 61: "Suralara karşı güçlü +%", 62: "Şamanlara karşı güçlü +%", 63: "Canavarlara karşı güçlü +%", 64: "Saldırı Değeri +%", 65: "Savunma +%", 66: "EXP +%", 67: "Nesne düşürme şansı % arttı", 68: "Yang düşürme şansı % arttı", 69: "Maks. HP %", 70: "Maks. SP +%", 71: "Beceri Hasarı %", 72: "Ortalama Zarar %", 73: "Beceri hasarına karşı koyma %", 74: "Ortalama Zarara Direniş %", 78: "Savaşçı saldırılarına karşı savunma şansı: %", 79: "Ninja saldırılarına karşı savunma şansı %", 80: "Sura saldırılarına karşı savunma şansı: %", 81: "Şaman saldırılarına karşı savunma şansı: %", 82: "Enerji ", 83: "Savunma +", 84: "Kostüm bonusu %", 85: "Büyü Saldırı +%", 86: "Büyü Saldırı / Yakın Dövüş Saldırı +%", 87: "Buz direnci +%", 88: "Toprak Direnci +%", 89: "Karanlık Direnci %", 90: "Kritik Vuruş Direnci +%", 91: "Delici Vuruş Direnci +%", 92: "Kanama saldırılarında direnç +%", 93: "Kanama Saldırısı +%", 94: "Lycanlar'a karşı güçlü + %", 95: "Lycanlar'a karşı savunma şansı +%", 96: "Pençe savunması +%", 97: "Emiş oranı: %", 98: "Büyü bozma %", 99: "Şimşeklerin gücü +%", 100: "Ateşin gücü +%", 101: "Buzun gücü +%", 102: "Rüzgarın gücü +%", 103: "Toprağın gücü +%", 104: "Karanlığın gücü +%", 105: "Zodyak canavarına karşı güçlü +%", 106: "Böceklere karşı güçlü +%", 107: "Çöl canavarına karşı güçlü +%", 108: "Kılıç savunmasından kopuş +%", 109: "Çift el savunmasından kopuş +%", 110: "Hançer savunmasından kopuş +%", 111: "Çan savunmasından kopuş +%", 112: "Yelpaze savunmasından kopuş +%", 113: "Ok savunmasından kopuş +%", 114: "Pençe savunmasından kopuş +%", 115: "Yarı insanlara karşı direnç %", 116: "Düşüş direnci +%", 119: "Üç yönlü kesme hasarı +%", 120: "Hamle hasarı +%", 121: "Kılıç çevirme hasarı +%", 122: "Ruh vuruşu hasarı +%", 123: "Şiddetli vuruş hasarı +%", 124: "Kılıç darbesi hasarı +%", 125: "Suikast hasarı +%", 126: "Hızlı saldırı hasarı +%", 127: "Bıçak çevirme hasarı +%", 128: "Zehirli bulut hasarı +%", 129: "Tekrarlanan atış hasarı +%", 130: "Ok yağmuru hasarı +%", 131: "Zehirli ok hasarı +%", 132: "Ateşli ok hasarı +%", 133: "Parmak darbesi hasarı +%", 134: "Ejderha dönüşü hasarı +%", 135: "Büyü çözme hasarı +%", 136: "Karanlık vuruş hasarı +%", 137: "Alev vuruşu hasarı +%", 138: "Karanlık taş hasarı +%", 139: "Uçan tılsım hasarı +%", 140: "Ejderha darbesi hasarı +%", 141: "Ejderha kükremesi hasarı +%", 142: "Şimşek atma hasarı +%", 143: "Şimşek çağırma hasarı +%", 144: "Şimşek pençesi hasarı +%", 145: "Yırtma hasarı +%", 146: "Kurt nefesi hasarı +%", 147: "Kurt atlayışı hasarı +%", 148: "Kurt pençesi hasarı +%", 149: "Patronlardan saldırı hasarı -%", 150: "Patronlardan beceri hasarı -%", 151: "Patronlara karşı saldırı hasarı +%", 152: "Patronlara karşı beceri hasarı +%", 153: "Savaşta sn boyunca ateşin gücünü al", 154: "Savaşta sn boyunca buzun gücünü al", 155: "Savaşta sn boyunca şimşeğin gücünü al", 156: "Savaşta sn boyunca rüzgarın gücünü al", 157: "Savaşta sn boyunca karanlığın gücünü al", 158: "Savaşta sn boyunca toprağın gücünü al", 159: "Savaşta sn boyunca ateş direnci al", 160: "Savaşta sn boyunca buz direnci al", 161: "Savaşta sn boyunca şimşek direnci al", 162: "Savaşta sn boyunca rüzgar direnci al", 163: "Savaşta sn boyunca karanlık direnci al", 164: "Savaşta sn boyunca toprak direnci al", 165: "Çivit kurt ruhu kullanımında hareket hızını sn artır", 166: "Çivit kurt ruhu kullanımında sihir hızını sn artır", 167: "Yırtma kullanımında kritik saldırı şansını sn artır", 168: "Zehirli bulut kullanımında sn saldırı bonusu al", 169: "Zehirli ok kullanımında sn saldırı bonusu al", 170: "Kırmızı kurt ruhu kullanımında sn savunma bonusu al", 171: "Büyülü keskinlik kullanımında sn savunma bonusu al", 172: "Dehşet kullanımında sn saldırı bonusu al", 173: "Ateş hayaleti kullanımında sn saldırı bonusu al", 174: "Karanlık koruma kullanımında sihir hızını sn artır", 175: "Kutsama kullanımında sn savunma bonusu al", 176: "Ejderha yardımı kullanımında sn saldırı bonusu al", 177: "Şifa kullanımında sn saldırı bonusu al", 178: "Saldırı+ kullanımında sn savunma bonusu al", 179: "Yaşama isteği kullanımında sn saldırı bonusu al", 180: "Güçlü beden kullanımında sihir hızını sn artır", 181: "Kılıç çemberi kullanımında sn saldırı bonusu al", 182: "Kamuflaj süresi + sn", 183: "Hafif adım süresi + sn", 184: "Hava kılıcı süresi + sn", 185: "Kırmızı kurt ruhu süresi + sn", 186: "Kılıç çevirme kullanımda % HP emer", 187: "Suikast kullanımda % HP emer", 188: "Tekrarlanan atış kullanımda % HP emer", 189: "Ejderha darbesi usage % HP emer", 190: "Şimşek pençesi kullanımında % HP emer", 191: "Kurt pençesi kullanımda % SP emer", 192: "Ruh vuruşu, düşmanları % şansla sersemletir", 193: "Bıçak çevirme düşmanları % şansla sersemletir", 194: "Büyü çözme, düşmanları % şansla sersemletir", 195: "Karanlık taş, düşmanları % şansla sersemletir", 196: "Kurt atlayışı, düşmanları % şansla sersemletir", 197: "Üç yönlü kesme, düşmanları % şansla sersemletir", 198: "Şiddetli vuruş, düşmanlara % şansla misilleme yapar", 199: "Sinsi zehir, düşmanlara % şansla misilleme yapar", 200: "Parmak darbesi, düşmanlara % şansla misilleme yapar", 201: "Alev vuruşu, düşmanlara % şansla misilleme yapar", 202: "Kurt atlayışı düşmanlara % şansla misilleme yapar", 203: "Ok yağmuru, düşmanlara % şansla misilleme yapar", 204: "Üç yönlü kesme soğuma süresi: - sn, %10 şansla", 205: "Kılıç darbesi soğuma süresi: - sn, %10 şansla", 206: "Şimşek saldırısı soğuma süresi: - sn, %10 şansla", 207: "Ok yağmuru soğuma süresi: - sn, %10 şansla", 208: "Ejderha dönüşü soğuma süresi: - sn, %10 şansla", 209: "Karanlık vuruş soğuma süresi: - sn, %10 şansla", 210: "Uçan tılsım soğuma süresi: - sn, %10 şansla", 211: "Şimşek atma soğuma süresi: - sn, %10 şansla", 212: "Kurt nefesi soğuma süresi: - sn, %10 şansla", 213: "Kurt pençesi soğuma süresi: - sn, %10 şansla", 214: "% Metin taşı karşısında güçlü", 215: "% hasarı HP olarak emer", 216: "% hasarı SP olarak emer", 217: "Düşük rütbe puanlarında verilen hasar artar.", 218: "Saldırı hasarı % şansla engellendi", 219: "%90'dan fazla HP'n olursa, aldığınd hasar % düşer.", 220: "Hayalet vuruşu kullanımda % HP emer", 221: "Ejderha kükremesi kullanımda % HP emer", 222: "Şimşek çağırma kullanımında maksimum % HP emersin.", 223: "1. eklenen Bonus +%", 224: "2. eklenen Bonus +%", 225: "3. eklenen Bonus +%", 226: "4. eklenen Bonus +%", 227: "5. eklenen Bonus +%", 228: "Üç yönlü kesme soğuma süresi: - saniye, %20 şansla", 229: "Kılıç darbesi soğuma süresi: - saniye, %20 şansla", 230: "Şimşek saldırısı soğuma süresi: - saniye, %20 şansla", 231: "Ok yağmuru soğuma süresi: - saniye, %20 şansla", 232: "Ejderha dönüşü soğuma süresi: - saniye, %20 şansla", 233: "Karanlık vuruş soğuma süresi: - saniye, %20 şansla", 234: "Uçan tılsım soğuma süresi: - saniye, % 20 şansla", 235: "Şimşek atma soğuma süresi: - saniye, %20 şansla", 236: "Kurt nefesi soğuma süresi: - saniye, %20 şansla", 237: "Kurt pençesi soğuma süresi: - saniye, %20 şansla", 238: "Yırtma kullanımında % HP emer", 239: " SungMa iradesi (STR)", 240: " SungMa iradesi (VIT)", 241: " SungMa iradesi (RES)", 242: " SungMa iradesi (INT)", 243: "Tamlık ", 245: "Yarı insanlara karşı güçlü (Toplam değerin +% oranında)", 246: "Hayvanlara karşı güçlü (Toplam değerin +% oranında)", 247: "Orklara karşı güçlü (Toplam değerin +% oranında)", 248: "Mistiklere karşı güçlü (Toplam değerin +% oranında)", 249: "Ölümsüzlere karşı güçlü (Toplam değerin +% oranında)", 250: "Şeytanlara karşı güçlü (Toplam değerin +% oranında)", 251: "Şimşeklerin gücü (Toplam değerin +% oranında)", 252: "Ateşin gücü (Toplam değerin +% oranında)", 253: "Buzun gücü (Toplam değerin +% oranında)", 254: "Rüzgarın gücü (Toplam değerin +% oranında)", 255: "Toprağın gücü (Toplam değerin +% oranında)", 256: "Karanlığın gücü (Toplam değerin +% oranında)", 257: "Zodyak canavarına karşı güçlü (Toplam değerin +% oranında)", 258: "Böceklere karşı güçlü (Toplam değerin +% oranında)", 259: "Çöl canavarına karşı güçlü (Toplam değerin +% oranında)", 260: "Metin taşı karşısında güçlü (Toplam değerin +% oranında)", 261: "Canavarlara karşı güçlü (Toplam değerin +% oranında)", 262: "Yarı insanlara karşı direnç (Toplam değerin +% oranında)", 263: "Buz direnci (Toplam değerin +% oranında)", 264: "Karanlık direnci (Toplam değerin +% oranında)", 265: "Toprak direnci (Toplam değerin +% oranında)", 266: "Ateşe karşı direnç (Toplam değerin +% oranında)", 267: "Şimşek direnci (Toplam değerin +% oranında)", 268: "Büyüye karşı direnç (Toplam değerin +% oranında)", 269: "Rüzgar direnci (Toplam değerin +% oranında)", 270: "SungMa iradesini (STR) savaşta saniye boyunca 15 oranında artırır", 271: "SungMa iradesini (RES) savaşta saniye boyunca 15 oranında artırır", 272: "SungMa iradesini (VIT) savaşta saniye boyunca 15 oranında artırır", 273: "SungMa iradesini (INT) savaşta saniye boyunca 15 oranında artırır", 274: "Bir bineğe bindiğinde hasar 10 saniye boyunca +% artar.", 275: "Binekten indiğinde hareket hızı 10 saniye boyunca % artar", 276: "Savaş esnasında güneş özütü efektine sahip olursun.", 277: "Savaş esnasında ay özütü efektine sahip olursun.", 278: "% olasılıkla becerilerinin soğuma süresini sıfırlar.", 279: "Bir Metin taşına saldırı düzenlediğinde 5 saniye boyunca +% hasar (Metin taşı karşısında güç) alırsın", 280: "Bir Metin taşına saldırı düzenlediğinde 5 saniye boyunca + savunma alırsın", 281: "Bir patron yenildiğinde senin drop şansın % artar", 282: "Saldırı esnasında % olasılıkla yakındaki tüm canavarlar sana saldırabilir (Cesaret Pelerini)", 283: "% olasılıkla ölümden kaçabilirn ve toplam HP'ni %30 oranında yenileyebilirsin.", 284: "% Olasılıkla 30 saniye boyunca yakınındaki eşyaları otomatik olarak toplayabilirsin", 285: "20 saniye boyunca düşmanları geri savurmama şansı %. 2 dakika soğuma süresi.", 286: "% SungMa iradesi (STR)", 287: "% SungMa iradesi (VIT)", 288: "% SungMa iradesi (RES)", 289: "% SungMa iradesi (INT)", 290: "Zehir karşısında bağışıklık", 291: "Kanama karşısında bağışıklık", 292: "Canavar saldırısında direnç ", 300: "Deprem kullandıldığında depremin bir sonraki soğuma süresini % ihtimalle 5 saniye düşürür.", 301: "Işık yıldızı kullandıldığında ışık yıldızının bir sonraki soğuma süresini % ihtimalle 5 saniye düşürür.", 302: "Saldırı ateşi kullandıldığında saldırı ateşinin bir sonraki soğuma süresini % ihtimalle 5 saniye düşürür.", 303: "Ateş darbesi kullandıldığında ateş darbesinin bir sonraki soğuma süresini % ihtimalle 5 saniye düşürür.", 304: "Ölüm dalgası kullandıldığında ölüm dalgasının bir sonraki soğuma süresini % ihtimalle 5 saniye düşürür.", 305: "Meteor kullandıldığında meteorun bir sonraki soğuma süresini % ihtimalle 5 saniye düşürür.", 306: "Eter kalkanı kullandıldığında % olasılıkla eter kalkanının bir sonraki soğuma süresini 5 saniye düşürür.", 307: "Pençe atağı kullandıldığında pençe atağının bir sonraki soğuma süresini % ihtimalle 5 saniye düşürür.", 308: "Eldivenlerinin temel özellikleri +% artırıldı.", 309: "Savaşta % şansla 15 saniye düşüş direnci kazan.", 310: "Yakındaki canavarlara normal saldırıya eşit hasar veren şimşekle saldır.", 311: "% Engelleme nüfuzu", 312: "Gizemlere karşı güçlü +%", 313: "Ejderhalara karşı güçlü + %", 321: "Şaşkınlık olasılığı: %%0.1f", 322: "Ay gölgesi canavarlarına karşı güçlü +%", 324: "Toplam değerin +% oranında", 325: "% Tamlık"
}

all_ids_map = {i: f"Efsun (ID {i})" for i in range(1, 326)}
all_ids_map.update(EFSUN_DICT)
EFSUN_OPTIONS = {f"{v} (ID {k})": k for k, v in all_ids_map.items()}
SORTED_EFSUNS = sorted(list(EFSUN_OPTIONS.keys()))

@st.cache_data(ttl=600)
def get_raw_item_names():
    try:
        r = random.randint(10000, 99999)
        url = f"https://metin2alerts.com/store/public/data/57.json?r={r}"
        res = requests.get(url, timeout=10).json()
        names = sorted(list(set([item.get('name', '') for item in res if item.get('name')])))
        return names
    except:
        return []

st.set_page_config(page_title="PAZARCI", layout="wide")
st.title("PAZARCI Terminal")

item_suggestions = get_raw_item_names()

if 'track_list' not in st.session_state:
    st.session_state.track_list = [{"name": "", "max_won": 3000, "attrs": [{"id": 72, "val": 0}]}]

st.sidebar.success("Telegram bağlantısı başarılı.")

for i in range(len(st.session_state.track_list)):
    item = st.session_state.track_list[i]
    header = f"🔍 Takip #{i+1}: {item['name']}" if item['name'] else f"🔍 Takip #{i+1}: Bekliyor..."
    
    with st.expander(header, expanded=True):
        c1, c2, c3 = st.columns([3, 1, 0.5])
        
        # ÇÖZÜM: Selectbox yerine serbest Metin Kutusu (text_input)
        # Artık seni hiçbir şeyi seçmeye zorlamaz, ne yazarsan o kalır.
        item['name'] = c1.text_input(
            "Eşya İsmi (Örn: Zehir Kılıcı +9 veya sadece Zehir)", 
            value=item['name'], 
            key=f"text_input_{i}",
            help="Buraya yazdığın metin pazardaki item isminde geçiyorsa bot yakalar."
        )
        
        if item['name'] and len(item['name']) > 1:
            matches = [s for s in item_suggestions if item['name'].lower() in s.lower()][:5]
            if matches:
                st.caption(f"💡 Pazardaki tam isimler: {', '.join(matches)}...")

        item['max_won'] = c2.number_input("Won Sınırı", value=item['max_won'], key=f"won_{i}")
        
        if c3.button("🗑️", key=f"del_{i}"):
            st.session_state.track_list.pop(i)
            st.rerun()

        st.markdown("---")
        for j in range(len(item['attrs'])):
            attr = item['attrs'][j]
            ec1, ec2, ec3 = st.columns([3, 1, 0.5])
            
            curr_label = next((k for k, v in EFSUN_OPTIONS.items() if v == attr['id']), SORTED_EFSUNS[0])
            choice = ec1.selectbox("Efsun", options=SORTED_EFSUNS, index=SORTED_EFSUNS.index(curr_label), key=f"ef_{i}_{j}")
            attr['id'] = EFSUN_OPTIONS[choice]
            attr['val'] = ec2.number_input("Min Değer (>=)", value=attr['val'], key=f"v_{i}_{j}")
            
            if ec3.button("❌", key=f"xa_{i}_{j}"):
                item['attrs'].pop(j)
                st.rerun()
        
        if len(item['attrs']) < 7 and st.button("➕ Efsun Ekle", key=f"ba_{i}"):
            item['attrs'].append({"id": 1, "val": 0})
            st.rerun()

if st.button("🚀 YENİ İTEM TAKİBİ EKLE"):
    st.session_state.track_list.append({"name": "", "max_won": 3000, "attrs": [{"id": 0, "val": 0}]})
    st.rerun()

if st.button("🔥 TARAMAYI BAŞLAT", type="primary"):
    st.info("Pazar taranıyor. Belirlediğin isimleri içeren tüm artılı/artısız itemler yakalanacak.")
    sent_cache = set()
    log_area = st.empty()
    
    while True:
        try:
            r = random.randint(10000, 99999)
            data = requests.get(f"https://metin2alerts.com/store/public/data/57.json?r={r}", timeout=10).json()
            
            for m_item in data:
                m_full_name = m_item.get('name', '')
                
                for crit in st.session_state.track_list:
                    if not crit['name']: continue
                    
                    if crit['name'].lower() in m_full_name.lower() and m_item['wonPrice'] <= crit['max_won']:
                        match_count = 0
                        for req in crit['attrs']:
                            for p_id, p_val in m_item.get('attrs', []):
                                if p_id == req['id'] and p_val >= req['val']:
                                    match_count += 1; break
                        
                        if match_count == len(crit['attrs']) and m_item['id'] not in sent_cache:
                            efsun_msg = ""
                            for p_id, p_val in m_item.get('attrs', []):
                                e_name = all_ids_map.get(p_id, f"ID {p_id}")
                                efsun_msg += f"▫️ {e_name} {p_val}\n"
                            
                            msg = (f"🎯 *ARANAN İTEM BULUNDU!*\n\n"
                                   f"📦 *Eşya:* {m_item['name']}\n"
                                   f"💰 *Fiyat:* {m_item['wonPrice']} Won\n"
                                   f"👤 *Satıcı:* {m_item['seller']}\n\n"
                                   f"✨ *Tüm Efsunlar:*\n{efsun_msg}\
                            
                            requests.post(f"https://api.telegram.org/bot{GOMULU_TOKEN}/sendMessage", 
                                         json={"chat_id": GOMULU_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
                            sent_cache.add(m_item['id'])
                            st.toast(f"Bildirim: {m_item['name']}")

            log_area.info(f"Son Tarama: {time.strftime('%H:%M:%S')} | Aktif İlan: {len(data)}")
            time.sleep(60)
        except:
            time.sleep(15)