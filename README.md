# mereni teploty a vlhkosti pomoci RPI a DHT22

1) Instalace python 
sudo apt install python3-build-hat
2) knihovna zpřístupňující DHT22 (Adafruit)
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
3) Instalace SQLite
4) python skript na měření teploty a vlhkosti
skript vyčte teplotu a vlhkost a uloží hodnoty do databáze a vypíše do stdout
5) crontab - každou minutu je spouštěn python skript na měření
myenv/bin/python /home/albert/dht_mereni.py >> /home/albert/mereni.txt
