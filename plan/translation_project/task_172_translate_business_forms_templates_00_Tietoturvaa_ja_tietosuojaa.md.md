# Translation Task 172

**File to translate:** /common/active/sblo/Dev/Manager/DummyMusicCompany/db/business_forms_templates/00 Tietoturvaa ja tietosuojaa.md

**Target location:** ../db_eng/business_forms_templates/00 Tietoturvaa ja tietosuojaa.md

## Instructions

1. Manually translate the content of the file from Finnish to English.
2. Translate the title of the file as well.
3. Save the translated file in the db_eng directory in the corresponding location.
4. Do not use automated translation tools - manual translation is required.

## Original Content

```
# Tietoturva ja tietosuoja yrittäjälle

Tämä asiakirja kokoaa keskeistä tietoa tietoturvasta, tietosuojasta ja nykyajan digitaalisista uhkakuvista. Sisältö perustuu eri asiantuntijalähteisiin ja uutisartikkeleihin.

---

## 1. Keskeinen tietoturvasanasto yrittäjälle

### Pilvipalvelut
Perinteisesti ohjelmia on säilytetty omalla tietokoneella, mutta pilvipalvelut (palvelimien verkosto) ovat huomattavasti turvallisempi ja helpompi ratkaisu.
- **Hyödyt:** Pääsy sovelluksiin ja tiedostoihin mistä ja milloin tahansa; tiedot eivät katoa laitteen rikkoutuessa.

### Microsoft 365 (M-365)
Maailman suosituin yritysliiketoimintaan kohdistettu pilvipalvelu (n. 1,2 miljardia käyttäjää).
- **Tenant:** Yksittäinen M-365-tili, jonka sisällä ovat kaikki organisaation käyttäjät, domainit ja tilaukset.
- **AD (Active Directory):** Microsoftin käyttäjätietokantapalvelu, joka mahdollistaa kertakirjautumisen (Single Sign-On) eri palveluihin (esim. M-365, Moodle).

### Verkkotunnus (Domain)
Nimipalvelu, joka antaa oikeuden käyttää yrityksen nimeä kotisivuilla (esim. `ullanleipomo.fi`) ja sähköposteissa. Useita domaineja voidaan kytkeä samaan M-365-palveluun rinnakkaisiksi osoitteiksi.

### SSL (Secure Sockets Layer)
Varmenne, joka osoittaa sivuston luotettavuuden (HTTPS-tunniste). Suojaa yrityksen ja asiakkaiden välisen liikenteen, mikä on välttämätöntä esimerkiksi verkkokaupoissa.

### Sähköpostin suojaus
Sähköpostien SMTP-protokolla on luonnostaan suojaamaton.
- **Salattu sähköposti:** Arkaluontoiset viestit tulee salata. EU suosittelee salausta kansalaisilleen.
- **Azure Information Protection (AIP):** Tietoturvalisenssi, jolla suojataan tiedostot ja sähköpostit. Mahdollistaa pääsysoikeuksien määrittämisen ja käytön todentamisen.

---

## 2. Tietosuoja vs. Tietoturva

- **Tietosuoja (Privacy):** Viittaa ihmisen perusoikeuksiin omien henkilötietojensa käsittelyssä. Kyse on yksityisyyden kunnioittamisesta ja oikeudesta määrätä tietojensa käytöstä.
- **Tietoturva (Security):** Tarkoittaa tiedon turvaamista tuhoutumiselta ja luvattomalta käytöltä. Tietoturvavaatimukset ovat osa tietosuojaa, mutta niitä tarvitaan myös muun kuin henkilötiedon suojelussa.

---

## 3. Lainsäädäntö

### Suomen tietosuojalaki
- Eduskunta hyväksyi EU:n tietosuoja-asetusta (GDPR) tarkentavan kansallisen lain 13.11.2018 (vahvistettu 5.12.2018).
- Laki tuli voimaan 1.1.2019, kumoten henkilötietolain.
- **Miksi kansallinen laki?** Vaikka EU-asetus on suoraan sovellettavaa oikeutta, se jättää kansallista liikkumavaraa, jota tietosuojalaki täsmentää ja tarkentaa.

---

## 4. Nykyhetken uhkakuvat ja esimerkkejä

### Identiteettivarkaudet
- Vuonna 2020 yli 750 000 suomalaista joutui yrityksen kohteeksi (yli 2000 päivässä).
- **Tietojen hintoja rikollisilla:**
    - Sosiaaliturvatunnus: 1 €
    - Maksu-/luottokortti: 5–110 €
    - Fullz info -paketti (nimi, sotu, tilitiedot): 30 €
    - PayPal-tunnus: 20–200 €
- **Vastaamo-tietomurto (2020):** Rikolliset saivat käsiinsä nimet, osoitteet, henkilötunnukset ja potilastiedot. Vuotaneilla tiedoilla voidaan tehdä tilauspetoksia.
- **Suojautuminen:** Luottokielto on järkevä, jos epäilee identiteettivarkautta tai paperit katoavat.

### Henkilötunnuksen (HETU) muuttaminen
- Vastaamon uhrat hakivat uusia henkilötunnuksia, mutta pelkkä tietomurron uhriksi joutuminen ei nykylainsäädännön mukaan riitä perusteeksi vaihtoon.
- Vaihtaminen on vaikeaa, koska tunnus on tarkoitettu pysyväksi, eikä se välttämättä poista kaikkia väärinkäytöksiä (vanha tunnus voi jäädä järjestelmiin).
- HETU-uudistusta on valmisteltu (työryhmä 2018), tavoitteena tunnuksen kehittäminen ja identiteetin hallinnan parantaminen.

### Kalastelu (Phishing) ja huijaukset
- **Väärennetyt puhelut:** Huijarit esiintyvät teknisenä tukena (esim. "Windows-huijarit").
- **Tori.fi / Posti / Postnord:** Viestejä lähetetään verkkokauppojen ja kuljetusyhtiöiden nimissä luottokorttitietojen kalasteluksi.
- **Hafnium:** Kiinasta operoiva valtiojohtoinen (state-sponsored) uhkatekijä, joka hyökkää taitavasti yritysten järjestelmiin.
- **Kömpelöt yritykset:** Esimerkkinä huonosti muotoillut "suojatun sähköpostin" ilmoitukset (esim. väärennetyt OP-viestit), jotka ohjaavat ulkopuolisille sivuille.

### Mobiililaitteiden uhat
- **TikTok:** Sovelluksen oma selain pystyy seuraamaan jokaista näytön ja näppäimistön napautusta (keylogging), mikä mahdollistaa salasanojen ja korttitietojen keräämisen.
- **iPhone (iOS):** Myytti täydellisestä turvallisuudesta särkyi, kun löytyi hyökkäyksiä, jotka asensivat haittaohjelmia pelkästään nettisivulla vierailemalla (iOS versiot 10–12).
- **Android-sovellukset:** McAfee löysi "Clicker"-haittaohjelman useista sovelluksista, joita oli ladattu jopa 20 miljoonaa kertaa.
    - *Haitallisia sovelluksia (esimerkkejä):* High-Speed Camera, Smart Task Manager, Flashlight+, Quick Note, Currency Converter, Joycode.
- **Clast82:** Dropper-haitake, joka levisi mm. Cake VPN, Pacific VPN ja QR/Barcode Scanner MAX -sovellusten mukana. Se ottaa laitteen haltuun ja kohdistuu rahaliikennesovelluksiin.

---

## 5. Yleisiä virheitä ja huomioita

- **Huolimattomuus ja ymmärtämättömyys:** Moni huijaus onnistuu, koska käyttäjä ei tunnista vaaraa tai päivitä laitteitaan.
- **Tekijänoikeudet:** Kuvien kopioiminen netistä "omaan käyttöön" tai kouluprojekteihin voi johtaa korvauksiin. Euroopan oikeusistuin (ECJ) on linjannut, että uusiokäyttöön tarvitaan aina kuvaajan lupa (vrt. tapaus saksalainen koululainen, 400 € vahingonkorvaus).
- **Viestintävirasto ja Kyberturvallisuuskeskus:** Tarjoavat ajankohtaista tietoa ja vastauksia uhreille.

```
