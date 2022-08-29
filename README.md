# Setup

## Screenshoty

Pro funkcionalitu screenshotů Je potřeba vytvořit OAuth API klíč přes Google Cloud console se zapnutým Google Drive API. Ten stáhnout jako .json a uložit do složky jako client_secret.json. Složku je vhodné namountovat jako /config volume.
Viz docker-compose jako example

## Export cookies

Skript umí načíst skupiny URL adres (každá skupina je načtena v nové instanci Chromia) a uložit jejich cookies a local storage. Poté data převede do csv formátu a pošle jako přílohu do emailu.

Stačí namountovat /config volume a do něj umístit soubor urlstocheck.json s následující strukturou:
`{ "cmpgroup1": ["https://www.o2.cz/", "https://www.datamanie.cz/"], "cmpgroup2": ["https://www.theverge.com/", "https://www.wired.com/"] }`

# First run

docker-compose up -d

Aplikace dále vyžaduje OAuth autentizaci na uživatelský účet, kam se budou screenshoty nahrávat. Při prvním spuštění vypíše do logu URL adresu pro autentizaci. Pokud se nepovede callback, je možné pustit aplikaci na localhostu a vygenerovaný token.json ve složce /config překopírovat na server. Token se již bude dále automaticky refreshovat.
