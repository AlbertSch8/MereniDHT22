# Měření teploty a vlhkosti pomocí RPi a DHT22

# Inatalace

1. Instalace python
   
      sudo apt install python3-build-hat

2. knihovna zpřístupňující DHT22 (Adafruit)

      git clone https://github.com/adafruit/Adafruit_Python_DHT.git

      cd Adafruit_Python_DHT

      sudo python setup.py install

3. Instalace SQLite

      sudo apt-get install sqlite3

      sqlite3 /opt/bertiho_db

      ` CREATE TABLE mereniDHT22(
    id INTEGER PRIMARY KEY,
    teplota float,
    vlhkost float,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
); `

5. python skript na měření teploty a vlhkosti

      skript vyčte teplotu a vlhkost a uloží hodnoty do databáze a vypíše do stdout

6. crontab - každou minutu je spouštěn python skript na měření

      myenv/bin/python /home/albert/dht_mereni.py >> /home/albert/mereni.txt


# Vizualizace dat 
Vizualizace dat probíhá pomocí Grafany , kde je vytvořen playbook, který z SQLite databáze zobrazuje v grafu teplotu a vlhkost.

Přístup na Grafanu

http://raspberrypi_IP_address:3000

Username: Admin

Password: pArgar-5kudvu-vabsuj
