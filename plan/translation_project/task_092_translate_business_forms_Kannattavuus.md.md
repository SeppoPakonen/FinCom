# Translation Task 092

**File to translate:** /common/active/sblo/Dev/Manager/DummyMusicCompany/db/business_forms/Kannattavuus.md

**Target location:** ../db_eng/business_forms/Kannattavuus.md

## Instructions

1. Manually translate the content of the file from Finnish to English.
2. Translate the title of the file as well.
3. Save the translated file in the db_eng directory in the corresponding location.
4. Do not use automated translation tools - manual translation is required.

## Original Content

```
# Kannattavuus, vakavaraisuus ja maksuvalmius

Tämä asiakirja käsittelee yrityksen talouden "terveyskolmiota" sekä antaa käytännön ohjeita ja laskukaavoja kannattavuuden hallintaan.

---

## 1. Talouden terveyskolmio

1. **Kannattavuus:** Yrityksen kyky tuottaa voittoa. Pitkällä aikavälillä tuottojen on oltava kustannuksia suuremmat.
2. **Vakavaraisuus:** Kyky selviytyä sitoumuksista pitkällä aikavälillä (oma pääoma vs. vieras pääoma).
3. **Maksuvalmius (Likviditeetti):** Kyky selviytyä juoksevista maksuista (laskut, palkat) ajallaan.

---

## 2. Kannattavuuden osatekijät ja hinnoittelualue

- **Hinta arvon mittarina:** Hinta viestii asiakkaalle tuotteen tai palvelun arvon.
- **Hinnoittelualue:**
    - **Yläraja:** Kysyntä (mitä asiakas on valmis maksamaan).
    - **Alaraja:** Kustannukset (mitä tuotteen valmistus/hankinta maksaa).
- **Tulokseen vaikuttavat:** Myyntimäärä (toiminta-aste), myyntihinta, muuttuvat ja kiinteät kustannukset sekä myyntijakauma (erikatteelliset tuotteet).

---

## 3. Kustannusten ryhmittely

| Tyyppi | Selitys | Esimerkkejä |
| :--- | :--- | :--- |
| **Muuttuvat kulut** | Riippuvat myynnin määrästä. | Raaka-aineet, tavaraostot, rahdit, urakkapalkat. |
| **Kiinteät kulut** | Pysyvät samana (lyhyellä aikavälillä). | Vuokra, kuukausipalkat, vakuutukset, poistot, hallinto. |
| **Välittömät kulut** | Voidaan kohdistaa suoraan tuotteelle. | Materiaalit, suora työ. |
| **Välilliset kulut** | Yleiskustannukset, jotka vyörytetään. | Toimitilakulut, markkinointi, siivous. |

---

## 4. Katetuottolaskenta (Tunnusluvut ja kaavat)

### Peruskaavat:
- **Katetuotto (Myyntikate):** Tuotot – Muuttuvat kustannukset
- **Katetuotto %:** (Katetuotto / Myyntituotot) × 100
- **Tulos:** Katetuotto – Kiinteät kustannukset
- **Voittoprosentti:** (Voitto / Myyntituotot) × 100

### Kriittinen piste ja varmuusmarginaali:
- **Kriittinen piste (€):** (Kiinteät kustannukset / Katetuotto %) × 100
- **Kriittinen piste (kpl):** Kriittinen piste € / Myyntihinta (alv 0 %)
- **Varmuusmarginaali:** Toteutunut myynti – Kriittinen myynti. Kertoo, paljonko myynti voi laskea ennen tappiota.

---

## 5. Myyntihinnan laskeminen (Vältä virheitä!)

Yleinen virhe on lisätä kateprosentti ostohintaan (kertolasku). Oikea tapa on jakaa (marginaalilaskenta).

**Oikea kaava (alv 0 %):**
> **Myyntihinta = (100 * Muuttuvat kustannukset) / (100 - Kateprosentti)**

*Esimerkki: Haluat 35 % katteen 100 euron ostohintaan.*
- *Oikein: 100 / (100-35) * 100 = **153,85 €** (Kate on 53,85 € eli 35 %).*
- *Väärin: 100 * 1,35 = 135 € (Kate on vain 26 %).*

### Hinnoittelukerroin:
- **Kerroin:** 100 / (100 - Katetuotto %)
- *Esimerkki: 60 % katetavoite -> 100/40 = 2,5. Ostohinta 12 € * 2,5 = 30 € (alv 0 %).*

---

## 6. Toimialakohtaisia nyrkkisääntöjä

### Keskimääräisiä myyntikatteita:
- Autokauppa: 20–25 %
- Kodintekniikka: 20 %
- Tukkukauppa: 28 %
- Vähittäiskauppa: 29 %
- Päivittäistavarakauppa: 26–28 %
- Vaatekauppa: 30 %

### Palveluyrityksen tuntihinta (alv-sis.):
- **Työvoimavaltainen:** 3 × työntekijän tuntipalkka.
- **Kone- ja tarvikevaltainen:** 4 × työntekijän tuntipalkka.

---

## 7. Kapasiteetti ja hävikki

- **Kapasiteetti:** Enimmäissuorituskyky (esim. 2500 kpl/kk).
- **Toiminta-aste:** Toteutunut määrä (esim. 2200 kpl -> käyttöaste 88 %).
- **Hävikki (Vähittäiskauppa):** Varkaudet, rikkoutumiset, vanhentuminen. Usein n. 4 % myynnistä.
    - *Laskenta:* (Alkuvarasto + Ostot) - Myynnit - Loppuvarasto = Hävikki.

---

## 8. Laskuharjoituksia

1. **Tuotehinnoittelu:** Ostohinta 89 €, rahti 3 €. Myyntikate 40 %, alennusvaraus 15 %, alv 25,5 %. Laske hyllyhinta.
2. **Luomutuote:** Ostohinta 6,90 €/kg. Kate 25 %, hävikki 10 %, alv 13,5 %. Laske hyllyhinta.
3. **Palvelu:** Palkkatavoite 2000 €/kk, vuokra 400 €, lainan korko 5 %, myyntikate 80 %, työtunteja 1300 h/v. Laske tuntihinta.
```
