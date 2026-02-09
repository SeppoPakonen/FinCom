# Translation Task 259

**File to translate:** /common/active/sblo/Dev/Manager/DummyMusicCompany/db/business_forms_templates/PRH - Rajapinta ohjelmistoyrityksille _ PRH.md

**Target location:** ../db_eng/business_forms_templates/PRH - Rajapinta ohjelmistoyrityksille _ PRH.md

## Instructions

1. Manually translate the content of the file from Finnish to English.
2. Translate the title of the file as well.
3. Save the translated file in the db_eng directory in the corresponding location.
4. Do not use automated translation tools - manual translation is required.

## Original Content

```
# PRH: IXBRL-rajapinta ohjelmistoyrityksille

Tämä ohje on tarkoitettu taloushallinnon ohjelmistoja kehittäville yrityksille, jotka haluavat liittää ohjelmistonsa PRH:n tilinpäätösrajapintaan.

## 1. Mikä rajapinta on?
* **Tyyppi:** REST API.
* **Tarkoitus:** IXBRL-muotoisten tilinpäätösten ja metatietojen lähettäminen suoraan kaupparekisteriin.
* **Tuetut muodot:** Tällä hetkellä osakeyhtiöiden tilinpäätökset ja säätiöiden vuosiselvitykset.

## 2. Tekniset vaatimukset
* **Muoto:** Tilinpäätöksen on oltava IXBRL-standardin mukainen (Inline XBRL upotettuna HTML-koodiin).
* **Autentikointi:** Erillinen autentikaatiopalvelin (Access Token).
* **Validointi:** Rajapinta tarkistaa metatietojen (Y-tunnus, tilikausi) ja IXBRL-tiedoston rakenteen oikeellisuuden.

## 3. Käyttöönotto
* Edellyttää sopimusta PRH:n kanssa.
* PRH tarjoaa testipalvelimen kehitystyötä varten.
* Työmääräarvio: Noin 10–15 henkilötyöpäivää.
* **Hinta:** Rajapinnan käyttö on maksutonta.

---
**Lisätiedot:** digitilinpaatos@prh.fi

```
