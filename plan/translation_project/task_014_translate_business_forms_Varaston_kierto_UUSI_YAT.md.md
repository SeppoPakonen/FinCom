# Translation Task 014

**File to translate:** /common/active/sblo/Dev/Manager/DummyMusicCompany/db/business_forms/Varaston kierto_UUSI_YAT.md

**Target location:** ../db_eng/business_forms/Varaston kierto_UUSI_YAT.md

## Instructions

1. Manually translate the content of the file from Finnish to English.
2. Translate the title of the file as well.
3. Save the translated file in the db_eng directory in the corresponding location.
4. Do not use automated translation tools - manual translation is required.

## Original Content

```
# Työkalu: Varaston hallinta ja kierto

Tehokas varastonhallinta vapauttaa pääomaa ja varmistaa toimitusvarmuuden. Tämä opas opastaa keskeisiin laskentakaavoihin.

## 1. Varaston kiertonopeus
Kertoo, kuinka monta kertaa varasto "tyhjenee" ja täyttyy vuoden aikana.
* **Kaava:** `Varaston kierto = Myytyjen tuotteiden hankintameno / Varaston keskiarvo`
* **Tavoite:** Mitä suurempi luku, sitä vähemmän pääomaa on sitoutuneena varastoon.

## 2. Varaston kiertoaika (päivinä)
Kertoo, kuinka monta päivää tuotteet keskimäärin viipyvät varastossa.
* **Kaava:** `365 / Varaston kiertonopeus`

## 3. Tilauspiste ja varmuusvarasto
Määrittele, milloin uusi tilaus on tehtävä, jotta tavara ei lopu kesken.
* **Tilauspiste** = (Keskimääräinen päiväkulutus × Toimitusaika päivinä) + Varmuusvarasto.
* **Varmuusvarasto:** Puskuri yllättäviä kysyntähuippuja tai toimitusviivästyksiä varten.

## 4. EOQ – Taloudellisin tilauserä
Laskee optimaalisen tilausmäärän, jossa tilauskustannukset ja varastoinnin ylläpitokustannukset ovat tasapainossa.
* **Vaikuttavat tekijät:** Vuotuinen kysyntä, tilauskustannus (euroa/tilaus) ja varastointikustannus (euroa/yksikkö).

## 5. Varastonhallinnan vinkit
* **ABC-analyysi:** Keskity A-tuotteisiin (suurin arvo/menekki).
* **FIFO (First In, First Out):** Vanhin tavara myydään ensin (tärkeää elintarvikkeissa ja trendituotteissa).
* **Inventaario:** Tee lakisääteinen inventaario vähintään kerran vuodessa tilinpäätöksen yhteydessä.

---
**Esimerkki:** Jos myyt vuodessa 100 000 eurolla (omakustannushinta) ja varastosi arvo on keskimäärin 20 000 euroa, kiertonopeus on 5. Tuotteet viipyvät varastossa keskimäärin 73 päivää.
```
