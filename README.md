WORK IN PROGRESS
# Flask-prosjekt -- Dokumentasjon

## 1. Forside

**Prosjekttittel: Review Site**\
**Navn: Eduard**\
**Klasse: 2IMI**\
**Dato: 2025-2026**

**Kort beskrivelse av prosjektet:**\
*En nettside der du kan lese andres reviews og lage dine egne. Du skal kunne se hvem som lagde reviewene.*

------------------------------------------------------------------------

## 2. Systembeskrivelse

**Formål med applikasjonen:**\
*Jeg vil lage en nettside der man kan dele og høre andres meninger.*

**Brukerflyt:**\
*Du går inn i hovedsiden ser andres reviews, hvis du liker en så kan du logge inn og like den og går til en annen side for å skrive din egen.*

**Teknologier brukt:**

-   Python / Flask\
-   MariaDB\
-   HTML / CSS / JS\
-   JPG

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

*F.eks.: Ubuntu VM, Docker, fysisk server.*

### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser\
-   3306\
-   Brannmurregler

Eksempel:

    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

-   systemctl / Supervisor\
-   Filrettigheter\
-   Miljøvariabler

------------------------------------------------------------------------

## 4. Prosjektstyring -- GitHub Projects (Kanban)

-   To Do / In Progress / Done\
-   Issues\
-   Skjermbilde (valgfritt)

Refleksjon: Hvordan hjalp Kanban arbeidet?

------------------------------------------------------------------------

## 5. Databasebeskrivelse

**Databasenavn:**

**Tabeller:**\
\| Tabell \| Felt \| Datatype \| Beskrivelse \|
\|--------\|-------\|-----------\|--------------\| \| customers \| id \|
INT \| Primærnøkkel \| \| customers \| name \| VARCHAR(255) \| Navn \|
\| customers \| address \| VARCHAR(255) \| Adresse \|

**SQL-eksempel:**

``` sql
CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
);
```

------------------------------------------------------------------------

## 6. Programstruktur

    GAMEREVIEWSITE/
     ├── app.py
     ├── StartServer.py
     ├── templates/
     |   └── Index.html
     |   └── UploadSite.html
     |   └── Login.html
     ├── static/
     |   └── Styles/
     |       └── Styles.css
     |   └── Scripts/
     |       └── LoginScript.js
     |       └── Upload.js
     |   └── Images/
     |       └── Unliked.svg
     ├── venv
     ├── .gitignore
     ├── README.md
     └── .env

Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Forklar ruter og funksjoner (kort).

------------------------------------------------------------------------

## 8. Sikkerhet og pålitelighet

-   .env\
-   Miljøvariabler\
-   Parameteriserte spørringer\
-   Validering\
-   Feilhåndtering

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil\
-   Hvordan du løste dem\
-   Testmetoder

------------------------------------------------------------------------

## 10. Konklusjon og refleksjon

-   Hva lærte du?\
-   Hva fungerte bra?\
-   Hva ville du gjort annerledes?\
-   Hva var utfordrende?

------------------------------------------------------------------------

## 11. Kildeliste

-   w3schools\

