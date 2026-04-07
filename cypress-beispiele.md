# 🌲 Cypress – Beispiele
**Autor:** Ramin Amini | Senior Software Tester | ISTQB-CTAL-TM  
**Eingesetzt in:** AIA AG (Makler- und Kundenportal)

---

## Was ist Cypress?

Cypress ist ein modernes Open-Source Testautomatisierungs-
framework für Web-Anwendungen. Es läuft direkt im Browser,
ist sehr schnell und ideal für End-to-End Tests, 
Integrationstests und API-Tests.

---

## 🌲 Beispiel 1 – Login Test
```javascript
// cypress/e2e/login.cy.js
// Projekt: AIA AG – Maklerportal

describe('Login – Maklerportal', () => {

  beforeEach(() => {
    cy.visit('https://portal.aia.de/login')
  })

  it('Erfolgreicher Login mit gültigen Daten', () => {
    cy.get('#username').type('makler@aia.de')
    cy.get('#password').type('Test1234!')
    cy.get('#btnLogin').click()
    cy.url().should('include', '/dashboard')
    cy.get('.welcome-message').should('contain', 'Willkommen')
  })

  it('Fehlermeldung bei falschem Passwort', () => {
    cy.get('#username').type('makler@aia.de')
    cy.get('#password').type('FalschesPasswort')
    cy.get('#btnLogin').click()
    cy.get('.error-message')
      .should('be.visible')
      .and('contain', 'Ungültige Anmeldedaten')
  })

  it('Pflichtfeld-Validierung bei leerem Benutzernamen', () => {
    cy.get('#btnLogin').click()
    cy.get('#username:invalid').should('exist')
  })
})
```

---

## 🌲 Beispiel 2 – Angebot erstellen (E2E Test)
```javascript
// cypress/e2e/angebot.cy.js
// End-to-End Test: Neues Versicherungsangebot

describe('Angebotserstellung – Haftpflicht', () => {

  before(() => {
    // Login vor allen Tests
    cy.login('makler@aia.de', 'Test1234!')
  })

  it('Neues Haftpflichtangebot erfolgreich erstellen', () => {
    
    // Navigation
    cy.get('#menuAngebote').click()
    cy.get('#btnNeuesAngebot').click()
    
    // Kundendaten eingeben
    cy.get('#vorname').type('Max')
    cy.get('#nachname').type('Mustermann')
    cy.get('#geburtsdatum').type('01.01.1980')
    cy.get('#plz').type('20354')
    
    // Produkt auswählen
    cy.get('#produktSelect').select('Haftpflicht')
    
    // Angebot berechnen
    cy.get('#btnBerechnen').click()
    
    // Ergebnis prüfen
    cy.get('#praemieAnzeige')
      .should('be.visible')
      .and('not.be.empty')
    
    cy.get('#angebotStatus')
      .should('contain', 'Offen')
    
    // Angebot speichern
    cy.get('#btnSpeichern').click()
    cy.get('.success-message')
      .should('contain', 'Angebot erfolgreich gespeichert')
  })
})
```

---

## 🌲 Beispiel 3 – API Test
```javascript
// cypress/e2e/api.cy.js
// API Test: Versicherungsdaten abrufen

describe('API Tests – Versicherungsportal', () => {

  it('GET – Kundendaten erfolgreich abrufen', () => {
    cy.request({
      method: 'GET',
      url: '/api/v1/kunden/12345',
      headers: {
        'Authorization': 'Bearer ' + Cypress.env('authToken')
      }
    }).then((response) => {
      expect(response.status).to.eq(200)
      expect(response.body).to.have.property('kundennummer')
      expect(response.body.nachname).to.eq('Mustermann')
    })
  })

  it('POST – Neues Angebot anlegen', () => {
    cy.request({
      method: 'POST',
      url: '/api/v1/angebote',
      headers: {
        'Authorization': 'Bearer ' + Cypress.env('authToken')
      },
      body: {
        kundennummer: '12345',
        produkt: 'Haftpflicht',
        vertragsbeginn: '2026-01-01'
      }
    }).then((response) => {
      expect(response.status).to.eq(201)
      expect(response.body).to.have.property('angebotId')
      expect(response.body.status).to.eq('Offen')
    })
  })

  it('DELETE – Nicht erlaubte Methode', () => {
    cy.request({
      method: 'DELETE',
      url: '/api/v1/angebote/99999',
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(403)
    })
  })
})
```

---

## 🔧 Cypress – Workflow in Projekten
Installation
→ npm install cypress --save-dev
Cypress öffnen
→ npx cypress open
Tests strukturieren
cypress/
├── e2e/
│   ├── login.cy.js
│   ├── angebot.cy.js
│   └── api.cy.js
├── fixtures/
│   └── testdaten.json
└── support/
└── commands.js
Testdaten auslagern
→ fixtures/testdaten.json für wiederverwendbare Daten
Custom Commands
→ support/commands.js für Login etc.
Tests ausführen
→ npx cypress run (headless)
→ npx cypress open (mit Browser)


---

## ✅ Best Practices

- Selektoren über data-cy Attribute verwenden
- cy.login() als Custom Command auslagern
- Testdaten in fixtures auslagern
- Keine harten Wartezeiten (cy.wait(5000)) – 
  stattdessen cy.get().should() verwenden
- API Tests parallel zu UI Tests schreiben
- Screenshots bei Fehlern automatisch speichern
