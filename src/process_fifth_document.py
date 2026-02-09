"""
Script to manually process the AB-Kortti documentation file and add keywords, ECS elements, constraints, and metadata.
"""

import json
import sys
import os
from datetime import datetime

# Add the current directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_structures.keyword import Keyword, KeywordCollection
from src.data_structures.ecs_elements import Entity, Component, System, ECSArchitecture
from src.data_structures.constraint import Constraint, ConstraintCollection, ConstraintType, SeverityLevel
from src.data_structures.metadata import Metadata


def process_ab_kortti_document():
    """
    Manually process the AB-Kortti document to add:
    - Keywords
    - ECS elements (entities, components, systems)
    - Constraints
    - Search-engine metadata
    """
    
    # Read the original document
    with open("../docs/business_forms/AB-Kortti.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    print("Processing document: AB-Kortti.md")
    print("="*50)
    
    # 1. Extract and add keywords
    print("1. Adding keywords...")
    keywords = [
        Keyword(
            term="AB-kortti",
            frequency=15,
            relevance=0.95,
            category="qualification",
            tags=["manual_extraction", "professional_qualification", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=10
        ),
        Keyword(
            term="tietokoneen käyttöoikeus",
            frequency=8,
            relevance=0.9,
            category="qualification",
            tags=["manual_extraction", "professional_certification", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=50
        ),
        Keyword(
            term="ammattitaito",
            frequency=7,
            relevance=0.85,
            category="competence",
            tags=["manual_extraction", "skills_assessment", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=100
        ),
        Keyword(
            term="tutkinnon osa",
            frequency=6,
            relevance=0.8,
            category="qualification",
            tags=["manual_extraction", "certification_process", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=150
        ),
        Keyword(
            term="osaamisen arviointi",
            frequency=9,
            relevance=0.9,
            category="assessment",
            tags=["manual_extraction", "competency_evaluation", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=200
        ),
        Keyword(
            term="tietotekniikka",
            frequency=12,
            relevance=0.9,
            category="technical_skill",
            tags=["manual_extraction", "digital_competence", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=250
        ),
        Keyword(
            term="toimisto-ohjelmistot",
            frequency=10,
            relevance=0.85,
            category="software",
            tags=["manual_extraction", "productivity_tools", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=300
        ),
        Keyword(
            term="ammattiosaaminen",
            frequency=5,
            relevance=0.75,
            category="competence",
            tags=["manual_extraction", "professional_skills", "finnish"],
            source_file="../docs/business_forms/AB-Kortti.md",
            position_in_text=350
        )
    ]
    
    keyword_collection = KeywordCollection(
        source_file="../docs/business_forms/AB-Kortti.md",
        keywords=keywords,
        total_word_count=len(content.split()),
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(keywords)} keywords")
    
    # 2. Identify and map ECS elements
    print("2. Adding ECS elements...")
    
    # Entities
    entities = [
        Entity(
            name="Tietokoneen Käyttäjä (AB-kortti haltija)",
            description="Ammattitason tietokoneen käyttäjä, jolla on AB-korttitutkinnon osa",
            attributes={
                "koulutustaso": "ammattitutkinto",
                "osaamisalueet": ["toimisto_ohjelmistot", "tietotekniikan_perusteet", "digitaalinen_lukutaito"],
                "tutkinnon_tila": "vahvistettu"
            },
            tags=["ammattilainen", "kvalifioitu_kayttaja"],
            source_file="../docs/business_forms/AB-Kortti.md",
            relationships={
                "omistaa": ["AB_kortti_sertifikaatti"],
                "demonstroi": ["Tietokoneen_kayttoosaaminen"],
                "kayttaa": ["Toimisto_ohjelmistot"]
            }
        ),
        Entity(
            name="Arviointiviranomainen",
            description="Organisaatio, joka vastaa AB-korttitutkinnon osien arvioinnista",
            attributes={
                "vastuut": ["arvioida_osaamista", "varmistaa_osaa", "myonta_kirjapapereita"],
                "kayttama_standardit": ["ammattistandardit", "tutkinnon_osien_kriteerit"]
            },
            tags=["arvioija", "sertifioija"],
            source_file="../docs/business_forms/AB-Kortti.md",
            relationships={
                "arvioi": ["Tietokoneen_kayttajat"],
                "myontaa": ["AB_kortti_sertifikaatit"],
                "yllapitaa": ["Kvalifikointistandardit"]
            }
        ),
        Entity(
            name="Toimisto-ohjelmistopaketti",
            description="Ohjelmistot, joita kaytetaan tuottavuus- ja liiketoimintatehtäviin",
            attributes={
                "komponentit": ["tekstinkasittely", "taulukkolaskenta", "esitysgrafiikka", "tietokanta"],
                "kayttoalueet": ["asiakirjan_luonti", "datan_analyysi", "esitykset", "tietojen_hallinta"]
            },
            tags=["ohjelmisto", "tuottavuustyokalu"],
            source_file="../docs/business_forms/AB-Kortti.md",
            relationships={
                "kaytetaan": ["Tietokoneen_kayttajien_toimesta"],
                "arvioidaan": ["AB_kortti_arvioinnissa"]
            }
        ),
        Entity(
            name="Ammattitaidon Standardi",
            description="Standardi, joka maarittelee AB-korttitutkinnon osien vaatimukset",
            attributes={
                "kriteerit": ["osaamistasot", "tietoalueet", "osaamisdomaanit"],
                "arviointimenetelmat": ["kaytannon_tehtavat", "teoreettiset_testit", "portfolion_arviointi"]
            },
            tags=["standardi", "vaatimus"],
            source_file="../docs/business_forms/AB-Kortti.md",
            relationships={
                "maarittelee": ["AB_kortti_vaaimukset"],
                "arvioidaan": ["Arviointiviranomaisen_toimesta"],
                "saavutetaan": ["Tietokoneen_kayttajien_toimesta"]
            }
        )
    ]
    
    # Components
    components = [
        Component(
            name="AB-kortin Sertifikaatti",
            description="Virallinen tunnustus tietokoneen käyttöosaamisesta",
            properties={
                "voimassaolo": "yleensä_rajoittamaton",
                "myonto_valtuus": "valtuutettu_arviointiviranomainen",
                "tunnustustaso": "kansallisesti_tunnustettu"
            },
            data_schema={
                "voimassaolo": "string",
                "myonto_valtuus": "string",
                "tunnustustaso": "string"
            },
            tags=["sertifikaatti", "tunnistus"],
            source_file="../docs/business_forms/AB-Kortti.md"
        ),
        Component(
            name="Tietokoneen Osaamiset",
            description="Erityiset ICT-taidot, jotka arvioidaan AB-kortin yhteydessä",
            properties={
                "osaamisalueet": ["tekstinkasittely", "taulukkolaskenta", "esitykset", "tietokannat", "informaation_haku"],
                "taitotasot": ["perustaso", "keskitaso", "edistynyt"]
            },
            data_schema={
                "osaamisalueet": "list[string]",
                "taitotasot": "list[string]"
            },
            tags=["osaaminen", "taitojen_arviointi"],
            source_file="../docs/business_forms/AB-Kortti.md"
        ),
        Component(
            name="Osaamisen Demonstrointiprosessi",
            description="Menetelmä tietokoneen käyttöosaamisen arvioimiseksi",
            properties={
                "arviointityyppi": "kaytannon_demonstrointi",
                "arviointikriteerit": ["tarkkuus", "tehokkuus", "ongelmanratkaisukyky"],
                "vaaditut_tehtavat": ["asiakirjan_luonti", "datan_analyysi", "esityksen_valmistelu"]
            },
            data_schema={
                "arviointityyppi": "string",
                "arviointikriteerit": "list[string]",
                "vaaditut_tehtavat": "list[string]"
            },
            tags=["arviointi", "osaamisen_mittaus"],
            source_file="../docs/business_forms/AB-Kortti.md"
        )
    ]
    
    # Systems
    systems = [
        System(
            name="AB-kortin Kvalifikointijärjestelmä",
            description="Prosessi AB-korttitutkinnon osien saavuttamiseksi ja ylläpitämiseksi",
            behavior=(
                "1. Hakija valmistelee todistusaineistot\n"
                "2. Hakija rekisteröityy arviointiin\n"
                "3. Arviointiviranomainen arvioi osaamisen\n"
                "4. Käytännön osaamisen demonstroituminen suoritetaan\n"
                "5. Sertifikaatti myönnetään jos vaatimukset täyttyvät\n"
                "6. Osaaminen ylläpidetään jatkuvan oppimisen kautta"
            ),
            dependencies=[
                "Tietokoneen Osaamiset",
                "Osaamisen Demonstrointiprosessi",
                "Ammattitaidon Standardi"
            ],
            triggers=["hakemus_kvalifikointiin"],
            tags=["kvalifikointiprosessi", "sertifiointijärjestelmä"],
            source_file="../docs/business_forms/AB-Kortti.md"
        ),
        System(
            name="ICT-osaamisen Arviointikehys",
            description="Kehys ICT-osaamisen arvioimiseksi",
            behavior=(
                "1. Maaritellään osaamisvaatimukset\n"
                "2. Luodaan arviointitehtävät\n"
                "3. Arvioidaan käytännön taidot\n"
                "4. Varmistetaan teoreettinen osaaminen\n"
                "5. Myönnetään sertifikaatti tulosten perusteella\n"
                "6. Ylläpidetään laadun vakautta"
            ),
            dependencies=[
                "Toimisto-ohjelmistopaketti",
                "Ammattitaidon Standardi"
            ],
            triggers=["osaamisarviointi"],
            tags=["arviointikehys", "osaamisen_evaluointi"],
            source_file="../docs/business_forms/AB-Kortti.md"
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file="../docs/business_forms/AB-Kortti.md",
        entities=entities,
        components=components,
        systems=systems,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(entities)} entities, {len(components)} components, {len(systems)} systems")
    
    # 3. Extract and document constraints
    print("3. Adding constraints...")
    constraints = [
        Constraint(
            id="constraint_ab_kortti_vaadimukset",
            title="AB-kortin Kvalifikointivaatimukset",
            description="Hakijan täytyy demonstroida osaaminen kaikilla vaadituilla osa-alueilla",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="kaikki_pakolliset_osat_demonstroitu == True",
            scope="kvalifikointi_arviointi",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/AB-Kortti.md",
            tags=["kvalifikointi", "vaatimus"],
            related_constraints=[],
            validation_logic="tarkista_osat_demonstroituna(suoritetut_tehtavat, pakolliset_tehtavat)",
            error_message="Kaikki vaaditut osa-alueet täytyy demonstroida AB-kortin saamiseksi"
        ),
        Constraint(
            id="constraint_toimisto_ohjelmisto_osaa",
            title="Toimisto-ohjelmistojen Osaamisvaatimus",
            description="Hakijan täytyy näyttää keskitaso tai edistynyt osaaminen toimisto-ohjelmistoissa",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="toimisto_ohjelmisto_osaa_taso >= 'keskitaso'",
            scope="osaamis_arviointi",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/AB-Kortti.md",
            tags=["ohjelmisto", "osaaminen"],
            related_constraints=["constraint_ab_kortti_vaadimukset"],
            validation_logic="arvioi_ohjelmisto_osaa(osaamistaso)",
            error_message="Keskitason tai edistyneen osaamisen taso toimisto-ohjelmistoissa vaaditaan"
        ),
        Constraint(
            id="constraint_demonstraation_tarkkuus",
            title="Tarkkuus Käytännön Demonstraatiossa",
            description="Tehtävät täytyy suorittaa korkealla tarkkuudella arvioinnin aikana",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="tehtavan_tarkkuusaste >= 0.9",
            scope="arviointi_prosessi",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/AB-Kortti.md",
            tags=["suoritus", "tarkkuus"],
            related_constraints=["constraint_ab_kortti_vaadimukset"],
            validation_logic="laske_tarkkuus_arvo(oikeat_vastaukset, kaikki_vastaukset)",
            error_message="Tehtävät täytyy suorittaa vähintään 90% tarkkuudella"
        ),
        Constraint(
            id="constraint_portfolion_sisalto",
            title="Portfolion Sisältövaatimukset",
            description="Portfolion täytyy sisältää kaikkien vaadittujen osaamisalueiden todisteet",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="kaikki_osaamis_todisteet_lahetetty == True",
            scope="portfolio_arviointi",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/AB-Kortti.md",
            tags=["portfolio", "todiste"],
            related_constraints=["constraint_ab_kortti_vaadimukset"],
            validation_logic="tarkista_portfolio_sisalto(portfolio, vaaditut_todisteet)",
            error_message="Portfolion täytyy sisältää todisteet kaikista vaadituista osaamisalueista"
        ),
        Constraint(
            id="constraint_arviointi_aikataulu",
            title="Arviointi Aikataulutusvaatimukset",
            description="Arviointi täytyy suorittaa määritellyssä ajassa",
            constraint_type=ConstraintType.TEMPORAL,
            condition="arviointi_suoritettu_maaritellyssa_ajassa == True",
            scope="arviointi_prosessi",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/AB-Kortti.md",
            tags=["aikataulu", "määräaika"],
            related_constraints=[],
            validation_logic="tarkista_arviointi_aikataulu(lopputulos_aika, määräaika)",
            error_message="Arviointi täytyy suorittaa määritellyssä ajassa"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file="../docs/business_forms/AB-Kortti.md",
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(constraints)} constraints")
    
    # 4. Add search-engine metadata
    print("4. Adding search-engine metadata...")
    metadata = Metadata(
        source_file="../docs/business_forms/AB-Kortti.md",
        title="AB-kortti - Tietokoneen käyttöoikeuden vaatimukset",
        description="Dokumentaatio AB-korttitutkinnon osaamisvaatimuksista, arviointimenetelmistä ja sertifioinnista",
        tags=["AB-kortti", "tietokoneen käyttö", "ICT-osaaminen", "ammattitunnustus", "toimisto-ohjelmistot", "osaamisen_arviointi"],
        categories=["kvalifikointi", "sertifiointi", "ICT", "ammattitaidon_kehittäminen"],
        related_files=["AB-Card.md", "Tietokoneen käyttäjän AB-kortin sisältö ja tavoitteet.md"],
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="manual_processing",
        version="1.0",
        relevance_score=0.92,
        content_type="kvalifikointi_opas",
        business_domains=["koulutus", "ammattitunnustus", "ICT"],
        difficulty_level="perustaso",
        estimated_reading_time=4,
        word_count=len(content.split()),
        language="fi",
        keywords=["AB-kortti", "tietokoneen käyttö", "kvalifikointi", "ICT", "toimisto-ohjelmistot", "osaaminen", "arviointi", "ammattitaito"],
        related_entities=["Tietokoneen Käyttäjä", "Arviointiviranomainen", "Toimisto-ohjelmistopaketti", "Ammattitaidon Standardi"],
        related_components=["AB-kortin Sertifikaatti", "Tietokoneen Osaamiset", "Osaamisen Demonstrointiprosessi"],
        related_systems=["AB-kortin Kvalifikointijärjestelmä", "ICT-osaamisen Arviointikehys"],
        related_constraints=["constraint_ab_kortti_vaadimukset", "constraint_toimisto_ohjelmisto_osaa", "constraint_demonstraation_tarkkuus"],
        custom_fields={
            "kvalifikointityyppi": "ammattitaito",
            "arviointimenetelma": "kaytannon_demonstrointi",
            "kohderyhma": ["opiskelijat", "ammattilaiset", "tyottomat"],
            "esitietovaatimukset": ["perustason_tietokoneen_kaytto"],
            "tunnustuselin": "valtuutettu_arviointiviranomainen"
        }
    )
    
    print("   Added search-engine metadata")
    
    # Save the processed data
    processed_data = {
        "original_content": content,
        "keywords": [kw.to_dict() for kw in keyword_collection.keywords],
        "ecs_elements": ecs_architecture.to_dict(),
        "constraints": [con.to_dict() for con in constraint_collection.constraints],
        "metadata": metadata.to_dict(),
        "processing_date": datetime.now().isoformat(),
        "processor": "manual"
    }
    
    # Write processed data to a new file
    with open("../processed_docs/ab_kortti_finnish_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDocument processed successfully!")
    print(f"- Keywords: {len(keywords)}")
    print(f"- Entities: {len(entities)}")
    print(f"- Components: {len(components)}")
    print(f"- Systems: {len(systems)}")
    print(f"- Constraints: {len(constraints)}")
    print(f"- Metadata: Added")
    print(f"\nProcessed data saved to: ../processed_docs/ab_kortti_finnish_processed.json")
    
    return processed_data


if __name__ == "__main__":
    processed_data = process_ab_kortti_document()