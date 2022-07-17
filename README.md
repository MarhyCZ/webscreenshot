# Setup

Je potřeba vytvořit OAuth API klíč přes Google Cloud console se zapnutým Google Drive API. Ten stáhnout jako .json a uložit do složky jako client_secret.json. Složku je vhodné namountovat jako /config volume.
Viz docker-compose jako example

# First run

docker-compose up -d

Aplikace dále vyžaduje OAuth autentizaci na uživatelský účet, kam se budou screenshoty nahrávat. Při prvním spuštění vypíše do logu URL adresu pro autentizaci. Pokud se nepovede callback, je možné pustit aplikaci na localhostu a vygenerovaný token.json ve složce /config překopírovat na server. Token se již bude dále automaticky refreshovat.
