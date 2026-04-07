# 🤖 TestComplete – Beispiele
**Autor:** Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM  
**Eingesetzt in:** AIA AG (WINSURE Core-Insurance-System)

---

## Was ist TestComplete?

TestComplete von SmartBear ist ein kommerzielles
Testautomatisierungstool für Desktop-, Web- und Mobile-Anwendungen.
Es unterstützt Keyword-driven, Skript-basierte und
aufgezeichnete Tests – ideal für komplexe Enterprise-Anwendungen.

---

## 🖥️ Beispiel 1 – Login Test (Keyword-Driven)

Test: Versicherungsportal_LoginKeyword Steps:
┌─────────────────────────────────────────────────────┐
│ Step 1: Browser öffnen                              │
│ → Aktion: Run Browser                               │
│ → URL: https://portal.versicherung.de               │
│                                                     │
│ Step 2: Benutzername eingeben                       │
│ → Aktion: Set Text                                  │
│ → Element: txtUsername                              │
│ → Wert: testuser@versicherung.de                    │
│                                                     │
│ Step 3: Passwort eingeben                           │
│ → Aktion: Set Text                                  │
│ → Element: txtPassword                              │
│ → Wert: ********                                    │
│                                                     │
│ Step 4: Login klicken                               │
│ → Aktion: Click                                     │
│ → Element: btnLogin                                 │
│                                                     │
│ Step 5: Erfolgsmeldung prüfen                       │
│ → Aktion: Check Text                                │
│ → Erwarteter Wert: "Willkommen"                     │
│ → Ergebnis: ✅ Passed                               │
└─────────────────────────────────────────────────────┘



---

## 🖥️ Beispiel 2 – Angebot erstellen (Skript-basiert)
```javascript
// TestComplete JavaScript Beispiel
// Projekt: AIA AG – WINSURE Portal
// Testfall: Neues Angebot erstellen

function Test_NeuesAngebotErstellen() {

  // Browser starten
  Browsers.Item(btChrome).Run("https://portal.aia.de");
  
  // Login
  Sys.Browser().Page("*").FindElement("#username").SetText("tester@aia.de");
  Sys.Browser().Page("*").FindElement("#password").SetText("Test1234!");
  Sys.Browser().Page("*").FindElement("#btnLogin").Click();
  
  // Navigation zu Angebote
  Sys.Browser().Page("*").FindElement("#menuAngebote").Click();
  Sys.Browser().Page("*").FindElement("#btnNeuesAngebot").Click();
  
  // Kundendaten eingeben
  Sys.Browser().Page("*").FindElement("#vorname").SetText("Max");
  Sys.Browser().Page("*").FindElement("#nachname").SetText("Mustermann");
  Sys.Browser().Page("*").FindElement("#geburtsdatum").SetText("01.01.1980");
  
  // Produkt auswählen
  Sys.Browser().Page("*").FindElement("#produktHaftpflicht").Click();
  
  // Angebot berechnen
  Sys.Browser().Page("*").FindElement("#btnBerechnen").Click();
  
  // Ergebnis prüfen
  var praemie = Sys.Browser().Page("*").FindElement("#praemieAnzeige").contentText;
  
  if (praemie != "") {
    Log.Message("✅ Angebot erfolgreich erstellt. Prämie: " + praemie);
  } else {
    Log.Error("❌ Angebot konnte nicht erstellt werden");
  }
}
```

---

## 🖥️ Beispiel 3 – Datengetriebener Test
```javascript
// Datengetriebener Test mit Excel-Testdaten
// Verschiedene Kundenprofile testen

function Test_AngebotMitTestdaten() {

  // Excel Testdaten laden
  var excelFile = "C:\\Testdaten\\Kundendaten.xlsx";
  var sheet = DDT.ExcelDriver(excelFile, "Kunden");
  
  while (!sheet.EOF()) {
  
    var vorname     = sheet.Value("Vorname");
    var nachname    = sheet.Value("Nachname");
    var gebDatum    = sheet.Value("Geburtsdatum");
    var produkt     = sheet.Value("Produkt");
    var erwartet    = sheet.Value("ErwartetePraemie");
    
    // Test ausführen
    var ergebnis = ErstelleAngebot(vorname, nachname, gebDatum, produkt);
    
    // Ergebnis prüfen
    if (ergebnis == erwartet) {
      Log.Message("✅ " + nachname + ": Prämie korrekt – " + ergebnis);
    } else {
      Log.Error("❌ " + nachname + ": Erwartet " + erwartet + 
                " aber erhalten " + ergebnis);
    }
    
    sheet.Next();
  }
  
  DDT.CloseDriver(sheet.Name);
}
```

---

## 🔧 TestComplete – Workflow in Projekten

Projekt anlegen
→ New Project → Web / Desktop / Mobile auswählen
Objekte aufzeichnen
→ Record & Playback für erste Skripte nutzen
→ Objekte im Object Browser identifizieren
Testfälle strukturieren
→ Keyword Tests für einfache Szenarien
→ Skripte für komplexe Logik
Testdaten verwalten
→ Excel / CSV für datengetriebene Tests
→ Variablen für Umgebungen (Test / Staging)
Ausführung & Reporting
→ Tests einzeln oder als Suite ausführen
→ Log-Ergebnisse analysieren
→ Report für Stakeholder exportieren



---

## ✅ Best Practices

- Objekte über ID oder Name ansprechen – nicht per Koordinaten
- Wiederverwendbare Funktionen auslagern
- Testdaten nie hardcoden – immer externe Dateien nutzen
- Nach jedem Schritt Assertions einbauen
- Logs aussagekräftig beschriften für spätere Analyse
- Regelmäßig Skripte warten bei UI-Änderungen
