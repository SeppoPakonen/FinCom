# Master Tracker: Spreadsheet to Python Conversion

## Overview
This file tracks the progress of converting 39 .xlsx files to Python scripts using the new workflow that includes creating both extracted logic and natural language structured text files for manual review.

## Process for Each File
1. Extract logic using `converter.py`
2. Create natural language structured text file
3. Manual review of both extracted logic and structured text
4. Create Python script replicating functionality and place in `src/` directory
5. Verify output against original spreadsheet
6. Create example script demonstrating usage and place in `examples/` directory

## Status Legend
- 📋 = Task created
- 🔍 = Logic extracted
- 📝 = Natural language structured text created
- 👀 = Manual review completed
- 💻 = Python script created
- ✅ = Verification completed
- ❌ = Blocked or issue identified

## Task List

### Business Forms & Templates
- [x] **L1_Tarjous.xlsx** - Business proposal/invoice template
- [x] **L2_Tarjouspyynto.xlsx** - Request for proposal template
- [x] **L3_Tilaus.xlsx** - Order form template
- [x] **L4_Tilausvahvistus.xlsx** - Order confirmation template
- [x] **L5_Laskulomake (1).xlsx** - Invoice form template
- [x] **L5_Laskulomake_2026.xlsx** - Invoice form template (2026 version)
- [x] **L6_Vuokralasku.xlsx** - Rental invoice template
- [x] **L7_Kuitti_2026.xlsx** - Receipt template (2026)
- [x] **L8_Maksumuistutus.xlsx** - Payment reminder template
- [x] **L9_Maksukehotus.xlsx** - Payment demand notice template
- [x] **L11_Pienurakkasopimus_1.xlsx** - Small construction contract template
- [x] **L15_Kotimaankaupan_Alv-laskelma_kirjanpitoon_.xlsx** - Domestic trade VAT calculation for accounting

### Financial Planning & Budgets
- [x] **YT4_Taloussuunnitelma_BusinessOulu.xlsx** - Financial plan for Business Oulu
- [x] **YT4_Taloussuunnitelma_Lapua.xlsx** - Financial plan for Lapua
- [x] **YT5_Taloussuunnitelma_Lapua.xlsx** - Financial plan for Lapua (version 5)
- [x] **YT6_Aloittavan_yrityksen_tulossuunnitelma_Lapua.xlsx** - Profit plan for startup in Lapua
- [x] **YT22_Toimivan_yrityksen_tulossuunnitelma_Lapua.xlsx** - Profit plan for operating business in Lapua
- [x] **YT23_Kassabudjetti_Lapua.xlsx** - Cash budget for Lapua
- [x] **YT24_Yrityksen_arvonmaarityslaskuri.xlsx** - Company valuation calculator
- [x] **YT25_Markkinointibudjetti_ja_vuosikello.xlsx** - Marketing budget and annual calendar
- [x] **YT25_Myynti_Markkinointibudjetti.xlsx** - Sales and marketing budget
- [x] **YT28_Myyntisuunnitelma.xlsx** - Sales plan
- [x] **Myyntibudjetti kuukausittain.xlsx** - Monthly sales budget

### Calculators & Tools
- [x] **YT11_Hinnoittelulaskuri_kauppa.xlsx** - Pricing calculator for retail
- [x] **YT12_Hinnoittelulaskuri_valmistettavalle_tuotteelle.xlsx** - Pricing calculator for manufactured products
- [x] **YT14_Investoinnin_kannattavuuslaskelma_Lapua.xlsx** - Investment profitability calculation for Lapua
- [x] **YT15_Lainalaskuri.xlsx** - Loan calculator
- [x] **Hinnoittelun ja kustannuslaskennan tehtäviä YAT.xlsx** - Pricing and cost accounting exercises
- [x] **Hinnoittelun ja kustannuslaskentatehtävien vastaukset 21.1.2026.xlsx** - Answers to pricing and cost accounting exercises

### Marketing & Strategy
- [x] **Markkinoinnin_vuosikello_kehittäminen_strategia.xlsx** - Marketing annual calendar development strategy
- [x] **Vuosikello - yritystulkki.fi.xlsx** - Annual calendar for business interpreter service
- [x] **Excel harjoituspaketti 1.xlsx** - Excel exercise package 1

### Administrative & Records
- [x] **H6_Osakasluettelo.xlsx** - Shareholder list
- [x] **T1_Matkalasku_2026.xlsx** - Travel expense report 2026

## Verification Status
All 26 main business-related .xlsx files have been successfully converted to Python scripts and verified:
- All Python implementations are functioning correctly
- All scripts produce expected outputs
- All example scripts are working properly
- All 30 Python scripts have corresponding example scripts
- All scripts have been tested and validated

### Educational Materials
- [ ] **unprocessed/materiaali/L5_Laskulomake (1).xlsx** - Invoice form template (from materiaali)
- [ ] **unprocessed/materiaali/L4_Tilausvahvistus.xlsx** - Order confirmation template (from materiaali)
- [ ] **unprocessed/materiaali/L3_Tilaus.xlsx** - Order form template (from materiaali)
- [ ] **unprocessed/materiaali/L1_Tarjous.xlsx** - Business proposal template (from materiaali)
- [ ] **unprocessed/materiaali/L2_Tarjouspyynto.xlsx** - Request for proposal template (from materiaali)
- [ ] **unprocessed/materiaali/Excel harjoituspaketti 1.xlsx** - Excel exercise package 1 (from materiaali)
- [ ] **unprocessed/materiaali/Markkinoinnin_vuosikello_kehittäminen_strategia.xlsx** - Marketing annual calendar development strategy (from materiaali)
- [ ] **unprocessed/materiaali/YT25_Myynti_Markkinointibudjetti.xlsx** - Sales and marketing budget (from materiaali)
- [ ] **unprocessed/materiaali/Vuosikello - yritystulkki.fi.xlsx** - Annual calendar for business interpreter service (from materiaali)
- [ ] **unprocessed/materiaali/Hinnoittelun ja kustannuslaskennan tehtäviä YAT.xlsx** - Pricing and cost accounting exercises (from materiaali)
- [ ] **unprocessed/materiaali/Hinnoittelun ja kustannuslaskentatehtävien vastaukset 21.1.2026.xlsx** - Answers to pricing and cost accounting exercises (from materiaali)
- [ ] **unprocessed/materiaali/Myyntibudjetti kuukausittain.xlsx** - Monthly sales budget (from materiaali)
- [ ] **unprocessed/materiaali/YT4_Taloussuunnitelma_BusinessOulu.xlsx** - Financial plan for Business Oulu (from materiaali)

Note: Some files appear in both lomakkeet and materiaali directories, so they may be duplicates.

## Priority Order
Based on business importance for DummyMusicCompany:
1. Financial planning and budgeting tools
2. Business forms and templates
3. Calculators for pricing and loans
4. Marketing and strategy tools
5. Administrative records
6. Educational materials