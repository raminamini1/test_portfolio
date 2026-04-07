# 🥒 Gherkin & Zephyr Scale – Beispiele
**Autor:** Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM  
**Eingesetzt in:** ITZBund (KVPV), DVZ M-V (SGB XIV)

---

## Was ist Gherkin?

Gherkin ist eine natürlichsprachliche Beschreibungssprache für
Testszenarien nach dem BDD-Prinzip (Behavior Driven Development).
Testfälle werden in der Form **Given – When – Then** geschrieben
und sind für Fachbereiche und Entwickler gleichermassen verständlich.

---

## Was ist Zephyr Scale?

Zephyr Scale ist ein Test-Management-Tool direkt in JIRA.
Es ermöglicht die Verwaltung von Testfällen, Testzyklen,
Testausführungen und Berichten – alles verknüpft mit JIRA-Tickets.

---

## 📋 Beispiel 1 – Versicherung: Angebotserstellung
```gherkin
Feature: Angebotserstellung im Versicherungsportal

  Background:
    Given der Makler ist im Portal eingeloggt
    And die Kundendaten sind vollständig erfasst

  Scenario: Erfolgreiches Erstellen eines Haftpflichtangebots
    Given der Makler öffnet die Angebotsmaske für "Haftpflicht"
    When er die Vertragsdaten eingibt
    And er auf "Angebot berechnen" klickt
    Then wird ein Angebot mit korrekter Prämie angezeigt
    And das Angebot erhält den Status "Offen"

  Scenario: Pflichtfeld nicht ausgefüllt
    Given der Makler öffnet die Angebotsmaske für "Haftpflicht"
    When er das Geburtsdatum des Kunden leer lässt
    And er auf "Angebot berechnen" klickt
    Then wird eine Fehlermeldung angezeigt
    And das Angebot wird nicht gespeichert
```

---

## 📋 Beispiel 2 – Öffentlicher Sektor: Datenaustausch
```gherkin
Feature: Elektronische Übermittlung von Krankenversicherungsdaten

  Background:
    Given die Schnittstelle zwischen BZSt und Krankenkasse ist aktiv
    And die Testdaten sind im SFTP-Verzeichnis bereitgestellt

  Scenario: Erfolgreiche Datenübermittlung
    Given eine gültige XML-Datei liegt im Eingangsverzeichnis vor
    When der automatische Übermittlungsprozess startet
    Then wird die Datei korrekt verarbeitet
    And eine Bestätigung wird ins Ausgangsverzeichnis geschrieben
    And der Status in der Datenbank ist "Erfolgreich"

  Scenario: Ungültiges XML-Format
    Given eine XML-Datei mit fehlerhafter Struktur liegt vor
    When der Übermittlungsprozess startet
    Then wird die Datei abgelehnt
    And eine Fehlermeldung wird protokolliert
    And der Status in der Datenbank ist "Fehler"
```

---

## 📋 Beispiel 3 – Logistik: Container-Tracking
```gherkin
Feature: Container-Verfolgung im C&T System

  Scenario: Container-Status abfragen
    Given der Nutzer ist im Tracking-Portal eingeloggt
    When er die Container-ID "MSKU1234567" eingibt
    And er auf "Suchen" klickt
    Then wird der aktuelle Standort des Containers angezeigt
    And der Status "In Transit" wird korrekt dargestellt

  Scenario: Ungültige Container-ID
    Given der Nutzer ist im Tracking-Portal eingeloggt
    When er eine ungültige Container-ID "XYZ000" eingibt
    And er auf "Suchen" klickt
    Then wird die Meldung "Container nicht gefunden" angezeigt
```

---

## 🔧 Zephyr Scale – Workflow
