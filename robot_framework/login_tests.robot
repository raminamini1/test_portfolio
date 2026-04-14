*** Settings ***
# ============================================================
# Robot Framework - Keyword-basierte Login-Tests
# Autor: Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM
# Framework: Robot Framework + SeleniumLibrary
# Zweck: Login-Formular auf Demo-Seite testen
# ============================================================
Library           SeleniumLibrary
Library           BuiltIn

Suite Setup       Browser oeffnen
Suite Teardown    Browser schliessen

*** Variables ***
${URL}              https://the-internet.herokuapp.com/login
${BROWSER}          chrome
${VALID_USER}       tomsmith
${VALID_PASS}       SuperSecretPassword!
${INVALID_USER}     wrong_user
${INVALID_PASS}     wrong_pass
${TIMEOUT}          10s

*** Test Cases ***

TC01 - Erfolgreicher Login mit gueltigen Zugangsdaten
    [Documentation]    Prueft ob ein Nutzer sich mit korrekten Daten einloggen kann.
    [Tags]             smoke    login    positiv
    Login ausfuehren    ${VALID_USER}    ${VALID_PASS}
    Erfolgsmeldung soll sichtbar sein

TC02 - Logout nach erfolgreichem Login
    [Documentation]    Nach Login soll der Logout-Button vorhanden und klickbar sein.
    [Tags]             regression    login
    Login ausfuehren    ${VALID_USER}    ${VALID_PASS}
    Click Button       xpath=//a[@href='/logout']
    Page Should Contain    Login Page

TC03 - Login mit falschem Benutzernamen schlaegt fehl
    [Documentation]    Falscher Nutzername -> Fehlermeldung erscheint.
    [Tags]             negativ    login
    Login ausfuehren    ${INVALID_USER}    ${VALID_PASS}
    Fehlermeldung soll sichtbar sein

TC04 - Login mit falschem Passwort schlaegt fehl
    [Documentation]    Falsches Passwort -> Fehlermeldung erscheint.
    [Tags]             negativ    login
    Login ausfuehren    ${VALID_USER}    ${INVALID_PASS}
    Fehlermeldung soll sichtbar sein

TC05 - Login mit leerem Benutzernamen schlaegt fehl
    [Documentation]    Leeres Namensfeld -> Fehlermeldung erscheint.
    [Tags]             negativ    grenzwert
    Login ausfuehren    ${EMPTY}    ${VALID_PASS}
    Fehlermeldung soll sichtbar sein

TC06 - Login mit leeren Feldern schlaegt fehl
    [Documentation]    Beide Felder leer -> Fehlermeldung erscheint.
    [Tags]             negativ    grenzwert
    Login ausfuehren    ${EMPTY}    ${EMPTY}
    Fehlermeldung soll sichtbar sein

TC07 - Login mit verschiedenen ungueltigen Kombinationen (Data-Driven)
    [Documentation]    Mehrere ungueltige Kombinationen in einem Test.
    [Tags]             negativ    data-driven
    [Template]         Login soll fehlschlagen
    wrong1             wrong1
    wrong2             wrong2
    ${EMPTY}           ${EMPTY}

*** Keywords ***

Browser oeffnen
    [Documentation]    Oeffnet den Browser und navigiert zur Login-Seite.
    Open Browser       ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}

Browser schliessen
    [Documentation]    Schliesst alle Browser nach dem Test-Suite.
    Close All Browsers

Login ausfuehren
    [Documentation]    Fuellt das Login-Formular aus und klickt Submit.
    [Arguments]        ${username}    ${password}
    Go To              ${URL}
    Input Text         id=username    ${username}
    Input Password     id=password    ${password}
    Click Button       css=button[type='submit']

Erfolgsmeldung soll sichtbar sein
    [Documentation]    Prueft ob die Erfolgsmeldung nach dem Login erscheint.
    Wait Until Element Is Visible    css=.flash.success    timeout=${TIMEOUT}
    Element Should Contain           css=.flash.success    You logged into a secure area!

Fehlermeldung soll sichtbar sein
    [Documentation]    Prueft ob die Fehlermeldung erscheint.
    Wait Until Element Is Visible    css=.flash.error    timeout=${TIMEOUT}
    Element Should Be Visible        css=.flash.error

Login soll fehlschlagen
    [Documentation]    Template-Keyword fuer datengetriebene negative Tests.
    [Arguments]        ${username}    ${password}
    Login ausfuehren    ${username}    ${password}
    Fehlermeldung soll sichtbar sein

# Terminal: robot login_tests.robot
# Mit Tags:  robot --include smoke login_tests.robot
