# 🤖 Robot Framework – Beispiele
**Autor:** Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM

---

## Was ist Robot Framework?

Robot Framework ist ein Open-Source Testautomatisierungs-
framework das Keyword-driven Testing unterstützt.
Es ist sehr lesbar, auch für Nicht-Programmierer geeignet
und wird häufig für Acceptance Testing und RPA eingesetzt.
Beliebt in Kombination mit SeleniumLibrary für Web-Tests
und RequestsLibrary für API-Tests.

---

## 🤖 Beispiel 1 – Login Test (Web)
```robot
*** Settings ***
Library     SeleniumLibrary
Resource    keywords.robot

Suite Setup     Browser öffnen
Suite Teardown  Browser schließen

*** Variables ***
${URL}          https://portal.versicherung.de
${BROWSER}      chrome
${VALID_USER}   makler@versicherung.de
${VALID_PASS}   Test1234!

*** Test Cases ***

Erfolgreicher Login Mit Gültigen Daten
    [Documentation]    Makler loggt sich erfolgreich ein
    [Tags]    Login    Smoke    Kritisch
    Öffne Login Seite
    Gib Benutzername Ein    ${VALID_USER}
    Gib Passwort Ein        ${VALID_PASS}
    Klicke Login Button
    Prüfe Dashboard Wird Angezeigt

Fehlermeldung Bei Falschem Passwort
    [Documentation]    Fehlermeldung bei ungültigen Daten
    [Tags]    Login    Negativ
    Öffne Login Seite
    Gib Benutzername Ein    ${VALID_USER}
    Gib Passwort Ein        FalschesPasswort
    Klicke Login Button
    Prüfe Fehlermeldung     Ungültige Anmeldedaten

*** Keywords ***

Öffne Login Seite
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id:username

Gib Benutzername Ein
    [Arguments]    ${username}
    Input Text    id:username    ${username}

Gib Passwort Ein
    [Arguments]    ${passwort}
    Input Password    id:password    ${passwort}

Klicke Login Button
    Click Button    id:btnLogin

Prüfe Dashboard Wird Angezeigt
    Wait Until Page Contains    Willkommen
    Location Should Contain     /dashboard

Prüfe Fehlermeldung
    [Arguments]    ${meldung}
    Wait Until Element Is Visible    class:error-message
    Element Should Contain    class:error-message    ${meldung}
```

---

## 🤖 Beispiel 2 – Angebotserstellung (E2E)
```robot
*** Settings ***
Library     SeleniumLibrary
Resource    login_keywords.robot

Suite Setup     Makler Login Durchführen

*** Variables ***
${VORNAME}      Max
${NACHNAME}     Mustermann
${GEBDATUM}     01.01.1980
${PRODUKT}      Haftpflicht

*** Test Cases ***

Neues Haftpflichtangebot Erstellen
    [Documentation]    End-to-End Test Angebotserstellung
    [Tags]    Angebot    E2E    Kritisch
    Navigiere Zu Angebote
    Klicke Neues Angebot
    Fülle Kundendaten Aus
    Wähle Produkt Aus       ${PRODUKT}
    Berechne Angebot
    Prüfe Prämie Wird Angezeigt
    Speichere Angebot
    Prüfe Erfolgsmeldung

*** Keywords ***

Navigiere Zu Angebote
    Click Element    id:menuAngebote
    Wait Until Page Contains    Angebote

Klicke Neues Angebot
    Click Button    id:btnNeuesAngebot
    Wait Until Element Is Visible    id:vorname

Fülle Kundendaten Aus
    Input Text    id:vorname        ${VORNAME}
    Input Text    id:nachname       ${NACHNAME}
    Input Text    id:geburtsdatum   ${GEBDATUM}
    Input Text    id:plz            20354

Wähle Produkt Aus
    [Arguments]    ${produkt}
    Select From List By Label    id:produktSelect    ${produkt}

Berechne Angebot
    Click Button    id:btnBerechnen
    Wait Until Element Is Visible    id:praemieAnzeige

Prüfe Prämie Wird Angezeigt
    Element Should Be Visible    id:praemieAnzeige
    Element Should Not Be Empty    id:praemieAnzeige

Speichere Angebot
    Click Button    id:btnSpeichern

Prüfe Erfolgsmeldung
    Wait Until Page Contains    Angebot erfolgreich gespeichert
```

---

## 🤖 Beispiel 3 – API Test
```robot
*** Settings ***
Library     RequestsLibrary
Library     Collections

Suite Setup    Erstelle Session

*** Variables ***
${BASE_URL}     https://api.versicherung.de
${AUTH_TOKEN}   Bearer test_token_123

*** Test Cases ***

GET Kundendaten Erfolgreich Abrufen
    [Documentation]    Kundendaten über API abrufen
    [Tags]    API    GET    Positiv
    ${headers}=    Create Dictionary
    ...    Authorization=${AUTH_TOKEN}
    ...    Content-Type=application/json
    ${response}=    GET On Session
    ...    versicherung_api
    ...    /api/v1/kunden/12345
    ...    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${body}    kundennummer
    Should Be Equal    ${body}[nachname]    Mustermann

POST Neues Angebot Anlegen
    [Documentation]    Neues Angebot über API erstellen
    [Tags]    API    POST    Positiv
    ${headers}=    Create Dictionary
    ...    Authorization=${AUTH_TOKEN}
    ...    Content-Type=application/json
    ${body}=    Create Dictionary
    ...    kundennummer=12345
    ...    produkt=Haftpflicht
    ...    vertragsbeginn=2026-01-01
    ${response}=    POST On Session
    ...    versicherung_api
    ...    /api/v1/angebote
    ...    headers=${headers}
    ...    json=${body}
    Should Be Equal As Numbers    ${response.status_code}    201
    ${result}=    Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${result}    angebotId
    Should Be Equal    ${result}[status]    Offen

*** Keywords ***

Erstelle Session
    Create Session    versicherung_api    ${BASE_URL}
```

---

## 🔧 Robot Framework – Workflow
```
1. Installation
   → pip install robotframework
   → pip install robotframework-seleniumlibrary
   → pip install robotframework-requestslibrary

2. Projektstruktur
   projekt/
   ├── tests/
   │   ├── login_tests.robot
   │   ├── angebot_tests.robot
   │   └── api_tests.robot
   ├── resources/
   │   ├── keywords.robot
   │   └── variables.robot
   └── results/
       ├── report.html
       └── log.html

3. Tests ausführen
   → robot tests/login_tests.robot
   → robot --include Kritisch tests/
   → robot --outputdir results tests/

4. Reports anzeigen
   → report.html im Browser öffnen
   → Detailliertes Log in log.html
```

---

## ✅ Best Practices

- Keywords in separate Resource-Dateien auslagern
- Sprechende Testnamen verwenden – kein technischer Jargon
- Tags für Kategorisierung nutzen (Smoke, Kritisch, Negativ)
- Variablen zentral in variables.robot verwalten
- Setup und Teardown für saubere Testumgebung nutzen
- Niemals Testdaten hardcoden – Variables Section verwenden
- Reports nach jedem Lauf archivieren
