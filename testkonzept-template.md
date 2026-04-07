# Testkonzept – [Projektname]
**Autor:** Ramin Amini  
**Version:** 1.0  
**Datum:** [Datum]

---

## 1. Projektziel & Testumfang

Beschreibung des Projekts und was getestet wird.

**Im Scope:**
- Funktionale Tests (Frontend, Backend, API)
- Regressionstests bei jedem Release
- End-to-End Geschäftsprozesse

**Nicht im Scope:**
- Performance Tests
- Penetrationstests

---

## 2. Teststrategie

| Teststufe | Beschreibung |
|---|---|
| Komponententest | Einzelne Module isoliert testen |
| Integrationstest | Zusammenspiel der Komponenten |
| Systemtest | Gesamtsystem gegen Anforderungen |
| Abnahmetest (UAT) | Fachliche Abnahme durch Auftraggeber |

**Vorgehensmodell:** Hybrid (agil + klassisch)  
**Testmethoden:** Äquivalenzklassen, Grenzwertanalyse, exploratives Testen

---

## 3. Testkriterien

**Eintrittskriterien:**
- Anforderungen sind dokumentiert und freigegeben
- Testumgebung ist stabil und verfügbar
- Testdaten sind vorbereitet

**Austrittskriterien:**
- Alle kritischen Testfälle bestanden
- Keine offenen Blocker oder Critical Bugs
- Testbericht erstellt und freigegeben

---

## 4. Risiken & Maßnahmen

| Risiko | Wahrscheinlichkeit | Maßnahme |
|---|---|---|
| Instabile Testumgebung | Mittel | Frühzeitig Umgebung prüfen |
| Unklare Anforderungen | Hoch | Review mit Fachbereich |
| Zeitdruck bei Releases | Hoch | Risikobasiertes Testen |

---

## 5. Tools

- **Testmanagement:** JIRA, XRay
- **Dokumentation:** Confluence
- **Automatisierung:** Cypress
- **API-Tests:** SOAP UI, Postman

---

## 6. Testteam & Verantwortlichkeiten

| Rolle | Person |
|---|---|
| Test Manager | Ramin Amini |
| Fachlicher Tester | [Name] |
| Entwickler | [Name] |
